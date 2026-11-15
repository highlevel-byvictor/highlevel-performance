"""Runde 13: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'werkzwo': (['Werk Zwo GmbH', 'Herrn Michael Ludmann und Herrn Enno Ortmann', 'Lange Straße 84', '49610 Quakenbrück'], 'Sehr geehrter Herr Ludmann, sehr geehrter Herr Ortmann,',
             'dass Ihre 4,8 Sterne bei Google und Ihr starkes Team auf der Startseite nicht auftauchen und es keinen klaren Button für einen Werkstatttermin gibt', 'Kfz-Meisterbetrieb', 'Werk Zwo'),
 'asreifen': (['AS Reifen-Service GmbH', 'Herrn Viktor Grigorev', 'Max-Planck-Straße 21', '49593 Bersenbrück'], 'Sehr geehrter Herr Grigorev,',
              'dass der erste Bildschirm eine große Grafik statt Ihrer starken Felgen- und Fahrzeugfotos zeigt und Ihre 4,8 Sterne bei Google fehlen', 'Reifenservice', 'AS Reifen-Service'),
 'boecker': (['Auto Böcker GmbH', 'Herrn Axel Böcker und Herrn Stefan Böcker', 'Hindenburgstraße 21', '49610 Quakenbrück'], 'Sehr geehrter Herr Axel Böcker, sehr geehrter Herr Stefan Böcker,',
             'dass Besucher zuerst ein Cookie-Fenster und Ihr Logo sehen, während Ihre Geschichte seit 1948 und Ihre 4,8 Sterne aus 221 Google-Bewertungen auf der Startseite gar nicht vorkommen', 'Autohaus', 'Auto Böcker'),
 'sendur': (['Autohaus Sendur GmbH', 'Herrn Seyhmus Sendur', 'Quakenbrücker Straße 24', '49637 Menslage'], 'Sehr geehrter Herr Sendur,',
            'dass auf der Seite viele Archivfotos statt Ihres Showrooms zu sehen sind und Ihre 4,9 Sterne aus 178 Google-Bewertungen fehlen', 'Autohaus', 'das Autohaus Sendur'),
 'berling': (['Auto Berling Kfz-Meisterbetrieb GmbH & Co. KG', 'Herrn Heinrich Berling', 'Loxtener Straße 1', '49577 Ankum'], 'Sehr geehrter Herr Berling,',
             'dass ein großes Cookie-Fenster fast den halben Bildschirm verdeckt und Ihre Werkstatt, Tankstelle und Ihr Waschpark neben dem Fahrzeugbestand kaum auffallen', 'Kfz-Meisterbetrieb', 'Auto Berling'),
 'goeke': (['Autohaus Göke & Schendel', 'J&S Mechatronik GmbH', 'Hermann-Kemper-Straße 1', '49593 Bersenbrück'], 'Sehr geehrte Damen und Herren,',
           'dass einige Unterseiten noch leer sind und Ihre 4,9 Sterne aus 101 Google-Bewertungen nirgends auftauchen', 'Kfz-Meisterbetrieb', 'Göke & Schendel'),
 'wilgen': (['Kfz-Reparatur Reinhard Wilgen', 'Herrn Reinhard Wilgen', 'Eilerskamp 9', '49610 Quakenbrück'], 'Sehr geehrter Herr Wilgen,',
            'dass die Startseite vor allem Rollerangebote mit Preisen zeigt und Ihre Werkstattleistungen und Ihre 4,7 Sterne bei Google erst weit unten oder gar nicht kommen', 'Kfz-Meisterbetrieb', 'Kfz Wilgen'),
 'fehrmann': (['Autohaus F. J. Fehrmann GmbH', 'Herrn Michael Rohling', 'Mühlenweg 4', '49596 Gehrde'], 'Sehr geehrter Herr Rohling,',
              'dass Besucher zuerst ein Cookie-Fenster sehen und Ihr starkes Plus-Kauf-System mit 7-Tage-Umtauschgarantie erst auf einer Unterseite steht', 'Autohaus', 'das Autohaus Fehrmann'),
 'welp': (['Auto Welp', 'Herrn Waldemar Rupp', 'Voßhöchteweg 6', '49638 Nortrup'], 'Sehr geehrter Herr Rupp,',
          'dass die Seite am Handy nicht angepasst ist, auf der Startseite nur zwei Sätze stehen und Ihre 4,9 Sterne aus 71 Google-Bewertungen nicht vorkommen', 'Kfz-Meisterbetrieb', 'Auto Welp'),
 'opelmenslage': (['Autohaus Menslage GmbH', 'Frau Maren Menslage-Biemann', 'Robert-Bosch-Ring 2', '49584 Fürstenau'], 'Sehr geehrte Frau Menslage-Biemann,',
                  'dass auf der Startseite zuerst ein Kontaktformular steht und Ihre über 90 Jahre Opel-Tradition erst weiter unten im Text auftauchen', 'Autohaus', 'das Autohaus Menslage'),
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
        bf = OUT / 'briefe-r13.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde13-Kfz-10.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
