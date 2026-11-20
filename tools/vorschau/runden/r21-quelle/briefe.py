"""Runde 21: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'alfhausen': (['Zahnarztpraxis Alfhausen', 'Herrn Dr. Hermann Meyer und Frau Ines Gennermann', 'In den Gärten 1', '49594 Alfhausen'], 'Sehr geehrter Herr Dr. Meyer, sehr geehrte Frau Gennermann,', 'oben das Menü als lose Wörter, darunter „Herzlich willkommen auf unserer Internetpräsenz“ und ein Cookie-Balken. Keine Telefonnummer zum Antippen, kein Termin-Button, und dass Sie von 7 bis 19 Uhr geöffnet haben, sieht man im ersten Bild nicht', 'Ihre Praxis'),
 'austermann': (['Zahnarztpraxis', 'Frau Dr. Stephanie Austermann', 'Lutterdamm 68-70', '49565 Bramsche'], 'Sehr geehrte Frau Dr. Austermann,', 'ein Stockfoto, „Herzlich Willkommen“ und ein langer Text in kleiner Schrift. Kein Termin-Button, und Ihr eigenes Labor, das kaum eine Praxis hat, kommt im ersten Bild nicht vor', 'Ihre Praxis'),
 'badbergen': (['Zahnarztpraxis Am Markt', 'Frau Sigrid E. Meyer', 'Am Markt 1', '49635 Badbergen'], 'Sehr geehrte Frau Meyer,', 'Sprechzeiten und Telefonnummer stehen da, lassen sich aber nicht antippen, und unten schiebt sich die Fußzeile über den Text. Ihre Leistungen von der Zahnreinigung bis zum Implantat findet man erst im Menü', 'Ihre Praxis'),
 'rieste': (['Zahnarztpraxis', 'Frau Galina Spasova', 'Malgartener Str. 5', '49597 Rieste'], 'Sehr geehrte Frau Spasova,', 'ein Stockfoto und ein langer, mittig gesetzter Text. Eine Telefonnummer oder einen Termin-Button sieht man im ersten Bild nicht', 'Ihre Praxis'),
 'kiefert': (['Zahnarztpraxis', 'Herrn Thomas Kiefert', 'Lindenstr. 1', '49434 Neuenkirchen-Vörden'], 'Sehr geehrter Herr Kiefert,', 'eine grüne Fläche mit kaum lesbarer Schrift, darunter ein Cookie-Hinweis in Grün auf Grün. Keine Telefonnummer, kein Termin-Button, keine Leistung im ersten Bild', 'Ihre Praxis'),
 'coenen': (['Zahnarztpraxis', 'Herrn Dr. Michael Coenen', 'Aslager Straße 6', '49577 Ankum'], 'Sehr geehrter Herr Dr. Coenen,', 'oben Telefonnummer und Adresse in kleiner Schrift, dann deckt der Cookie-Dialog mehr als die Hälfte des Bildschirms ab. Einen Termin-Button sieht man nicht, und Ihr Leitsatz „Zähne erhalten statt ersetzen“ auch nicht', 'Ihre Praxis'),
 'tischler': (['Zahnarztpraxis', 'Herrn Carsten Tischler', 'Mühlenstraße 32', '49401 Damme'], 'Sehr geehrter Herr Tischler,', 'nach Logo und Teamfoto folgt ein langer Fließtext, über dem ein grüner Cookie-Kasten liegt. Kein Termin-Button, und Ihr Schwerpunkt Angstpatienten geht im Text unter', 'Ihre Praxis'),
 'lefert': (['Zahnärztliche Gemeinschaftspraxis', 'Frau Dr. Constanze Lefert und Frau Jana Kohl', 'Bahnhofstraße 9', '49413 Dinklage'], 'Sehr geehrte Frau Dr. Lefert, sehr geehrte Frau Kohl,', 'der Cookie-Dialog füllt den ganzen Bildschirm, bevor man etwas von Ihrer Praxis sieht. In der Fußzeile steht das Jahr 2016', 'Ihre Praxis'),
 'osada': (['Zahnärzte Osada', 'Frau Tina-Vanessa Osada und Herrn Falk Osada', 'Bahnhofstraße 3', '49401 Damme'], 'Sehr geehrte Frau Osada, sehr geehrter Herr Osada,', 'Ihr Logo, ein Kinderfoto, dann eine graue Fläche. Keine Telefonnummer, keine Sprechzeiten und kein Termin-Button im ersten Bild', 'Ihre Praxis'),
 'natorp': (['Zahnarztpraxis', 'Frau Dr. Michaela Natorp', 'Große Straße 32 b', '49451 Holdorf'], 'Sehr geehrte Frau Dr. Natorp,', 'die Seite ist für den großen Bildschirm gebaut und erscheint winzig klein. Man muss mit zwei Fingern aufziehen, um Telefonnummer oder Sprechzeiten zu lesen', 'Ihre Praxis'),
}
ALT = Path('/home/claude/vorschau-ausgabe/alt20')

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
            qrf = OUT / f'{sl}-qr-form.svg'; segno.make(url + '#hlp-anfrage', error='m').save(str(qrf), scale=10, border=0, dark='#0A1A3A')
            an, anrede, problem, kurz = BRIEF[k]
            absaetze = [
                f"das linke Handy unten zeigt {s['web']}, so wie ein neuer Patient die Seite heute öffnet: {problem}. Das rechte Handy zeigt, was ich daraus gebaut habe. <b>Kostenlos und ohne dass Sie etwas bestellt haben.</b>",
                "Warum mir das wichtig erscheint: 70 bis 80 Prozent der Patienten suchen ihren Zahnarzt heute online, die meisten am Smartphone (zm, Zahnärztliche Mitteilungen 21/2023). Und gut jeder Zweite geht mit Anspannung zum Zahnarzt (Umfrage IDZ/Allensbach). Wer neu sucht, entscheidet am Handy in Sekunden, wo er sich gut aufgehoben fühlt.",
                f"<b>Wichtig: Sie bekommen keine zweite Website.</b> Wir bringen Ihre bestehende Seite auf den neuesten Stand. Sie bleibt unter {s['web']} erreichbar, mit Ihren Inhalten und Bildern, nur schneller, am Handy sauber lesbar und mit einem klaren Weg zum Termin und einem Praxis-Lotsen, der Patienten in 30 Sekunden zur passenden Leistung führt. Am Ende haben Sie eine Website, nicht zwei.",
                "Ich bin Viktor Fehl aus Bersenbrück. Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite ein, wann wir Sie erreichen. Julian ruft Sie innerhalb von 24 Stunden an. Wenn nicht, löschen wir den Entwurf wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='So sieht Ihre Website heute auf dem Handy aus.', betreff_2=f'Und so könnte sie aussehen: mein Entwurf für {kurz}.', web=s['web'], shot_alt=str(ALT / f'{k}.jpg'),
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), qr_form=str(qrf), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief18.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r21.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde21-Zahnarztpraxen-30km.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
