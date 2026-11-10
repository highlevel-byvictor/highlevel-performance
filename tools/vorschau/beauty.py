"""Beauty-Vorlage: Freisteller der Inhaberin (rembg, lokal) + weich verschwommener Studio-Hintergrund."""
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

def freisteller(src: Path, dest: Path, maxh=1400, keep=1.0):
    """Person freistellen (u2net_human_seg + Alpha-Matting), auf Inhalt zuschneiden, als WebP mit Transparenz."""
    if dest.exists() and dest.stat().st_mtime > max(src.stat().st_mtime, Path(__file__).stat().st_mtime):
        im = Image.open(dest); return dest.name, im.size
    from rembg import remove, new_session
    im = Image.open(src).convert("RGB")
    out = remove(im, session=new_session("u2net_human_seg"), alpha_matting=True,
                 alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=20,
                 alpha_matting_erode_size=12)
    a = out.getchannel("A").point(lambda v: 0 if v < 12 else v)
    out.putalpha(a)
    bb = a.getbbox()
    if bb:
        out = out.crop(bb)
        if keep < 1: out = out.crop((0, 0, out.width, round(out.height * keep)))
        pad = Image.new("RGBA", (round(out.width * 1.06), round(out.height * 1.08)), (0, 0, 0, 0))
        pad.paste(out, ((pad.width - out.width) // 2, pad.height - out.height)); out = pad
    if out.height > maxh: out = out.resize((round(out.width * maxh / out.height), maxh), Image.LANCZOS)
    out.save(dest, "WEBP", quality=90, method=6)
    return dest.name, out.size

def blur_bg(src: Path, dest: Path, radius=22):
    """Studio-Foto weich verschwommen und leicht aufgehellt als Hero-Hintergrund."""
    if dest.exists() and dest.stat().st_mtime > src.stat().st_mtime: return dest.name
    im = Image.open(src).convert("RGB")
    im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(radius))
    im = ImageEnhance.Brightness(im).enhance(1.06)
    im = ImageEnhance.Color(im).enhance(.85)
    im.save(dest, "WEBP", quality=80)
    return dest.name

def prepare(f, d: Path, allimg: dict):
    B = f["beauty"]; img = d / "img"
    src = lambda k: d / allimg[k]
    bg = blur_bg(src(B["hero_bg_src"]), img / "hero-bg.webp", radius=7 if B.get("split_bg") else 22)
    B.setdefault("pos", {})
    auto_pos(B, d, allimg)
    out = dict(cutout=None, hero_bg="img/" + bg)
    if B.get("cut_src"):
        cut, (w, h) = freisteller(src(B["cut_src"]), img / "inhaberin.webp", keep=B.get("cut_keep", 1.0))
        out.update(cutout="img/" + cut, cut_w=w, cut_h=h)
    if not B.get("no_map") and f.get("adresse"):
        k = karte(f["adresse"], d)
        if k: out.update(karte=k[0])
    return out

def auto_pos(B, d: Path, allimg: dict):
    """Bildausschnitt automatisch nach Gesichtern ausrichten (object-position), wenn nicht von Hand gesetzt.
    Verteilt den abgeschnittenen Rand so, dass Köpfe (mit Haaren) möglichst komplett sichtbar bleiben."""
    import qa
    for k, rel in allimg.items():
        if k in B["pos"]: continue
        fs = qa.faces(d / rel)
        if not fs: continue
        x0 = max(0, min(f[0] for f in fs) - 0.05); x1 = min(1, max(f[0] + f[2] for f in fs) + 0.05)
        y0 = max(0, min(f[1] - f[3] * 0.5 for f in fs)); y1 = min(1, max(f[1] + f[3] * 1.15 for f in fs))
        px = x0 / (x0 + (1 - x1)) if (x0 + 1 - x1) > 0 else .5
        py = y0 / (y0 + (1 - y1)) if (y0 + 1 - y1) > 0 else .5
        B["pos"][k] = f"{px*100:.0f}% {py*100:.0f}%"

def karte(adresse: str, d: Path):
    """Standort-Karte als eigenes Bild (OpenStreetMap-Kacheln, lokal gespeichert -> kein Google-Aufruf beim Besucher).
    Gibt (pfad, lat, lon) zurück oder None."""
    import json, math, urllib.request, urllib.parse, io
    dest = d / "img" / "karte.webp"; meta = d / "img" / "karte.json"
    if dest.exists() and meta.exists():
        m = json.loads(meta.read_text())
        if m.get("adresse") == adresse: return "img/karte.webp", m["lat"], m["lon"]
    UA = {"User-Agent": "HLP-Vorschau/1.0 (Website-Entwurf, einmalige Kartenerstellung)"}
    q = urllib.parse.urlencode({"q": adresse, "format": "json", "limit": 1, "countrycodes": "de"})
    try:
        r = json.loads(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?" + q, headers=UA), timeout=20).read())
        if not r:  # ohne Hausnummer erneut
            q = urllib.parse.urlencode({"q": adresse.split(",")[-1].strip(), "format": "json", "limit": 1, "countrycodes": "de"})
            r = json.loads(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?" + q, headers=UA), timeout=20).read())
        lat, lon = float(r[0]["lat"]), float(r[0]["lon"])
        z = 16; n = 2 ** z
        px = (lon + 180) / 360 * n * 256
        py = (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n * 256
        W, H = 1600, 720
        x0, y0 = px - W / 2, py - H / 2
        canvas = Image.new("RGB", (W, H), "white")
        for tx in range(int(x0 // 256), int((x0 + W) // 256) + 1):
            for ty in range(int(y0 // 256), int((y0 + H) // 256) + 1):
                u = f"https://tile.openstreetmap.org/{z}/{tx}/{ty}.png"
                t = Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20).read())).convert("RGB")
                canvas.paste(t, (int(tx * 256 - x0), int(ty * 256 - y0)))
        canvas.save(dest, "WEBP", quality=88)
        meta.write_text(json.dumps({"adresse": adresse, "lat": lat, "lon": lon}))
        return "img/karte.webp", lat, lon
    except Exception as e:
        print("  Karte nicht möglich:", e)
        return None
