"""Runde 17: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
import sys, re, hashlib, datetime, json
from pathlib import Path
from markupsafe import Markup
import segno, jinja2
from playwright.sync_api import sync_playwright
H = Path(__file__).parent; ROOT = Path('/home/claude/highlevel-performance'); TPL = ROOT / 'tools/vorschau'
sys.path.insert(0, str(TPL)); sys.path.insert(0, str(H))
import qa
from sites import SITES
OUT = Path('/home/claude/vorschau-ausgabe'); OUT.mkdir(exist_ok=True)
BASE = 'https://www.highlevel-performance.de/vorschau/'
JT = '+49 176 63213512'

BRIEF = {}
BRIEF.update({
 'willmann': (['Ihr Küchenpartner Willmann', 'Herrn Daniel Willmann', 'Scheelenkamp 6', '49163 Bohmte-Hunteburg'], 'Sehr geehrter Herr Willmann,',
              'dass die Startseite mit „Herzlich Willkommen“ und viel Fließtext beginnt, es keinen Button für eine Terminanfrage gibt und Ihre 4,8 Sterne aus 64 Google-Bewertungen nirgends zu sehen sind', 'den Küchenpartner Willmann'),
 'zwinger': (['Küchen Center Zwinger e.K.', 'Herrn Viktor Zwinger', 'Gartenkamp 212', '49492 Westerkappeln'], 'Sehr geehrter Herr Zwinger,',
             'dass Ihre 21 Auszeichnungen zum 1a-Fachhändler erst weiter unten auftauchen, Telefon und Öffnungszeiten in einer schmalen Leiste am Rand stehen und Ihre 4,8 Sterne aus 67 Google-Bewertungen fehlen', 'das Küchen Center Westerkappeln'),
 'stegink': (['Küchen Stegink GmbH &amp; Co. KG', 'Herrn Helmut Lambers', 'Dietrich-Borggreve-Straße 18', '49828 Neuenhaus'], 'Sehr geehrter Herr Lambers,',
             'dass Ihre 4,8 Sterne aus 77 Google-Bewertungen nirgends zu sehen sind, oben kein direkter Weg zum Beratungstermin steht und Ihre Ausstellungsküchen erst in einem Untermenü zu finden sind', 'Küchen Stegink'),
 'feldhaus': (['Feldhaus Küchen Design + Technik GmbH', 'Geschäftsführung', 'Ostlandstraße 1', '49685 Emstek'], 'Sehr geehrter Herr Feldhaus,',
              'dass oben zuerst ein Foto des Gebäudes steht, Ihre Auszeichnungen erst unter „Über uns“ zu finden sind und Ihre 5,0 Sterne bei Google nirgends auftauchen', 'Feldhaus Küchen'),
})

def slug(s): return s['slug'] + '-' + hashlib.sha1(s['firma'].encode()).hexdigest()[:4]

def run(keys):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TPL)))
    briefe = []; fehler = {}
    with sync_playwright() as p:
        br = p.chromium.launch()
        for k in keys:
            s = SITES[k]; sl = slug(s); d = ROOT / 'vorschau' / sl
            import os
            fe = [] if os.environ.get('NOQA') else qa.check_page(br, d)
            if fe: fehler[k] = fe; print('QA-FEHLER', k, *fe, sep='\n  ')
            else: print('QA OK', k)
            sd, sm = OUT / f'{sl}-desk.jpg', OUT / f'{sl}-mob.jpg'
            hide = "document.querySelectorAll('.hlp-note,.bot,.lot,.mcall,.pop,.tbar').forEach(e=>e.style.display='none');document.querySelectorAll('[data-r]').forEach(e=>e.classList.add('in'))"
            pg = br.new_page(viewport={'width': 1280, 'height': 860}, device_scale_factor=1.5); pg.goto((d / 'index.html').as_uri()); pg.wait_for_timeout(1600); pg.evaluate(hide); pg.screenshot(path=str(sd), type='jpeg', quality=85); pg.close()
            pg = br.new_page(viewport={'width': 390, 'height': 800}, device_scale_factor=2, is_mobile=True); pg.goto((d / 'index.html').as_uri()); pg.wait_for_timeout(1600); pg.evaluate(hide); pg.screenshot(path=str(sm), type='jpeg', quality=85); pg.close()
            url = BASE + sl + '/'; qr = OUT / f'{sl}-qr.svg'
            segno.make(url, error='m').save(str(qr), scale=10, border=0, dark='#0A1A3A')
            an, anrede, problem, kurz = BRIEF[k]
            absaetze = [
                "wer heute eine neue Küche plant, schaut sich zuerst am Handy um: Bilder, Bewertungen, ein schneller Weg zum Termin. Erst danach fährt man ins Studio. Eine Küche ist eine Entscheidung über viele tausend Euro, und den Auftrag bekommt meist das Studio, dem man schon vor dem ersten Besuch vertraut: <b>echte Küchen aus der Ausstellung, zufriedene Kunden, ein Gesicht hinter der Firma.</b>",
                f"Ich bin Viktor Fehl aus Bersenbrück. Auf {s['web']} ist mir aufgefallen, {problem}. Darum habe ich Ihnen einen groben Entwurf gebaut, <b>kostenlos</b> und mit Ihren eigenen Bildern. Mit dabei: ein digitaler Küchen-Lotse, der Besucher rund um die Uhr durch Ihre Seite führt und Fragen zu Öffnungszeiten und Terminen beantwortet.",
                "Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite einfach kurz ein, wann wir Sie erreichen. Julian von unserem Hotline-Service ruft Sie innerhalb von 24 Stunden für ein <b>kostenloses Erstgespräch</b> zurück. Wenn nicht, löschen wir den Entwurf einfach wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='Warum Küchenkunden zuerst online entscheiden.', betreff_2=f'Ein kostenloser Website-Entwurf für {kurz}.',
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r17.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde17-Kuechenstudios-80km.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
