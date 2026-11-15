"""Runde 12: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'bsb': (['Bersenbrücker Küchenstudio', 'Herrn Siegfried Hüdepohl', 'Robert-Bosch-Straße 6–8', '49593 Bersenbrück'], 'Sehr geehrter Herr Hüdepohl,',
         'dass die Seite am Handy nicht angepasst ist und Ihre 14 Musterküchen und die reduzierten Ausstellungsküchen in kleinem Text untergehen', 'Küchenstudio', 'das Bersenbrücker Küchenstudio'),
 'pk': (['Küche + Design, Peters + Kuhlmann', 'Herrn Alexander Peters und Herrn Leon Kuhlmann', 'Ankumer Straße 19', '49593 Bersenbrück'], 'Sehr geehrter Herr Peters, sehr geehrter Herr Kuhlmann,',
        'dass Ihre 84 Fünf-Sterne-Bewertungen bei Google auf der Startseite fehlen und Ihre Stärken, Hausbesuch und Küche in 3D mit der VR-Brille, erst auf Unterseiten auftauchen', 'Küchenstudio', 'Küche + Design'),
 'ortland': (['ORTLAND Küche + Design', 'Herrn Martin Ortland', 'St. Annenstraße 12', '49610 Quakenbrück'], 'Sehr geehrter Herr Ortland,',
             'dass die Startseite vor allem aus grauen Kacheln mit kleiner Schrift besteht und Ihre schönen Küchen und Ihr Team erst auf Unterseiten zu sehen sind', 'Küchenstudio', 'Ortland Küche + Design'),
 'ts': (['Tischlerei TS-Möbel Design & Küchenstudio', 'Herrn Thomas Steinkamp', 'Bahnhofstraße 5a', '49594 Alfhausen'], 'Sehr geehrter Herr Steinkamp,',
        'dass Besucher als Erstes eine Gartenbank vor dem Eingang sehen und Ihre Küchen und Möbel nach Maß erst in der Galerie auftauchen', 'Küchenstudio', 'TS-Möbel Design'),
 'beckermann': (['Tischlerei Beckermann', 'Herrn Frederick Sommerei', 'Braunschweiger Straße 3', '49434 Neuenkirchen-Vörden'], 'Sehr geehrter Herr Sommerei,',
                'dass Ihre besondere Stärke, Küchen von jemandem geplant, der selbst leidenschaftlich kocht, erst auf einer Unterseite steht', 'Küchenstudio', 'die Tischlerei Beckermann'),
 'meyer': (['Meyer Möbelwerkstätten', 'Herrn Carl Meyer', 'Am Cordtskamp 1', '49577 Eggermühlen'], 'Sehr geehrter Herr Meyer,',
           'dass Ihre 1.000 m² Ausstellung, das Holz aus der Region und Ihre fünf Sterne bei Google auf der Startseite kaum auffallen', 'Küchenstudio', 'die Meyer Möbelwerkstätten'),
 'imbusch': (['Imbusch Einrichtungen GmbH', 'Herrn Peter Imbusch und Herrn Dennis Hemme', 'Europaring 1b', '49624 Löningen'], 'Sehr geehrter Herr Imbusch, sehr geehrter Herr Hemme,',
             'dass Ihr Kontaktformular wegen einer technischen Störung gerade nicht funktioniert und Ihre schönen Küchen erst weiter unten auf der Startseite auftauchen', 'Küchenstudio', 'Imbusch Einrichtungen'),
 'albers': (['Küchenwelt Albers', 'Frau Andrea Albers und Herrn Frank Albers', 'Ziegelstraße 12–16', '49688 Lastrup'], 'Sehr geehrte Frau Albers, sehr geehrter Herr Albers,',
            'dass die Startseite mit einem sehr langen Text beginnt und Ihre Kochschule und die reduzierten Ausstellungsküchen erst auf Unterseiten zu finden sind', 'Küchenstudio', 'die Küchenwelt Albers'),
 'kwerk': (['Küchenwerk Wallenhorst', 'Herrn Musli Zeqiri', 'Borsigstraße 6', '49134 Wallenhorst'], 'Sehr geehrter Herr Zeqiri,',
           'dass Besucher zuerst ein großes Cookie-Fenster sehen und Ihre fünf Sterne bei Google auf der Seite gar nicht auftauchen', 'Küchenstudio', 'das Küchenwerk Wallenhorst'),
 'kmeyer': (['Küchen Meyer GmbH', 'Frau Britta Meyer', 'Oeseder Feld 20', '49124 Georgsmarienhütte'], 'Sehr geehrte Frau Meyer,',
            'dass Besucher zuerst ein großes Cookie-Fenster sehen und Ihre Imagefilme, auch der aus Bramsche, erst nach einer Cookie-Freigabe abspielbar sind', 'Küchenstudio', 'Küchen Meyer'),
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
        bf = OUT / 'briefe-r12.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde12-Kuechenstudios-10.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
