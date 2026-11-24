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
 'meiners': (['Meiners Optik Uhren Schmuck', 'Herrn Hubertus Meiners', 'Königstraße 149', '26810 Westoverledingen'], 'Sehr geehrter Herr Meiners,', 'winzige Schrift, ein roter Menübalken und kleine Bilder, die sich nicht ans Handy anpassen. Sie und Birgit Meiners, Ihren Hausbesuch-Service und einen Termin-Button sieht man im ersten Bild nicht', 'Meiners'),
 'borgmann': (['Borgmann Optik', 'Herrn Ulrich Borgmann', 'Alter Markt 6', '49733 Haren (Ems)'], 'Sehr geehrter Herr Borgmann,', 'ein großes Logo, darunter die Öffnungszeiten in roter Schrift und ein langer Begrüßungstext. Ihr Team und Ihre 4,9 Sterne bei Google sieht man im ersten Bild nicht', 'Borgmann Optik'),
 'hoelscher': (['Hölscher GmbH', 'Familie Hölscher', 'Dahlhok 29', '48488 Emsbüren'], 'Sehr geehrte Familie Hölscher,', 'ein Cookie-Fenster deckt fast alles ab, dahinter ein Foto Ihres Geschäfts. Ihr großes Team und Ihre 4,9 Sterne aus 53 Google-Bewertungen sieht man im ersten Bild nicht', 'Hölscher'),
 'reher': (['Brillen + Akustik-Studio Reher GmbH', 'Herrn Daniel Reher', 'Bahnhofstraße 4', '49661 Cloppenburg'], 'Sehr geehrter Herr Reher,', 'ein Cookie-Fenster auf Englisch, dahinter ein dunkles Bild mit grauer Schrift. Ihre Familie und Ihre 4,7 Sterne bei Google sieht man im ersten Bild nicht', 'Reher'),
 'sibo': (['Sibo Müller Sehzentrum Hörzentrum Rhauderfehn GmbH', 'Herrn Sibo Müller', 'Untenende 69', '26817 Rhauderfehn'], 'Sehr geehrter Herr Müller,', 'ein Cookie-Fenster auf Englisch, dahinter ein blasses Bild mit heller Schrift. Sie selbst und Ihre 4,8 Sterne aus 284 Google-Bewertungen sieht man im ersten Bild nicht', 'Sibo Müller'),
 'lonnemann': (["Lonnemann Optik's & Hörakustik", 'Frau Mariele Lonnemann', 'Hauptstraße 26', '48480 Spelle'], 'Sehr geehrte Frau Lonnemann,', 'ein Cookie-Fenster auf Englisch, darüber ein kleines Foto und eine lange Überschrift. Ihr Team und Ihre 4,8 Sterne bei Google sieht man im ersten Bild nicht', 'Lonnemann'),
 'kloetgen': (['Optik Klötgen GmbH', 'Herrn Dirk Klötgen', 'Bahnhofstraße 21', '49832 Freren'], 'Sehr geehrter Herr Klötgen,', 'ein dunkles Bild mit Schrift, darüber ein großes Cookie-Fenster. Ihr Team, den kostenlosen Computer-Sehtest und eine Telefonnummer sieht man im ersten Bild nicht', 'Optik Klötgen'),
 'luetkeniehoff': (['Lütkeniehoff', 'Frau Miriam Altenschulte', 'Lingener Straße 8', '49835 Wietmarschen'], 'Sehr geehrte Frau Altenschulte,', 'Ihr Logo, darunter eine Überschrift und viel Fließtext. Ihre 5,0 Sterne aus 65 Google-Bewertungen und einen Termin-Button sieht man im ersten Bild nicht', 'Lütkeniehoff'),
 'buskeu': (['Optik Busse & Keute GmbH & Co. KG', 'Herrn Hans Peter Keute', 'Rhauderwieke 3–5', '26817 Rhauderfehn'], 'Sehr geehrter Herr Keute,', 'ein Teamfoto mit kleiner Schrift, darunter ein Cookie-Hinweis. Ihre 4,8 Sterne bei Google, eine Telefonnummer und einen Termin-Button sieht man im ersten Bild nicht', 'Busse & Keute'),
 'suerken': (['Optik Sürken GmbH', 'Herrn Karl-Heinz Sürken', 'Große Straße 82', '26871 Papenburg'], 'Sehr geehrter Herr Sürken,', 'ein Cookie-Fenster deckt die ganze Seite ab, dahinter ist nur das Logo zu sehen. Ihr großes Team und Ihre 4,7 Sterne aus 90 Google-Bewertungen sieht man im ersten Bild nicht', 'Sürken'),
}
ALT = Path('/home/claude/vorschau-ausgabe/alt26')

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
                f"das linke Handy unten zeigt {s['web']}, so wie ein neuer Kunde die Seite heute öffnet: {problem}. Das rechte Handy zeigt, was ich daraus gebaut habe. <b>Kostenlos und ohne dass Sie etwas bestellt haben.</b>",
                "Warum mir das wichtig erscheint: Wer eine neue Brille oder einen Hörtest sucht, schaut heute zuerst am Handy, wer in der Nähe ist, wie die Bewertungen sind und ob man schnell einen Termin bekommt. Bei Hörgeräten suchen oft auch die erwachsenen Kinder für ihre Eltern. Wer dann nur Cookie-Fenster und Fließtext sieht, ruft beim nächsten Anbieter an.",

                f"<b>Wichtig: Sie bekommen keine zweite Website.</b> Wir bringen Ihre bestehende Seite auf den neuesten Stand. Sie bleibt unter {s['web']} erreichbar, mit Ihren Inhalten und Bildern, nur schneller, am Handy sauber lesbar und mit einem klaren Weg zum Termin und einem digitalen Lotsen, der Kunden in 30 Sekunden zur passenden Leistung führt. Am Ende haben Sie eine Website, nicht zwei.",
                "Ich bin Viktor Fehl aus Bersenbrück. Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite ein, wann wir Sie erreichen. Julian ruft Sie innerhalb von 24 Stunden an. Wenn nicht, löschen wir den Entwurf wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='So sieht Ihre Website heute auf dem Handy aus.', betreff_2=f'Und so könnte sie aussehen: mein Entwurf für {kurz}.', web=s['web'], shot_alt=str(ALT / f'{k}.jpg'),
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), qr_form=str(qrf), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief18.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r26.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde26-Optiker-Werlte.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
