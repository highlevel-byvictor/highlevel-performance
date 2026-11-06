#!/usr/bin/env python3
"""Qualitäts-Check vor jeder Auslieferung.
Prüft im fertig gerenderten Zuschnitt (Desktop + Handy):
  1. Abgeschnittene Köpfe/Personen: jedes Gesicht in jedem sichtbaren Bild muss samt Kopf (Haare, Kinn) komplett sichtbar sein
     – oder komplett außerhalb liegen. Teilweise sichtbare Köpfe = Fehler.
  2. Text über Gesichtern: kein Element darf über einem Gesicht liegen.
  3. Verdeckter Text: Überschriften/Absätze/Buttons dürfen von nichts überdeckt werden.
  4. Horizontales Überlaufen der Seite.
Aufruf: python3 tools/vorschau/qa.py vorschau/<slug>    (Exit 1 bei Fehlern)
"""
import sys, json
from pathlib import Path
import cv2, numpy as np

MODEL = Path(__file__).parent / "models" / "face_detection_yunet_2023mar.onnx"
VIEWS = [("Desktop", 1440, 900, 1, False), ("Laptop", 1280, 800, 1, False), ("Handy", 390, 844, 2, True)]
_cache = {}

def faces(path: Path):
    """Gesichter im Originalbild: Liste (x,y,w,h) relativ 0..1."""
    k = str(path)
    if k in _cache: return _cache[k]
    raw = cv2.imread(k, cv2.IMREAD_UNCHANGED)
    if raw is None: _cache[k] = []; return []
    if raw.ndim == 3 and raw.shape[2] == 4:  # transparente PNG/WebP auf Weiß legen
        a = raw[:, :, 3:4] / 255.0; raw = (raw[:, :, :3] * a + 255 * (1 - a)).astype(np.uint8)
    elif raw.ndim == 2: raw = cv2.cvtColor(raw, cv2.COLOR_GRAY2BGR)
    h, w = raw.shape[:2]; s = min(1.0, 1600 / max(w, h))
    im = cv2.resize(raw, (round(w * s), round(h * s))) if s < 1 else raw
    det = cv2.FaceDetectorYN.create(str(MODEL), "", (im.shape[1], im.shape[0]), 0.72)
    r = det.detect(im)[1]
    out = [] if r is None else [tuple(float(v) for v in (x[0] / im.shape[1], x[1] / im.shape[0], x[2] / im.shape[1], x[3] / im.shape[0])) for x in r
                                if x[2] * x[3] > 0.0004 * im.shape[0] * im.shape[1]]
    _cache[k] = out; return out

JS_IMGS = """() => [...document.images].map((im,i)=>{const r=im.getBoundingClientRect();const cs=getComputedStyle(im);
 return {i, src:im.currentSrc||im.src, w:r.width, h:r.height, top:r.top+scrollY, nw:im.naturalWidth, nh:im.naturalHeight,
 fit:cs.objectFit, pos:cs.objectPosition, vis:cs.visibility!=='hidden'&&cs.display!=='none'&&r.width>30&&r.height>30&&parseFloat(cs.opacity)>0.05}})"""

JS_PROBE = """([i, pts]) => { const im=document.images[i]; const r=im.getBoundingClientRect(); return pts.map(([x,y])=>{
 if(x<0||y<0||x>=innerWidth||y>=innerHeight) return 'off';
 if(x<r.left-1||x>r.right+1||y<r.top-1||y>r.bottom+1) return 'out';
 const e=document.elementFromPoint(x,y); if(!e) return 'out'; if(e===im) return 'ok';
 if(e.contains(im)) return 'clip';
 return 'cover:'+e.tagName.toLowerCase()+(typeof e.className==='string'&&e.className?'.'+e.className.split(' ')[0]:'')+' "'+(e.textContent||'').trim().slice(0,40)+'"';});}"""

JS_TEXT = """() => { const out=[]; const sel='h1,h2,h3,p,li,a.btn,button,blockquote,figcaption,.eyebrow,small,label';
 const vis=e=>{const cs=getComputedStyle(e);return cs.visibility!=='hidden'&&cs.display!=='none'&&parseFloat(cs.opacity)>0.05};
 document.querySelectorAll(sel).forEach(el=>{ if(!vis(el)||el.closest('.pv,.robo,.bot,.callbar,[aria-hidden=true]')) return;
  if(el.closest('blockquote')&&!el.closest('blockquote.on')&&el.closest('.quotes')) return;
  const r=el.getBoundingClientRect(); if(r.width<4||r.height<4) return;
  out.push({top:r.top+scrollY, left:r.left, w:r.width, h:r.height, t:(el.innerText||'').trim().slice(0,50), tag:el.tagName}); }); return out; }"""

JS_TPROBE = """([b]) => { const res=[]; const xs=[.12,.5,.88], ys=[.3,.7];
 for(const fx of xs) for(const fy of ys){ const x=b.left+b.w*fx, y=b.top-scrollY+b.h*fy; if(y<0||y>=innerHeight||x<0||x>=innerWidth) continue;
  const e=document.elementFromPoint(x,y); if(!e) continue;
  const own=document.elementsFromPoint(x,y).find(n=>n.innerText&&n.innerText.trim().slice(0,50)===b.t);
  if(own && (e===own||own.contains(e)||e.contains(own))) continue;
  if(!own) continue;
  res.push(e.tagName.toLowerCase()+(typeof e.className==='string'&&e.className?'.'+e.className.split(' ')[0]:'')); } return res; }"""

def visible_src_box(o):
    """Welcher Ausschnitt des Originalbilds (0..1) ist im Element sichtbar? (object-fit cover/contain/fill)"""
    W, H, nw, nh = o["w"], o["h"], o["nw"], o["nh"]
    if not nw or not nh: return None
    kw = {"left": "0%", "top": "0%", "center": "50%", "right": "100%", "bottom": "100%"}
    px, py = [float(v.strip("%")) / 100 if v.endswith("%") else .5 for v in [kw.get(t, t) for t in (o["pos"].split() + ["50%"])[:2]]]
    if o["fit"] == "cover": s = max(W / nw, H / nh)
    elif o["fit"] == "contain": s = min(W / nw, H / nh)
    elif o["fit"] == "fill": return (0, 0, W / nw, H / nh, 0, 0)  # gestreckt
    else: s = 1
    dw, dh = nw * s, nh * s
    ox, oy = (W - dw) * px, (H - dh) * py   # Versatz des Bildes im Element (px)
    return (s, s, None, None, ox, oy)

def check_page(br, page_dir: Path, shots=None):
    url = (page_dir / "index.html").as_uri() + "?qa=1"
    errs = []
    for name, vw, vh, dpr, mob in VIEWS:
        pg = br.new_page(viewport={"width": vw, "height": vh}, device_scale_factor=dpr, is_mobile=mob, has_touch=mob)
        pg.goto(url); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
        # alle Lazy-Bilder laden
        H = pg.evaluate("document.documentElement.scrollHeight")
        for y in range(0, H, vh // 2): pg.evaluate(f"scrollTo(0,{y})"); pg.wait_for_timeout(40)
        pg.evaluate("[...document.images].forEach(i=>i.loading='eager')")
        pg.evaluate("Promise.race([Promise.all([...document.images].map(i=>i.complete?1:new Promise(r=>{i.onload=i.onerror=r}))),new Promise(r=>setTimeout(r,8000))])")
        pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(200)
        ow = pg.evaluate("document.documentElement.scrollWidth - innerWidth")
        if ow > 1: errs.append(f"[{name}] Seite läuft {ow}px seitlich über")
        for o in pg.evaluate(JS_IMGS):
            if not o["vis"]: continue
            p = Path(o["src"].replace("file://", "").split("?")[0])
            fs = faces(p)
            if not fs: continue
            m = visible_src_box(o)
            if not m: continue
            sx, sy, _, _, ox, oy = m
            sx = o["w"] / o["nw"] if m[2] is not None else sx
            sy = o["h"] / o["nh"] if m[3] is not None else sy
            # Element in die Bildschirmmitte scrollen
            pg.evaluate(f"scrollTo(0,{max(0, o['top'] + o['h']/2 - vh/2)})"); pg.wait_for_timeout(60)
            r = pg.evaluate(f"(()=>{{const r=document.images[{o['i']}].getBoundingClientRect();return [r.left,r.top]}})()")
            for (fx, fy, fw, fh) in fs:
                X, Y, Wf, Hf = fx * o["nw"] * sx + ox + r[0], fy * o["nh"] * sy + oy + r[1], fw * o["nw"] * sx, fh * o["nh"] * sy
                if Wf < 14: continue  # winzig (z. B. Gesicht auf Werbeplakat im Hintergrund)
                if not all(np.isfinite([X, Y, Wf, Hf])): errs.append(f"[{name}] {p.name}: Zuschnitt nicht berechenbar ({o['fit']} {o['pos']})"); continue
                face = [(X + Wf * a, Y + Hf * b) for a in (.2, .5, .8) for b in (.2, .5, .85)]
                head = [(X + Wf * a, Y - Hf * .45) for a in (.2, .5, .8)] + [(X - Wf * .12, Y + Hf * .4), (X + Wf * 1.12, Y + Hf * .4), (X + Wf * .5, Y + Hf * 1.12)]
                rf = pg.evaluate(JS_PROBE, [o["i"], face]); rh = pg.evaluate(JS_PROBE, [o["i"], head])
                if "ok" not in rf:
                    if "ok" in rh: errs.append(f"[{name}] {p.name}: Person angeschnitten, Gesicht fehlt im Zuschnitt")
                    continue
                cov = [v[6:] for v in rf if v.startswith("cover:")]
                if cov: errs.append(f"[{name}] {p.name}: Gesicht überdeckt von {cov[0]}")
                if any(v in ("out", "clip") for v in rf + rh):
                    errs.append(f"[{name}] {p.name}: Kopf/Gesicht abgeschnitten (Zuschnitt {o['w']:.0f}x{o['h']:.0f}px)")
        # Texte
        for b in pg.evaluate(JS_TEXT):
            pg.evaluate(f"scrollTo(0,{max(0, b['top'] + b['h']/2 - vh/2)})")
            hit = pg.evaluate(JS_TPROBE, [b])
            if hit: errs.append(f"[{name}] Text \"{b['t'][:40]}\" ({b['tag']}) wird verdeckt von {hit[0]}")
        if shots is not None:
            pg.evaluate("scrollTo(0,0)")
            sp = Path(shots) / f"qa-{page_dir.name}-{name.lower()}.jpg"
            pg.screenshot(path=str(sp), full_page=True, type="jpeg", quality=70)
        pg.close()
    return sorted(set(errs))

if __name__ == "__main__":
    from playwright.sync_api import sync_playwright
    d = Path(sys.argv[1]).resolve()
    with sync_playwright() as p:
        br = p.chromium.launch()
        e = check_page(br, d, shots=sys.argv[2] if len(sys.argv) > 2 else None)
        br.close()
    print("\n".join(e) if e else "QA OK: keine abgeschnittenen Köpfe, kein verdeckter Text.")
    sys.exit(1 if e else 0)
