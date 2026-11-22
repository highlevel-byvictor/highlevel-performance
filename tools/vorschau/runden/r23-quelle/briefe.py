"""Runde 23: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'bauer': (['Praxis für Oralchirurgie', 'Herrn Dr. Christoph Bauer', 'Hauptstraße 33', '49757 Werlte'], 'Sehr geehrter Herr Dr. Bauer,', 'Ihr Logo, ein roter Knopf „Karriere bei uns“ und grauer Fließtext, unten ein Cookie-Balken. Keine Telefonnummer zum Antippen, kein Termin-Button, und Sie selbst sieht man im ersten Bild nicht', 'Ihre Praxis'),
 'malinowski': (['Zahnarztpraxis', 'Frau Melanie Malinowski', 'Zum Kavenkamp 2', '49696 Molbergen'], 'Sehr geehrte Frau Malinowski,', 'ein Cookie-Hinweis liegt über dem oberen Teil der Seite, darunter stehen Name und Adresse. Einen Termin-Button, Ihr Team oder Ihre 4,7 Sterne bei Google sieht man im ersten Bild nicht', 'Ihre Praxis'),
 'boven': (['Zahnärztliche Gemeinschaftspraxis', 'Herrn Dr. Hermann Boven', 'Bahnhofstraße 1', '49740 Haselünne'], 'Sehr geehrter Herr Dr. Boven,', 'nach dem Foto folgt ein langer, mittig gesetzter Text in dünner Schrift, und der Cookie-Hinweis verdeckt das untere Drittel. Keine Telefonnummer, kein Termin-Button im ersten Bild', 'Ihre Praxis'),
 'melso': (['Zahnärzte Meldau & Sowinski', 'Herrn Thomas Meldau und Herrn Martin Sowinski', 'Markt 12', '49740 Haselünne'], 'Sehr geehrter Herr Meldau, sehr geehrter Herr Sowinski,', 'oben steht die Telefonnummer, dann folgt ein langer Begrüßungstext. Ihr eigenes Praxislabor und Ihre 4,8 Sterne bei Google kommen im ersten Bild nicht vor', 'Ihre Praxis'),
 'lucke': (['Praxis für Zahnheilkunde', 'Frau Dr. Katharina Lucke und Herrn Dr. Tobias Lucke', 'Poststraße 17', '49624 Löningen'], 'Sehr geehrte Frau Dr. Lucke, sehr geehrter Herr Dr. Lucke,', 'der Cookie-Dialog verdeckt die untere Hälfte, darüber ein Stockfoto und ein Auswahlfeld statt eines Menüs. Sie beide sieht man nicht, und in der Fußzeile steht das Jahr 2015', 'Ihre Praxis'),
 'roelleke': (['Zahnarztpraxis', 'Herrn Dr. Christian Rölleke', 'Kolpingstraße 8', '49716 Meppen'], 'Sehr geehrter Herr Dr. Rölleke,', 'ein großes Logo, „Willkommen“ und Fließtext. Telefonnummer und Termin-Button fehlen im ersten Bild, und Ihr Team sieht man nicht', 'Ihre Praxis'),
 'leicht': (['Zahnarztpraxis Leicht', 'Herrn Ulrich Leicht und Herrn Reemt Leicht', 'Haselünner Str. 53', '49716 Meppen'], 'Sehr geehrte Herren Leicht,', 'ein blauer Cookie-Kasten füllt fast den ganzen Bildschirm, bevor man etwas von Ihrer Praxis sieht. Ihr Meisterlabor und die Telefonnummer kommen im ersten Bild nicht vor', 'Ihre Praxis'),
 'bode': (['Zahnärzte Bode', 'Herrn Dr. Peter Bode und Herrn Maximilian Bode', 'Am Neuen Markt 78', '49716 Meppen'], 'Sehr geehrter Herr Dr. Bode, sehr geehrter Herr Bode,', 'Ihr Logo, ein kleines Bild vom Empfang und Text. Keine Telefonnummer, kein Termin-Button, und Sie beide sieht man im ersten Bild nicht', 'Ihre Praxis'),
 'franke': (['Zahnarztpraxis', 'Frau Dr. Karin Franke und Herrn Dr. Lutz Franke', 'Lessingstraße 12', '49716 Meppen'], 'Sehr geehrte Frau Dr. Franke, sehr geehrter Herr Dr. Franke,', 'die Seite ist für den großen Bildschirm gebaut und erscheint winzig klein. Man muss mit zwei Fingern aufziehen, um überhaupt etwas zu lesen, und Ihre 5,0 Sterne bei Google sieht niemand', 'Ihre Praxis'),
 'degener': (['Zahnarztpraxis', 'Frau Dr. Carolin Degener', 'Bookgastweg 67', '26169 Friesoythe'], 'Sehr geehrte Frau Dr. Degener,', 'Ihr Name über einem dunklen Foto, darunter ein Stockfoto. Telefonnummer, Sprechzeiten und Termin-Button fehlen im ersten Bild, und Ihr Team sieht man nicht', 'Ihre Praxis'),
}
ALT = Path('/home/claude/vorschau-ausgabe/alt23')

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
        bf = OUT / 'briefe-r23.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde23-Zahnarztpraxen-Werlte-40km.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
