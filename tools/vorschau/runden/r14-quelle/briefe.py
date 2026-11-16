"""Runde 14: QA, Screenshots, QR-Codes und Briefe (brief.html.j2) für die handgebauten Seiten."""
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
 'saller': (['Fahrschule K.H. Saller', 'Herrn Henrik Grover', 'Hauptstraße 64', '49635 Badbergen'], 'Sehr geehrter Herr Grover,',
            'dass mitten auf der Startseite ein technischer Hinweis „PHP-Core geschützt“ steht, Ihre 4,8 Sterne fehlen und Fahrzeuge wie Oskar und Obelix erst auf einer Unterseite auftauchen', 'Fahrschule Saller'),
 'albers': (['Fahrschule Bernhard Albers', 'Herrn Bernhard Albers', 'Postfach 1343', '49577 Ankum'], 'Sehr geehrter Herr Albers,',
            'dass die Seite seit 2011 kaum verändert wurde, am Handy nicht passt und auf der Startseite außer zwei Kacheln nichts über Ihre Fahrschule steht', 'die Fahrschule Albers'),
 'hp66': (['Fahrschule HP 66', 'Herrn Peter Hackmann', 'Kirchstraße 1', '49638 Nortrup'], 'Sehr geehrter Herr Hackmann, sehr geehrte Frau Hackmann-Paschert,',
          'dass Besucher Ihre Fahrzeuge sehen, aber nirgends ein Foto von Ihnen beiden, obwohl Ihre Fahrschüler in den 5,0-Sterne-Bewertungen genau Sie persönlich loben', 'die Fahrschule HP 66'),
 'beckermann': (['H. Beckermann GmbH', 'Fahrschule Beckermann', 'Herrn Jörg Beckermann', 'Osnabrücker Straße 16', '49565 Bramsche'], 'Sehr geehrter Herr Beckermann,',
                'dass zuerst ein großes Cookie-Fenster erscheint und Ihre eindrucksvolle Flotte vom Roller bis zum Reisebus auf der Startseite gar nicht zu sehen ist', 'die Fahrschule Beckermann'),
 'tepe': (['Fahrschule Tepe GmbH', 'Herrn Reinhold Tepe', 'Mühlenstraße 12', '49565 Bramsche'], 'Sehr geehrter Herr Tepe,',
          'dass Ihr Fahrsimulator, das stärkste Mittel gegen die Angst vor der ersten Fahrstunde, nur im Fließtext steht und Ihre 4,7 Sterne nicht auftauchen', 'die Fahrschule Tepe'),
 'city': (['City-Fahrschule Michalowski GmbH', 'Herrn Simon Michalowski', 'Möserstraße 31', '49074 Osnabrück'], 'Sehr geehrter Herr Michalowski,',
          'dass der erste Bildschirm von einem Cookie-Fenster verdeckt wird und Ihre 50 Jahre Geschichte und Ihr Team aus 30 Leuten erst auf Unterseiten zu finden sind', 'die City Fahrschule'),
 'moschitz': (['Moschitz … die Fahrschule', 'Herrn Gaston Moschitz und Frau Heide Moschitz', 'Natruper Straße 232', '49090 Osnabrück'], 'Sehr geehrter Herr Moschitz, sehr geehrte Frau Moschitz,',
              'dass Ihr stärkstes Angebot, die komplette Theorie in sieben Tagen, auf der Startseite gar nicht vorkommt und die nächsten Kurstermine erst auf einer Unterseite stehen', 'Moschitz'),
 'kindermann': (['Fahrschule Kindermann', 'Herrn André Kindermann', 'Sutthauser Straße 87', '49080 Osnabrück'], 'Sehr geehrter Herr Kindermann,',
                'dass Ihr Antragsservice kaum auffällt und Fahrschüler mit ausländischem Führerschein, die Sie laut Bewertungen besonders schätzen, nirgends direkt angesprochen werden', 'die Fahrschule Kindermann'),
 'beinke': (['Fahrschule Beinke', 'Herrn Thomas Beinke', 'Rosenplatz 22', '49074 Osnabrück'], 'Sehr geehrter Herr Beinke,',
            'dass Ihre 4,9 Sterne aus 197 Bewertungen und Ihr Unterricht auf Englisch, der in den Bewertungen immer wieder gelobt wird, auf der Startseite nicht auftauchen', 'die Fahrschule Beinke'),
 'eggert': (['Fahrschule St. Eggert', 'Herrn Stefan Eggert', 'Osnabrücker Straße 5', '49201 Dissen am Teutoburger Wald'], 'Sehr geehrter Herr Eggert,',
            'dass Ihre neue Frauenfahrschule auf der Startseite noch mit „Zeiten folgen“ steht und Besucher sich zwischen vielen Adressen erst zurechtfinden müssen', 'die Fahrschule Eggert'),
 'simon': (['Fahrschule Simon GbR', 'Frau Hildegard Simon und Herrn Jörn Simon', 'Am Langenkamp 2', '49143 Bissendorf'], 'Sehr geehrte Frau Simon, sehr geehrter Herr Simon,',
           'dass die Seite am Handy nicht angepasst ist und der Satz mit Ihren Ausbildungsklassen sechsmal untereinander auf der Startseite steht', 'die Fahrschule Simon'),
 'loheide': (['Loheide + Kraft Fahrschulen GmbH', 'Herrn Christoph Loheide und Herrn Wladimir Kraft', 'Kronenbrink 4', '49179 Ostercappeln'], 'Sehr geehrter Herr Loheide, sehr geehrter Herr Kraft,',
             'dass beim Öffnen zuerst ein großes Datenschutz-Fenster erscheint und Ihre 4,9 Sterne, Ihr Team und Ihre Hall of Fame erst auf Unterseiten zu finden sind', 'Loheide + Kraft'),
 'ludwig': (['Fahrschule CL', 'Herrn Carsten Ludwig', 'Bremer Straße 16', '49163 Bohmte'], 'Sehr geehrter Herr Ludwig,',
            'dass die Startseite vor allem aus einem Cookie-Fenster und Bildern ohne Text besteht und die guten Bewertungen über Sie und Detlev nicht vorkommen', 'die Fahrschule CL'),
 'napierski': (['Fahrschule Napierski GmbH', 'Herrn Aaron Napierski und Herrn Klaus Napierski', 'Poststraße 12', '49624 Löningen'], 'Sehr geehrter Herr Aaron Napierski, sehr geehrter Herr Klaus Napierski,',
               'dass Ihr starkes Team zwar zu sehen ist, Ihr nächster Kurs am 7. Dezember und eine schnelle Anmeldung aber nicht im ersten Bildschirm stehen', 'die Fahrschule Napierski'),
 'witte': (['Fahrschule Burkard Witte & Sohn', 'Herrn Burkard Witte', 'Eisenbahnweg 1', '49661 Cloppenburg'], 'Sehr geehrter Herr Witte,',
           'dass Ihr einzigartiger Theorieraum mit dem Wandbild und Ihre 4,7 Sterne aus 66 Bewertungen auf der Startseite kaum auffallen', 'die Fahrschule Witte'),
 'mammen': (['Fahrschule Dirk Mammen', 'Herrn Dirk Mammen', 'Eschstraße 1', '49661 Cloppenburg'], 'Sehr geehrter Herr Mammen,',
            'dass auf der Startseite fast nur Grafiken und Ortsnamen zu sehen sind und Ihre Ratenzahlung, gerade jetzt Ihr stärkstes Argument, nur als Werbebanner auftaucht', 'die Fahrschule Mammen'),
 'schulz': (['Fahrschule Schulz', 'Herrn Björn Stratemann', 'Deichstraße 14', '49393 Lohne'], 'Sehr geehrter Herr Stratemann,',
            'dass die Startseite mit Bildunterschriften statt einer klaren Botschaft startet und Ihre 4,9 Sterne und die kostenlosen Snacks im Unterricht kaum auffallen', 'die Fahrschule Schulz'),
 'moss': (['Fahrschule Moss', 'Herrn Robert Moss', 'Allensteiner Straße 1', '49377 Vechta'], 'Sehr geehrter Herr Moss,',
          'dass vorne vor allem Preise stehen, die bald ohnehin jeder in der Datenbank vergleicht, während Ihre Hall of Fame und Ihr Team erst weiter unten kommen', 'die Fahrschule Moss'),
 'christians': (['Christians Fahrschul-Team', 'Herrn Christian Gericke', 'Lindenstraße 18', '49393 Lohne'], 'Sehr geehrter Herr Gericke,',
                'dass der erste Bildschirm von einem großen Datenschutz-Fenster verdeckt wird und Ihre 5,0 Sterne aus 47 Bewertungen nirgends zu sehen sind', 'Christians Fahrschul-Team'),
 'kaiser': (['Fahrschule Kaiser GmbH', 'Herrn Christoph Kaiser', 'Dinklager Straße 77', '49393 Lohne'], 'Sehr geehrter Herr Kaiser,',
            'dass Besucher zuerst ein Pop-up zu einem bereits vergangenen Crashkurs und ein Cookie-Fenster sehen, während Ihre 5,0 Sterne und Ihre Flotte erst später kommen', 'die Kaiser Fahrschule'),
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
                "Gefällt Ihnen der Entwurf? Julian von unserem Hotline-Service vereinbart gern ein <b>kostenloses Erstgespräch</b> mit Ihnen. Wenn nicht, löschen wir ihn einfach wieder.",
            ]
            briefe.append(dict(anschrift=an, anrede=anrede, betreff_1='Warum Fahrschüler gerade online entscheiden.', betreff_2=f'Ein kostenloser Website-Entwurf für {kurz}.',
                               absaetze=[Markup(a) for a in absaetze], shot_desktop=str(sd), shot_mobile=str(sm), qr=str(qr), url_kurz='highlevel-performance.de/vorschau/' + sl))
            print('OK', k, url)
        jq = OUT / 'julian-qr.svg'; segno.make('tel:+4917663213512', error='m').save(str(jq), scale=10, border=0, dark='#0A1A3A')
        html = env.get_template('brief.html.j2').render(briefe=briefe, root=str(ROOT), datum=datetime.date.today().strftime('%d.%m.%Y'), julian_tel=JT, julian_qr=str(jq))
        bf = OUT / 'briefe-r14.html'; bf.write_text(html)
        pg = br.new_page(); pg.goto(bf.as_uri()); pg.wait_for_timeout(1500)
        pdf = OUT / 'HLP-Briefe-Runde14-Fahrschulen-20.pdf'
        pg.pdf(path=str(pdf), format='A4', print_background=True, prefer_css_page_size=True); br.close()
    print('PDF', pdf); print('FEHLER', json.dumps(fehler, ensure_ascii=False))

if __name__ == '__main__':
    run(sys.argv[1:] or list(SITES))
