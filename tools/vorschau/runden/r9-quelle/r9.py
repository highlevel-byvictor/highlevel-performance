"""Runde 9 Fitness: Konfiguration bauen + Bilder in den Cache kopieren.
Rohdaten: /home/claude/r9raw/<firma>/img/iNNN.jpg (Crawl der Originalseite, nur eigenes Material)."""
import json, hashlib, sys
from pathlib import Path
from PIL import Image, ImageOps
ROOT = Path('/home/claude/highlevel-performance'); RAW = Path('/home/claude/r9raw')
OUT = ROOT / 'tools/vorschau/runden/2026-11-fitness-runde9.json'
HERE = Path(__file__).parent
FIRMEN = []

def steps(sie):
    if sie:
        return [["Probetraining vereinbaren", "Rufen Sie an oder nutzen Sie das Formular."], ["Kennenlernen", "Studio, Trainer und Ihre Ziele."],
                ["Ihr Plan", "Ein Trainingsplan, der zu Ihnen passt."], ["Dranbleiben", "Mit Betreuung Schritt für Schritt zum Ziel."]]
    return [["Probetraining sichern", "Anrufen oder Formular ausfüllen."], ["Kennenlernen", "Studio, Trainer und deine Ziele."],
            ["Dein Plan", "Ein Trainingsplan, der zu dir passt."], ["Dranbleiben", "Mit Betreuung Schritt für Schritt zum Ziel."]]

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
    cfg['template'] = 'beauty'; cfg.setdefault('theme', 'fitness'); cfg.setdefault('min_w', 300)
    FIRMEN.append(cfg); return slug

exec(open(HERE / 'firmen.py').read())
if __name__ == '__main__':
    OUT.write_text(json.dumps({'runde': '2026-11-Fitness-Runde9', 'template': 'beauty', 'firmen': FIRMEN}, ensure_ascii=False, indent=1))
    print('OK', len(FIRMEN), 'Firmen ->', OUT)
