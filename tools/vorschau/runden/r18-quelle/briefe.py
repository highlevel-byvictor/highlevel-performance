"""Runde 18: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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

BRIEF = {
 'sartorius': (['Sartorius GmbH', 'Herrn Dieter Dreckmann', 'Molberger Straße 4', '49688 Lastrup'], 'Sehr geehrter Herr Dreckmann,',
               'oben das Logo, darunter ein schmales Bild und dann ein langer Text zur Firmengeschichte. Kein Button für einen Beratungstermin, keine Ihrer 133 Google-Bewertungen', 'Sartorius'),
 'nowatzke': (['Kamin- und Kachelofenbau Siegbert Nowatzke e.K.', 'Herrn Arne Funke', 'Ochsenweg 9', '49324 Melle'], 'Sehr geehrter Herr Funke,',
              'viel rote Fläche, ein Cookie-Hinweis über das untere Drittel und kein einziger Ihrer gebauten Kamine. Dabei liegen in Ihrer Galerie über 60 starke Fotos', 'Nowatzke'),
 'colnrade': (['Ofenhaus Colnrade', 'Herrn Björn Dauskardt', 'Dorfstraße 21', '27243 Colnrade'], 'Sehr geehrter Herr Dauskardt,',
              'ein schönes Foto, aber kein Button für eine Beratung und kein Wort von Ihren 458 Google-Bewertungen. Unten auf der Seite steht noch „Copyright 2019“', 'das Ofenhaus Colnrade'),
 'schulte': (['Ofen Schulte GmbH', 'Herrn Patrick Schulte', 'Osterbrocker Straße 17', '49844 Bawinkel'], 'Sehr geehrter Herr Schulte,',
             'ein Cookie-Fenster, das fast den ganzen Bildschirm füllt. Von Ihren 130 Feuerstätten und Ihren 4,9 Sternen aus 145 Google-Bewertungen sieht man erst einmal nichts', 'Ofen Schulte'),
 'vogt': (['Dänisches Ofenstudio Vogt', 'Herrn Heiko Weigelt', 'Steubenstraße 12', '32312 Lübbecke'], 'Sehr geehrter Herr Weigelt,',
          'das Logo und eine große Überschrift, aber kein einziger Ofen und kein Button für einen Termin. Ihre 4,8 Sterne aus 79 Google-Bewertungen fehlen ganz', 'das Dänische Ofenstudio Vogt'),
 'recker': (['Ralf Recker Ofenbaumeister', 'Herrn Ralf Recker', 'Am Schulkamp 85', '48369 Saerbeck'], 'Sehr geehrter Herr Recker,',
            'die Worte „Herzlich willkommen“ über einem unscharfen Foto. Ihre gebauten Öfen, also das, was Kunden überzeugt, kommen erst weiter unten', 'Ihren Ofenbau'),
 'anten': (['Kachel und Kamin Anten GmbH', 'Herrn Norbert Anten und Herrn Michael Anten', 'Fladderweg 1', '49393 Lohne'], 'Sehr geehrte Herren Anten,',
           'ein grauer Cookie-Text über mehr als den halben Bildschirm, dahinter das Menü. Von Ihren 1.000 m² Ausstellung sieht man nichts', 'Kachel + Kamin Anten'),
 'evers': (['Evers eGbR Kamine &amp; Öfen', 'Herrn Manuel Evers', 'Im Mersch 1a', '49577 Eggermühlen'], 'Sehr geehrter Herr Evers,',
           'ein Cookie-Hinweis über die untere Hälfte, kein Ofen im Bild und kein Button, um einen Termin zu vereinbaren', 'Evers Kamine &amp; Öfen'),
}
ALT = Path('/home/claude/vorschau-ausgabe/alt18')

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
                f"das linke Handy unten zeigt {s['web']}, so wie ein Kunde die Seite heute öffnet: {problem}. Das rechte Handy zeigt, was ich daraus gebaut habe. <b>Kostenlos und ohne dass Sie etwas bestellt haben.</b>",
                "Warum mir das wichtig erscheint: Nach Schätzung des Branchenverbands HKI ersetzen mehr als drei von vier verkauften Öfen einen alten. Diese Kunden schauen sich vorher in Ruhe am Handy um und fahren dann zu dem Studio, das ihnen dort schon gezeigt hat, was es kann.",
                f"<b>Wichtig: Sie bekommen keine zweite Website.</b> Wir bringen Ihre bestehende Seite auf den neuesten Stand. Sie bleibt unter {s['web']} erreichbar, mit Ihren Inhalten und Bildern, nur schneller, am Handy sauber lesbar und mit einem klaren Weg zum Beratungstermin. Am Ende haben Sie eine Website, nicht zwei.",
                "Ich bin Viktor Fehl aus Bersenbrück. Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite ein, wann wir Sie erreichen. Julian ruft Sie innerhalb von 24 Stunden an. Wenn nicht, löschen wir den Entwurf wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='So sieht Ihre Website heute auf dem Handy aus.', betreff_2=f'Und so könnte sie aussehen: mein Entwurf für {kurz}.', web=s['web'], shot_alt=str(ALT / f'{k}.jpg'),
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief18.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r18.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde18-Kaminstudios-60km.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
