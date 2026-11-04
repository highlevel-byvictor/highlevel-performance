#!/usr/bin/env python3
"""Website-statt-Kaltmail: baut Vorschau-Seiten + Druck-Briefe.
Aufruf: python3 tools/vorschau/build.py tools/vorschau/runden/<runde>.json
"""
import json, sys, os, io, re, urllib.request, ssl, hashlib, datetime
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import jinja2, segno
from markupsafe import Markup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
TPL = Path(__file__).parent
BASE = "https://www.highlevel-performance.de/vorschau/"
OUT_PDF = ROOT.parent / "vorschau-ausgabe"
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>'

THEMES = {
 "holz":    dict(dark="#1B130C", acc="#C27A3A", acc2="#F2C185", tint="#FBF6EF", on="#1B130C"),
 "dach":    dict(dark="#12151E", acc="#D9472B", acc2="#FF9E7D", tint="#F7F4F2", on="#fff"),
 "maler":   dict(dark="#170F2E", acc="#7C3AED", acc2="#F472B6", tint="#FAF7FF", on="#fff"),
 "shk":     dict(dark="#06182B", acc="#0A8FD8", acc2="#4FE3D1", tint="#F2F8FC", on="#04121F"),
 "elektro": dict(dark="#0B0E17", acc="#F2B200", acc2="#FFE27A", tint="#FFFBEF", on="#0B0E17"),
 "garten":  dict(dark="#0D1F16", acc="#2E9E5A", acc2="#B4EBA0", tint="#F3FAF4", on="#08160F"),
 "fliesen": dict(dark="#10191B", acc="#0F8C82", acc2="#9BEFE2", tint="#F1F8F7", on="#071211"),
 "bau":     dict(dark="#15171C", acc="#E0761C", acc2="#FFC37A", tint="#F8F6F3", on="#15171C"),
}

env = jinja2.Environment(loader=jinja2.FileSystemLoader(TPL), autoescape=True)
ctx = ssl.create_default_context()

def fetch_img(url, dest, maxw=1600):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=30, context=ctx).read()
    im = Image.open(io.BytesIO(data))
    orig = im.size
    logo = dest.stem == "logo"
    if logo:
        im = im.convert("RGBA")
        if im.width > 600: im = im.resize((600, round(im.height * 600 / im.width)))
        dest = dest.with_suffix(".png"); im.save(dest, optimize=True)
    else:
        im = im.convert("RGB")
        if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
        elif im.width < 1100: im = im.resize((1100, round(im.height * 1100 / im.width)), Image.LANCZOS)
        # Bild aufwerten: Tonwerte, Farbe, Kontrast, Schärfe
        im = ImageOps.autocontrast(im, cutoff=0.6)
        im = ImageEnhance.Color(im).enhance(1.14)
        im = ImageEnhance.Contrast(im).enhance(1.06)
        im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=3))
        dest = dest.with_suffix(".webp"); im.save(dest, "WEBP", quality=84)
    return dest.name, orig

def tel_link(t):
    t = re.sub(r"[^\d+]", "", t or "")
    if t.startswith("0"): t = "+49" + t[1:]
    return t

def build(runde_file):
    data = json.loads(Path(runde_file).read_text())
    briefe = []
    OUT_PDF.mkdir(exist_ok=True)
    with sync_playwright() as p:
        br = p.chromium.launch()
        for f in data["firmen"]:
            if f.get("skip"): continue
            slug = f["slug"] + "-" + hashlib.sha1(f["firma"].encode()).hexdigest()[:4]
            d = ROOT / "vorschau" / slug; (d / "img").mkdir(parents=True, exist_ok=True)
            imgs = []
            for i, u in enumerate(f.get("bild_urls", [])):
                try:
                    n, sz = fetch_img(u, d / "img" / f"b{i+1}")
                    if sz[0] >= f.get("min_w", 700 if data.get("template") == "v2" else 500): imgs.append("img/" + n)
                except Exception as e:
                    print("  Bild fehlt:", u, e)
            logo = None
            if f.get("logo_url"):
                try: logo = "img/" + fetch_img(f["logo_url"], d / "img" / "logo")[0]
                except Exception as e: print("  Logo fehlt:", e)
            if not imgs: raise SystemExit(f"Keine Bilder für {f['firma']}")
            hero = imgs[f.get("hero_idx", 0) % len(imgs)]
            rest = [x for x in imgs if x != hero]
            v = dict(f, slug=slug, logo=logo, hero=hero,
                     about_img=rest[0] if rest else hero,
                     galerie=rest[1:6] if len(rest) >= 3 else rest[:5], imgs=imgs,
                     tel_link=tel_link(f.get("telefon")),
                     website_kurz=re.sub(r"^https?://(www\.)?|/$", "", f["website"]))
            if data.get("template") == "v2":
                order = [imgs[(f.get("hero_idx", 0) + k) % len(imgs)] for k in range(len(imgs))]
                cyc = lambda k: order[k % len(order)]
                v.update(mosaic=[cyc(0), cyc(1), cyc(2)], band=(None if f.get("band_idx") == "none" else cyc(f.get("band_idx", 3))), about_img=cyc(4), about_img2=cyc(5),
                         galerie=order, imgs=order, pos=f.get("pos", {}))
                html = env.get_template("vorschau2.html.j2").render(f=v, t=THEMES[f.get("theme", "shk")], icon_phone=Markup(PHONE_SVG))
            else:
                html = env.get_template("vorschau.html.j2").render(f=v, icon_phone=Markup(PHONE_SVG))
            (d / "index.html").write_text(html)
            # Screenshots für den Brief
            sd, sm = OUT_PDF / f"{slug}-desk.jpg", OUT_PDF / f"{slug}-mob.jpg"
            pg = br.new_page(viewport={"width": 1280, "height": 860}, device_scale_factor=1.5)
            pg.goto((d / "index.html").as_uri()); pg.wait_for_timeout(900)
            pg.evaluate("document.querySelector('.pv').style.display='none'")
            pg.screenshot(path=str(sd), type="jpeg", quality=85); pg.close()
            pg = br.new_page(viewport={"width": 390, "height": 800}, device_scale_factor=2, is_mobile=True)
            pg.goto((d / "index.html").as_uri()); pg.wait_for_timeout(900)
            pg.evaluate("document.querySelector('.pv').style.display='none';document.querySelector('.callbar')&&(document.querySelector('.callbar').style.display='none')")
            pg.screenshot(path=str(sm), type="jpeg", quality=85); pg.close()
            url = BASE + slug + "/"
            qr = OUT_PDF / f"{slug}-qr.svg"
            segno.make(url, error="m").save(str(qr), scale=10, border=0, dark="#0A1A3A")
            b = f["brief"]
            web = re.sub(r'^https?://(www\.)?|/$', '', f['website'])
            absaetze = [
                f"ich bin Viktor Fehl von High Level Performance aus Bersenbrück. Ich habe mir Ihre Website {web} angeschaut und dabei gesehen, {b['problem']}.",
                f"Heute suchen die meisten Kunden zuerst am Handy nach einem {b['suche']} in der Nähe – und rufen dann den Betrieb an, dessen Seite sofort überzeugt.",
                "Darum habe ich einen ersten, groben Entwurf Ihrer neuen Website gebaut: <b>kostenlos und unverbindlich</b>, mit Ihren eigenen Bildern und Texten. Scannen Sie einfach den QR-Code – der Entwurf öffnet sich direkt auf Ihrem Handy. Bei einer Zusammenarbeit gehen wir natürlich noch viel intensiver ins Detail.",
                "Gefällt Ihnen, was Sie sehen? Dann rufen Sie uns an: Julian von unserem Hotline-Service vereinbart mit Ihnen ein <b>kostenloses Erstgespräch</b>. Dort zeigen wir Ihnen, wie aus der Seite mehr Anfragen werden. Gefällt sie Ihnen nicht, löschen wir den Entwurf einfach wieder.",
            ]
            briefe.append(dict(b, betreff_1="Ein erster Entwurf Ihrer neuen Website.",
                               betreff_2=f"Kostenlos für {f['kurzname']} gebaut – einfach anschauen.",
                               absaetze=[Markup(a) for a in absaetze],
                               shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr),
                               url_kurz="highlevel-performance.de/vorschau/" + slug))
            print("OK", f["firma"], "→", url)
        datum = datetime.date.today().strftime("%d.%m.%Y")
        jt = os.environ.get("JULIAN_TEL", "JULIAN-NUMMER FEHLT")
        jq = OUT_PDF / "julian-qr.svg"
        segno.make("tel:" + tel_link(jt), error="m").save(str(jq), scale=10, border=0, dark="#0A1A3A")
        html = env.get_template("brief.html.j2").render(briefe=briefe, root=str(ROOT), datum=datum, julian_tel=jt, julian_qr=str(jq))
        bf = OUT_PDF / "briefe.html"; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT_PDF / f"HLP-Briefe-{data['runde']}.pdf"
        pg.pdf(path=str(pdf), format="A4", print_background=True, prefer_css_page_size=True)
        br.close()
    print("PDF:", pdf)

if __name__ == "__main__":
    build(sys.argv[1])
