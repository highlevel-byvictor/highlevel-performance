"""Runde 8 Gastro: Konfiguration bauen + Bilder in den Cache kopieren."""
import json, hashlib, shutil, sys
from pathlib import Path
from PIL import Image
ROOT = Path('/home/claude/highlevel-performance'); RAW = Path('/home/claude/r8raw')
OUT = ROOT / 'tools/vorschau/runden/2026-11-gastro-runde8.json'
GSTEPS = [["Tisch reservieren","Rufen Sie an – wir halten Ihren Platz frei."],["Ankommen","Wir empfangen Sie herzlich und nehmen uns Zeit."],["Genießen","Frisch zubereitet, mit Liebe angerichtet."],["Wiederkommen","Wir freuen uns schon auf Ihren nächsten Besuch."]]
FIRMEN = []

def firma(cfg, raw, imgs):
    """imgs: Liste Rohdateien (relativ zu RAW/raw) -> b1..bN"""
    slug = cfg['slug'] + '-' + hashlib.sha1(cfg['firma'].encode()).hexdigest()[:4]
    d = ROOT / 'vorschau' / slug / 'img'; d.mkdir(parents=True, exist_ok=True)
    for old in d.glob('b*.*'):
        if old.stem[1:].isdigit(): old.unlink()
    urls = []
    for i, fn in enumerate(imgs, 1):
        src = RAW / raw / fn
        im = Image.open(src).convert('RGB')
        if im.width > 2400: im = im.resize((2400, round(im.height * 2400 / im.width)), Image.LANCZOS)
        im.save(d / f'b{i}.jpg', quality=88)
        urls.append(f'local://{raw}/{fn}')
    cfg['bild_urls'] = urls; cfg.setdefault('steps', GSTEPS); cfg['template'] = 'beauty'; cfg.setdefault('theme', 'gastro')
    cfg.setdefault('min_w', 300)
    FIRMEN.append(cfg); return slug

exec(open('/home/claude/r8b/firmen.py').read())
if __name__ == '__main__':
    OUT.write_text(json.dumps({'runde': '2026-11-Gastro-Runde8', 'template': 'beauty', 'firmen': FIRMEN}, ensure_ascii=False, indent=1))
    print('OK', len(FIRMEN), 'Firmen ->', OUT)
