"""Runde 11: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'werlter': (['Werlter Fitness Studio & Physiotherapie', 'Frau Katrin Diepholz', 'Raddeweg 4', '49757 Werlte'], 'Sehr geehrte Frau Diepholz,',
             'dass Besucher zuerst ein großes Cookie-Fenster sehen und Ihre Stärke, die Physiotherapie ohne Rezept direkt neben dem Studio, erst weit unten auftaucht', 'Fitnessstudio', 'Werlter Fitness Studio'),
 'huemmling': (['FC Fitnessclub Hümmling GmbH', 'Frau Andrea und Herrn Hans van de Merbel', 'Unfriedstraße 4', '49757 Werlte'], 'Sehr geehrte Frau van de Merbel, sehr geehrter Herr van de Merbel,',
               'dass das Cookie-Fenster auf Niederländisch erscheint und Ihre Erfolge bei Deutschen Meisterschaften erst auf einer Unterseite stehen', 'Fitnessstudio', 'den Fitnessclub Hümmling'),
 'optimumm': (['optiMumm Physiotherapie und Fitness-Studio', 'Herrn Holger Otten', 'Erlenweg 2', '26897 Esterwegen'], 'Sehr geehrter Herr Otten,',
              'dass die Fotos Ihres Studios sehr klein erscheinen und Ihr größter Vorteil, Physiotherapie und Fitness unter einem Dach, kaum ins Auge fällt', 'Physiotherapeuten', 'optiMumm'),
 'sprenkel': (['reaktiv Sprenkel', 'Praxis für Physiotherapie und Rehabilitation', 'Herrn Thomas Sprenkel', 'Wahner Straße 10', '49751 Sögel'], 'Sehr geehrter Herr Sprenkel,',
              'dass Ihr Imagefilm erst nach einem Cookie-Klick startet und Besucher am Handy viel Text lesen, bevor sie zu Ihrer neuen MTT kommen', 'Physiotherapeuten', 'reaktiv Sprenkel'),
 'physiovital': (['Physio Vital & Physio Fit', 'Frau Katja und Herrn Peter Moritz', 'Von-Stauffenberg-Straße 6', '49751 Sögel'], 'Sehr geehrte Frau Moritz, sehr geehrter Herr Moritz,',
                 'dass Physio Vital, Physio Fit und PEP auf der Startseite nebeneinanderstehen und Interessenten nicht sofort sehen, womit sie anfangen sollen', 'Physiotherapeuten', 'Physio Vital & Physio Fit'),
 'meiners': (['Reha-Zentrum Meiners', 'Frau Alexandra Meiners', 'Loruper Straße 21', '49757 Werlte'], 'Sehr geehrte Frau Meiners,',
             'dass Ihr hauseigenes Schwimmbad und die Akutsprechstunde zwar genannt werden, Besucher aber zuerst ein Cookie-Fenster über Ihrem Startbild sehen', 'Physiotherapeuten', 'das Reha-Zentrum Meiners'),
 'happiness': (['Happiness Studio Werlte', 'Frau Jana Untiedt-Kroner', 'Marktstraße 2', '49757 Werlte'], 'Sehr geehrte Frau Untiedt-Kroner,',
               'dass Ihre wunderschönen Fotos auf der Startseite hinter einer dunklen Fläche liegen und Ihre Kurse erst nach dem Scrollen auftauchen', 'Yogakurs', 'das Happiness Studio'),
 'inbalance': (['INBalance Aktiv & Gesund GmbH & Co. KG', 'Herrn Stefan Backhaus', 'Pegasusstraße 2a', '49688 Lastrup'], 'Sehr geehrter Herr Backhaus,',
               'dass Ihre starken Konzepte und Kundenstimmen auf einer sehr dunklen Startseite stehen und am Handy zuerst ein großes Cookie-Fenster erscheint', 'Gesundheitsstudio', 'das INBalance'),
 'prime': (['Prime Sportclub', 'Roevenkamp 12', '49624 Löningen'], 'Sehr geehrte Damen und Herren,',
           'dass Ihr neuer HYROX-Bereich in Löningen weit unten steht und auf der Seite noch ein Bild mit „Super Corona Deals“ liegt', 'Fitnessstudio', 'den Prime Sportclub'),
 'freunde': (['Fitness Freunde Lindern', 'z. Hd. Herrn Thorge Takenberg', 'Lastruper Straße 29', '49699 Lindern (Oldenburg)'], 'Sehr geehrter Herr Takenberg,',
             'dass Ihre Startseite mit einer Preisliste beginnt und Besucher erst weit unten erfahren, was Fitness Freunde besonders macht', 'Fitnessstudio', 'Fitness Freunde'),
}

def slug(s): return s['slug'] + '-' + hashlib.sha1(s['firma'].encode()).hexdigest()[:4]

def run(keys):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TPL)))
    briefe = []; fehler = {}
    with sync_playwright() as p:
        br = p.chromium.launch()
        for k in keys:
            s = SITES[k]; sl = slug(s); d = ROOT / 'vorschau' / sl
            fe = qa.check_page(br, d)
            if fe: fehler[k] = fe; print('QA-FEHLER', k, *fe, sep='\n  ')
            else: print('QA OK', k)
            sd, sm = OUT / f'{sl}-desk.jpg', OUT / f'{sl}-mob.jpg'
            hide = "document.querySelectorAll('.hlp-note,.bot,.mcall,.pop').forEach(e=>e.style.display='none');document.querySelectorAll('[data-r]').forEach(e=>e.classList.add('in'))"
            pg = br.new_page(viewport={'width': 1280, 'height': 860}, device_scale_factor=1.5); pg.goto((d / 'index.html').as_uri()); pg.wait_for_timeout(1600); pg.evaluate(hide); pg.screenshot(path=str(sd), type='jpeg', quality=85); pg.close()
            pg = br.new_page(viewport={'width': 390, 'height': 800}, device_scale_factor=2, is_mobile=True); pg.goto((d / 'index.html').as_uri()); pg.wait_for_timeout(1600); pg.evaluate(hide); pg.screenshot(path=str(sm), type='jpeg', quality=85); pg.close()
            url = BASE + sl + '/'; qr = OUT / f'{sl}-qr.svg'
            segno.make(url, error='m').save(str(qr), scale=10, border=0, dark='#0A1A3A')
            an, anrede, problem, suche, kurz = BRIEF[k]
            absaetze = [
                f"ich bin Viktor Fehl von High Level Performance aus Bersenbrück. Ich habe mir Ihre Website {s['web']} angeschaut und dabei gesehen, {problem}.",
                f"Heute suchen die meisten Menschen zuerst am Handy nach einem {suche} in der Nähe und melden sich dann dort, wo die Seite sofort überzeugt.",
                "Darum habe ich einen ersten, groben Entwurf Ihrer neuen Website gebaut: <b>kostenlos und unverbindlich</b>, mit Ihren eigenen Bildern und Texten. Scannen Sie einfach den QR-Code, dann öffnet sich der Entwurf direkt auf Ihrem Handy. Bei einer Zusammenarbeit arbeiten wir natürlich alles noch viel genauer aus.",
                "Gefällt Ihnen, was Sie sehen? Dann rufen Sie uns an: Julian von unserem Hotline-Service vereinbart mit Ihnen ein <b>kostenloses Erstgespräch</b>. Dort zeigen wir Ihnen, wie aus der Seite mehr Anfragen werden. Gefällt sie Ihnen nicht, löschen wir den Entwurf einfach wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='Ein erster Entwurf Ihrer neuen Website.', betreff_2=f'Kostenlos für {kurz} gebaut. Einfach anschauen.',
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r11.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde11-Fitness-Werlte.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
