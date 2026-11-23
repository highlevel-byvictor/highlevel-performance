"""Akquise-Agent 23.11.2026 (Montag, Fahrschulen): 5 Fahrschulen in NRW mit Instagram und veralteter Website.
Texte, Leistungen, Bilder und Videos stammen von den Originalseiten. Keine erfundenen Preise oder Stimmen.
Google-Sterne werden nicht gezeigt (nicht geprüft). Stimmen nur von den eigenen Kundenstimmen-Seiten der Betriebe."""
from common import *
SITES = {}

def stimmen(id, ey, h2, items, src, cls=''):
    c = ''.join(f'<figure class="vz" data-r><blockquote>„{t}“</blockquote><figcaption><b>{n}</b>{x}</figcaption></figure>' for t, n, x in items)
    return f'<section class="sec vzs {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2)}</div><div class="vz-g">{c}</div><p class="note">{src}</p></div></section>'

def mini_team(id, ey, h2, lead, people, cls=''):
    p = ''.join(f'<figure class="mt" data-r><img src="img/{i}" alt="{E(n)}" loading="lazy" style="object-position:{pos}"><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for i, n, r, pos in people)
    return f'<section class="sec mts {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="mt-g">{p}</div></div></section>'

def standorte(id, ey, h2, lead, items, cls=''):
    r = ''.join(f'<article class="so" data-r><h3>{a}</h3><p>{b}</p><span>{c}</span><a href="{MAPL(m)}" target="_blank" rel="noopener">Route planen ↗</a></article>' for a, b, c, m in items)
    return f'<section class="sec sos {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="so-g">{r}</div></div></section>'

BASE = '''
.btn{border-radius:999px!important}.sec{scroll-margin-top:80px}@media(max-width:900px){.hx .g2{display:none}}
.vz-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;margin-top:36px}
.vz{margin:0;background:var(--s);border-left:5px solid var(--p);padding:26px 26px 22px;box-shadow:0 14px 34px rgba(0,0,0,.06)}
.vz blockquote{margin:0;font-size:17px;line-height:1.6}.vz figcaption{margin-top:16px;font-size:14px;color:var(--mute)}.vz figcaption b{display:block;color:var(--ink);font-size:16px}
.vzs .note{margin-top:18px;font-size:13px;color:var(--mute)}
.mt-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:26px 20px;margin-top:36px}
.mt{margin:0;text-align:center}.mt img{width:150px;height:150px;border-radius:50%;object-fit:cover;display:block;margin:0 auto 14px;border:4px solid #fff;box-shadow:0 0 0 2px var(--p)}
.mt b{display:block;font:700 17px var(--fh)}.mt span{display:block;font-size:14px;color:var(--mute);margin-top:4px;line-height:1.4}
.so-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;margin-top:34px}
.so{background:var(--s);padding:24px 24px 22px;border-top:5px solid var(--p)}.so h3{font:800 24px var(--fh);margin:0 0 8px}.so p{margin:0;color:var(--mute)}
.so span{display:block;margin-top:12px;font-weight:700;font-size:15px}.so a{display:inline-block;margin-top:12px;color:var(--p);font-weight:700;text-decoration:none}
'''

# ───────────── 1 · Fahrschule am Stadtbrunnen, Greven ─────────────
def b_stadtbrunnen(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-gla.jpg', pos='50% 60%', quick=['auto', 'moto', 'anh', 'lkw'],
        ey='Fahrschule am Stadtbrunnen · Greven seit 1989',
        h1='Wir machen <em>Greven mobil.</em>',
        sub='Ausbildung aller Klassen mitten in der Grevener Innenstadt, in klimatisierten Räumen. Vom Roller bis zum Reisebus, in lockerer Atmosphäre statt Schulbankdrücken.',
        g1=('Seit 1989', 'in der Grevener Innenstadt')))
        + marquee(['AM · A1 · A2 · A', 'B · B197 · BE · B96', 'C · CE', 'D Bus', 'Berufskraftfahrer', 'Fahr-Fitness-Check 50+', 'Sicherheitstraining', 'Geschenkgutscheine'], 'hm')
        + klassen('klassen', 'Fahrerlaubnisklassen', 'Vom Roller <em>bis zum Reisebus.</em>', 'Tippen Sie auf eine Klasse, dann prüft Birte mit Ihnen in 30 Sekunden, ob sie passt.', [
            ('AM', 'Roller', 'Kleinkrafträder bis 45 km/h, schon ab 15 Jahren.', 'ab 15', 'roller'),
            ('A1 · A2 · A', 'Motorrad', 'Von der 125er bis zur offenen Maschine, auf Honda und KTM.', 'ab 16', 'moto'),
            ('B · B197', 'Auto', 'Schalter oder Automatik mit Schlüsselzahl B197 auf Mercedes A-Klasse, GLA und GLC.', 'ab 17', 'auto'),
            ('BE · B96', 'Anhänger', 'Mit dem Mercedes GLC und Anhänger.', 'ab 18', 'anh'),
            ('C · CE', 'Lkw', 'Auf dem MAN TGA 360 Gliederzug.', 'ab 18', 'lkw'),
            ('D', 'Bus', 'Im Setra-Reisebus.', 'ab 21', 'lkw')], 'dk')
        + story('ueber', 'Wir über uns', 'Fahren lernen <em>ohne Schulbankdrücken.</em>', [
            'Die Fahrschule am Stadtbrunnen wurde 1989 von Herbert Sobeck und Birgit Gnoth-Sobeck in Greven gegründet, im Herzen des Münsterlandes.',
            'Von Anfang an wollten wir anders sein als die üblichen Fahrschulen: lockere Atmosphäre statt „Schulbankdrücken ohne Spaß und Freude“. In moderner Einrichtung und mit viel Liebe zu unserem Beruf vermitteln wir die Lerninhalte kompetent und schnell verständlich.'],
            'u-raum.jpg', cap='Unser Unterrichtsraum an der Münsterstraße', tl=[('1989', 'gegründet in Greven'), ('Di &amp; Do', 'Theorie 18:30 – 20:00 Uhr'), ('klimatisiert', 'Räume in der Innenstadt')], rev=True)
        + flotte('fahrzeuge', 'Unsere Ausbildungsfahrzeuge', 'Mercedes, Honda, KTM, <em>MAN und Setra.</em>', 'Für jede Klasse das passende Fahrzeug.', [
            ('f-a.jpg', 'Mercedes A 200 d', 'Klasse B · Schaltwagen', '50% 60%'),
            ('f-gla.jpg', 'Mercedes GLA 200 d', 'Klasse B · Automatik (B197)', '50% 60%'),
            ('f-glc.jpg', 'Mercedes GLC + Anhänger', 'Klasse BE / B96', '50% 60%'),
            ('f-hornet.jpg', 'Honda Hornet 750', 'Klasse A', '50% 60%'),
            ('f-ktm.jpg', 'KTM Duke 125', 'Klasse A1 / B196', '50% 60%'),
            ('f-setra.jpg', 'Setra', 'Klasse D', '50% 60%')])
        + story('team', 'Ihre Fahrlehrer', 'Zwei Gesichter, <em>seit 1989.</em>', [
            '<b>Herbert Sobeck</b> ist Fahrlehrer aller Klassen und Industriemeister Kraftverkehr. Mobil: 0172 7057984.',
            '<b>Birgit Gnoth-Sobeck</b> ist Fahrlehrerin für die Klassen B und BE. Mobil: 0172 7057985.'],
            'h-team.jpg', cap='Herbert Sobeck und Birgit Gnoth-Sobeck', cls='alt')
        + svc('service', 'Service', 'Mehr als <em>nur der Führerschein.</em>', 'Auch nach der Prüfung sind wir für Sie da.', [
            ('Berufskraftfahrer', 'Fortbildungen für Lkw- und Busfahrer.'),
            ('Generation 50+', 'Fahr-Fitness-Check für Senioren in Zusammenarbeit mit dem ADAC.'),
            ('Sicherheitstraining', 'Individuelle Fahrtrainings und Sicherheitstraining.'),
            ('Aufbauseminare', 'Für auffällig gewordene Fahranfänger.'),
            ('Geschenkgutscheine', 'Der Führerschein oder ein Training als Geschenk.')])
        + contact(s) + footer(s))

S = SITES['stadtbrunnen'] = site(
    slug='fahrschule-am-stadtbrunnen-greven', firma='Fahrschule am Stadtbrunnen GmbH', web='fahrschule-am-stadtbrunnen.de', fonts='r14loh', du=False,
    title='Fahrschule am Stadtbrunnen – Greven seit 1989', desc='Fahrschule am Stadtbrunnen in Greven: Ausbildung aller Klassen von AM bis D, Theorie dienstags und donnerstags, seit 1989.',
    tel='02571 53024', tel_i='+49257153024', mail='FahrschuleAmStadtbrunnenGmbH@T-Online.de', adresse='Münsterstr. 35/37, 48268 Greven', google=None,
    logo_txt='<i>FS</i><span>Fahrschule am Stadtbrunnen<small>Greven</small></span>',
    cta='Jetzt anmelden', nav=[('Klassen', 'klassen'), ('Über uns', 'ueber'), ('Fahrzeuge', 'fahrzeuge'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Di &amp; Do', '18:00 – 18:30 Anmeldung'), ('Di &amp; Do', '18:30 – 20:00 Theorie'), ('Mobil', '0172 7057984 / -85')],
    form_lbl='Führerschein', form_opts=['Auto · B / B197', 'Anhänger · BE / B96', 'Motorrad · A / A2 / A1', 'Roller · AM', 'Lkw · C / CE', 'Bus · D', 'Fortbildung / Training'],
    form_h3='Jetzt anmelden', form_p='Schicken Sie uns Ihre Daten. Wir melden uns und besprechen Ihren Start.', form_btn='Anmeldung abschicken',
    kt_ey='Kontakt', kt_h2='Münsterstraße 35/37, <em>Greven.</em>', kt_p='Rufen Sie an oder kommen Sie dienstags oder donnerstags ab 18 Uhr vorbei. Dann sind wir für Informationen, Anmeldungen und Vorprüfungen da.',
    vars='--bg:#f6f9fa;--ink:#13262c;--mute:#53666c;--p:#1490c8;--p-ink:#fff;--a:#1490c8;--a-ink:#fff;--dk:#0d3a46;--s:#fff;--s2:#e8f1f4;--fh:"Exo 2",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:2px;--r2:4px;--br:2px;--mq-bg:#0d3a46;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#13262c;--logo-h:44px;--ft-bg:#0d3a46;--hx-r:4px;--hx-ar:4/3',
    css=BASE + '''
.lt-logo{display:inline-flex;align-items:center;gap:10px;font:800 17px/1.05 var(--fh)}.lt-logo i{background:#1490c8;color:#fff;font-style:normal;padding:8px 9px;border-radius:4px 14px 4px 4px}.lt-logo small{display:block;font:600 11px var(--fb);letter-spacing:.14em;text-transform:uppercase;color:#1490c8}.ft .lt-logo{color:#fff}
.hx{background:linear-gradient(180deg,#e8f1f4,#f6f9fa)}.hx h1{font-weight:800}.hx h1 em{display:block;font-style:italic}.h2 em{font-style:italic;color:var(--p)}.dk .h2 em{color:#6fd0ff}
.hx .pic{border-bottom:6px solid #1490c8}.kl .k b{color:#1490c8}.dk .kl .k b,.kl.dk .k b{color:#6fd0ff}.sv .row div{border-top:4px solid #1490c8}''')
S['bot'] = BOT('Birte', 'Ihre Stadtbrunnen-Lotsin', 'der Fahrschule am Stadtbrunnen', S, ['B', 'B197', 'BE', 'B96', 'A', 'A2', 'A1', 'AM', 'C', 'CE', 'D'],
    {'schnell': 'Theorie zweimal pro Woche, dienstags und donnerstags.', 'ruhe': 'Lockere Atmosphäre statt Schulbankdrücken: seit 1989 unser Prinzip.', 'flex': 'Schalter oder Automatik (B197): Sie haben die Wahl.', 'angst': 'Wir erklären freundlich und verständlich. Viele unserer Schüler kommen über Empfehlung.'},
    qa=[('bus|setra|d ', 'Den Busführerschein Klasse D bilden wir im Setra-Reisebus aus.'), ('senior|50|adac', 'Für Generation 50+ bieten wir mit dem ADAC einen Fahr-Fitness-Check an.'), ('gutschein', 'Geschenkgutscheine bekommen Sie direkt bei uns in der Fahrschule.')],
    tour=[('#klassen', 'Alle Klassen auf einen Blick.'), ('#ueber', 'Wer wir sind.'), ('#fahrzeuge', 'Unsere Fahrzeuge.'), ('#kontakt', 'Hier melden Sie sich an.')], du=False)
B = 'stadtbrunnen/img/'
S['img'] = {'h-team.jpg': (B + '010.jpg', 0), 'h-gla.jpg': (B + '016.jpg', 0), 'u-raum.jpg': (B + '002.jpg', 0),
    'f-a.jpg': (B + '004.jpg', 0), 'f-gla.jpg': (B + '016.jpg', 0), 'f-glc.jpg': (B + '018.jpg', 0), 'f-hornet.jpg': (B + '020.jpg', 0), 'f-ktm.jpg': (B + '024.jpg', 0), 'f-man.jpg': (B + '028.jpg', 0), 'f-setra.jpg': (B + '030.jpg', 0),
}
S['body'] = b_stadtbrunnen
S['social'] = [('Instagram', 'https://www.instagram.com/fahrspass_am_stadtbrunnen/')]

# ───────────── 2 · Fahrschule Gehle, Gütersloh ─────────────
def b_gehle(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-lkw.jpg', pos='50% 55%', quick=['auto', 'moto', 'lkw', 'trak'],
        ey='Fahrschule Gehle · Gütersloh · Steinhagen · Friedrichsdorf',
        h1='Unsere Berufung <em>seit 1946.</em>',
        sub='Führerschein in allen Klassen, Berufskraftfahrer-Ausbildung und geförderte Weiterbildung aus einer Hand. TQCert-zertifizierter Bildungsträger, Förderung über Agentur für Arbeit oder Jobcenter möglich.',
        g1=('Seit 1946', 'drei Generationen Fahrausbildung'), g2=('3 Standorte', 'Gütersloh · Steinhagen · Friedrichsdorf')))
        + video('film', 'Unser Film', 'Straße. <em>Freiheit.</em> Gehle.', 'Ein kurzer Eindruck von der Fahrschule Gehle.', 'film.mp4', 'film.jpg')
        + marquee(['B · BE', 'A1 · A2 · A', 'C · CE', 'D · DE', 'Berufskraftfahrer', 'Bildungsgutschein', 'Staplerschulung', 'Erste Hilfe &amp; Sehtest'], 'hm')
        + promo('foerderung', 'p-lkw.jpg', 'Geförderte Maßnahmen', 'Zukunft sichern. <em>Qualifikation schaffen.</em>',
                'Sie möchten sich beruflich weiterentwickeln oder den Einstieg in die Logistikbranche schaffen? Kraftfahrer werden dringend gesucht. Wir begleiten Sie von der Beratung bis zur Integration in die Arbeitswelt.',
                ['Kraftfahrer/-in C/CE und D/DE, gefördert per Bildungsgutschein', 'Kraftfahrerqualifikation mit Sprachmodul', 'Qualifizierung zum Baumaschinenführer', 'Nächster Kursstart TQ 1 oder 3: 30.11.2026'], 'Beratung anfragen')
        + klassen('klassen', 'Führerschein', 'In allen <em>Fahrerlaubnisklassen.</em>', 'Tippen Sie auf eine Klasse, dann prüft Greta mit Ihnen, ob sie passt.', [
            ('B · BE', 'Auto &amp; Anhänger', 'Individuelle Beratung und Betreuung für eine hohe Erfolgsquote.', 'ab 17', 'auto'),
            ('A1 · A2 · A', 'Motorrad', 'Das beste Mittel gegen Langeweile hat zwei Räder.', 'ab 16', 'moto'),
            ('C · CE', 'Lkw', 'Beste Zukunftschancen auf dem Arbeitsmarkt.', 'ab 18', 'lkw'),
            ('D · DE', 'Bus', 'Seit drei Generationen bilden wir Busfahrer aus, mit Praxis aus dem eigenen Omnibusbetrieb.', 'ab 21', 'lkw'),
            ('L · T', 'Traktor', 'In unserer Zweigstelle Friedrichsdorf.', 'ab 16', 'trak')], 'dk')
        + svc('services', 'Schulungen &amp; Services', 'Alles <em>aus einer Hand.</em>', 'Als Generaldienstleister für das Kraftverkehrsgewerbe erfüllen wir nahezu alle branchenrelevanten Kundenwünsche.', [
            ('BKF-Weiterbildung', '35 Stunden in 5 Jahren, praxisnah mit Fachleuten als Dozenten.'),
            ('Arbeitsmedizin', 'Untersuchung nach Anlage 5 &amp; 6 FeV, ca. 20 Minuten, ohne Wartezeit.'),
            ('Staplerschulung', 'Theorie und Praxis für den sicheren Umgang mit Flurförderfahrzeugen.'),
            ('Ladungssicherung', 'Schulungen für Fahrer und Unternehmen.'),
            ('Firmenschulungen', 'Themen und Umfang stimmen Sie mit uns ab.'),
            ('Erste Hilfe &amp; Sehtest', 'Direkt bei uns in Gütersloh-Avenwedde.')])
        + mini_team('team', 'Unser Team', 'Menschen, <em>die Sie begleiten.</em>', 'Fahrlehrer, Dozenten und Verwaltung: Olaf Gehle und sein Team.', [
            ('t1.jpg', 'Olaf Gehle', 'Fahrschulleiter · Fahrlehrer aller Klassen', '50% 30%'), ('t2.jpg', 'Oliver Weigel', 'Fahrlehrer aller Klassen', '50% 30%'),
            ('t3.jpg', 'Gisela „Betty“ Perßon', 'B/BE, C/CE &amp; D/DE', '50% 30%'), ('t4.jpg', 'Stefan Nowak', 'B/BE, C/CE &amp; D/DE', '50% 30%'),
            ('t5.jpg', 'René Großelanghorst', 'B/BE &amp; C/CE', '50% 30%'), ('t6.jpg', 'Tobias Ihl', 'A, B/BE und C/CE', '50% 30%'),
            ('t7.jpg', 'Melanie Sczesny', 'B/BE', '50% 30%'), ('t8.jpg', 'Marius Gehle', 'B/BE/A', '50% 30%'),
            ('t9.jpg', 'Konstantin Schinas', 'B/BE', '50% 30%'), ('t10.jpg', 'Bianca Weigel', 'Büroleitung · Bildungsberatung', '50% 30%')])
        + standorte('standorte', 'Unsere Standorte', 'Dreimal <em>in Ihrer Nähe.</em>', 'Theorie an fünf Abenden pro Woche.', [
            ('Gütersloh-Avenwedde', 'Nikolaus-Otto-Str. 3<br>Hauptstelle mit GTÜ-Prüfstelle', 'Unterricht Mo &amp; Mi 18:30 – 20:00', 'Nikolaus-Otto-Str. 3, Gütersloh'),
            ('Steinhagen', 'Am Markt 27<br>seit November 2023', 'Unterricht Di, Mi &amp; Do 18:30 – 20:00', 'Am Markt 27, Steinhagen'),
            ('Friedrichsdorf', 'Brackweder Str. 6<br>seit gut 40 Jahren', 'Unterricht Di &amp; Do 18:30 – 20:00', 'Brackweder Str. 6, Gütersloh-Friedrichsdorf')], 'alt')
        + stimmen('stimmen', 'Das sagen unsere Kunden', 'Direkt beim ersten Mal <em>bestanden.</em>', [
            ('Als ich mir beim Beratungsgespräch die Räumlichkeiten angesehen habe, war ich mir sicher, dass ich hier richtig bin. Ich habe alle Prüfungen direkt beim ersten Mal bestanden.', 'Eduard Esau', 'Lkw-Führerschein'),
            ('Ich war besonders mit dem praktischen Teil der Ausbildung sehr zufrieden. Es hat alles super geklappt, ich genieße jetzt das Motorradfahren.', 'Viktor Klassen', 'Motorrad-Führerschein'),
            ('Von Anfang an hatte ich hier ein gutes Gefühl.', 'Ewald Esau', 'Lkw-Führerschein')], 'Stimmen von fahrschule-gehle.de, gekürzt.')
        + gallery('raeume', 'Unsere Räume', 'Moderne <em>Ausbildungsumgebung.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 50%')])
        + contact(s) + footer(s))

S = SITES['gehle'] = site(
    slug='fahrschule-gehle-guetersloh', firma='Fahrschule Gehle', web='fahrschule-gehle.de', fonts='r14bec', du=False,
    title='Fahrschule Gehle – seit 1946 in Gütersloh', desc='Fahrschule Gehle in Gütersloh, Steinhagen und Friedrichsdorf: alle Klassen, Berufskraftfahrer, geförderte Weiterbildung. Seit 1946.',
    tel='05241 4034810', tel_i='+4952414034810', mail='verwaltung@fahrschule-gehle.de', adresse='Nikolaus-Otto-Str. 3, 33335 Gütersloh', google=None,
    cta='Jetzt anmelden', nav=[('Film', 'film'), ('Förderung', 'foerderung'), ('Klassen', 'klassen'), ('Team', 'team'), ('Standorte', 'standorte'), ('Kontakt', 'kontakt')],
    hours=[('Büro Mo – Fr', '8:00 – 15:00 Uhr'), ('Sa', 'geschlossen'), ('Mobil', '0172 5203582')],
    form_lbl='Anliegen', form_opts=['Führerschein Auto · B / BE', 'Motorrad · A / A2 / A1', 'Lkw · C / CE', 'Bus · D / DE', 'Geförderte Weiterbildung', 'BKF-Weiterbildung', 'Firmenschulung'],
    form_orte=['Gütersloh-Avenwedde', 'Steinhagen', 'Friedrichsdorf'],
    form_h3='Beratungstermin anfragen', form_p='Schicken Sie uns Ihre Daten. Wir rufen Sie zurück und beraten Sie persönlich, auch zu Fördermöglichkeiten.', form_btn='Anfrage abschicken',
    kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Rufen Sie an oder schreiben Sie uns. Wir bearbeiten Ihr Anliegen kurzfristig.',
    logo='logo.png',
    vars='--bg:#f5f6f8;--ink:#141a28;--mute:#566074;--p:#1d3f8f;--p-ink:#fff;--a:#1d3f8f;--a-ink:#fff;--dk:#101a33;--s:#fff;--s2:#e9ecf2;--fh:"Barlow Condensed",system-ui,sans-serif;--fb:"Heebo",system-ui,sans-serif;--r:0px;--r2:2px;--br:0px;--mq-bg:#1d3f8f;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#141a28;--logo-h:34px;--ft-bg:#101a33;--hx-r:0px;--hx-ar:4/3',
    css=BASE + '''
.hx h1,.h2{font-weight:700;text-transform:uppercase;letter-spacing:.005em}.hx h1 em{display:block;color:#1d3f8f}.h2 em{color:#1d3f8f;font-style:normal}.dk .h2 em{color:#8fb0ff}
.hx .pic{clip-path:polygon(8% 0,100% 0,100% 100%,0 100%,0 10%)}.hx .gl{border-radius:0;border-left:4px solid #1d3f8f}
.hd .logo img{height:34px}.ft .logo img,.ft img{height:34px;background:#fff;padding:6px 10px}.kl .k b{color:#8fb0ff}.sv .row div{border-top:4px solid #1d3f8f}
.so{background:#fff}.mt img{box-shadow:0 0 0 2px #1d3f8f}''')
S['bot'] = BOT('Greta', 'Ihre Gehle-Lotsin', 'der Fahrschule Gehle', S, ['B', 'BE', 'A', 'A2', 'A1', 'AM', 'C', 'CE', 'D', 'DE', 'L', 'T'],
    {'schnell': 'Theorie an drei Standorten, an fünf Abenden pro Woche.', 'ruhe': 'Seit 1946 bilden wir aus. Viele Schüler bestehen direkt beim ersten Mal.', 'flex': 'Gütersloh-Avenwedde, Steinhagen oder Friedrichsdorf: Sie wählen.', 'angst': 'Wir nehmen uns Zeit. Unterricht und Beratung bieten wir auch in mehreren Sprachen an.'},
    qa=[('förder|bildungsgutschein|jobcenter|arbeit', 'Lkw- und Bus-Führerschein können über Bildungsgutschein von Agentur für Arbeit oder Jobcenter gefördert werden. Wir beraten Sie gern.'), ('stapler', 'Staplerschulungen bieten wir regelmäßig an, Theorie und Praxis.'), ('sehtest|erste hilfe', 'Erste-Hilfe-Kurs und Sehtest machen Sie direkt bei uns in Avenwedde.')],
    tour=[('#film', 'Unser Film.'), ('#foerderung', 'Geförderte Weiterbildung.'), ('#klassen', 'Alle Klassen.'), ('#kontakt', 'Hier melden Sie sich an.')], du=False)
G = 'gehle/img/'
S['img'] = {'logo.png': (G + '001.png', 600), 'h-lkw.jpg': (G + '018.jpg', 0), 'film.mp4': ('/home/claude/r24raw/gehle/film.mp4', 0), 'film.jpg': ('/home/claude/r24raw/gehle/film.jpg', 0),
    'p-lkw.jpg': (G + '022.jpg', 1200),
    't1.jpg': (G + '043.jpg', 0), 't2.jpg': (G + '044.jpg', 0), 't3.jpg': (G + '045.jpg', 0), 't4.jpg': (G + '046.jpg', 0), 't5.jpg': (G + '047.jpg', 0),
    't6.jpg': (G + '048.jpg', 0), 't7.jpg': (G + '050.jpg', 0), 't8.jpg': (G + '051.jpg', 0), 't9.jpg': (G + '052.jpg', 0), 't10.jpg': (G + '057.jpg', 0),
    'g1.jpg': (G + '034.jpg', 1600), 'g2.jpg': (G + '030.jpg', 1000), 'g3.jpg': (G + '026.jpg', 1000), 'g4.jpg': (G + '036.jpg', 1600)}
S['body'] = b_gehle
S['social'] = [('Instagram', 'https://www.instagram.com/gehle4u/')]

# ───────────── 3 · Fahrschule Tesmer, Lichtenau / Paderborn ─────────────
def b_tesmer(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-moto.jpg', pos='40% 50%', quick=['auto', 'moto', 'lkw', 'trak'],
        ey='Fahrschule Tesmer · Inh. Ferdinand Bunte',
        h1='Alle Klassen. <em>Vier Standorte.</em>',
        sub='Lichtenau, Schwaney, Paderborn und Etteln: Bei uns hast du Spaß an der Führerscheinausbildung und bekommst Spitzenleistungen zu fairen Preisen. Vom Auto über Motorrad und Traktor bis zu Bus und Lkw.',
        g1=('Seit 1982', 'im Kreis Paderborn')))
        + marquee(['AM · A1 · A2 · A', 'B · B96 · BE', 'C1 · C · CE', 'D1 · D · DE', 'L · T', 'BKF-Grundqualifikation', 'Fahren Lernen Max', '11 Sprachen'], 'hm')
        + standorte('standorte', 'Wir sind für dich da', 'Viermal <em>im Kreis Paderborn.</em>', 'Anmeldung und Unterricht direkt vor Ort.', [
            ('Lichtenau', 'Lange Str. 17<br>33165 Lichtenau', 'Di &amp; Do · 18:30 Uhr', 'Lange Str. 17, 33165 Lichtenau'),
            ('Paderborn', 'Warburger Str. 62<br>33098 Paderborn', 'Mo &amp; Mi · 18:30 Uhr', 'Warburger Str. 62, 33098 Paderborn'),
            ('Schwaney', 'Osttorstr. 42<br>33184 Altenbeken', 'Di &amp; Do · 19:00 Uhr', 'Osttorstr. 42, 33184 Altenbeken'),
            ('Etteln', 'Kirchstr. 15a<br>33178 Borchen', 'Mo &amp; Mi · 18:30 Uhr', 'Kirchstr. 15a, 33178 Borchen')])
        + klassen('klassen', 'Klassentreffen', 'Ob Auto, Motorrad <em>oder Trecker.</em>', 'Alles ist eine Klasse für sich. Tipp drauf, und Tessa sagt dir, ob sie zu dir passt.', [
            ('A · A1 · A2 · AM', 'A wie Ausritt', 'Zum 16. Geburtstag muss der erste Zweiradführerschein her.', 'ab 15', 'moto'),
            ('B · B96 · BE', 'Der Klassiker', 'Wer A wie Auto sagt, muss B machen.', 'ab 17', 'auto'),
            ('C1 · C · CE', 'Lkw', 'Die Kapitäne der Landstraße.', 'ab 18', 'lkw'),
            ('D1 · D · DE', 'Bus', 'Verantwortung für die Passagiere, im Nahverkehr oder auf Reisen.', 'ab 21', 'lkw'),
            ('L · T', 'Traktor', 'Für Land- und Forstwirtschaft.', 'ab 16', 'trak')], 'dk')
        + story('ueber', 'Our Story', 'Eine Fahrschule <em>mit Geschichte.</em>', [
            'Unsere Fahrschule wurde 1982 von Heinz Tesmer gegründet und wird seit 2005 von Ferdinand Bunte weitergeführt. Mit vier Standorten sind wir im Kreis Paderborn gut präsent.',
            'Lernen in entspannter, aber konzentrierter Atmosphäre. Anspruchsvolle theoretische und praktische Ausbildung. Kompetente, freundliche und faire Fahrlehrer.'],
            'u-trak.jpg', cap='Auch der Trecker-Führerschein gehört dazu', tl=[('1982', 'gegründet von Heinz Tesmer'), ('2005', 'Ferdinand Bunte übernimmt'), ('4', 'Standorte im Kreis Paderborn')])
        + mini_team('team', 'Das Team', 'Wir geben <em>alles für euch.</em>', 'Damit deine Ausbildung nicht nur Erfolg bringt, sondern auch Spaß macht.', [
            ('t1.jpg', 'Ferdinand Bunte', 'Kraftverkehrsmeister · Fahrlehrer aller Klassen · Inhaber seit 2005', '50% 30%'),
            ('t2.jpg', 'Matthias Plümper', 'Fahrlehrer Klasse B und BE', '50% 30%'),
            ('t3.jpg', 'Maike Bunte', 'Fahrlehrerin Klasse B, BE und A', '50% 30%')], 'alt')
        + promo('app', 'p-app.jpg', 'Theorie', 'Deine App <em>für die Theorie.</em>',
                'Fahren Lernen Max begleitet dich durch die Ausbildung. Mit dem geführten Lernweg kommst du sicher durch die Theorieprüfung, und mit „Meine Stunden“ und „Meine Dokumente“ hast du sogar den Papierkram im Blick.',
                ['Geführter Lernweg', 'Mobiles Lerntraining in 11 Sprachen', 'Praxistraining für die Fahrstunden'], 'Jetzt anmelden')
        + contact(s) + footer(s))

S = SITES['tesmer'] = site(
    slug='fahrschule-tesmer-lichtenau', firma='Fahrschule Tesmer', web='fahrschule-tesmer.de', fonts='r16geyer',
    title='Fahrschule Tesmer – Lichtenau, Schwaney, Paderborn, Etteln', desc='Fahrschule Tesmer, Inh. Ferdinand Bunte: alle Führerscheinklassen an vier Standorten im Kreis Paderborn. Seit 1982.',
    tel='05292 9316825', tel_i='+4952929316825', mail='mail@fahrschule-tesmer-bunte.de', adresse='Schöne Aussicht 1, 33165 Lichtenau-Husen', google=None,
    logo_txt='<span>TESMER</span><small>Fahrschule · Inh. Ferdinand Bunte</small>',
    cta='Jetzt anmelden', nav=[('Standorte', 'standorte'), ('Klassen', 'klassen'), ('Über uns', 'ueber'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Lichtenau', 'Di &amp; Do 18:30'), ('Paderborn', 'Mo &amp; Mi 18:30'), ('Schwaney', 'Di &amp; Do 19:00'), ('Etteln', 'Mo &amp; Mi 18:30')],
    form_lbl='Führerschein', form_opts=['Auto · B / B96 / BE', 'Motorrad · A / A2 / A1 / AM', 'Lkw · C1 / C / CE', 'Bus · D1 / D / DE', 'Traktor · L / T', 'BKF-Qualifikation'],
    form_orte=['Lichtenau', 'Paderborn', 'Schwaney', 'Etteln'],
    form_h3='Melde dich an', form_p='Schick uns deine Daten. Wir melden uns und besprechen deinen Start.', form_btn='Anmeldung abschicken',
    kt_ey='So erreichst du uns', kt_h2='Ganz egal, <em>was dich beschäftigt.</em>', kt_p='Fragen zu den Klassen, zum Unterricht oder zur Anmeldung? Ruf an unter 05292 9316825 oder mobil 0172 9946665.',
    vars='--bg:#f4f8f6;--ink:#17221d;--mute:#56645d;--p:#1fa874;--p-ink:#fff;--a:#f28c1b;--a-ink:#17221d;--dk:#18221e;--s:#fff;--s2:#e4f2ec;--fh:"Montserrat",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:2px;--r2:4px;--br:2px;--mq-bg:#1fa874;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#17221d;--logo-h:40px;--ft-bg:#18221e;--hx-r:2px;--hx-ar:5/4',
    css=BASE + '''
.lt-logo{display:inline-flex;flex-direction:column;line-height:1}.lt-logo span{font:900 26px var(--fh);letter-spacing:.12em;border:3px solid #17221d;padding:3px 10px;border-radius:4px}.lt-logo small{font:600 10px var(--fb);letter-spacing:.12em;text-transform:uppercase;color:#1fa874;margin-top:5px}
.ft .lt-logo span{color:#fff;border-color:#fff}
.hx{background:linear-gradient(180deg,#e4f2ec,#f4f8f6)}.hx h1{font-weight:900;text-transform:uppercase}.hx h1 em{display:block;color:#f28c1b;font-style:normal}
.h2{font-weight:900;text-transform:uppercase}.h2 em{color:#1fa874;font-style:normal}.dk .h2 em{color:#f6a54a}.kl .k b{color:#f6a54a}
.hx .gl{background:#1fa874;color:#fff;border-radius:0 0 16px 0}.hx .gl b{color:#fff}.so{border-top-color:#f28c1b}''')
S['bot'] = BOT('Tessa', 'deine Tesmer-Lotsin', 'der Fahrschule Tesmer', S, ['B', 'B96', 'BE', 'A', 'A2', 'A1', 'AM', 'C1', 'C', 'CE', 'D1', 'D', 'DE', 'L', 'T'],
    {'schnell': 'Unterricht an vier Standorten, jeden Abend von Montag bis Donnerstag.', 'ruhe': 'Entspannte, aber konzentrierte Atmosphäre: so lernst du bei uns.', 'flex': 'Lichtenau, Paderborn, Schwaney oder Etteln: Du suchst dir den Standort aus.', 'angst': 'Unsere Fahrlehrer sind kompetent, freundlich und fair.'},
    qa=[('app|max|theorie', 'Die Theorie lernst du mit der App Fahren Lernen Max, auch in 11 Sprachen.'), ('bkf|berufskraft', 'Berufskraftfahrer-Grundqualifikation und Modulschulungen bieten wir an.')],
    tour=[('#standorte', 'Unsere vier Standorte.'), ('#klassen', 'Alle Klassen.'), ('#team', 'Unser Team.'), ('#kontakt', 'Hier meldest du dich an.')])
T = 'tesmer/img/'
S['img'] = {'h-moto.jpg': (T + '025.jpg', 1600), 'u-trak.jpg': (T + '041.jpg', 1400), 'p-app.jpg': (T + '029.jpg', 1400),
    't1.jpg': (T + '001.jpg', 0), 't2.jpg': (T + '010.jpg', 0), 't3.jpg': (T + '011.jpg', 0)}
S['body'] = b_tesmer
S['social'] = [('Instagram', 'https://www.instagram.com/fahrschule_tesmer/')]

# ───────────── 4 · Fahrschule Pöppelmann, Nottuln ─────────────
def b_poeppelmann(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-mc.jpg', pos='50% 40%', quick=['auto', 'moto', 'roller', 'trak'],
        ey='Fahrschule Pöppelmann · Nottuln',
        h1='Motorrad fahren <em>mit dem Autoführerschein.</em>',
        sub='B196, Motorrad-Intensivkurs in 7 Tagen und Ausbildung „Bike to Bike“: Deine Fahrlehrerin fährt selbst auf dem Motorrad mit. Dazu Theorie in nur 7 Tagen, E-Autos und Trecker-Führerschein.',
        g1=('Bike to Bike', 'Fahrlehrerin fährt mit')))
        + marquee(['B196', 'Motorrad in 7 Tagen', 'Theorie in 7 Tagen', 'FUN LEARN', 'VW ID.3 Automatik', 'Klasse T', 'Passbilder &amp; Sehtest', 'Erste Hilfe'], 'hm')
        + promo('motorrad', 'p-moto.jpg', 'Top-Thema', 'Werde eins <em>mit der Straße.</em>',
                'Unsere Fahrprofis sind Biker aus Leidenschaft. Mit einer großen Auswahl an Maschinen bringen wir dich zu fairen Preisen spielerisch durch die Prüfung. Motorradkleidung stellen wir auf Wunsch, sogar inklusive Helm mit Airbag-Weste.',
                ['B196: 125er mit dem Autoführerschein', 'Motorrad-Intensivkurs: Führerschein in 7 Tagen möglich', 'Yamaha MT-07 extra tiefergelegt für kleinere Fahrer'], 'Platz sichern')
        + flotte('fahrzeuge', 'Unser Fuhrpark', 'Damit <em>lernst du.</em>', 'Jede Fahrstunde ein Erlebnis.', [
            ('f-troc.jpg', 'VW T-Roc', 'Klasse B und BE · Schaltwagen', '50% 55%'),
            ('f-id3.jpg', 'VW ID.3', 'E-Automatik, geladen mit eigener Photovoltaik', '50% 55%'),
            ('f-mt.jpg', 'Yamaha MT-07', 'Klasse A, auch tiefergelegt', '50% 60%'),
            ('f-ktm.jpg', 'KTM', 'Zweiradklassen', '50% 60%'),
            ('f-grom.jpg', 'Honda', 'Klasse A1 / B196', '50% 60%'),
            ('f-roller.jpg', 'E-Roller', 'Klasse AM', '50% 60%')], 'dk')
        + promo('funlearn', 'p-sim.jpg', 'Theorie', 'FUN LEARN: <em>dein etwas anderer Unterricht.</em>',
                'Schluss mit stumpfem Frontalunterricht. Eine Mischung aus Spiel, Spaß und Lernen, „learning by doing“. Dazu Fahrsimulator und unsere Wall of Fame.',
                ['Theorie in nur 7 Tagen', 'Fahrsimulator für den Einstieg', 'Passbilder und Sehtest direkt bei uns'], 'Jetzt anmelden', 'alt')
        + mini_team('team', 'Unser Team', 'Keine Oberlehrer. <em>Menschen.</em>', 'Wir lieben unseren Job. Schimpfen gehört nicht dazu.', [
            ('t1.jpg', 'Marie-Claire Pöppelmann', 'Leiterin · B/BE, alle Zweiradklassen, T · Erste Hilfe', '50% 30%'),
            ('t2.jpg', 'Pia Lux', 'Fahrtrainerin B/BE und Zweiradklassen · Theorie', '50% 25%'),
            ('t3.jpg', 'Birgit Pöppelmann', 'Die gute Seele · Sehtest · Fahrsimulator', '50% 30%'),
            ('t4.jpg', 'Paul', 'Unser Mann für die Sicherheit', '50% 45%')])
        + stimmen('stimmen', 'Kundenstimmen', 'Bestens <em>aufgehoben.</em>', [
            ('Mein Mann und ich haben den B196 bei Marie gemacht. Wir haben uns von Anfang bis Ende bestens aufgehoben gefühlt. Das gesamte Team ist super organisiert.', 'Lili R.', 'B196'),
            ('Ich habe mich von Anfang an sehr gut aufgehoben und unterstützt gefühlt. Mir wurde alles geduldig erklärt.', 'Julina Tunney', 'Klasse B'),
            ('Motorradkleidung wurde sogar gestellt, inklusive Helm mit Airbag-Weste. Sehr nette Fahrlehrerin.', 'ActiveBlue', 'B196 und Klasse A')], 'Stimmen von fahrschule-poeppelmann.de, gekürzt.', 'alt')
        + contact(s) + footer(s))

S = SITES['poeppelmann'] = site(
    slug='fahrschule-poeppelmann-nottuln', firma='Fahrschule Pöppelmann GmbH &amp; Co. KG', web='fahrschule-poeppelmann.de', fonts='r14nap',
    title='Fahrschule Pöppelmann – Nottuln', desc='Fahrschule Pöppelmann in Nottuln: B196, Motorrad in 7 Tagen, Bike to Bike, FUN LEARN, E-Autos und Klasse T.',
    tel='02502 9256', tel_i='+4925029256', mail='info@fahrschule-poeppelmann.de', adresse='Mauritzstraße 12, 48301 Nottuln', google=None,
    logo='logo.png', cta='Jetzt anmelden', nav=[('Motorrad', 'motorrad'), ('Fahrzeuge', 'fahrzeuge'), ('FUN LEARN', 'funlearn'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '16:00 – 18:30 Uhr'), ('Beratung', 'oder nach Vereinbarung'), ('Mobil', '0151 25329567')],
    form_lbl='Führerschein', form_opts=['B196 · 125er mit Autoführerschein', 'Motorrad · A / A2 / A1', 'Auto · B / BE', 'Automatik · E-Auto', 'Roller · AM', 'Traktor · T'],
    form_h3='Beratungstermin vereinbaren', form_p='Schick uns deine Daten. Wir melden uns, oder komm einfach auf einen Kaffee vorbei.', form_btn='Termin anfragen',
    kt_ey='Kontakt', kt_h2='Komm auf einen <em>Kaffee vorbei.</em>', kt_p='Mauritzstraße 12 in Nottuln. Unser freundliches Team ist jederzeit gern persönlich für dich da.',
    vars='--bg:#f7f5f4;--ink:#1a1717;--mute:#5c5555;--p:#d0262f;--p-ink:#fff;--a:#d0262f;--a-ink:#fff;--dk:#1a1717;--s:#fff;--s2:#efe9e7;--fh:"Red Hat Display",system-ui,sans-serif;--fb:"Open Sans",system-ui,sans-serif;--r:0px;--r2:2px;--br:0px;--mq-bg:#1a1717;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#1a1717;--logo-h:44px;--ft-bg:#1a1717;--hx-r:0px;--hx-ar:1/1',
    css=BASE + '''
.hx h1{font-weight:900}.hx h1 em{display:block;color:#d0262f;font-style:normal}.h2{font-weight:900}.h2 em{color:#d0262f;font-style:normal}.dk .h2 em{color:#ff6b72}
.hx .pic{border-radius:0 0 0 60px}.hx .gl{background:#d0262f;color:#fff;border-radius:0 18px 0 0}.hx .gl b{color:#fff}
.hd .logo img{height:44px}.ft img{background:#fff;padding:6px 10px;height:50px}.promo figure img{border-radius:0 0 48px 0}''')
S['bot'] = BOT('Mia', 'deine Pöppelmann-Lotsin', 'der Fahrschule Pöppelmann', S, ['B', 'BE', 'B196', 'A', 'A2', 'A1', 'AM', 'T'],
    {'schnell': 'Theorie in nur 7 Tagen und Motorrad-Intensivkurs: Führerschein in 7 Tagen möglich.', 'ruhe': 'Bei uns musst du keine Angst vor Fehlern haben. Schimpfen gehört nicht dazu.', 'flex': 'Schalter (T-Roc) oder Automatik (E-Auto ID.3): Du hast die Wahl.', 'angst': 'Wir nehmen Ängste ernst und gehen darauf ein. So steht es auch in unseren Kundenstimmen.'},
    qa=[('b196|125', 'B196: Mit dem Autoführerschein 125er fahren. Bei uns mit Ausbildung „Bike to Bike“.'), ('kleidung|helm', 'Motorradkleidung stellen wir auf Wunsch, inklusive Helm mit Airbag-Weste.'), ('passbild|sehtest', 'Passbilder und Sehtest machst du direkt bei uns.')],
    tour=[('#motorrad', 'Motorrad und B196.'), ('#fahrzeuge', 'Unser Fuhrpark.'), ('#team', 'Unser Team.'), ('#kontakt', 'Hier meldest du dich an.')])
P = 'poeppelmann/img/'
S['img'] = {'logo.png': (P + '001.jpg', 0), 'h-mc.jpg': (P + '012.jpg', 0), 'p-moto.jpg': (P + '039.jpeg', 0), 'p-sim.jpg': (P + '019.jpeg', 0),
    'f-troc.jpg': (P + '025.jpg', 1200), 'f-id3.jpg': (P + '027.jpeg', 0), 'f-mt.jpg': (P + '023.jpeg', 0), 'f-ktm.jpg': (P + '033.jpeg', 0), 'f-grom.jpg': (P + '041.jpeg', 0), 'f-roller.jpg': (P + '045.jpg', 0),
    't1.jpg': (P + '012.jpg', 0), 't2.jpg': (P + '014.jpeg', 0), 't3.jpg': (P + '015.jpg', 0), 't4.jpg': (P + '016.jpeg', 0)}
S['body'] = b_poeppelmann
S['social'] = [('Instagram', 'https://www.instagram.com/fahrschule_poeppelmann/')]

# ───────────── 5 · MOTOSCHOOL, Dülmen ─────────────
def b_motoschool(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-bmw.jpg', pos='50% 55%', quick=['moto', 'auto', 'lkw', 'trak'],
        ey='MOTOSCHOOL · Fahrschule in Dülmen',
        h1='Mit Sicherheit <em>mehr Spaß.</em>',
        sub='Motorrad-Führerschein in 1 Woche, Schnupperkurs auf dem abgesperrten Gelände der alten Kaserne, Fahrsimulator und Auto-Führerschein in 11 Tagen. Fahrschulleiter Gernot Kempkes ist seit 1994 Fahrlehrer.',
        g1=('Zweirad-Fahrschule', 'Qualitätssiegel ifz'), g2=('4 Standorte', 'im Kreis Coesfeld')))
        + marquee(['Motorrad in 1 Woche', 'Schnupperkurs', 'Motorrad-Tanzkurs', 'Alpentour', 'Auto in 11 Tagen', 'Fahrsimulator', 'Handicap-Ausbildung', 'Lkw · Bus · Traktor'], 'hm')
        + promo('schnupper', 'p-honda.jpg', 'Motorrad-Schnupperkurs', 'Jetzt aufsteigen <em>und abfahren.</em>',
                'Auf unserem abgesperrten Trainingsgelände in der alten Kaserne gehen wir gemeinsam die ersten Schritte. Auch für Wiedereinsteiger. Mehrere Motorräder stehen zur Auswahl, von ganz tief bis ganz hoch.',
                ['3 Stunden schnuppern', '1 Fahrlehrer für max. 3 Teilnehmer', 'Schutzkleidung auf Wunsch'], 'Schnupperkurs anfragen')
        + flotte('motorraeder', 'Unser Fuhrpark', 'Für jede Größe <em>die passende Maschine.</em>', 'Körpergröße 155 cm? Passt.', [
            ('f-gs.jpg', 'BMW R1200 GS Adventure', 'Klasse A', '50% 60%'),
            ('f-rebel.jpg', 'Honda CMX 500', 'Klasse A2 · besonders tief', '50% 60%'),
            ('f-grom.jpg', 'Honda', 'Klasse A1', '50% 60%'),
            ('f-tiguan.jpg', 'VW Tiguan', 'Klasse B', '50% 55%'),
            ('f-id3.jpg', 'VW ID.3', 'Klasse B · Elektro', '50% 55%'),
            ('f-anh.jpg', 'Gespann', 'Klasse BE', '50% 55%')], 'dk')
        + svc('specials', 'Specials', 'Mehr als <em>Fahrstunden.</em>', 'Bei uns bleibt garantiert niemand auf der Strecke.', [
            ('Fahrsimulator', 'Anfahren, Schalten, Überholen: Die Grundlagen lernst du zuerst am Simulator, dann brauchst du weniger Übungsfahrten.'),
            ('Handicap-Ausbildung', 'VW Golf Sportsvan mit Multifunktionsdrehknopf und Handbediengerät.'),
            ('Motorrad-Tanzkurs', 'Und Sicherheitstraining auf der Straße oder Schräglagentraining.'),
            ('Motorrad-Alpentour', 'Gemeinsam unterwegs, nach dem Führerschein geht es erst richtig los.'),
            ('Lkw, Bus, Traktor', 'BKF-Aus- und Weiterbildung in familiärer Atmosphäre.'),
            ('Hypnose', 'Zum besseren Lernen und gegen Prüfungsstress.')])
        + standorte('standorte', 'Unsere Filialen', 'Viermal <em>in deiner Nähe.</em>', 'Komm auf einen Kaffee vorbei.', [
            ('Dülmen', 'Friedrich-Ruin-Str. 50', 'Theorie Mo – Do ab 18:00', 'Friedrich-Ruin-Str. 50, Dülmen'),
            ('Senden', 'Münsterstr. 37', 'Di – Do 16:00 – 17:00', 'Münsterstr. 37, Senden'),
            ('Buldern', 'Max-Planck-Str. 13', 'Di &amp; Do 17:30 – 19:00', 'Max-Planck-Str. 13, Dülmen-Buldern'),
            ('Merfeld', 'Rekener Straße 39', 'Mi 17:30 – 19:00', 'Rekener Straße 39, Dülmen-Merfeld')], 'alt')
        + stimmen('stimmen', 'Kundenstimmen', 'Einfach <em>nur TOP.</em>', [
            ('Seit 2008 machen wir die Führerscheine der ganzen Familie hier. Fair, effizient, beste Betreuung.', 'Frank Lange', ''),
            ('Von meiner Frau zum Motorrad-Schnupperkurs entführt worden. Es hat richtig Spaß gemacht. Gernot und Isabelle haben Ruhe und Vertrauen ausgestrahlt.', 'Sven H.', 'Schnupperkurs'),
            ('Heute meine praktische Prüfung bestanden, und ich hatte die ganze Zeit sehr viel Spaß.', 'Isabel Kemper', 'Führerschein')], 'Stimmen von motoschool.de, gekürzt.')
        + gallery('eindruecke', 'Eindrücke', 'So sieht <em>MOTOSCHOOL</em> aus.', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', 'w2', '50% 60%')])
        + contact(s) + footer(s))

S = SITES['motoschool'] = site(
    slug='motoschool-duelmen', firma='MOTOSCHOOL', web='motoschool.de', fonts='r15mob',
    title='MOTOSCHOOL – Fahrschule in Dülmen, Senden, Buldern, Merfeld', desc='MOTOSCHOOL von Gernot Kempkes: Motorrad-Führerschein in 1 Woche, Schnupperkurs, Fahrsimulator, Auto in 11 Tagen. Dülmen, Senden, Buldern, Merfeld.',
    tel='02594 2424', tel_i='+4925942424', mail='info@motoschool.de', adresse='Friedrich-Ruin-Str. 50, 48249 Dülmen', google=None,
    logo='logo.png', cta='Jetzt anmelden', nav=[('Schnupperkurs', 'schnupper'), ('Fuhrpark', 'motorraeder'), ('Specials', 'specials'), ('Filialen', 'standorte'), ('Kontakt', 'kontakt')],
    hours=[('Mo &amp; Fr', '14:00 – 19:00 Uhr'), ('Di – Do', '14:00 – 17:00 Uhr'), ('Gernot', '0172 2840840')],
    form_lbl='Führerschein', form_opts=['Motorrad · A / A2 / A1', 'Motorrad-Schnupperkurs', 'Auto · B / BE', 'Automatik / Handicap', 'Roller · AM', 'Lkw · Bus · Traktor', 'Sicherheitstraining'],
    form_orte=['Dülmen', 'Senden', 'Buldern', 'Merfeld'],
    form_h3='Beratungstermin vereinbaren', form_p='Schick uns deine Daten. Wir melden uns bei dir.', form_btn='Anfrage abschicken',
    kt_ey='Kontakt', kt_h2='Beste Grüße <em>mit viel PS.</em>', kt_p='Ruf an unter 02594 2424 oder komm in eine unserer vier Filialen.',
    vars='--bg:#f6f5f3;--ink:#1c1c1e;--mute:#5d5d63;--p:#ec5b16;--p-ink:#fff;--a:#ec5b16;--a-ink:#fff;--dk:#1c1c1e;--s:#fff;--s2:#efebe6;--fh:"Saira",system-ui,sans-serif;--fb:"Saira",system-ui,sans-serif;--r:2px;--r2:4px;--br:2px;--mq-bg:#ec5b16;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#1c1c1e;--logo-h:46px;--ft-bg:#1c1c1e;--hx-r:2px;--hx-ar:4/3',
    css=BASE + '''
.hx h1{font-weight:800;text-transform:uppercase;font-style:italic;line-height:1.1;margin-top:26px;padding-top:4px}.hx h1 em{display:block;color:#ec5b16;font-style:italic}.h2{font-weight:800;text-transform:uppercase;font-style:italic}.h2 em{color:#ec5b16}.dk .h2 em{color:#ff8a4f}
.hx .pic{transform:skewX(-3deg);border-right:8px solid #ec5b16}.hx .pic img{transform:skewX(3deg) scale(1.08)}.hx .gl{transform:skewX(3deg);border-radius:0 14px 0 0}
.hd .logo img{height:46px}.ft img{background:#fff;padding:6px 10px;height:50px}.so{border-top-color:#2a9d57}''')
S['bot'] = BOT('Moe', 'dein MOTOSCHOOL-Lotse', 'MOTOSCHOOL', S, ['A', 'A2', 'A1', 'AM', 'B', 'BE', 'B196', 'C', 'CE', 'D', 'L', 'T'],
    {'schnell': 'Motorrad-Führerschein in 1 Woche oder Auto-Führerschein in 11 Tagen.', 'ruhe': 'Bei uns musst du keine Angst vor Fehlern haben. Schimpfen gehört nicht dazu.', 'flex': 'Vier Filialen: Dülmen, Senden, Buldern und Merfeld.', 'angst': 'Erst am Simulator üben, dann auf die Straße. Und gegen Prüfungsstress gibt es sogar Hypnose.'},
    qa=[('schnupper|probe', 'Der Motorrad-Schnupperkurs dauert 3 Stunden auf dem abgesperrten Gelände der alten Kaserne, max. 3 Teilnehmer pro Fahrlehrer.'), ('klein|groß|tief|155', 'Wir haben tiefergelegte Maschinen. Körpergröße 155 cm? Passt.'), ('handicap|behinder', 'Wir bilden auch mit Handicap aus, im umgebauten VW Golf Sportsvan.')],
    tour=[('#schnupper', 'Der Schnupperkurs.'), ('#motorraeder', 'Unser Fuhrpark.'), ('#specials', 'Unsere Specials.'), ('#kontakt', 'Hier meldest du dich an.')])
M = 'motoschool/img/'
S['img'] = {'logo.png': (M + '000.png', 0, 'trim'), 'h-bmw.jpg': (M + '101.jpg', 1400), 'p-honda.jpg': (M + '130.jpg', 1200),
    'f-gs.jpg': (M + '101.jpg', 900), 'f-rebel.jpg': (M + '115.jpg', 900), 'f-grom.jpg': (M + '128.jpg', 900), 'f-tiguan.jpg': (M + '071.jpg', 900), 'f-id3.jpg': (M + '053.jpeg', 900), 'f-anh.jpg': (M + '094.jpg', 0),
    'g1.jpg': (M + '041.jpeg', 1400), 'g2.jpg': (M + '044.jpg', 900), 'g3.jpg': (M + '040.jpeg', 900), 'g4.jpg': (M + '069.jpg', 1400)}
S['body'] = b_motoschool
S['social'] = [('Instagram', 'https://www.instagram.com/motoschool.de/')]
