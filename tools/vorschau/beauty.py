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
    bg = blur_bg(src(B["hero_bg_src"]), img / "hero-bg.webp")
    B.setdefault("pos", {})
    auto_pos(B, d, allimg)
    out = dict(cutout=None, hero_bg="img/" + bg)
    if B.get("cut_src"):
        cut, (w, h) = freisteller(src(B["cut_src"]), img / "inhaberin.webp", keep=B.get("cut_keep", 1.0))
        out.update(cutout="img/" + cut, cut_w=w, cut_h=h)
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
