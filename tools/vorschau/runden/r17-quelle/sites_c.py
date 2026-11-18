"""Runde 17 · Teil C: Wenzky-Küchen, Sandra Büssemaker, Küchen Plaza."""
from common import *
from sites_a import V
from sites_b import DKHD
SITES = {}

# ───────────── 10. Wenzky-Küchen, Rheine ─────────────
def b_wenzky(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['a1.jpg', 'a2.jpg'], big='1970',
        ubar=[('Seit 1970', 'gegründet von Hans Wenzky'), ('Ausstellung', 'mehrere Hersteller zur Wahl'), ('Kochevents', 'Küche live erleben')],
        ey='Wenzky-Küchen · Rheine · seit 1970',
        h1='Küchen <em>zum Anfassen.</em>',
        sub='Seit über 45 Jahren steht das Team von Küchen Wenzky für hohe Qualität, Flexibilität und Kundennähe. Ob neues Küchengerät, kleine Einbauküche oder großer Koch-Event-Raum.'))
        + story('team', 'Unser Team', 'Freundlich, kompetent, <em>effizient.</em>', [
            'Gute und freundliche Mitarbeiter sind das Herz eines jeden Unternehmens. Deshalb legen wir bei unseren Kundenbetreuern Wert auf soziale Kompetenz und fachliche Ausbildung.',
            'Geführt wird das Unternehmen heute von Luise Kenning. Sie hat ihre Karriere vor 30 Jahren bei Wenzky begonnen und sich in jedes Detail der Firma eingearbeitet.'], 'team.jpg', 'Blick in unsere Ausstellung am Bauhof', cls='hb')
        + svc('welten', 'Küchenwelten', 'Ihre passende Küche <em>finden Sie bei Wenzky.</em>', 'Funktionalität, Design, Auslastung des Raums: Unsere Küchenprofis stehen Ihnen mit Rat und Tat zur Seite.', [
            ('Ausstellung', 'In unserem großen Ausstellungsraum können Sie nach Herzenslust schauen und Farben und Formen aussuchen.'),
            ('Hersteller', 'Sie wählen unter verschiedenen Herstellern für Küchen, Elektrogeräte und Zubehör.'),
            ('Referenzen', 'Wohnlich, puristisch oder elegant: Sie entscheiden, wie Ihre Traumküche aussieht.'),
            ('Aktionen', 'Küchen, Geräte und Zubehör zu besten Preisen.')], 'alt')
        + gallery('ausstellung', 'Impressionen', 'Ein Blick in <em>unsere Ausstellung.</em>', [
            ('a1.jpg', 'a', '50% 50%'), ('a2.jpg', 'b', '50% 50%'), ('a3.jpg', 'c', '50% 50%')])
        + promo('events', 'event.jpg', 'Kochevents', 'Erleben Sie, was moderne <em>Küchen heute können.</em>',
                'Bei unseren Kochevents zeigen wir interessierten Kunden, welche Möglichkeiten moderne Küchen bieten, zum Beispiel das Dampfgaren: die sanfteste Art, Gemüse, Fisch oder Fleisch zuzubereiten.',
                ['Geräte live ausprobieren', 'Fragen direkt an die Küchenprofis'], 'Termin für ein Kochevent anfragen', 'alt')
        + reviews_ns(s, ['Die Beratung war hochprofessionell. Unsere Ideen wurden perfekt umgesetzt und um viele gute Vorschläge ergänzt. Alle Termine wurden eingehalten.',
                         'Die Beratung durch Herrn Kenning war fachlich hervorragend, ehrlich und ohne Druck. Lieferzeiten wurden eingehalten, die Montage lief reibungslos.',
                         'Die Küche steht jetzt seit zwei Jahren, und wir würden es genauso wieder machen.',
                         'Frau und Herr Kenning haben mir sehr schnell geholfen, nachdem mich ein anderes Küchenstudio im Stich gelassen hatte.'])
        + contact(s) + footer(s))

S = SITES['wenzky'] = site(
    slug='wenzky-kuechen-rheine', firma='Wenzky-Küchen GmbH', web='wenzky-kuechen.de', fonts='r16meppens',
    title='Wenzky-Küchen Rheine – Küchen zum Anfassen seit 1970', desc='Wenzky-Küchen in Rheine: große Küchenausstellung, mehrere Hersteller, Kochevents. Qualität und Kundennähe seit 1970.',
    tel='05971 2682', tel_i='+4959712682', mail='info@wenzky-kuechen.de', adresse='Am Bauhof 27, 48431 Rheine',
    cta='Beratungstermin anfragen', nav=[('Team', 'team'), ('Küchenwelten', 'welten'), ('Ausstellung', 'ausstellung'), ('Kochevents', 'events'), ('Kontakt', 'kontakt')],
    hours=[('Mo', 'geschlossen'), ('Di – Fr', '9:00 – 12:30, 14:30 – 18:00'), ('Sa', '9:00 – 12:30')],
    form_opts=['Neue Küche', 'Küchengerät', 'Kochevent', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kontaktieren <em>Sie uns.</em>', kt_p='Besuchen Sie unsere Ausstellung am Bauhof in Rheine oder rufen Sie uns an.',
    social=[('Facebook', 'https://www.facebook.com/wenzky.kuechen/')],
    vars=V.format(ink='#1a1a1a', mute='#555', p='#E3001B', pi='#fff', dk='#1a1a1a', s2='#f4f4f4', fh='"Open Sans",system-ui,sans-serif', fb='"Open Sans",system-ui,sans-serif', lh=64, ft='#111'),
    css='''.hs h1,.h2{font-weight:800;letter-spacing:-.025em;line-height:1.04}.hs h1{font-size:clamp(44px,7vw,108px)}.hs h1 em,.h2 em{font-style:normal;color:#E3001B}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #E3001B}
.st.hb figure img{aspect-ratio:1920/600;object-fit:cover;height:auto}.st.hb .w{grid-template-columns:1fr;gap:28px}.gl .grid{grid-template-columns:repeat(3,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:3/2}
.ft img{height:70px}@media(max-width:820px){.gl .grid{grid-template-columns:1fr}}''')
S['css2'] = '.hz{--hz-bg:#1a1a1a;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(227,0,27,.3);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:800}.hz h1 em{color:#ff3b4e}.hz .ey{color:#ff3b4e}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['bot'] = BOT('Wanda', 'Ihre Küchen-Lotsin', 'Wenzky-Küchen', S, [
    ['Öffnungszeiten', 'Di–Fr 9:00–12:30 und 14:30–18:00 Uhr, Sa 9:00–12:30 Uhr. Montags geschlossen.'],
    ['Gibt es Kochevents?', 'Ja, bei unseren Kochevents zeigen wir, was moderne Küchen können. Fragen Sie nach dem nächsten Termin.'],
    ['Welche Hersteller haben Sie?', 'Sie können bei uns unter verschiedenen Herstellern für Küchen, Geräte und Zubehör wählen.']],
    ['#team', '#welten', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r17raw/wenzky/logo.jpg', 0), 'h1.jpg': ('wenzky/img/i025.jpg', 0), 'h2.jpg': ('wenzky/img/i031.jpg', 0), 'h3.jpg': ('wenzky/img/i039.jpg', 0),
    'team.jpg': ('wenzky/img/i038.jpg', 0), 'a1.jpg': ('wenzky/img/i035.jpg', 0), 'a2.jpg': ('wenzky/img/i036.jpg', 0), 'a3.jpg': ('wenzky/img/i070.jpg', 0), 'event.jpg': ('wenzky/img/i062.jpg', 0)}
S['body'] = b_wenzky

# ───────────── 11. Sandra Büssemaker, Osnabrück ─────────────
def b_buessemaker(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], side='l',
        ubar=[('Bei Ihnen zu Hause', 'persönliche Beratung'), ('Unabhängig', 'breite Auswahl an Anbietern'), ('Ein Ansprechpartner', 'von Planung bis Montage')],
        ey='Sandra Büssemaker · Individuelle Küchenlösungen · Osnabrück',
        h1='Die Küche, die zu <em>Ihrem Leben passt.</em>',
        sub='Für die meisten ist die Küche ein Raum zum Wohlfühlen, ein Ort zum Kochen, Essen, Lachen, Leben. Damit das gelingt, plane ich Ihre Küche ganz persönlich, bei Ihnen zu Hause.'))
        + marquee(['Lingen', 'Hopsten', 'Beesten', 'Wallenhorst', 'Lübbecke', 'Osnabrück', 'Bielefeld', 'Bissendorf'], 'bm')
        + gallery('referenzen', 'Referenzen', 'Vorher, nachher: <em>echte Küchen meiner Kunden.</em>', [
            ('r1.jpg', 'a', '50% 50%'), ('r2.jpg', 'b', '50% 50%'), ('r3.jpg', 'c', '50% 50%'), ('r4.jpg', 'd', '50% 50%'), ('r5.jpg', 'e', '50% 50%'), ('r6.jpg', 'f', '50% 50%')])
        + ablauf('weg', 'So arbeite ich', 'Persönlich, offen, <em>unabhängig.</em>', 'Warum brauchen Sie mich und kein Küchenstudio? Weil ich Ihre Wohnumgebung, Ihre Abläufe und Ihre Vorlieben in die Planung einbeziehe.', [
            ('Beratung zu Hause', 'Wir klären offen, was räumlich und finanziell machbar ist und was nicht.'),
            ('Material und Technik', 'Dutzende Oberflächen, hunderte Farben: Ich helfe Ihnen, die passende Wahl zu treffen.'),
            ('Ausstellungen der Partner', 'Auf Wunsch sehen wir uns Materialien und Geräte gemeinsam im Original an.'),
            ('Montage', 'Sauber, organisiert, zügig: Ich koordiniere Fachbetriebe aus Osnabrück und Umgebung, die ich seit vielen Jahren kenne.')], 'alt')
        + reviews(s, ['Frau Büssemaker hat uns von der ersten Planung bis zur Montage mit größtem Einsatz begleitet. Alles Besprochene wurde umgesetzt.',
                      'Wer schon einmal Probleme bei Planung oder Betreuung einer neuen Küche hatte, ist bei Frau Büssemaker in guten Händen.',
                      'Sehr zufrieden mit der persönlichen, fachkundigen Beratung vor Ort, der Umsetzung und dem Ergebnis.',
                      'Ein Traum aus Exklusivität, Funktionalität und Individualität. Hochprofessionell umgesetzt.'])
        + contact(s) + footer(s))

S = SITES['buessemaker'] = site(
    slug='buessemaker-kuechen-osnabrueck', firma='Sandra Büssemaker e.K.', web='büssemaker-küchen.de', fonts='r10vagts',
    title='Sandra Büssemaker – individuelle Küchenlösungen in Osnabrück', desc='Sandra Büssemaker plant Küchen persönlich und unabhängig, bei Ihnen zu Hause in Osnabrück und Umgebung. Mit Vorher-nachher-Referenzen.',
    tel='0541 201930-20', tel_i='+4954120193020', adresse='Wittkopstraße 13, 49088 Osnabrück', google=('5,0', 7),
    cta='Beratung zu Hause anfragen', nav=[('Referenzen', 'referenzen'), ('So arbeite ich', 'weg'), ('Kundenstimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung'), ('Mobil', '0170 809 7458')],
    form_opts=['Neue Küche', 'Küche umgestalten', 'Beratung zu Hause', 'Sonstiges'],
    form_h3='Beratung zu Hause anfragen', form_p='Ich komme zu Ihnen. Nennen Sie mir kurz Ihr Vorhaben, ich rufe Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr direkter Draht <em>zur Traumküche.</em>', kt_p='Sie haben eine breite Auswahl an Anbietern, aber nur eine Ansprechpartnerin: mich.',
    rv_h2='Das sagen <em>meine Kunden.</em>',
    vars=V.format(ink='#33322a', mute='#656454', p='#656454', pi='#fff', dk='#4a4940', s2='#F2F1E5', fh='"Lato",system-ui,sans-serif', fb='"Source Sans 3",system-ui,sans-serif', lh=64, ft='#33322a') + DKHD.format(c='#4a4940'),
    css='''.h2{font-weight:300;letter-spacing:-.01em;line-height:1.1;font-size:clamp(32px,4.2vw,60px)}.h2 em{font-style:normal;font-weight:900;color:#656454}.alt{background:var(--s2)}.mq.bm span{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:15px}
.gl .grid{grid-template-columns:repeat(3,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:1200/782}.rd .road div::before{background:#918F77}.hd .nav a{color:#fff}.ft img{height:70px}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr 1fr}}''')
S['css2'] = '.hz{--hz-bg:#F2F1E5;--hz-ink:#33322a;--hz-mute:#656454;--hz-cols:46fr 54fr}.hz h1{font-weight:300;font-size:clamp(38px,4.5vw,72px)}.hz h1 em{font-weight:900;color:#656454}.hz .ey{color:#918F77}'
S['bot'] = BOT('Bea', 'Ihre Küchen-Lotsin', 'Sandra Büssemaker', S, [
    ['Wo findet die Beratung statt?', 'Ganz persönlich bei Ihnen zu Hause, in Osnabrück und weit darüber hinaus.'],
    ['Wer montiert die Küche?', 'Qualifizierte Fachbetriebe aus Osnabrück und Umgebung. Organisation und Koordination übernehme ich.'],
    ['Kann ich Material vorher ansehen?', 'Ja, auf Wunsch fahren wir gemeinsam in die Ausstellungen meiner Lieferanten.']],
    ['#referenzen', '#weg', '#stimmen', '#kontakt'])
S['img'] = {'logo.png': ('/home/claude/r17raw/buessemaker/logo.png', 600), 'h1.jpg': ('buessemaker/img/i044.jpg', 0), 'h2.jpg': ('buessemaker/img/i032.jpg', 0), 'h3.jpg': ('buessemaker/img/i050.jpg', 0),
    'r1.jpg': ('buessemaker/img/i033.jpg', 0), 'r2.jpg': ('buessemaker/img/i036.jpg', 0), 'r3.jpg': ('buessemaker/img/i040.jpg', 0), 'r4.jpg': ('buessemaker/img/i042.jpg', 0), 'r5.jpg': ('buessemaker/img/i045.jpg', 0), 'r6.jpg': ('buessemaker/img/i054.jpg', 0)}
S['body'] = b_buessemaker

# ───────────── 12. Küchen Plaza, Rheine ─────────────
def b_plaza(s):
    return (hd(s, False) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'],
        ey='Küchen Plaza · Rheine',
        h1='Träume <em>werden wahr.</em>',
        sub='Eine Küche ist nicht einfach eine Küche: Küche ist Lebensraum. Wir zeigen Ihnen Küchen mit Persönlichkeit, ganz auf Ihre Wünsche zusammengestellt. Maßarbeit und Handwerkskunst.',
        ubar=[('Maßarbeit', 'und Handwerkskunst'), ('Mo – Sa', 'geöffnet, samstags bis 15 Uhr'), ('Schüller, Rotpunkt', 'und weitere Marken')]))
        + marquee(['Traditionell', 'Modern', 'Landhausstil', 'Schüller', 'Rotpunkt', 'Quooker', 'Finanzierung'], 'pz')
        + scroller('modelle', 'Küchenmodelle', 'Immer ein Stil, <em>der zu Ihnen passt.</em>', 'Jeder lebt anders und hat andere Wünsche. Finden Sie die Küche, die zu Ihrem Lebensstil passt.', [
            ('Modern mit Insel', 'k1.jpg', 'Schwarz matt, klare Linien.', '50% 50%'),
            ('Hell und offen', 'k2.jpg', 'Viel Licht, viel Stauraum.', '50% 50%'),
            ('Mit Holz kombiniert', 'k3.jpg', 'Warm und wohnlich.', '50% 50%'),
            ('Landhaus', 'k4.jpg', 'Sandgrau mit Rahmenfronten.', '50% 50%'),
            ('Farbakzente', 'k5.jpg', 'Akzente in Blau und Gelb.', '50% 50%')], 'alt')
        + svc('service', 'Unser Service', 'Wir sind <em>für Sie da.</em>', 'Vereinbaren Sie unverbindlich einen Termin.', [
            ('Beratung', 'Mit jahrelanger Erfahrung zu Design, Bedienung und Preis.'),
            ('Planung', 'Gemeinsam mit Ihnen entsteht die schönste Aufstellung für Ihren Raum.'),
            ('Finanzierung', 'Auf Wunsch finanzieren Sie Ihre Küche. Sprechen Sie uns an.'),
            ('Angebote', 'Ausstellungsküchen, Geräte und Spülen zu Angebotspreisen.')])
        + reviews(s, ['Sergej hat unsere neue Küche fantastisch geplant und alle Wünsche erfüllt. Montiert wurde termingerecht und sehr professionell.',
                      'Nachdem die Beratung in anderen Küchenstudios zu wünschen übrig ließ, fühlten wir uns bei Küchen Plaza gut aufgehoben. Auch das Preis-Leistungs-Verhältnis war das beste.',
                      'Sehr gute Beratung, freundliche und hilfsbereite Mitarbeiter. Die Küche ist noch schöner geworden, als wir sie uns vorgestellt hatten.',
                      'Schnelle und unkomplizierte Hilfe, sehr freundliche Mitarbeiter und kundenfreundliche Öffnungszeiten.'])
        + contact(s) + footer(s))

S = SITES['plaza'] = site(
    slug='kuechen-plaza-rheine', firma='Küchen Plaza', web='kuechenplaza.eu', fonts='r16hirnstein',
    title='Küchen Plaza Rheine – Träume werden wahr', desc='Küchen Plaza in Rheine: Küchen mit Persönlichkeit, Maßarbeit und Handwerkskunst, Finanzierung möglich.',
    tel='05971 9977524', tel_i='+4959719977524', mail='info@kuechenplaza.eu', adresse='Osnabrücker Str. 298, 48429 Rheine', google=('5,0', 14),
    cta='Termin planen', nav=[('Küchenmodelle', 'modelle'), ('Service', 'service'), ('Kundenstimmen', 'stimmen'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '10:00 – 18:00'), ('Sa', '10:00 – 15:00'), ('So', 'geschlossen')],
    form_opts=['Neue Küche', 'Angebot / Ausstellungsküche', 'Finanzierung', 'Sonstiges'],
    form_h3='Termin planen', form_p='Möchten Sie wissen, was wir für Sie tun können? Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Lassen Sie sich <em>überraschen.</em>', kt_p='Besuchen Sie uns an der Osnabrücker Straße in Rheine.',
    rv_h2='Das sagen <em>unsere Kunden.</em>', social=[('Instagram', 'https://www.instagram.com/kuechenplaza/'), ('Facebook', 'https://www.facebook.com/profile.php?id=61550208636975')],
    vars=V.format(ink='#242424', mute='#5c5c5c', p='#ED1E24', pi='#fff', dk='#242424', s2='#f3f3f3', fh='"Roboto Slab",Georgia,serif', fb='"Source Sans 3",system-ui,sans-serif', lh=54, ft='#161616') + DKHD.format(c='#242424'),
    css='''.hs h1,.h2{font-weight:700;letter-spacing:-.02em;line-height:1.05}.hs h1{font-size:clamp(44px,7vw,108px)}.hs h1 em,.h2 em{font-style:normal;color:#ED1E24}.alt{background:var(--s2)}
.mq.pz span{font-family:var(--fh);font-weight:700}.sv .row div{border-top:4px solid #ED1E24}.hd .nav a{color:#fff}''')
S['bot'] = BOT('Pia', 'Ihre Küchen-Lotsin', 'Küchen Plaza', S, [
    ['Öffnungszeiten', 'Mo–Fr 10–18 Uhr, Sa 10–15 Uhr. Sonntags geschlossen.'],
    ['Kann ich finanzieren?', 'Ja, eine Finanzierung ist möglich. Sprechen Sie uns einfach an.'],
    ['Gibt es Angebote?', 'Ja, Ausstellungsküchen, Geräte und Spülen gibt es zu Angebotspreisen.']],
    ['#modelle', '#service', '#stimmen', '#kontakt'])
S['img'] = {'logo.png': ('plaza/img/i056.png', 600), 'h1.jpg': ('plaza/img/i001.jpg', 0), 'h2.jpg': ('plaza/img/i037.jpg', 0), 'h3.jpg': ('plaza/img/i027.jpg', 0),
    'k1.jpg': ('plaza/img/i001.jpg', 1300), 'k2.jpg': ('plaza/img/i013.jpg', 1300), 'k3.jpg': ('plaza/img/i014.jpg', 1300), 'k4.jpg': ('plaza/img/i052.jpg', 1300), 'k5.jpg': ('plaza/img/i037.jpg', 1300)}
S['body'] = b_plaza
