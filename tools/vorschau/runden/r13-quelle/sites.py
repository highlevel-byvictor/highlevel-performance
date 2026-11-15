"""Runde 13: Kfz-Werkstätten und Autohäuser im Umkreis von 15 km um Bersenbrück. Nur Material der Originalseiten und belegte Fakten."""
from lib import *
SITES = {}

def BOT(name, tag, firma, qa, tour):
    return dict(name=name, tag=tag, hello=f'Hallo! Ich bin {name}. Soll ich Ihnen kurz zeigen, was Sie bei {firma} erwartet?', hi=f'Hallo! Ich bin {name} von {firma}. Wobei darf ich helfen?', qa=qa, tour=[[f'#{t}'] for t in tour])

# ───────────────────────── 1. Werk Zwo, Quakenbrück ─────────────────────────
def b_werkzwo(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='ZWO', pos={'h1.jpg': '50% 60%', 'h2.jpg': '60% 50%', 'h3.jpg': '50% 50%'},
        ey='Old- &amp; Youngtimer-Service · Quakenbrück',
        h1='Neues Leben <em>für altes Blech.</em>',
        sub='Zwei Kfz-Meister, ein Team, eine Leidenschaft: Wir warten, reparieren und restaurieren Klassiker aus den 70ern, 80ern und 90ern. Und Ihr aktuelles Auto gleich mit.',
        ubar=[('Seit 2022', 'eigene Werkstatt in Quakenbrück'), ('4 Kfz-Meister', 'im Team'), ('H-Abnahme', 'mit TÜV Nord und Dekra')]))
        + marquee(['Service &amp; Instandhaltung', 'Restauration', 'Reparatur', 'Konservierung', 'Hauptuntersuchung', 'H-Abnahme', 'Service für alle Baujahre'])
        + story('wir', 'Das sind wir', 'Aus dem Hobby <em>wurde ein Beruf.</em>', [
            'Michael Ludmann und Enno Ortmann haben sich in der Berufsschule kennengelernt, gemeinsam die Meisterschule gemacht und unzählige Stunden an alten Autos geschraubt.',
            '2022 wurde aus der Freizeit der Hauptberuf: die eigene Werkstatt mit Schwerpunkt Young- und Oldtimer. Ob Ölwechsel oder Vollrestauration, die Freude an einem seltenen Auto in der Halle spürt man bei jedem Auftrag.'],
            'team.jpg', cap='Das Team von Werk Zwo mit eigenen Klassikern', tl=[('2022', 'Start der eigenen Werkstatt'), ('70er–90er', 'unsere Lieblingsjahrgänge'), ('4,8', 'Sterne bei Google')])
        + tabs('leistungen', 'Unser Angebot', 'Vom Bremsbelag <em>bis zur Vollrestauration.</em>', 'Alles aus einer Hand, für Klassiker und für Ihr Alltagsauto.', [
            ('Service &amp; Instandhaltung', 'l-service.jpg', 'Alle Wartungsarbeiten für Ihr Fahrzeug, vom Bremsbelag bis zur Saisonabschluss-Durchsicht.', ['Wartung', 'Durchsicht']),
            ('Restauration', 'l-resto.jpg', 'Einmal alles, bitte. Wir übernehmen Ihr Projekt, auch wenn es mehr Liebe braucht: Projektplanung, Kalkulation und Koordination der Fremdfirmen aus einer Hand.', ['Planung', 'Kalkulation', 'Koordination']),
            ('Reparatur', 'l-rep.jpg', 'Der Zahn der Zeit hat zugeschlagen oder die letzte Ausfahrt ging schief? Für Reparaturen aller Art an Young- und Oldtimern sind wir die Richtigen.', ['Karosserie', 'Mechanik']),
            ('Konservierung', 'l-kons.jpg', 'Was einem am Herzen liegt, muss geschützt werden. Mit unserem Partner Mike Sanders halten wir den Rost lange fern.', ['Mike Sanders']),
            ('HU &amp; H-Abnahme', 'l-hu.jpg', 'Hauptuntersuchung durch unsere Partner von TÜV Nord und Dekra, ebenso die H-Abnahme Ihres Klassikers.', ['TÜV Nord', 'Dekra']),
            ('Service für alle Baujahre', 'l-modern.jpg', 'Natürlich betreuen wir auch Ihr aktuelles Auto, inklusive Inspektion nach Herstellervorgaben.', ['Inspektion nach Herstellervorgabe'])], 'dk')
        + faces('team', 'Das Team', 'Mit wem Sie es <em>zu tun haben.</em>', 'Vom Kfz-Meister mit Jahrzehnten Erfahrung bis zum Auszubildenden: Alle arbeiten eng zusammen und lernen voneinander.', [
            ('t-michael.jpg', 'Michael Ludmann · Kfz-Meister'), ('t-enno.jpg', 'Enno Ortmann · Kfz-Meister'), ('t-helmut.jpg', 'Helmut Nelson · Kfz-Meister'), ('t-thomas.jpg', 'Thomas Roth · Kfz-Meister, Karosseriebauer'),
            ('t-karl.jpg', 'Karl-Alexander Kessen · Kfz-Mechatroniker'), ('t-hauke.jpg', 'Hauke Doll · Kfz-Mechatroniker'), ('t-julia.jpg', 'Julia Wehmeyer · Buchhaltung'), ('t-mika.jpg', 'Mika Lehners · Auszubildender')])
        + promo('ankauf', 'p-ankauf.jpg', 'Klassiker abzugeben?', 'Träume auf die <em>Straße bringen.</em>', 'Beim Hauskauf einen Oldtimer in der Garage entdeckt oder die Restauration unterschätzt? Wir machen Ihnen ein Angebot für Ihren Klassiker, egal welche Marke, welches Alter, welcher Zustand. Und wir helfen bei der Suche nach dem Auto, von dem Sie als Kind geträumt haben.', ['Ankauf jeder Marke und jedes Zustands', 'Unterstützung bei der Fahrzeugsuche'], 'Klassiker anbieten', 'alt')
        + reviews(s, ['Mit Abstand die beste Werkstatt, in der ich je war. Ehrliche Kommunikation, keine unnötigen Reparaturen, keine versteckten Kosten.',
                      'Hervorragende Werkstatt für Old- und Youngtimer. Immer freundlich, viel Fachwissen und echter Einsatz.',
                      'Zuverlässig, pünktlich und fair im Preis. Alle Zusagen wurden eingehalten.',
                      'Enno und Michael wissen genau, was sie tun. Freundlicher Empfang, auch ohne Termin.'])
        + contact(s, 'dk') + footer(s) + pop(dict(img='p-ankauf.jpg', ey='Ankauf', h='Klassiker in der Garage?', p='Wir machen Ihnen ein Angebot, egal in welchem Zustand.', btn='Jetzt anfragen')))

SITES['werkzwo'] = dict(
    slug='werk-zwo-quakenbrueck', firma='Werk Zwo GmbH', web='werkzwo.de', fonts='r13werk',
    title='Werk Zwo – Old- & Youngtimer-Service in Quakenbrück', desc='Kfz-Meisterwerkstatt für Old- und Youngtimer in Quakenbrück: Service, Restauration, Reparatur, Konservierung, HU und H-Abnahme.',
    tel='05431 9579428', tel_i='+4954319579428', mail='info@werkzwo.de', adresse='Lange Straße 84, 49610 Quakenbrück', google=('4,8', 26),
    cta='Werkstatttermin anfragen', nav=[('Über uns', 'wir'), ('Leistungen', 'leistungen'), ('Team', 'team'), ('Ankauf', 'ankauf'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 16:30')],
    form_opts=['Service &amp; Wartung', 'Restauration', 'Reparatur', 'Konservierung', 'HU / H-Abnahme', 'Klassiker verkaufen'], form_h3='Werkstatttermin anfragen', form_p='Erzählen Sie uns kurz von Ihrem Auto. Wir rufen zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Bringen Sie <em>Ihren Klassiker vorbei.</em>', kt_p='Ob Saisoncheck oder Projekt fürs Leben: Wir beraten Sie gern.',
    rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Otto', 'Ihr Oldtimer-Lotse', 'Werk Zwo', [['Nur Oldtimer?', 'Schwerpunkt sind Young- und Oldtimer, aber wir betreuen auch Ihr aktuelles Auto nach Herstellervorgabe.'], ['H-Abnahme?', 'Ja, mit unseren Partnern von TÜV Nord und Dekra.'], ['Öffnungszeiten', 'Mo–Fr 8:00–16:30 Uhr. Telefon 05431 9579428.']], ['wir', 'leistungen', 'team', 'kontakt']),
    vars='--bg:#f4efe6;--ink:#17150f;--mute:#5e584c;--p:#17150f;--a:#e9dcc2;--a-ink:#17150f;--dk:#17150f;--s:#fffaf1;--s2:#ebe3d3;--fh:"Bebas Neue",Impact,sans-serif;--fb:"Libre Franklin",system-ui,sans-serif;--r:6px;--r2:8px;--br:4px;--hero-ov:linear-gradient(90deg,rgba(15,13,9,.86) 0%,rgba(15,13,9,.5) 55%,rgba(15,13,9,.1) 100%);--mq-bg:#17150f;--mq-ink:#e9dcc2;--hd-bg:rgba(23,21,15,.92);--hd-ink:#f4efe6;--logo-h:44px;--ft-bg:#0f0d09',
    css='''.hs h1,.h2{font-weight:400;letter-spacing:.01em;line-height:.95;text-transform:uppercase}.hs h1{font-size:clamp(56px,7.4vw,124px)}.h2{font-size:clamp(44px,5vw,78px)}
.hs h1 em{font-style:normal;color:#e9dcc2}.h2 em{font-style:normal;color:#8a6d3b}.dk .h2 em{color:#e9dcc2}
.hs .big{font-family:var(--fh);-webkit-text-stroke:2px rgba(233,220,194,.28)}
.hd .logo img{background:#fffaf1;padding:6px 10px;border-radius:4px}.ft img{background:#fffaf1;padding:8px 12px;border-radius:4px;height:52px}
.alt{background:var(--s2)}#wir figure img{aspect-ratio:1500/845;height:auto}.fc{--fc-ar:1/1}.fc figure{background:#fffaf1}
.mq span{font-family:var(--fh);font-size:26px;letter-spacing:.04em}.sp .row div::before,.chip b{font-family:var(--fh)}
.tb .pv figure{aspect-ratio:4/3;height:auto}''',
    img={'logo.png': ('werkzwo/img/i003.jpg', 0, 'trimalpha'), 'h1.jpg': ('werkzwo/img/i006.jpg', 0), 'h2.jpg': ('werkzwo/img/i007.jpg', 0), 'h3.jpg': ('werkzwo/img/i008.jpg', 0),
         'team.jpg': ('werkzwo/img/i016.jpg', 0), 'p-ankauf.jpg': ('werkzwo/img/i004.jpg', 0),
         'l-service.jpg': ('werkzwo/img/i004.jpg', 0), 'l-resto.jpg': ('werkzwo/img/i001.jpg', 0, (0, .17, 1, .67)), 'l-rep.jpg': ('werkzwo/img/i007.jpg', 1200, (0, 0, .8, 1)), 'l-kons.jpg': ('werkzwo/img/i006.jpg', 1200, (.1, 0, .85, 1)),
         'l-hu.jpg': ('werkzwo/img/i002.jpg', 0), 'l-modern.jpg': ('werkzwo/img/i019.jpg', 0),
         't-michael.jpg': ('werkzwo/img/i014.jpg', 700), 't-enno.jpg': ('werkzwo/img/i009.jpg', 700), 't-helmut.jpg': ('werkzwo/img/i011.jpg', 700), 't-thomas.jpg': ('werkzwo/img/i017.jpg', 700),
         't-karl.jpg': ('werkzwo/img/i013.jpg', 700), 't-hauke.jpg': ('werkzwo/img/i010.jpg', 700), 't-julia.jpg': ('werkzwo/img/i012.jpg', 700), 't-mika.jpg': ('werkzwo/img/i015.jpg', 700)},
    body=b_werkzwo)

# ───────────────────────── 2. AS Reifen-Service, Bersenbrück ─────────────────────────
def b_asreifen(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 60%',
        ey='Reifen- und Fahrzeugservice · Bersenbrück',
        h1='Ihr Profi für Reifen. <em>Seit 1994.</em>',
        sub='Reifen, Felgen, Achsvermessung und Reparaturen für alle Marken, vom Kleinwagen bis zum Lkw. Dazu Gebrauchtwagen mit Garantie und Finanzierung. Alles an der Max-Planck-Straße.',
        badge=('1994', 'gegründet in Bersenbrück')))
        + marquee(['Reifenservice', 'Felgen', 'Achsvermessung', 'Reifeneinlagerung', 'RDKS', 'Kfz-Reparatur', 'Autoglas', 'Fahrzeughandel'])
        + duo('leistungen', 'Zwei Schwerpunkte', 'Reifen-Experte <em>und Meisterwerkstatt.</em>', 'Für alle Marken und alle Fahrzeugklassen.', [
            ('Reifen &amp; Felgen', 'Reifenservice', 'd-reifen.jpg', 'Motorrad-, Pkw-, Lkw-, Bau- und Landmaschinenreifen fast aller Hersteller. Montage von UHP- und Runflat-Reifen nach WDK-Vorgabe in allen Größen.', ['Reifenreparatur', 'RDKS-Diagnose', 'Einlagerung', 'Felgenaufbereitung'], 'Reifentermin anfragen'),
            ('Werkstatt', 'Kfz-Service', 'd-werk.jpg', 'Reparatur aller Fahrzeugklassen: Zahnriemen, Ölwechsel, Bremsen, Fahrwerk und Achsvermessung mit Idealwerten für lange Reifenlebensdauer.', ['Achsvermessung', 'Fahrwerkstechnik', 'Autoglas', 'Hauptuntersuchung'], 'Werkstatttermin anfragen')])
        + gallery('galerie', 'Aus unserer Halle', 'Felgen, die <em>Eindruck machen.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', '', '50% 50%'), ('g7.jpg', '', '50% 50%'), ('g8.jpg', '', '50% 50%')], 'alt')
        + promo('fahrzeuge', 'p-auto.jpg', 'Fahrzeughandel', 'Gebrauchtwagen <em>mit Garantie.</em>', 'Ständig Gebrauchtwagen vor Ort. Wir beraten Sie beim Kauf, zur Garantie und zur Finanzierung mit Laufzeit, Anzahlung und Rate nach Ihren Wünschen.', ['Gebrauchtwagengarantie', 'Finanzierung mit festen Raten', 'Ankauf Ihres Fahrzeugs'], 'Fahrzeug anfragen')
        + story('team', 'Unternehmen', 'Ein Betrieb, <em>zwei Macher.</em>', [
            'Andreas Stuckwisch hat AS Reifen-Service 1994 gegründet. Seit September 2019 führt Viktor Grigorev den Betrieb, in der Werkstatt unterstützt von Michail Prichodjko.',
            'Was gleich geblieben ist: Sie als Kunde stehen im Mittelpunkt. Ehrliche Beratung, saubere Arbeit und Lösungen, die passen.'],
            'haus.jpg', cap='Unser Betrieb an der Max-Planck-Straße 21', tl=[('1994', 'Gründung'), ('2019', 'neue Geschäftsführung'), ('4,8', 'Sterne bei Google')], rev=True)
        + reviews(s, ['Reifenwechsel gemacht und begeistert: freundlich, sauber, schnell und fair im Preis.',
                      'Zwei entspannte Typen, mit denen man gut reden kann, und technisch einwandfreie Arbeit. Mit meinem Oldtimer bin ich Stammkunde.',
                      'Schnell, unkompliziert und preiswert. Mögliche Probleme werden direkt angesprochen, mit passender Lösung.',
                      'Top Service.'])
        + contact(s) + footer(s) + pop(dict(img='g2.jpg', ey='Reifenwechsel', h='Jetzt Termin sichern', p='Wechsel, Einlagerung und Felgenservice an einem Ort.', btn='Termin anfragen')))

SITES['asreifen'] = dict(
    slug='as-reifen-service-bersenbrueck', firma='AS Reifen-Service GmbH', web='a-s-reifen.de', fonts='r13as',
    title='AS Reifen-Service – Reifen und Kfz-Service in Bersenbrück', desc='Reifenservice, Felgen, Achsvermessung und Kfz-Reparaturen für alle Marken in Bersenbrück, seit 1994. Gebrauchtwagen mit Garantie und Finanzierung.',
    tel='05439 2107', tel_i='+4954392107', mail='info@a-s-reifen.de', adresse='Max-Planck-Straße 21, 49593 Bersenbrück', google=('4,8', 57),
    cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), ('Galerie', 'galerie'), ('Fahrzeuge', 'fahrzeuge'), ('Über uns', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 12:30'), ('', '13:30 – 17:00'), ('Sa', 'nach Vereinbarung')],
    form_opts=['Reifenwechsel', 'Felgen', 'Achsvermessung', 'Reparatur', 'Gebrauchtwagen', 'Sonstiges'], form_h3='Termin anfragen', form_p='Wir rufen Sie zurück und finden einen Termin.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Rollen Sie <em>einfach vorbei.</em>', kt_p='Oder rufen Sie an, wir nehmen uns Zeit für Ihre Fragen.',
    social=[('Instagram', 'https://www.instagram.com/as_reifen_service_gmbh/'), ('Facebook', 'https://www.facebook.com/profile.php?id=100063517571788'), ('TikTok', 'https://www.tiktok.com/@asreifenservice')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Rita', 'Ihre Reifen-Lotsin', 'AS Reifen-Service', [['Reifen einlagern?', 'Ja, wir lagern Ihre Sommer- oder Winterräder fachgerecht ein.'], ['Alle Marken?', 'Ja, Reparaturen aller Marken und Fahrzeugklassen.'], ['Öffnungszeiten', 'Mo–Fr 8:00–12:30 und 13:30–17:00 Uhr, Samstag nach Vereinbarung.']], ['leistungen', 'galerie', 'fahrzeuge', 'kontakt']),
    vars='--bg:#fff;--ink:#141414;--mute:#55575c;--p:#d71920;--a:#d71920;--a-ink:#fff;--dk:#141414;--s:#fff;--s2:#f3f3f3;--fh:"Saira Condensed",system-ui,sans-serif;--fb:"Saira",system-ui,sans-serif;--r:4px;--r2:6px;--br:4px;--mq-bg:#d71920;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.95);--hd-ink:#141414;--logo-h:52px;--ft-bg:#111;--hp-bg:linear-gradient(115deg,#fff 0%,#fff 55%,#f1f1f1 55%,#e9e9e9 100%)',
    css='''.hp h1,.h2{font-weight:800;text-transform:uppercase;letter-spacing:-.005em;line-height:1.04;padding-top:4px}.hp h1{font-size:clamp(50px,6vw,96px)}.comp{height:clamp(380px,38vw,500px)}.hp .ey{margin-bottom:14px}.h2{font-size:clamp(40px,4.6vw,70px)}
.hp h1 em,.h2 em{font-style:normal;color:var(--p)}.hp::before{display:none}.comp figure{border-radius:4px;transform:skewX(-3deg)}.comp figure img{transform:skewX(3deg) scale(1.06)}
.comp .badge{background:#141414;color:#fff;transform:skewX(-6deg)}.comp .badge b{color:#fff}
.mq span{font-family:var(--fh);font-weight:800;text-transform:uppercase;font-size:24px}.alt{background:var(--s2)}
.ft img{background:#fff;padding:8px 12px;border-radius:4px;height:60px}.duo .wd{min-height:520px}''',
    img={'logo.png': ('asreifen/img/i184.png', 0, 'alphacrop'), 'h1.jpg': ('asreifen/img/i028.jpg', 0), 'h2.jpg': ('asreifen/img/i027.jpg', 0), 'h3.jpg': ('asreifen/img/i001.jpg', 0),
         'd-reifen.jpg': ('asreifen/img/i005.jpg', 0), 'd-werk.jpg': ('asreifen/img/i002.jpg', 0), 'p-auto.jpg': ('asreifen/img/i041.jpg', 0), 'haus.jpg': ('asreifen/img/i011.jpg', 0),
         'g1.jpg': ('asreifen/img/i039.jpg', 0), 'g2.jpg': ('asreifen/img/i017.jpg', 0), 'g3.jpg': ('asreifen/img/i029.jpg', 0), 'g4.jpg': ('asreifen/img/i037.jpg', 0), 'g5.jpg': ('asreifen/img/i042.jpg', 0), 'g6.jpg': ('asreifen/img/i026.jpg', 0), 'g7.jpg': ('asreifen/img/i003.jpg', 0), 'g8.jpg': ('asreifen/img/i019.jpg', 0)},
    body=b_asreifen)

# ───────────────────────── 3. Auto Böcker, Quakenbrück ─────────────────────────
def b_boecker(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h3.jpg'], big='1948', pos={'h1.jpg': '50% 60%', 'h3.jpg': '50% 50%'},
        ey='Auto Böcker · Quakenbrück · seit 1948',
        h1='Hyundai. Mercedes-Benz. <em>Lkw aller Marken.</em>',
        sub='Seit drei Generationen Ihr Partner in Quakenbrück: Neu- und Gebrauchtwagen, Service für Pkw, Vans und Lkw, Unfallservice und Ersatzteile aus einer Hand.',
        ubar=[('Hyundai Partner', 'Verkauf und Service'), ('Mercedes-Benz Partner', 'Pkw und Van-Werkstatt'), ('Freie Lkw-Werkstatt', 'für jede Marke')]))
        + duo('marken', 'Unsere Partnermarken', 'Zwei Marken. <em>Ein Ansprechpartner.</em>', 'Verkauf an der Badberger Straße 46, Service an der Hindenburgstraße 21.', [
            ('Hyundai Partner', 'Hyundai', 'd-hyundai.jpg', 'Neuwagen, Leasing und Finanzierung, Jahres- und Gebrauchtwagen. In der Werkstatt betreuen wir Hyundai-Verbrenner und Elektroautos.', ['Neuwagen &amp; Leasing', 'Service Verbrenner', 'Service Elektro'], 'Hyundai anfragen'),
            ('Mercedes-Benz Partner', 'Mercedes-Benz', 'd-mb.jpg', 'Jahreswagen, Finanzierungen und Gebrauchtfahrzeuge. Unsere Werkstatt kümmert sich um Mercedes-Pkw und Vans wie den Sprinter.', ['Jahreswagen', 'Pkw-Service', 'Van-Service'], 'Servicetermin anfragen')])
        + panels('service', 'Werkstatt &amp; Service', 'Damit Sie <em>schnell wieder fahren.</em>', 'Für Pkw, Vans und Nutzfahrzeuge.', [
            ('Lkw-Werkstatt', 'p-lkw.jpg', 'Als freie Lkw-Werkstatt reparieren und warten wir Lkw aller Marken, von Mercedes über MAN bis Volvo, und beschaffen Originalteile.', '50% 40%'),
            ('Unfallservice', 'p-unfall.jpg', 'Glasschaden, Beule oder großer Unfall: Wir kümmern uns vom Gutachten über die Reparatur bis zur Abwicklung mit Ihrer Versicherung.', '50% 50%'),
            ('Pkw-Werkstatt', 'p-pkw.jpg', 'Wartung, Diagnose und Reparatur für Hyundai und Mercedes-Benz, mit geschultem Team und Original-Technik.', '50% 50%'),
            ('Ersatzteile', 'p-teile.jpg', 'Original- und Teile aus dem freien Handel für Pkw und Lkw aller Marken. Preisanfrage oder Bestellung ganz einfach per Formular.', '50% 50%')], 'dk')
        + story('historie', 'Seit drei Generationen', 'Angefangen mit <em>Hammer und Zange.</em>', [
            '1948 gründete Franz Böcker das Unternehmen mit seiner Frau Wilhelmine. Er beulte Kotflügel der ersten Nachkriegsautos aus, bald folgten Reparaturen, Spezialaufbauten und Anhänger.',
            'Heute führen Stefan und Axel Böcker die Böcker Gruppe, und die vierte Generation ist schon an Bord.'],
            'hist.jpg', cap='Aus den Anfängen der Firma Böcker', tl=[('1948', 'Gründung durch Franz und Wilhelmine Böcker'), ('1959', 'Daimler-Benz Vertragswerkstatt'), ('2019', 'Hyundai kommt dazu'), ('2021', 'die vierte Generation startet')])
        + gallery('chronik', 'Chronik in Bildern', 'Von der Werkstatt <em>zum Autohaus.</em>', [
            ('c1.jpg', 'w2 h2r', '50% 50%'), ('c2.jpg', '', '50% 50%'), ('c3.jpg', '', '50% 50%'), ('c4.jpg', '', '50% 50%'), ('c5.jpg', '', '50% 50%')], 'alt')
        + reviews(s, ['Fahrzeug online entdeckt, kurz telefonisch beraten und gekauft. Die Abholung lief sehr gut und unkompliziert, mit Getränk und montierten Kennzeichen.',
                      'Beim nächsten Hyundai kaufen wir gern wieder hier.',
                      'Super.'])
        + contact(s) + footer(s) + pop(dict(img='p-unfall.jpg', ey='Unfallservice-Hotline', h='Es hat gekracht?', p='Wir helfen schnell, vom Gutachten bis zur Versicherung. 05431 94550.', btn='Jetzt melden')))

SITES['boecker'] = dict(
    slug='auto-boecker-quakenbrueck', firma='Auto Böcker GmbH', web='auto-boecker.de', fonts='r13boe',
    title='Auto Böcker – Hyundai und Mercedes-Benz Partner in Quakenbrück', desc='Hyundai und Mercedes-Benz Partner in Quakenbrück seit 1948: Neu- und Gebrauchtwagen, Pkw-, Van- und Lkw-Werkstatt, Unfallservice und Ersatzteile.',
    tel='05431 94550', tel_i='+49543194550', mail='info@boecker-gruppe.de', adresse='Hindenburgstraße 21, 49610 Quakenbrück', google=('4,8', 221),
    cta='Servicetermin anfragen', nav=[('Marken', 'marken'), ('Service', 'service'), ('Historie', 'historie'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '07:30 – 18:00'), ('Sa', '07:30 – 12:00')],
    form_opts=['Hyundai-Servicetermin', 'Mercedes-Servicetermin', 'Lkw-Werkstatt', 'Unfallservice', 'Fahrzeugangebot', 'Ersatzteile'], form_h3='Termin anfragen', form_p='Sagen Sie uns, worum es geht. Wir melden uns zeitnah.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Zwei Standorte. <em>Ein Team.</em>', kt_p='Service an der Hindenburgstraße 21, Verkauf an der Badberger Straße 46 in Quakenbrück.',
    rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Franz', 'Ihr Böcker-Lotse', 'Auto Böcker', [['Welche Marken?', 'Wir sind Hyundai und Mercedes-Benz Partner, die Lkw-Werkstatt arbeitet markenfrei.'], ['Unfall?', 'Unfallservice-Hotline: 05431 94550.'], ['Öffnungszeiten', 'Mo–Fr 7:30–18 Uhr, Sa 7:30–12 Uhr.']], ['marken', 'service', 'historie', 'kontakt']),
    vars='--bg:#fff;--ink:#0f1a2a;--mute:#556274;--p:#1f5fae;--a:#1f5fae;--a-ink:#fff;--dk:#0d1726;--s:#fff;--s2:#f1f4f8;--fh:"Plus Jakarta Sans",system-ui,sans-serif;--fb:"Plus Jakarta Sans",system-ui,sans-serif;--r:12px;--r2:18px;--br:999px;--hero-ov:linear-gradient(90deg,rgba(9,17,30,.9) 0%,rgba(9,17,30,.55) 55%,rgba(9,17,30,.15) 100%);--mq-bg:#0d1726;--mq-ink:#fff;--hd-bg:rgba(13,23,38,.94);--hd-ink:#fff;--logo-h:38px;--ft-bg:#09111e',
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.03em;line-height:1.02}.hs h1{font-size:clamp(40px,5vw,78px)}.hs h1 em,.h2 em{font-family:"Libre Caslon Text",Georgia,serif;font-style:italic;font-weight:400;color:#8fb8ea}
.h2 em{color:var(--p)}.dk .h2 em{color:#8fb8ea}.hs .big{font-family:"Libre Caslon Text",serif;font-style:italic;-webkit-text-stroke:1.5px rgba(143,184,234,.3)}
.hd .logo img{background:#fff;padding:6px 12px;border-radius:8px}.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:50px}
.alt{background:var(--s2)}#historie figure img{aspect-ratio:3/2;height:auto;filter:sepia(.15)}.gl figure img{filter:sepia(.1)}''',
    img={'logo.png': ('boecker/img/i008.png', 0, 'alphacrop'), 'h1.jpg': ('boecker/img/i038.jpg', 0), 'h3.jpg': ('boecker/img/i042.jpg', 0),
         'd-hyundai.jpg': ('boecker/img/i007.jpg', 0), 'd-mb.jpg': ('boecker/img/i049.jpg', 0),
         'p-lkw.jpg': ('boecker/img/i034.jpg', 1800), 'p-unfall.jpg': ('boecker/img/i026.jpg', 0), 'p-pkw.jpg': ('boecker/img/i028.jpg', 0), 'p-teile.jpg': ('boecker/img/i040.jpg', 0),
         'hist.jpg': ('boecker/img/i053.jpg', 0), 'c1.jpg': ('boecker/img/i052.jpg', 0), 'c2.jpg': ('boecker/img/i045.jpg', 0), 'c3.jpg': ('boecker/img/i054.jpg', 0), 'c4.jpg': ('boecker/img/i058.jpg', 0), 'c5.jpg': ('boecker/img/i062.jpg', 0)},
    body=b_boecker)

# ───────────────────────── 4. Autohaus Sendur, Menslage ─────────────────────────
def b_sendur(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 60%', 'h2.jpg': '50% 60%', 'h3.jpg': '50% 60%'},
        ey='Autohaus Sendur · Menslage',
        h1='Ihr nächstes Auto <em>steht schon hier.</em>',
        sub='Geprüfte Gebrauchtwagen vieler Marken, fairer Ankauf und eine eigene Kfz-Werkstatt. Transparent, persönlich und mit 4,9 Sternen aus 178 Google-Bewertungen.',
        ubar=[('Gebrauchtwagen', 'gründlich geprüft'), ('Fahrzeugankauf', 'fair bewertet'), ('Werkstatt', 'Reifen, Unfall, TÜV')]))
        + marquee(['Gebrauchtwagen', 'Fahrzeugankauf', 'Kfz-Werkstatt', 'Unfallservice', 'Reifenservice', 'Inspektion &amp; TÜV', 'Autoglas'])
        + scroller('fahrzeuge', 'Aus unserem Showroom', 'Vielfalt, <em>die Sie sehen können.</em>', 'Jedes Fahrzeug wird vor dem Verkauf gründlich geprüft. Den aktuellen Bestand zeigen wir Ihnen gern persönlich.', [
            ('Kompakt bis SUV', 'f1.jpg', 'Vom Stadtflitzer bis zum Familien-SUV.', '50% 60%'), ('Geprüfte Qualität', 'f2.jpg', 'Jedes Auto wird auf Herz und Nieren geprüft.', '50% 60%'),
            ('Viele Marken', 'f3.jpg', 'Fahrzeuge unterschiedlichster Hersteller.', '50% 60%'), ('Faire Preise', 'f4.jpg', 'Transparent und ohne Überraschungen.', '50% 60%'), ('Probefahrt', 'f5.jpg', 'Kommen Sie vorbei und fahren Sie Probe.', '50% 60%')])
        + promo('ankauf', 'p-ankauf.jpg', 'Fahrzeugankauf', 'Wir kaufen <em>Ihr Auto.</em>', 'Egal welche Marke, welches Modell, welcher Zustand: Unsere Experten bewerten Ihr Fahrzeug sachkundig und machen Ihnen ein faires Angebot.', ['Unabhängig von Marke und Zustand', 'Transparente Bewertung', 'Unkomplizierter Ablauf'], 'Auto bewerten lassen', 'alt')
        + svc('werkstatt', 'Werkstatt &amp; Service', 'Alles rund ums Auto <em>unter einem Dach.</em>', 'Moderne Diagnosetechnik und hochwertige Ersatzteile.', [
            ('Kfz-Werkstatt', 'Inspektionen bis spezialisierte Reparaturen an Motor, Bremsen, Fahrwerk und Elektronik.'), ('Unfallservice', 'Karosserie und Lack, damit Ihr Auto wieder in den Originalzustand kommt.'),
            ('Reifenservice', 'Reifen namhafter Marken, Montage und Auswuchtung.'), ('Inspektion &amp; TÜV', 'Vorab-Check und reibungsloser Ablauf bei der Hauptuntersuchung.')], 'dk')
        + reviews(s, ['Auto hier gekauft und alles lief genau wie erwartet. Viele Infos, Fotos, Videos und sogar die Servicehistorie, und viel Geduld bei der Entscheidung.',
                      'Herr Sendur hat jede Frage klar beantwortet, auch aus der Ferne. Von Anfang an großes Vertrauen.',
                      'Schnelle Lösungen und freundliches Personal.', 'Top Service.'])
        + contact(s) + footer(s) + pop(dict(img='p-ankauf.jpg', ey='Ankauf', h='Was ist Ihr Auto wert?', p='Wir bewerten es fair und unkompliziert.', btn='Jetzt anfragen')))

SITES['sendur'] = dict(
    slug='autohaus-sendur-menslage', firma='Autohaus Sendur GmbH', web='autohaus-sendur.de', fonts='r13sen',
    title='Autohaus Sendur – Gebrauchtwagen und Werkstatt in Menslage', desc='Geprüfte Gebrauchtwagen vieler Marken, fairer Fahrzeugankauf und Kfz-Werkstatt in Menslage.',
    tel='05437 9696923', tel_i='+4954379696923', mail='info@autohaus-sendur.de', adresse='Quakenbrücker Straße 24, 49637 Menslage', google=('4,9', 178),
    cta='Probefahrt anfragen', nav=[('Fahrzeuge', 'fahrzeuge'), ('Ankauf', 'ankauf'), ('Werkstatt', 'werkstatt'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 17:00'), ('Sa', '08:00 – 13:00')],
    form_opts=['Probefahrt', 'Fahrzeug anfragen', 'Auto verkaufen', 'Werkstatttermin', 'Unfall', 'Sonstiges'], form_h3='Anfrage senden', form_p='Wir melden uns schnell, auch per WhatsApp.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Sie.</em>', kt_p='Kommen Sie nach Menslage, oder schreiben Sie uns per WhatsApp: 0176 34373185.',
    social=[('WhatsApp', 'https://api.whatsapp.com/send?phone=4917634373185')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Selin', 'Ihre Autohaus-Lotsin', 'Autohaus Sendur', [['Kaufen Sie mein Auto?', 'Ja, unabhängig von Marke, Modell und Zustand.'], ['Probefahrt?', 'Gern, rufen Sie an: 05437 9696923.'], ['Öffnungszeiten', 'Mo–Fr 8–17 Uhr, Sa 8–13 Uhr.']], ['fahrzeuge', 'ankauf', 'werkstatt', 'kontakt']),
    vars='--bg:#fff;--ink:#1b1c20;--mute:#5a5d66;--p:#d01c27;--a:#d01c27;--a-ink:#fff;--dk:#1b1c20;--s:#fff;--s2:#f2f2f4;--fh:"Exo 2",system-ui,sans-serif;--fb:"Nunito Sans",system-ui,sans-serif;--r:14px;--r2:22px;--br:999px;--hero-ov:linear-gradient(180deg,rgba(18,18,22,.15) 0%,rgba(18,18,22,.55) 45%,rgba(18,18,22,.9) 100%);--mq-bg:#1b1c20;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.95);--hd-ink:#1b1c20;--logo-h:46px;--ft-bg:#141418',
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.02em;line-height:1}.hs h1{font-size:clamp(44px,5.6vw,88px)}.hs h1 em,.h2 em{font-style:italic;color:var(--p)}.hs h1 em{color:#ff5a62}
.hs .w{justify-content:flex-end}.hs .ey{color:#ff8a90!important}.hd.lt:not(.scr) .logo img{filter:brightness(0) invert(1)}.alt{background:var(--s2)}.ft img{background:#fff;padding:8px 12px;border-radius:10px;height:54px}
.sc .cd figure{aspect-ratio:16/10}''',
    img={'logo.png': ('sendur/img/i008.png', 0, 'alphacrop'), 'h1.jpg': ('sendur/img/i019.jpg', 0), 'h2.jpg': ('sendur/img/i034.jpg', 0), 'h3.jpg': ('sendur/img/i041.jpg', 0),
         'f1.jpg': ('sendur/img/i023.jpg', 1100), 'f2.jpg': ('sendur/img/i046.jpg', 1100), 'f3.jpg': ('sendur/img/i037.jpg', 1100), 'f4.jpg': ('sendur/img/i022.jpg', 1100), 'f5.jpg': ('sendur/img/i044.jpg', 1100),
         'p-ankauf.jpg': ('sendur/img/i031.jpg', 0)},
    body=b_sendur)

# ───────────────────────── 5. Auto Berling, Ankum ─────────────────────────
def b_berling(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 60%',
        ey='Kfz-Meisterbetrieb · Ankum',
        h1='Autohaus, Werkstatt, <em>Tankstelle.</em>',
        sub='Gebrauchtwagen aller Marken mit EGA-Qualitätscheck, Reparatur aller Marken mit moderner Diagnose, freie Tankstelle und Waschpark. Leidenschaft ist unser Antrieb.',
        badge=('84', 'Punkte-Check für jeden Gebrauchten')))
        + duo('angebot', 'Drei Bereiche', 'Alles rund ums Auto <em>in Ankum.</em>', '', [
            ('Werkstatt', 'Reparatur aller Marken', 'd-werk.jpg', 'Mit Diagnosegeräten und Original-Markentestern lesen wir die Fehlerspeicher aller gängigen Modelle. Wartung nach Herstellervorschrift, auf Wunsch mit Mobilitätsgarantie. Auch Wohnmobile sind bei uns in guten Händen.', ['Diagnose', 'Wartung nach Vorschrift', 'Nachrüstung'], 'Werkstatttermin anfragen'),
            ('Autohaus', 'Gebrauchtwagen mit Check', 'd-auto.jpg', 'Jedes Fahrzeug durchläuft vor dem Verkauf einen 84-Punkte-Check, umfangreicher als eine Hauptuntersuchung. Dazu auf Wunsch eine umfassende Garantie.', ['EGA-Qualitätscheck', 'Garantie', 'Wunschautosuche'], 'Fahrzeug anfragen')])
        + promo('tanken', 'p-tanken.jpg', 'Tanken &amp; Waschen', 'Frei tanken. <em>Sauber fahren.</em>', 'Als freie Tankstelle unabhängig von großen Konzernen: Super und SuperPlus an der Loxtener Straße 1 und der Bersenbrücker Straße 19. Im Waschpark an der Alfons-Schulte-Straße 8 warten zwei Pkw- und ein Lkw-Waschplatz und eine Waschanlage mit Osmose-Wasser.', ['Super &amp; SuperPlus', 'Waschanlage mit 6 Programmen', 'Handwäsche-Plätze für Pkw und Lkw'], 'Route planen', 'alt')
        + faces('team', 'Ihre Ansprechpartner', 'Ein Team, <em>das Sie kennt.</em>', 'Geschäftsleitung: Heinrich Berling und Ben Kortland. Im Verkauf berät Sie unter anderem Gudrun Berling.', [
            ('t1.jpg', 'Gudrun Berling · Verkauf'), ('t2.jpg', ''), ('t3.jpg', ''), ('t4.jpg', ''), ('t5.jpg', ''), ('t6.jpg', ''), ('t7.jpg', ''), ('t8.jpg', ''), ('t9.jpg', ''), ('t10.jpg', '')])
        + reviews(s, ['Mit unserem Wohnmobil sind wir Stammkunden. Sehr gute Arbeit, Termine werden eingehalten und die Mitarbeiter sind unglaublich freundlich.',
                      'Wischergestänge am Wohnmobil gebrochen: herzlicher Empfang, Teile sofort bestellt, am nächsten Morgen ging die Reise weiter.',
                      'Batterie leer mitten in Ankum, der Mechaniker war in wenigen Minuten da. Einfach fantastisch.',
                      'Top Werkstatt. Ben regelt alles perfekt.'])
        + contact(s, 'dk') + footer(s) + pop(dict(img='d-werk.jpg', ey='Werkstatt', h='Panne mit dem Wohnmobil?', p='Wir helfen schnell, auch auf der Durchreise. 05462 366.', btn='Jetzt anfragen')))

SITES['berling'] = dict(
    slug='auto-berling-ankum', firma='Auto Berling', web='auto-berling.de', fonts='r13ber',
    title='Auto Berling – Werkstatt, Autohaus und Tankstelle in Ankum', desc='Kfz-Meisterbetrieb in Ankum: Reparatur aller Marken, Gebrauchtwagen mit 84-Punkte-Check, freie Tankstelle und Waschpark.',
    tel='05462 366', tel_i='+495462366', mail='info@auto-berling.de', adresse='Loxtener Straße 1, 49577 Ankum', google=('4,9', 23),
    cta='Termin anfragen', nav=[('Angebot', 'angebot'), ('Tanken &amp; Waschen', 'tanken'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '07:00 – 18:00'), ('Sa', '08:00 – 13:00')],
    form_opts=['Werkstatttermin', 'Wohnmobil-Service', 'Gebrauchtwagen', 'Wunschauto suchen', 'Sonstiges'], form_h3='Termin anfragen', form_p='Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Leidenschaft <em>ist unser Antrieb.</em>', kt_p='Kommen Sie an die Loxtener Straße 1 in Ankum oder rufen Sie an.',
    rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Heini', 'Ihr Berling-Lotse', 'Auto Berling', [['Alle Marken?', 'Ja, Diagnose und Reparatur aller Automarken, auch Wohnmobile.'], ['Tanken?', 'Freie Tankstelle an der Loxtener Straße 1 und Bersenbrücker Straße 19.'], ['Öffnungszeiten', 'Mo–Fr 7–18 Uhr, Sa 8–13 Uhr.']], ['angebot', 'tanken', 'team', 'kontakt']),
    vars='--bg:#fff;--ink:#16161a;--mute:#5a5a62;--p:#d3122a;--a:#d3122a;--a-ink:#fff;--dk:#16161a;--s:#fff;--s2:#f4f2f2;--fh:"Barlow Condensed",system-ui,sans-serif;--fb:"Barlow",system-ui,sans-serif;--r:10px;--r2:14px;--br:999px;--mq-bg:#d3122a;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#16161a;--logo-h:40px;--ft-bg:#111114;--hp-bg:radial-gradient(120% 90% at 100% 0%,#fde9eb 0%,#fff 55%)',
    css='''.hp h1,.h2{font-weight:800;text-transform:uppercase;letter-spacing:0;line-height:.95}.hp h1{font-size:clamp(52px,6.2vw,100px)}.h2{font-size:clamp(42px,4.8vw,72px)}
.hp h1 em,.h2 em{font-style:italic;font-weight:700;color:var(--p)}.dk .h2 em{color:#ff5a6c}.alt{background:var(--s2)}
.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:46px}.fc .grid{grid-template-columns:repeat(5,1fr)}@media(max-width:900px){.fc .grid{grid-template-columns:repeat(2,1fr)}}''',
    img={'logo.png': ('berling/x/l1.jpg', 0, 'trimalpha'), 'h1.jpg': ('berling/img/i017.jpg', 0), 'h2.jpg': ('berling/img/i022.jpg', 0), 'h3.jpg': ('berling/img/i003.jpg', 0),
         'd-werk.jpg': ('berling/img/i005.jpg', 0), 'd-auto.jpg': ('berling/img/i035.jpg', 0), 'p-tanken.jpg': ('berling/img/i023.jpg', 0),
         't1.jpg': ('berling/img/i004.jpg', 0), 't2.jpg': ('berling/img/i006.jpg', 0), 't3.jpg': ('berling/img/i007.jpg', 0), 't4.jpg': ('berling/img/i008.jpg', 0), 't5.jpg': ('berling/img/i009.jpg', 0),
         't6.jpg': ('berling/img/i010.jpg', 0), 't7.jpg': ('berling/img/i011.jpg', 0), 't8.jpg': ('berling/img/i012.jpg', 0), 't9.jpg': ('berling/img/i013.jpg', 0), 't10.jpg': ('berling/img/i015.jpg', 0)},
    body=b_berling)

# ───────────────────────── 6. Autohaus Göke & Schendel, Bersenbrück ─────────────────────────
def b_goeke(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 50%',
        ey='Freie Meisterwerkstatt · Bersenbrück',
        h1='Ihre Werkstatt <em>für alle Marken.</em>',
        sub='Inspektion, HU mit AU, Reparatur und Unfallinstandsetzung mit moderner Diagnosetechnik und Original-Ersatzteilen namhafter Hersteller. Ehrlich, schnell und persönlich.',
        badge=('4,9 ★', '101 Google-Bewertungen')))
        + svc('leistungen', 'Leistungen', 'Alles, was <em>Ihr Auto braucht.</em>', 'Von der fachgerechten Reparatur bis zur ausführlichen Inspektion sind wir Ihr Ansprechpartner.', [
            ('Inspektion', 'Wartung nach Herstellervorgabe, damit Ihr Auto zuverlässig bleibt.'), ('HU mit AU', 'In Zusammenarbeit mit autorisierten Prüforganisationen.'),
            ('Motordiagnose', 'Moderne Werkstatt- und Diagnosegeräte finden den Fehler schnell.'), ('Bremsanlage', 'Beläge, Scheiben und Bremsflüssigkeit vom Profi.'),
            ('Klimaanlage', 'Service und Prüfung für frische Luft im Sommer.'), ('Rad &amp; Reifen', 'Reifenwechsel, Einlagerung und Achsvermessung.'),
            ('Unfallinstandsetzung', 'Wir bringen Ihr Auto nach einem Schaden wieder in Form.'), ('Glas, Auspuff, Batterie', 'Auch die kleinen Dinge erledigen wir zuverlässig.')])
        + story('werkstatt', 'Unsere Werkstatt', 'Regional, unabhängig <em>und professionell.</em>', [
            'An der Hermann-Kemper-Straße in Bersenbrück kümmern wir uns um Ihr Auto, egal welche Marke. Wir verwenden ausschließlich Original-Ersatzteile namhafter Markenhersteller.',
            'Unsere Kunden schätzen vor allem die ehrliche Beratung, die freundliche Atmosphäre und dass sie nicht lange warten müssen. Auch Klassiker sind bei uns willkommen.'],
            'werk.jpg', cap='Unsere Werkstatt in Bersenbrück', tl=[('Alle Marken', 'freie Werkstatt'), ('4,9', 'Sterne aus 101 Bewertungen')])
        + reviews(s, ['Ich bin Stammkunde und hatte nur gute Erfahrungen: von der Beratung bis zur pünktlichen, professionellen Arbeit lief immer alles reibungslos.',
                      'Ehrliches und seriöses Team, super Service, kompetente Beratung und keine langen Wartezeiten. Auch für Oldtimer.',
                      'Wie immer freundlich, schnell und professionell.', 'Top Werkstatt, hat meine Erwartungen voll erfüllt.'])
        + steps('So einfach geht es', 'In drei Schritten <em>zum Termin.</em>', [('Anrufen oder schreiben', 'Telefon 05439 92801, E-Mail oder WhatsApp.'), ('Auto bringen', 'Wir sagen Ihnen vorher, was gemacht wird.'), ('Weiterfahren', 'Sie holen Ihr Auto ab, ohne böse Überraschungen.')], 'alt')
        + contact(s, 'dk') + footer(s) + pop(dict(img='h2.jpg', ey='Werkstatt', h='HU fällig?', p='Wir übernehmen HU mit AU und den Check vorab.', btn='Termin anfragen')))

SITES['goeke'] = dict(
    slug='autohaus-goeke-schendel-bersenbrueck', firma='Autohaus Göke & Schendel', web='kfz-goeke.de', fonts='r13goe', logo_txt='Göke <span style="color:var(--p)">&amp;</span> Schendel',
    title='Autohaus Göke & Schendel – Kfz-Werkstatt in Bersenbrück', desc='Freie Kfz-Werkstatt in Bersenbrück: Inspektion, HU mit AU, Diagnose, Bremsen, Klima, Reifen und Unfallinstandsetzung für alle Marken.',
    tel='05439 92801', tel_i='+49543992801', mail='', adresse='Hermann-Kemper-Straße 1, 49593 Bersenbrück', google=('4,9', 101),
    cta='Werkstatttermin anfragen', nav=[('Leistungen', 'leistungen'), ('Werkstatt', 'werkstatt'), ('Bewertungen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 12:00'), ('', '13:00 – 17:00')],
    form_opts=['Inspektion', 'HU / AU', 'Reparatur', 'Reifen', 'Unfallschaden', 'Sonstiges'], form_h3='Werkstatttermin anfragen', form_p='Wir rufen zurück und nennen Ihnen einen Termin.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir sind <em>für Sie da.</em>', kt_p='Rufen Sie an, schreiben Sie per WhatsApp oder kommen Sie vorbei.',
    rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Jan', 'Ihr Werkstatt-Lotse', 'Göke &amp; Schendel', [['Alle Marken?', 'Ja, wir sind eine freie Werkstatt für alle Marken.'], ['HU?', 'HU mit integrierter AU in Zusammenarbeit mit autorisierten Prüforganisationen.'], ['Öffnungszeiten', 'Mo–Fr 8–12 und 13–17 Uhr.']], ['leistungen', 'werkstatt', 'kontakt']),
    vars='--bg:#f6f8fa;--ink:#122033;--mute:#55657a;--p:#2a63b8;--a:#2a63b8;--a-ink:#fff;--dk:#122033;--s:#fff;--s2:#e9eef4;--fh:"Rubik",system-ui,sans-serif;--fb:"Rubik",system-ui,sans-serif;--r:16px;--r2:24px;--br:14px;--mq-bg:#2a63b8;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.95);--hd-ink:#122033;--ft-bg:#0c1624;--hp-bg:linear-gradient(180deg,#eef3f9,#f6f8fa)',
    css='''.hp h1,.h2{font-weight:700;letter-spacing:-.025em;line-height:1.02}.hp h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#7fb0ff}
.alt{background:var(--s2)}.comp .badge b{font-size:26px}.sv .row div{border-radius:18px}''',
    img={'h1.jpg': ('goeke/img/i002.jpg', 0), 'h2.jpg': ('goeke/img/i001.jpg', 0), 'h3.jpg': ('goeke/img/i005.jpg', 0), 'werk.jpg': ('goeke/img/i003.jpg', 0)},
    body=b_goeke)

# ───────────────────────── 7. Kfz Reinhard Wilgen, Quakenbrück ─────────────────────────
def b_wilgen(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg'], big='KFZ',
        ey='Kfz-Meisterbetrieb · Quakenbrück · Eurorepar Car Service',
        h1='Gut und günstig <em>unterwegs.</em>',
        sub='Reparatur und Wartung aller Marken, HU-Vorabcheck mit Vorfahrt zur Prüfstelle und Peugeot Motocycles zur Probefahrt. Ihre unabhängige Werkstatt am Eilerskamp.',
        ubar=[('Alle Marken', 'unabhängige Meisterwerkstatt'), ('HU-Vorabcheck', 'auf Wunsch fahren wir vor'), ('Peugeot Motocycles', 'Roller zur Probefahrt')]))
        + svc('leistungen', 'Unsere Leistungen', 'Wir kümmern uns <em>um alles.</em>', 'Wir helfen Ihnen, größere Schäden zu vermeiden und Kosten zu sparen.', [
            ('Inspektion', 'Wartung für viele Modelle und Fabrikate.'), ('Bremsen', 'Prüfung und Reparatur der Bremsanlage.'), ('Zahnriemen', 'Wechsel inklusive Wasserpumpe zum festen Komplettpreis.'), ('Klimaanlage', 'Service für Ihre Klimaanlage.'),
            ('Ölwechsel', 'Mit Markenöl nach Herstellerspezifikation.'), ('Reifen', 'Wechsel und Reparatur.'), ('Auspuff &amp; Batterie', 'Schnell erledigt.'), ('Federung &amp; Mechanik', 'Fahrwerk und Mechanik vom Meister.')], 'dk')
        + promo('tuev', 'p-haus.jpg', 'TÜV / Dekra', 'Sicher durch <em>die HU.</em>', 'Die Hauptuntersuchung ist bei Neuwagen nach drei Jahren fällig, danach alle zwei Jahre, zusammen mit der AU. Mit unserem Vorabcheck sparen Sie Zeit und oft auch Geld. Auf Wunsch fahren wir Ihr Auto bei der Prüfstelle vor.', ['Voruntersuchung vor der HU', 'Vorfahrt bei der Prüfstelle', 'Termin oder einfach vorbeikommen'], 'HU-Vorabcheck anfragen')
        + vgrid('peugeot', 'Neu bei uns', 'Peugeot Motocycles <em>zur Probefahrt.</em>', 'Testen Sie Ihren Wunschroller vor dem Kauf. Wir begleiten Sie von der Auswahl bis zur Finanzierung.', [
            ('Peugeot Motocycles: Partnerfilm', 'mp4', 'peugeot.mp4', 'v-peugeot.jpg')], 'alt')
        + reviews(s, ['Abends eine Panne: Nach kurzem Anruf hat der Chef mich nach Feierabend abgeschleppt und sich am nächsten Werktag gekümmert.',
                      'Kompetente Werkstatt, in der ich mich wohl und sicher fühle. Auch bei dringenden Problemen wird schnell geholfen.',
                      'Reifenreparatur schnell und günstig erledigt. Der Ton ist direkt, aber herzlich.',
                      'Sehr gutes Preis-Leistungs-Verhältnis und eine breite Palette an Leistungen.'])
        + contact(s) + footer(s) + pop(dict(img='p-haus.jpg', ey='HU-Vorabcheck', h='Plakette fällig?', p='Wir checken vorab und fahren auf Wunsch vor.', btn='Termin anfragen')))

SITES['wilgen'] = dict(
    slug='kfz-wilgen-quakenbrueck', firma='Kfz-Reparatur Reinhard Wilgen', web='kfzwilgen.de', fonts='r13wil',
    title='Kfz Reinhard Wilgen – Meisterwerkstatt in Quakenbrück', desc='Unabhängige Kfz-Meisterwerkstatt in Quakenbrück: Reparatur und Wartung aller Marken, HU-Vorabcheck, Peugeot Motocycles.',
    tel='05431 8885', tel_i='+4954318885', mail='kfz-wilgen@outlook.de', adresse='Eilerskamp 9, 49610 Quakenbrück', google=('4,7', 59),
    cta='Termin vereinbaren', nav=[('Leistungen', 'leistungen'), ('TÜV', 'tuev'), ('Peugeot', 'peugeot'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 12:00'), ('', '13:00 – 17:30')],
    form_opts=['Inspektion', 'Reparatur', 'HU-Vorabcheck', 'Reifen', 'Roller-Probefahrt', 'Sonstiges'], form_h3='Termin vereinbaren', form_p='Wir melden uns schnell zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Mit uns fahren Sie <em>gut und günstig.</em>', kt_p='Rufen Sie an oder kommen Sie direkt am Eilerskamp 9 vorbei.',
    social=[('Facebook', 'https://www.facebook.com/KfzWilgen/')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Rudi', 'Ihr Werkstatt-Lotse', 'Kfz Wilgen', [['Alle Marken?', 'Ja, wir sind eine unabhängige Werkstatt für viele Modelle und Fabrikate.'], ['Roller testen?', 'Peugeot-Roller können Sie bei uns Probe fahren.'], ['Öffnungszeiten', 'Mo–Fr 8–12 und 13–17:30 Uhr.']], ['leistungen', 'tuev', 'peugeot', 'kontakt']),
    vars='--bg:#fff;--ink:#121212;--mute:#575757;--p:#e30613;--a:#e30613;--a-ink:#fff;--dk:#121212;--s:#fff;--s2:#f3f3f3;--fh:"Teko",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:2px;--r2:4px;--br:2px;--hero-ov:linear-gradient(100deg,rgba(10,10,10,.9) 0%,rgba(10,10,10,.6) 50%,rgba(10,10,10,.15) 100%);--mq-bg:#e30613;--mq-ink:#fff;--hd-bg:rgba(18,18,18,.95);--hd-ink:#fff;--logo-h:58px;--ft-bg:#0b0b0b',
    css='''.hs h1,.h2{font-weight:600;text-transform:uppercase;letter-spacing:.01em;line-height:1;padding-top:.08em}.ey{margin-bottom:10px}.hs h1{font-size:clamp(60px,7.6vw,128px)}.h2{font-size:clamp(46px,5.2vw,80px)}
.hs h1 em,.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff3b45}.hs .big{font-family:var(--fh);-webkit-text-stroke:2px rgba(227,6,19,.45)}
.hd .logo img{background:#fff;padding:4px 8px;border-radius:2px}.ft img{background:#fff;padding:6px 10px;height:64px}.alt{background:var(--s2)}
.vg .grid{grid-template-columns:1fr;max-width:980px}''',
    img={'logo.png': ('wilgen/img/i037.png', 0), 'h1.jpg': ('wilgen/img/i038.jpg', 0), 'p-haus.jpg': ('wilgen/img/i038.jpg', 1000, (.1, 0, .9, 1)),
         'peugeot.mp4': ('/home/claude/r13raw/vid/wilgen-720.mp4', 0), 'v-peugeot.jpg': ('/home/claude/r13raw/vid/wilgen-poster.jpg', 1280)},
    body=b_wilgen)

# ───────────────────────── 8. Autohaus F. J. Fehrmann, Gehrde ─────────────────────────
def b_fehrmann(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 65%', 'h2.jpg': '50% 60%'},
        ey='Autohaus Fehrmann · Gehrde im Artland',
        h1='Ihr Wunschauto. <em>Ohne Anzahlung.</em>',
        sub='Mitsubishi- und Citroën-Vertragshändler, freie Kfz-Werkstatt für alle Marken und Gebrauchtwagenprofis. Mit dem Plus-Kauf-System fahren Sie entspannt los.',
        ubar=[('Mitsubishi &amp; Citroën', 'Vertragshändler'), ('Alle Marken', 'Meisterwerkstatt'), ('4,7 Sterne', 'aus 218 Google-Bewertungen')]))
        + promo('pluskauf', 'p-plus.jpg', 'Das Fehrmann Plus-Kauf-System', 'Damit Ihre anderen Wünsche <em>nicht zu kurz kommen.</em>', 'Keine Anzahlung, bequeme Raten über unsere Hausbank und eine Laufzeit, die Sie bestimmen. Ihren Gebrauchten nehmen wir in Zahlung, auf Wunsch mit sofortiger Barauszahlung.', ['7-Tage-Umtauschgarantie und Rückkaufgarantie', 'Fahrzeuggarantie', '3 Jahre Service zum Festpreis'], 'Plus-Kauf anfragen')
        + duo('marken', 'Neuwagen', 'Mitsubishi <em>und Citroën.</em>', 'Als Vertragshändler beraten wir Sie persönlich, und über EU-Fahrzeuge ist von A wie Alfa bis V wie VW alles machbar.', [
            ('Vertragshändler', 'Mitsubishi', 'd-mit.jpg', 'Neuwagen, Probefahrt und Service vom Vertragshändler im Artland.', ['Neuwagen', 'Service'], 'Mitsubishi anfragen'),
            ('Vertragshändler', 'Citroën', 'd-cit.jpg', 'Aktuelle Citroën-Modelle, Beratung und Werkstatt aus einer Hand.', ['Neuwagen', 'Service'], 'Citroën anfragen')], 'alt')
        + story('werkstatt', '1a Autoservice', 'Werkstatt <em>für alle Marken.</em>', [
            'Audi, Opel, Ford, VW, Peugeot, Toyota oder Mercedes: Als auf Mehrmarkenservice spezialisierte Werkstatt bieten wir Ihnen schnellen, persönlichen und zuverlässigen Kfz-Meisterservice.',
            'Ersatzteile in Top-Qualität besorgen wir für nahezu jedes Fahrzeug. Und wer uns einen neuen Kunden empfiehlt, bekommt 100 Euro.'],
            'werk.jpg', cap='Unser Betrieb am Mühlenweg 4 in Gehrde', tl=[('Werkstatt', 'Mo–Fr 8:00–16:45'), ('Verkauf', 'Mo–Fr 8:00–18:30')], rev=True)
        + gallery('gelaende', 'Von oben', 'Unser Gelände <em>in Gehrde.</em>', [('a1.jpg', '', '50% 50%'), ('a2.jpg', '', '50% 50%'), ('a3.jpg', '', '50% 50%'), ('a4.jpg', '', '50% 50%')])
        + reviews(s, ['Samstagmorgen ein Kraftstoffproblem, gut gelaunt und erstklassig gelöst, mit ständiger Info zum Stand der Arbeit.',
                      'Super freundlicher und schneller Mechaniker. Zwei Stunden nach der Panne ging es weiter.',
                      'Tolles Team, super Service.', 'Sehr freundliches Personal, sehr zufrieden.'])
        + contact(s, 'dk') + footer(s) + pop(dict(img='p-plus.jpg', ey='Kunden werben Kunden', h='100 € für Ihre Empfehlung', p='Wenn Sie uns einen neuen Fahrzeugkunden vermitteln.', btn='Mehr erfahren')))

SITES['fehrmann'] = dict(
    slug='autohaus-fehrmann-gehrde', firma='Autohaus F. J. Fehrmann GmbH', web='autohaus-fehrmann.de', fonts='r13feh',
    title='Autohaus Fehrmann – Mitsubishi, Citroën und Werkstatt in Gehrde', desc='Mitsubishi- und Citroën-Vertragshändler, freie Kfz-Werkstatt und Gebrauchtwagen mit Plus-Kauf-System in Gehrde.',
    tel='05439 93023', tel_i='+49543993023', mail='info@autohaus-fehrmann.de', adresse='Mühlenweg 4, 49596 Gehrde', google=('4,7', 218),
    cta='Termin anfragen', nav=[('Plus-Kauf', 'pluskauf'), ('Marken', 'marken'), ('Werkstatt', 'werkstatt'), ('Kontakt', 'kontakt')],
    hours=[('Verkauf Mo – Fr', '08:00 – 18:30'), ('Werkstatt Mo – Fr', '08:00 – 16:45'), ('Sa', '08:00 – 12:00')],
    form_opts=['Servicetermin', 'Plus-Kauf', 'Mitsubishi', 'Citroën', 'Gebrauchtwagen', 'Ersatzteile'], form_h3='Termin anfragen', form_p='Ein Mitarbeiter meldet sich und vereinbart einen Termin.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Im schönen Artland, <em>direkt in Gehrde.</em>', kt_p='Wir freuen uns auf Ihre Anfrage.',
    social=[('Facebook', 'https://www.facebook.com/autohaus.fehrmann/')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Franzi', 'Ihre Autohaus-Lotsin', 'Autohaus Fehrmann', [['Plus-Kauf?', 'Keine Anzahlung, Raten über die Hausbank, Laufzeit nach Wahl, 7-Tage-Umtauschgarantie.'], ['Alle Marken?', 'Ja, unsere Werkstatt betreut alle Marken.'], ['Öffnungszeiten', 'Verkauf Mo–Fr 8–18:30, Werkstatt Mo–Fr 8–16:45 Uhr.']], ['pluskauf', 'marken', 'werkstatt', 'kontakt']),
    vars='--bg:#fff;--ink:#17181c;--mute:#5a5c64;--p:#c8102e;--a:#c8102e;--a-ink:#fff;--dk:#17181c;--s:#fff;--s2:#f4f4f6;--fh:"Red Hat Display",system-ui,sans-serif;--fb:"Red Hat Text",system-ui,sans-serif;--r:12px;--r2:20px;--br:12px;--hero-ov:linear-gradient(90deg,rgba(15,15,18,.86) 0%,rgba(15,15,18,.5) 55%,rgba(15,15,18,.1) 100%);--mq-bg:#c8102e;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#17181c;--logo-h:44px;--ft-bg:#111215',
    css='''.hs h1,.h2{font-weight:900;letter-spacing:-.03em;line-height:1}.hs h1{font-size:clamp(44px,5.6vw,90px)}.hs h1 em{font-style:normal;color:#ff4d63}.h2 em{font-style:normal;color:var(--p)}.dk .h2 em{color:#ff4d63}

.hd.lt:not(.scr) .logo img{filter:brightness(0) invert(1)}.hs .ey{color:#ff8a98!important}.alt{background:var(--s2)}.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:50px}.gl .grid{grid-template-columns:repeat(4,1fr)}@media(max-width:800px){.gl .grid{grid-template-columns:1fr 1fr}}''',
    img={'logo.png': ('fehrmann/img/i004.png', 0, 'alphacrop'), 'h1.jpg': ('fehrmann/img/i001.jpg', 0), 'h2.jpg': ('fehrmann/img/i018.jpg', 0), 'p-plus.jpg': ('fehrmann/img/i018.jpg', 0),
         'd-mit.jpg': ('fehrmann/img/i029.jpg', 0), 'd-cit.jpg': ('fehrmann/img/i030.jpg', 0), 'werk.jpg': ('fehrmann/img/i001.jpg', 1100),
         'a1.jpg': ('fehrmann/img/i006.jpg', 0), 'a2.jpg': ('fehrmann/img/i007.jpg', 0), 'a3.jpg': ('fehrmann/img/i008.jpg', 0), 'a4.jpg': ('fehrmann/img/i010.jpg', 0)},
    body=b_fehrmann)

# ───────────────────────── 9. Auto Welp, Nortrup ─────────────────────────
def b_welp(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg'], pos0='50% 60%',
        ey='Kfz-Meisterbetrieb · Nortrup · seit 1995',
        h1='Kaufen, fahren, <em>warten lassen.</em>',
        sub='Neu-, Jahres- und Gebrauchtwagen auf unserem Firmengelände und eine freie Kfz-Meisterwerkstatt für alle Servicearbeiten. Mitten in Nortrup.',
        badge=('1995', 'im Herzen von Nortrup')))
        + svc('leistungen', 'Unsere Leistungen', 'Alles für Ihr Auto <em>an einem Ort.</em>', 'In unserer Kfz-Meisterwerkstatt.', [
            ('Inspektion &amp; Wartung', 'Alle Servicearbeiten an Ihrem Fahrzeug.'), ('Reifen &amp; Räder', 'Wechsel und Service rund ums Rad.'), ('Reparaturen', 'Instandsetzung vom Meisterbetrieb.'), ('Diagnose', 'Mit modernsten Geräten.'),
            ('Abgasuntersuchung', 'AU direkt bei uns.'), ('Hauptuntersuchung', 'In Zusammenarbeit mit dem TÜV Nord.'), ('Fahrzeughandel', 'Neu-, Jahres- und Gebrauchtwagen.'), ('An- und Verkauf', 'Wir kaufen auch Ihr Auto.')])
        + promo('hu', 'h1.jpg', 'TÜV NORD Online-Termin', 'HU-Termin <em>bequem online.</em>', 'Unsere freie Werkstatt arbeitet für Hauptuntersuchungen mit dem TÜV Nord zusammen. Ihren Termin reservieren Sie ganz bequem online, die HU findet direkt bei uns statt.', ['HU direkt in Nortrup', 'Termin online reservieren'], 'HU-Termin anfragen', 'dk')
        + reviews(s, ['Spitzenwerkstatt mit Herz und Sachverstand: zuverlässig, schnell und absolut fair. Hier wird kreativ repariert statt teuer getauscht.',
                      'Jahrelang hier gewartet. Kompetente Beratung, sehr schneller Service, und mehrmals aus der Klemme geholfen.',
                      'Top Werkstatt, top Kommunikation. Immer zufrieden.', 'Perfekt!'])
        + contact(s) + footer(s) + pop(dict(img='h1.jpg', ey='TÜV Nord', h='HU fällig?', p='Termin direkt bei uns in Nortrup.', btn='Termin anfragen')))

SITES['welp'] = dict(
    slug='auto-welp-nortrup', firma='Auto Welp, Inh. Waldemar Rupp', web='auto-welp.de', fonts='r13welp',
    title='Auto Welp – Kfz-Meisterbetrieb in Nortrup', desc='Kfz-Meisterwerkstatt und Fahrzeughandel in Nortrup seit 1995: Inspektion, Reifen, Reparatur, AU und HU mit dem TÜV Nord.',
    tel='05436 8555', tel_i='+4954368555', mail='info@auto-welp.de', adresse='Voßhöchteweg 6, 49638 Nortrup', google=('4,9', 71),
    cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), ('HU', 'hu'), ('Bewertungen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 17:00')],
    form_opts=['Inspektion', 'Reparatur', 'Reifen', 'HU / AU', 'Fahrzeugkauf', 'Auto verkaufen'], form_h3='Termin anfragen', form_p='Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kommen Sie <em>nach Nortrup.</em>', kt_p='Voßhöchteweg 6, mitten im Ort.',
    rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=BOT('Willi', 'Ihr Werkstatt-Lotse', 'Auto Welp', [['HU?', 'Ja, in Zusammenarbeit mit dem TÜV Nord direkt bei uns.'], ['Gebrauchtwagen?', 'Neu-, Jahres- und Gebrauchtwagen auf unserem Gelände.'], ['Öffnungszeiten', 'Mo–Fr 8–17 Uhr.']], ['leistungen', 'hu', 'kontakt']),
    vars='--bg:#fffdf2;--ink:#0d1f5c;--mute:#46507a;--p:#1438a6;--a:#ffe100;--a-ink:#0d1f5c;--dk:#0d1f5c;--s:#fff;--s2:#fff6c2;--fh:"Oswald",system-ui,sans-serif;--fb:"Lato",system-ui,sans-serif;--r:8px;--r2:12px;--br:8px;--mq-bg:#ffe100;--mq-ink:#0d1f5c;--hd-bg:rgba(255,253,242,.96);--hd-ink:#0d1f5c;--logo-h:52px;--ft-bg:#0a1747;--hp-bg:linear-gradient(160deg,#fff7b8 0%,#fffdf2 55%)',
    css='''.hp h1,.h2{font-weight:700;text-transform:uppercase;letter-spacing:.005em;line-height:1}.hp h1{font-size:clamp(46px,5.6vw,88px)}.hp h1 em,.h2 em{font-style:normal;color:var(--p);box-shadow:inset 0 -.28em 0 #ffe100}
.dk .h2 em{color:#ffe100;box-shadow:none}.hp h1{line-height:1.1;padding-top:6px}.hp .ey{margin-bottom:14px}.comp{height:clamp(300px,29vw,400px)}.comp .c1{inset:0}.ft img{height:56px;border-radius:6px}.hp .chip b{background:var(--p)}''',
    img={'logo.png': ('welp/img/i001.gif', 0), 'h1.jpg': ('welp/img/i008.jpg', 0)},
    body=b_welp)

# ───────────────────────── 10. Autohaus Menslage (Opel), Fürstenau ─────────────────────────
def b_opel(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], pos0='50% 50%', badge=('90+', 'Jahre Opel im Altkreis Bersenbrück'),
        ey='Autohaus Opel Menslage · Fürstenau',
        h1='Seit über 90 Jahren <em>Opel im Altkreis.</em>',
        sub='Neuwagen, Service und Teile vom Opel-Partner am Robert-Bosch-Ring. Ehrlich, fachlich und persönlich beraten, mit zehn Arbeitsplätzen in der Werkstatt.'))
        + marquee(['Neuwagen', 'Inspektion', 'Reparatur', 'HU &amp; AU', 'Hol- und Bringservice', 'Teile &amp; Zubehör', 'Fahrzeugbewertung'])
        + scroller('modelle', 'Aktuelle Modelle', 'Die neue <em>Opel-Generation.</em>', 'Corsa, Mokka, Frontera, Grandland, Combo und Rocks-e: Probefahrt und Beratung bei uns in Fürstenau. Bilder: Opel.', [
            ('Kleinwagen', 'm1.jpg', 'Wendig in der Stadt, als Verbrenner oder elektrisch.', '50% 60%'), ('Crossover', 'm2.jpg', 'Kompakt außen, hoch sitzen innen.', '50% 60%'), ('SUV', 'm3.jpg', 'Viel Platz für die Familie.', '50% 60%'),
            ('Elektrisch', 'm4.jpg', 'Viele Modelle auch mit E-Antrieb.', '50% 60%'), ('Kompaktklasse', 'm5.jpg', 'Sportlich und effizient.', '50% 60%')], 'dk')
        + svc('service', 'Unsere Dienstleistungen', 'Service, <em>der bleibt.</em>', 'Der Ausbildungsstand unserer Mitarbeiter wird von Opel laufend durch verdeckte Werkstatttests geprüft.', [
            ('Inspektionen', 'Optimiertes Inspektionssystem für Wert und Zuverlässigkeit.'), ('Reparaturen', 'Rundum-Service vom Abschleppdienst bis zur Anlieferung.'),
            ('HU und AU', 'Wagen am Vortag bringen, Untersuchung bei uns. Auf Wunsch holen und bringen wir.'), ('Zubehör', 'Von der Schneekette bis zum Kindersitz.'),
            ('Fahrzeugbewertung', 'Damit Sie beim Verkauf den besten Preis erzielen.'), ('Kühlsystem-Check', 'Mit Garantie-Zertifikat.'),
            ('Teile', 'Original-Teile und Zubehör im Haus.'), ('Ausbildung', 'Qualifizierte Ausbildungsplätze zum Kfz-Mechatroniker.')])
        + story('ueber-uns', 'Tradition verpflichtet', 'Ihre Zufriedenheit ist <em>unsere Motivation.</em>', [
            'Seit über 90 Jahren vertritt das Autohaus Menslage die Marke Opel im Altkreis Bersenbrück und darüber hinaus.',
            'Erstklassiger Service zu fairen Preisen und eine ehrliche, fachliche und persönliche Beratung sind uns das Wichtigste. Darum bilden wir alle Mitarbeiter konsequent weiter.'],
            'haus.jpg', cap='Autohaus Menslage am Robert-Bosch-Ring 2', tl=[('90+', 'Jahre Opel-Partner'), ('10', 'Werkstatt-Arbeitsplätze')], cls='alt')
        + contact(s) + footer(s) + pop(dict(img='m2.jpg', ey='Probefahrt', h='Den neuen Opel erleben', p='Vereinbaren Sie Ihre Probefahrt in Fürstenau.', btn='Probefahrt anfragen')))

SITES['opelmenslage'] = dict(
    slug='autohaus-opel-menslage-fuerstenau', firma='Autohaus Menslage GmbH', web='opel-menslage.de', fonts='r13opel',
    title='Autohaus Opel Menslage – Opel-Partner in Fürstenau', desc='Opel-Partner in Fürstenau seit über 90 Jahren: Neuwagen, Inspektion, Reparatur, HU/AU, Teile und Zubehör.',
    tel='05901 4306', tel_i='+4959014306', mail='info@opel-menslage.de', adresse='Robert-Bosch-Ring 2, 49584 Fürstenau', google=None,
    cta='Probefahrt anfragen', nav=[('Modelle', 'modelle'), ('Service', 'service'), ('Über uns', 'ueber-uns'), ('Kontakt', 'kontakt')],
    hours=[('Verkauf Mo – Fr', '08:00 – 18:00'), ('Verkauf Sa', '08:00 – 12:00'), ('Service Mo – Fr', '08:00 – 12:00, 13:00 – 16:30')],
    form_opts=['Probefahrt', 'Neuwagen', 'Servicetermin', 'HU / AU', 'Teile &amp; Zubehör', 'Fahrzeugbewertung'], form_h3='Anfrage senden', form_p='Wir melden uns zeitnah bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Am Robert-Bosch-Ring 2 in Fürstenau.',
    bot=BOT('Ella', 'Ihre Opel-Lotsin', 'Autohaus Menslage', [['Probefahrt?', 'Gern, rufen Sie an: 05901 4306.'], ['HU?', 'Wagen am Vortag bringen, Untersuchung im Haus. Hol- und Bringservice auf Wunsch.'], ['Öffnungszeiten', 'Verkauf Mo–Fr 8–18, Sa 8–12 Uhr. Service Mo–Fr 8–12 und 13–16:30 Uhr.']], ['modelle', 'service', 'kontakt']),
    vars='--bg:#fff;--ink:#111;--mute:#585858;--p:#111;--a:#f7ff14;--a-ink:#111;--dk:#111;--s:#fff;--s2:#f5f5f0;--fh:"Outfit",system-ui,sans-serif;--fb:"Inter",system-ui,sans-serif;--r:0px;--r2:0px;--br:0px;--hero-ov:linear-gradient(90deg,rgba(10,10,10,.9) 0%,rgba(10,10,10,.55) 55%,rgba(10,10,10,.1) 100%);--mq-bg:#f7ff14;--mq-ink:#111;--hd-bg:rgba(255,255,255,.96);--hd-ink:#111;--logo-h:34px;--ft-bg:#0a0a0a;--hp-bg:linear-gradient(120deg,#fff 0%,#fff 52%,#fbffc4 52%,#f7ff14 100%)',
    css='''.hp h1,.h2{font-weight:800;letter-spacing:-.035em;line-height:.98}.hp h1{font-size:clamp(44px,5.4vw,86px)}.dk .h2 em{font-style:normal;color:#f7ff14}.hp h1 em,.h2 em{font-style:normal;background:#f7ff14;padding:0 .12em}.hp::before{display:none}.comp .badge b{color:#111;background:#f7ff14;display:inline-block;padding:2px 8px}
.dk .h2 em{background:none;padding:0}.alt{background:var(--s2)}
.hd .logo img{border:1px solid #ddd;padding:6px 10px}.ft img{background:#fff;padding:8px 12px;height:44px}#ueber-uns figure img{aspect-ratio:1000/600;height:auto}''',
    img={'logo.png': ('opelmenslage/img/i046.jpg', 0), 'h1.jpg': ('opelmenslage/img/i044.jpg', 0, (.5, 0, 1, 1)), 'h2.jpg': ('opelmenslage/img/i044.jpg', 0, (0, 0, .5, 1)), 'haus.jpg': ('opelmenslage/img/i044.jpg', 0, (0, 0, .5, 1)),
         'm1.jpg': ('opelmenslage/img/i038.jpg', 0), 'm2.jpg': ('opelmenslage/img/i037.jpg', 0), 'm3.jpg': ('opelmenslage/img/i033.jpg', 0), 'm4.jpg': ('opelmenslage/img/i034.jpg', 0), 'm5.jpg': ('opelmenslage/img/i041.jpg', 0)},
    body=b_opel)
