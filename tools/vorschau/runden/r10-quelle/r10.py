"""Runde 10 SHK/Elektro: Konfiguration bauen + Bilder in den Cache kopieren.
Rohdaten: /home/claude/r10raw/<firma>/img/iNNN.jpg (Crawl der Originalseite, nur eigenes Material)."""
import json, hashlib, sys
from pathlib import Path
from PIL import Image, ImageOps
ROOT = Path('/home/claude/highlevel-performance'); RAW = Path('/home/claude/r10raw')
OUT = ROOT / 'tools/vorschau/runden/2026-11-shk-runde10.json'
HERE = Path(__file__).parent
FIRMEN = []

def steps(sie):
    return [["Kostenlos beraten lassen", "Anrufen oder Formular ausfüllen – wir melden uns schnell."], ["Vor-Ort-Termin", "Wir schauen uns alles an und hören zu."],
            ["Klares Angebot", "Transparent, mit Fördermittel-Check."], ["Saubere Umsetzung", "Termintreu montiert – und danach Service aus einer Hand."]]

def firma(cfg, raw, imgs):
    """imgs: Liste von 'iNNN.jpg' oder ('iNNN.jpg', (l, t, r, b)) mit Zuschnitt in Anteilen -> b1..bN"""
    slug = cfg['slug'] + '-' + hashlib.sha1(cfg['firma'].encode()).hexdigest()[:4]
    d = ROOT / 'vorschau' / slug / 'img'; d.mkdir(parents=True, exist_ok=True)
    for old in d.glob('b*.*'):
        if old.stem[1:].isdigit(): old.unlink()
    urls = []
    for i, it in enumerate(imgs, 1):
        fn, crop = (it, None) if isinstance(it, str) else it
        im = ImageOps.exif_transpose(Image.open(RAW / raw / 'img' / fn)).convert('RGB')
        if crop:
            w, h = im.size; l, t, r, b = crop
            im = im.crop((round(l * w), round(t * h), round(r * w), round(b * h)))
        if im.width > 2400: im = im.resize((2400, round(im.height * 2400 / im.width)), Image.LANCZOS)
        im.save(d / f'b{i}.jpg', quality=88)
        urls.append(f'local://{raw}/{fn}')
    cfg['bild_urls'] = urls; cfg.setdefault('steps', steps(not cfg['beauty'].get('du')))
    cfg['template'] = 'beauty'; cfg.setdefault('theme', 'shk'); cfg.setdefault('min_w', 300)
    FIRMEN.append(cfg); return slug

exec(open(HERE / 'firmen.py').read())
if __name__ == '__main__':
    OUT.write_text(json.dumps({'runde': '2026-11-SHK-Runde10', 'template': 'beauty', 'firmen': FIRMEN}, ensure_ascii=False, indent=1))
    print('OK', len(FIRMEN), 'Firmen ->', OUT)
