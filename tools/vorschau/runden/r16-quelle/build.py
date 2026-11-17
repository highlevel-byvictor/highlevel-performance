"""Runde 16 Küchenstudios um Werlte: Seiten aus lib.py + sites.py bauen.
Aufruf: python3 build.py [key ...]"""
import sys, hashlib, shutil
from pathlib import Path
from PIL import ImageColor, Image, ImageOps, ImageChops
H = Path(__file__).parent
ROOT = Path('/home/claude/highlevel-performance')
RAW = Path('/home/claude/r16raw')
sys.path.insert(0, str(H)); sys.path.insert(0, str(ROOT / 'tools/vorschau'))
import lib
from sites import SITES

def slugdir(s):
    d = ROOT / 'vorschau' / (s['slug'] + '-' + hashlib.sha1(s['firma'].encode()).hexdigest()[:4])
    (d / 'img').mkdir(parents=True, exist_ok=True)
    return d

def trim(im, bg=(255, 255, 255), pad=10):
    diff = ImageChops.difference(im.convert('RGB'), Image.new('RGB', im.size, bg)).convert('L').point(lambda p: 255 if p > 18 else 0)
    bb = diff.getbbox()
    return im.crop((max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.width, bb[2]+pad), min(im.height, bb[3]+pad))) if bb else im

def white2alpha(im):
    im = im.convert('RGBA'); px = im.getdata()
    im.putdata([(r, g, b, 0) if r > 238 and g > 238 and b > 238 else (r, g, b, a) for r, g, b, a in px]); return im

def prep(s, d):
    for dst, spec in s['img'].items():
        src, w = spec[0], spec[1]; op = spec[2] if len(spec) > 2 else None
        src = Path(src) if str(src).startswith('/') else RAW / src
        out = d / 'img' / dst
        if not src.exists():
            g = sorted(src.parent.glob(src.stem + '.*'))
            if g: src = g[0]
        if str(src).endswith(('.mp4', '.svg')): shutil.copy(src, out); continue
        im = ImageOps.exif_transpose(Image.open(src))
        if isinstance(op, tuple):
            W, Hh = im.size; l, t, r, b = op; im = im.crop((round(l*W), round(t*Hh), round(r*W), round(b*Hh)))
        if dst.endswith('.png'):
            if op == 'trim': im = trim(im.convert('RGB'))
            if op == 'trimalpha': im = white2alpha(trim(im.convert('RGB')))
            if op == 'alphacrop': im = im.convert('RGBA'); im = im.crop(im.getbbox())
            im = im.convert('RGBA')
            if w and im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            im.save(out, optimize=True); continue
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            im = im.convert('RGBA'); bgc = Image.new('RGBA', im.size, ImageColor.getrgb(op) + (255,) if isinstance(op, str) and op.startswith('#') else (255, 255, 255, 255)); bgc.alpha_composite(im); im = bgc
        im = im.convert('RGB')
        if w and im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        im.save(out, quality=84, optimize=True, progressive=True)

def build(key):
    s = SITES[key]; d = slugdir(s); prep(s, d)
    import beauty; beauty.karte(s['adresse'], d)
    html = lib.page(s, s['body'](s))
    html = html.replace('<!--KIT_CSS-->', (H / 'kit.css').read_text()).replace('<!--LIB_CSS-->', (H / 'lib.css').read_text()).replace('<!--LIB14_CSS-->', (H / 'lib14.css').read_text())
    html = html.replace('</head>', '<style>' + (H / 'r16b.css').read_text() + (s.get('css2') or '') + '</style></head>', 1)
    html = html.replace('<!--KIT_JS-->', (H / 'kit.js').read_text())
    html = html.replace('<!--FONTS-->', (ROOT / 'tools/vorschau/fonts' / f"{s['fonts']}.css").read_text())
    (d / 'index.html').write_text(html); (H / f'{key}.built.html').write_text(html)
    print('OK', key, '->', d.name)
    return d

if __name__ == '__main__':
    for k in (sys.argv[1:] or list(SITES)): build(k)
