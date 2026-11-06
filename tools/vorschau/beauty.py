"""Beauty-Vorlage: Freisteller der Inhaberin (rembg, lokal) + weich verschwommener Studio-Hintergrund."""
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

def freisteller(src: Path, dest: Path, maxh=1400):
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
    cut, (w, h) = freisteller(src(B["cut_src"]), img / "inhaberin.webp")
    bg = blur_bg(src(B["hero_bg_src"]), img / "hero-bg.webp")
    B.setdefault("pos", {})
    return dict(cutout="img/" + cut, cut_w=w, cut_h=h, hero_bg="img/" + bg)
