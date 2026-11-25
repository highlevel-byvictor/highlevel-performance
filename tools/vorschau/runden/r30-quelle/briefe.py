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
 'nuss': (['Physiotherapie Oliver Nuss', 'Herrn Oliver Nuss', 'Lindenstraße 11', '49593 Bersenbrück'], 'Sehr geehrter Herr Nuss,', 'ein Logo, eine lange Überschrift und ein kleines Foto vom Eingang. Ihr achtköpfiges Team, Ihre 4,7 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'Physiotherapie Nuss'),
 'vogel': (['Praxis für Osteopathie & Physiotherapie', 'Frau Nicole Vogel', 'Lange Straße 3', '49610 Quakenbrück'], 'Sehr geehrte Frau Vogel,', 'neongelbe Schrift liegt über einem dunklen Foto und ist kaum zu lesen. Ihr Olympia-Gold mit den 3x3-Basketballerinnen, Ihre 4,8 Sterne bei Google und eine Telefonnummer sieht man im ersten Bild nicht', 'die Praxis Vogel'),
 'theilmann': (['Praxis für Physiotherapie', 'Herrn Matthias Theilmann', 'Achtern Hoff 23', '49401 Damme'], 'Sehr geehrter Herr Theilmann,', 'ein Cookie-Fenster auf Englisch deckt fast alles ab. Ihr Team in Grün, Ihre 5,0 Sterne bei Google und Ihre Stellenanzeige sieht man im ersten Bild nicht', 'die Praxis Theilmann'),
 'damme': (['Physiotherapie Centrum Damme GmbH', 'Frau Kerstin Trenk', 'Lindenstraße 10–12', '49401 Damme'], 'Sehr geehrte Frau Trenk,', 'ein Foto vom Flur, darunter ein Begrüßungstext. Ihr Bewegungsbad, Ihre 5,0 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'das Physiotherapie Centrum Damme'),
 'seebeck': (['Praxis für Physiotherapie', 'Thomas Seebeck und Kerstin Ortmann-Seebeck', 'Clemens-August-Straße 3', '49413 Dinklage'], 'Sehr geehrte Frau Ortmann-Seebeck, sehr geehrter Herr Seebeck,', 'Ihr Praxisname in großer Schrift über einem Wasserbild, darunter ein Cookie-Hinweis. Sie beide und einen Termin-Button sieht man im ersten Bild nicht', 'die Praxis Seebeck'),
 'athletics': (['ATHLETICS Functional Training & Physiotherapie', 'Herrn Horst Angrick', 'Hansastraße 1a', '49134 Wallenhorst'], 'Sehr geehrter Herr Angrick,', 'ein dunkler Hintergrund mit sehr kleiner Schrift, die man am Handy kaum lesen kann. Ihre 4,9 Sterne aus 120 Google-Bewertungen und Ihre 24-Stunden-Hilfe sieht man im ersten Bild nicht', 'ATHLETICS'),
 'physioplus': (['PhysioPlus', 'Herrn Oliver Slak', 'Brinkstraße 1–3', '49393 Lohne (Oldenburg)'], 'Sehr geehrter Herr Slak,', 'ein Logo, ein Menü und ein grünes Cookie-Fenster, das die halbe Seite abdeckt. Sie selbst, Ihre 4,8 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'PhysioPlus'),
 'henke': (['Praxis für Physiotherapie', 'Herrn Ulrich Henke', 'Venner Straße 14', '49565 Bramsche'], 'Sehr geehrter Herr Henke,', 'ein blauer Kasten mit dem Praxisnamen und ein Teamfoto. Dass Sie als Heilpraktiker auch ohne Rezept behandeln, eine Telefonnummer und einen Termin-Button sieht man im ersten Bild nicht', 'die Praxis Henke'),
 'redzichfrye': (['Physiotherapie Redzich-Frye', 'Frau Kerstin Redzich-Frye', 'Lindenstraße 56a', '49191 Belm'], 'Sehr geehrte Frau Redzich-Frye,', 'Ihr Logo und die Adresse auf weißer Fläche. Ihr Team, Ihre Erfahrung seit 1989 und einen Termin-Button sieht man im ersten Bild nicht', 'die Physiotherapie Redzich-Frye'),
 'koerperhelden': (['Körperhelden Physiotherapie GbR', 'Christina Wörmann und Inga Bolz', 'Jeggener Straße 40', '49191 Belm'], 'Sehr geehrte Frau Wörmann, sehr geehrte Frau Bolz,', 'ein Foto vom Hof und ein Willkommenstext. Ihre Intensivwochen, Ihre 5,0 Sterne bei Google und einen Weg zur Anfrage sieht man im ersten Bild nicht', 'die Körperhelden'),
 'pflug': (['Praxis für Physiotherapie', 'Herrn Andreas Pflug', 'August-Hölscher-Straße 45', '49080 Osnabrück'], 'Sehr geehrter Herr Pflug,', 'ein dunkler Kasten mit dem Praxisnamen und ein graues Menü. Ihre Öffnungszeiten ab 7 Uhr, Ihre 5,0 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'die Praxis Pflug'),
 'physioportal': (['Nickels PhysioPortal an der Soeste', 'Herrn Alexander Nickels', 'Mühlenstraße 27', '49661 Cloppenburg'], 'Sehr geehrter Herr Nickels,', 'ein dunkles Fenster mit der Stellenanzeige liegt über der ganzen Seite. Ihre schönen Räume, Ihr Team und Ihre 4,7 Sterne bei Google sieht man im ersten Bild nicht', 'das PhysioPortal'),
 'lienert': (['Therapiezentrum Lienert', 'Silke und Ralf Lienert', 'Wankelstraße 2', '49356 Diepholz'], 'Sehr geehrte Frau Lienert, sehr geehrter Herr Lienert,', 'weiße Schrift auf einem dunklen, bunten Gemälde, schwer zu lesen. Ihr großes Team und Ihre 4,8 Sterne aus 140 Google-Bewertungen sieht man im ersten Bild nicht', 'das Therapiezentrum Lienert'),
 'bissendorf': (['PhysioTeam Bissendorf', 'Frau Iris Campbell', 'Osnabrücker Straße 5', '49143 Bissendorf'], 'Sehr geehrte Frau Campbell,', 'ein Foto vom Wartebereich und gelbe Schrift auf Weiß, die schwer zu lesen ist. Ihre 4,9 Sterne bei Google, eine Telefonnummer und einen Termin-Button sieht man im ersten Bild nicht', 'das PhysioTeam Bissendorf'),
 'westerhoff': (['Physiotherapie Westerhoff', 'Frau Heike Zwanefeld', 'Overbergstraße 6', '49429 Visbek'], 'Sehr geehrte Frau Zwanefeld,', 'die Seite passt sich dem Handy nicht an. Schrift und Logo sind winzig, das Foto ist abgeschnitten. Ihre 4,6 Sterne aus 29 Google-Bewertungen sieht man im ersten Bild nicht', 'die Physiotherapie Westerhoff'),
 'hoerstel': (['Therapiezentrum Hörstel', 'Herrn Eric ten Bos', 'Alte Glashüttenstraße 2', '48477 Hörstel'], 'Sehr geehrter Herr ten Bos,', 'eine Fehlermeldung statt Ihrer Startseite: „Not Acceptable“. Ihr Team und Ihre 4,6 Sterne bei Google sieht man nicht', 'das Therapiezentrum Hörstel'),
 'imkamp': (['Therapiezentrum Im Kamp', 'Frau Yana Komning', 'Im Kamp 57', '49205 Hasbergen'], 'Sehr geehrte Frau Komning,', 'eine Stellenanzeige und die Öffnungszeiten in Kästen. Ihre Praxis, Ihre 5,0 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'das Therapiezentrum Im Kamp'),
 'physioaktiv': (['PhysioAktiv', 'Frau Tanja Sudowe', 'Osterheide 7', '49124 Georgsmarienhütte'], 'Sehr geehrte Frau Sudowe,', 'ein dunkles Foto mit grauer Schrift, darüber ein Cookie-Fenster. Ihr Team, Ihre 5,0 Sterne aus 20 Google-Bewertungen und einen Termin-Button sieht man im ersten Bild nicht', 'PhysioAktiv'),
 'reinermann': (['Physiotherapie Reinermann', 'Herrn Rudolf Reinermann', 'Schorfteichstraße 13', '49584 Fürstenau'], 'Sehr geehrter Herr Reinermann,', 'ein orangefarbener Balken und ein Bild von Händen aus einer Bilddatenbank. Ihr zehnköpfiges Team, Ihre 4,9 Sterne bei Google und einen Termin-Button sieht man im ersten Bild nicht', 'die Physiotherapie Reinermann'),
 'troebs': (['Praxis für Physiotherapie', 'Frau Stefanie Tröbs-Kütemann', 'Richtweg 1', '49356 Diepholz'], 'Sehr geehrte Frau Tröbs-Kütemann,', 'weiße Schrift auf türkisfarbenem Grund und ein Bild mit Steinen aus einer Bilddatenbank. Ihr Team und Ihren großen Trainingsbereich sieht man im ersten Bild nicht', 'die Praxis Tröbs'),
}
ALT = Path('/home/claude/vorschau-ausgabe/alt28')

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
                "Warum mir das wichtig erscheint: Wer Rückenschmerzen hat oder ein Rezept bekommt, sucht heute zuerst am Handy, welche Praxis in der Nähe ist, wie die Bewertungen sind und ob man schnell einen Termin bekommt. Auch Therapeuten auf Stellensuche schauen zuerst auf Ihre Website. Mein Entwurf holt deshalb Ihre Bewertungen nach vorn und bittet zufriedene Patienten um neue.",

                f"<b>Wichtig: Sie bekommen keine zweite Website.</b> Wir bringen Ihre bestehende Seite auf den neuesten Stand. Sie bleibt unter {s['web']} erreichbar, mit Ihren Inhalten und Bildern, nur schneller, am Handy sauber lesbar und mit einem klaren Weg zum Termin und einem digitalen Lotsen, der Patienten in 30 Sekunden zur passenden Leistung führt. Am Ende haben Sie eine Website, nicht zwei.",
                "Ich bin Viktor Fehl aus Bersenbrück. Gefällt Ihnen der Entwurf? Dann tragen Sie unten auf der Seite ein, wann wir Sie erreichen. Julian ruft Sie innerhalb von 24 Stunden an. Wenn nicht, löschen wir den Entwurf wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='So sieht Ihre Website heute auf dem Handy aus.', betreff_2=f'Und so könnte sie aussehen: mein Entwurf für {kurz}.', web=s['web'], shot_alt=str(ALT / f'{k}.jpg'),
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), qr_form=str(qrf), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief18.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r28.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde28-Physiotherapie.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
