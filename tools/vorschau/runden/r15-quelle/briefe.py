"""Runde 15: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'haneburger': (['Fahrschule Haneburger', 'Herrn Frank Haneburger', 'Große Straße 100', '26871 Papenburg'], 'Sehr geehrter Herr Haneburger,',
            'dass die Startseite vor allem aus Ihrem Jubiläums-Plakat besteht, Besucher sich nirgends direkt anmelden können und Ihre Klassen vom Mofa bis zum Lkw erst in Untermenüs auftauchen', 'die Fahrschule Haneburger'),
 'jewa': (['Fahrschule JeWa GmbH', 'Herrn Jens Schwindeler und Herrn Waldemar Schierling', 'Schwedenschanze 87', '49809 Lingen (Ems)'], 'Sehr geehrter Herr Schwindeler, sehr geehrter Herr Schierling,',
          'dass oben auf der Startseite statt Ihres Logos ein Platzhalter erscheint, es dort keinen Anmelde-Button gibt und Ihre 4,8 Sterne bei Google nirgends zu sehen sind', 'die Fahrschule JeWa'),
 'neehoff': (['Fahrschule Bernd Neehoff', 'Herrn Bernd Neehoff', 'Lange Straße 56', '49733 Haren (Ems)'], 'Sehr geehrter Herr Neehoff,',
             'dass Ihr stärkstes Angebot, die Theorie in sieben Abenden, mitten im Fließtext steht, auf der Startseite zwei Ladekreise hängen bleiben und Ihre 4,7 Sterne aus 93 Bewertungen fehlen', 'die Fahrschule Neehoff'),
 'mobilmacher': (['Fahrschule Steinkamp &amp; Gröninger', 'Die Mobilmacher', 'Herrn Martin Steinkamp und Frau Simone Gröninger', 'Gropiusplatz 7', '49716 Meppen'], 'Sehr geehrter Herr Steinkamp, sehr geehrte Frau Gröninger,',
                 'dass auf der Startseite kein Anmelde-Button zu finden ist, Ihre 5,0 Sterne bei Google fehlen und unter „Aktuelles“ noch eine Meldung von 2018 steht', 'Die Mobilmacher'),
 'kemper': (['Fahrschule Kemper', 'Herrn Timo Kemper', 'Weberstraße 6', '49716 Meppen'], 'Sehr geehrter Herr Kemper,',
            'dass Ihr starkes kostenloses Lerncoaching in einem langen Textblock versteckt ist und man sich auf der Startseite nur über einen kleinen Textlink anmelden kann', 'die Fahrschule Kemper'),
 'hofschroeer': (['Fahrschule Hofschröer GmbH', 'Herrn Christian Hofschröer', 'Frerener Straße 5', '49809 Lingen (Ems)'], 'Sehr geehrter Herr Hofschröer,',
                 'dass Ihr tolles Team zwar zu sehen ist, Ihre 4,9 Sterne aus 65 Bewertungen aber fehlen und der Weg zur Anmeldung erst ganz unten als Schriftzug auftaucht', 'die Fahrschule Hofschröer'),
 'scherpenberg': (['Fahrschule Scherpenberg', 'Frau Elisa Kottig Rodrigues und Herrn Michael Kottig', 'St.-Georg-Straße 1', '49584 Fürstenau'], 'Sehr geehrte Frau Kottig Rodrigues, sehr geehrter Herr Kottig,',
                  'dass unter Ihrem Logo eine große leere Fläche folgt, die Seite der Führerscheinklassen nur „Klasse B“ zeigt und Ihre 5,0 Sterne aus 60 Bewertungen nirgends auftauchen', 'die Fahrschule Scherpenberg'),
}

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
                "seit November 2025 melden sich laut einer Umfrage unter 2.424 Fahrschulen im Schnitt <b>54 % weniger Fahrschüler</b> an. Und wer sich anmeldet, vergleicht vorher am Handy. Mit der Reform sollen Preise und Bestehensquoten bald öffentlich vergleichbar sein. Gewinnen wird, wer zeigt, was keine Datenbank zeigt: <b>geduldige Fahrlehrer, gepflegte Autos, zufriedene Fahrschüler.</b>",
                f"Ich bin Viktor Fehl aus Bersenbrück. Auf {s['web']} ist mir aufgefallen, {problem}. Darum habe ich Ihnen einen groben Entwurf gebaut, <b>kostenlos</b> und mit Ihren eigenen Bildern. Mit dabei: ein Führerschein-Lotse, der Interessenten in 30 Sekunden zur passenden Klasse führt und die Anmeldung vorausfüllt.",
                "Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite einfach kurz ein, wann wir Sie erreichen. Julian von unserem Hotline-Service ruft Sie innerhalb von 24 Stunden für ein <b>kostenloses Erstgespräch</b> zurück. Wenn nicht, löschen wir den Entwurf einfach wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='Warum Fahrschüler gerade online entscheiden.', betreff_2=f'Ein kostenloser Website-Entwurf für {kurz}.',
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r15.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde15-Fahrschulen-Emsland.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
