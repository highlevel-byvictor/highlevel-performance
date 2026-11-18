"""Runde 17 · Teil A: Küchenpartner Willmann, Küchen Center Zwinger, Küchen Stegink, Feldhaus Küchen."""
from common import *
SITES = {}
V = '--bg:#fff;--ink:{ink};--mute:{mute};--p:{p};--p-ink:{pi};--a:{p};--a-ink:{pi};--dk:{dk};--s:#fff;--s2:{s2};--fh:{fh};--fb:{fb};--r:0px;--r2:0px;--br:2px;--mq-bg:{dk};--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:{ink};--logo-h:{lh}px;--ft-bg:{ft};--hp-bg:{s2}'

# ───────────── 1. Ihr Küchenpartner Willmann, Hunteburg ─────────────
def b_willmann(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '40% 50%', 'h2.jpg': '50% 50%', 'h3.jpg': '50% 50%'},
        ey='Ihr Küchenpartner Willmann · Hunteburg / Bohmte',
        h1='Einfach <em>gute Küchen.</em>',
        sub='Seit über 35 Jahren planen, liefern und montieren wir Küchen im Umkreis von 30 km um Hunteburg. Mit eigener Werkstatt für alles, was es nicht von der Stange gibt.',
        ubar=[('Über 35 Jahre', 'Erfahrung rund um die Einbauküche'), ('Über 300 Geräte', 'ständig im eigenen Lager'), ('Eigene Werkstatt', 'für Sonderanfertigungen')]))
        + marquee(['Bohmte', 'Stirpe', 'Bad Essen', 'Ostercappeln', 'Damme', 'Neuenkirchen-Vörden', 'Engter', 'Belm', 'Osnabrück', 'Lemförde', 'Diepholz', 'Levern'], 'wm')
        + panels('planung', 'Individuelle Planung', 'Küche, Hauswirtschaftsraum, Bad <em>oder Möbel nach Maß.</em>', 'Ob modern, klassisch oder Landhausstil: Sprechen Sie uns einfach an.', [
            ('Küchen', 'p1.jpg', 'Umfassende Beratung, Planungsvorschläge in 3D, ein detailliertes Angebot und termingenaue Lieferung.', '50% 50%'),
            ('Ausstellung', 'p2.jpg', 'Sehen, anfassen, ausprobieren: Oberflächen, Materialien und Raumkonzepte direkt bei uns in Hunteburg.', '50% 50%'),
            ('Sonderanfertigungen', 'p3.jpg', 'In unserer Schreinerei werden vorgefertigte Küchenmöbel zu Unikaten nach Ihren Vorstellungen.', '50% 50%'),
            ('Innenausstattung', 'p4.jpg', 'Auszüge, Einsätze und Zubehör, damit in Ihrer Küche alles seinen Platz hat.', '50% 50%')])
        + promo('lager', 'lager.jpg', 'Lagerware', 'Über 300 Geräte <em>sofort verfügbar.</em>',
                'Was ist eine Küche ohne zuverlässige Geräte? In unserem großen Lager halten wir ständig über 300 Stand- und Einbaugeräte bereit. Dazu Arbeitsplatten, Spülen, Armaturen und Zubehör.',
                ['Waschmaschinen, Trockner, Kühlschränke, Spülmaschinen', 'Mikrowellen und Dampfgarer', 'Lieferung und Montage für einen geringen Aufpreis'], 'Gerät anfragen', 'alt')
        + svc('service', 'Unser Kundendienst', 'Immer <em>für Sie da.</em>', 'Ein Auftrag ist erst erledigt, wenn Sie zufrieden sind.', [
            ('Eigenes Personal', 'Wir arbeiten mit eigenen, geschulten Küchenmonteuren, inklusive aller Elektro- und Wasseranschlüsse.'),
            ('Schnell zur Stelle', 'Mit unserem gut ausgestatteten Fuhrpark sind wir schnell bei Ihnen, auch im Notfall.'),
            ('Fair und unabhängig', 'Wir beraten fair und finden für jeden Geldbeutel die richtige Lösung.'),
            ('Auch danach', 'Für spätere Anpassungen, Umbauten oder Ergänzungen stehen wir gerne zur Verfügung.')])
        + story('ueber', 'Unsere Leidenschaft', 'Was wir machen, <em>machen wir richtig gerne.</em>', [
            'Geschäftsführer Daniel und Hans Willmann und ihr Team stehen Ihnen mit Rat und Tat rund um die Einbauküche zur Seite. Wir gehen gerne ins Detail: Erst wenn alles bedacht ist, alles genau passt und einwandfrei funktioniert, sind wir zufrieden.',
            'Schließlich ist die Küche oft der Mittelpunkt des Hauses. Und der Mittelpunkt unseres Schaffens.'], 'luft.jpg', 'Unser Firmensitz im Industriegebiet Hunteburg', cls='dk',
            tl=[('3D', 'Planungsvorschläge'), ('30 km', 'Einzugsgebiet'), ('Mo – Sa', 'geöffnet')])
        + reviews(s, ['Hier steht der Kunde wirklich an erster Stelle. Hervorragende Beratung, kompetente Mitarbeiter, und es wird immer eine Lösung gefunden.',
                      'Gestern gekauft, heute geliefert. Gute und kompetente Verkaufsberatung. Der Einbau war knifflig, wurde vom Monteur aber perfekt gelöst.',
                      'Auch ein kleiner Auftrag wurde angenommen, professionell geplant und überraschend zeitnah und akkurat ausgeführt.',
                      'Arbeitsplatte, Spüle, Backofen und Kochfeld getauscht: schnell, sauber und professionell. Die Monteure waren sehr freundlich.'])
        + contact(s) + footer(s))

S = SITES['willmann'] = site(
    slug='kuechenpartner-willmann-hunteburg', firma='Ihr Küchenpartner Willmann', web='kuechenwillmann.de', fonts='r10vagts',
    title='Ihr Küchenpartner Willmann – Küchen in Hunteburg / Bohmte', desc='Küchenpartner Willmann in Hunteburg: Küchen, Hauswirtschaftsräume und Möbel nach Maß, eigene Werkstatt, über 300 Geräte am Lager.',
    tel='05475 1754', tel_i='+4954751754', mail='info@kuechenwillmann.de', adresse='Scheelenkamp 6, 49163 Bohmte-Hunteburg', google=('4,8', 64),
    cta='Beratungstermin anfragen', nav=[('Planung', 'planung'), ('Lagerware', 'lager'), ('Service', 'service'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 12:30, 13:30 – 18:00'), ('Sa', '9:00 – 12:30')],
    form_opts=['Neue Küche', 'Hauswirtschaftsraum / Bad', 'Sonderanfertigung', 'Gerät aus dem Lager', 'Umbau / Ergänzung', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Was können wir <em>für Sie tun?</em>', kt_p='Schreiben Sie uns oder kommen Sie vorbei, wir freuen uns auf Ihren Besuch.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#252527', mute='#55555f', p='#E0090C', pi='#fff', dk='#444452', s2='#f1f1f5', fh='"Lato",system-ui,sans-serif', fb='"Lato",system-ui,sans-serif', lh=64, ft='#2b2b33'),
    css='''.hs h1,.h2{font-weight:900;text-transform:uppercase;letter-spacing:.005em;line-height:1.02}.hs h1{font-size:clamp(44px,7vw,112px)}.hs h1 em,.h2 em{font-style:normal;color:#E0090C}.dk .h2 em{color:#ff6b6d}
.mq.wm span{font-weight:900;text-transform:uppercase;letter-spacing:.08em;font-size:15px}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #E0090C}
.hs .ubar b{color:#fff}.ft img{background:#fff;padding:6px 10px;height:64px}.st.dk{background:#444452;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}''')
S['bot'] = BOT('Wilma', 'Ihre Küchen-Lotsin', 'Küchenpartner Willmann', S, [
    ['Öffnungszeiten', 'Mo–Fr 9:00–12:30 und 13:30–18:00 Uhr, Sa 9:00–12:30 Uhr.'],
    ['Liefern Sie zu mir?', 'Unser Einzugsgebiet liegt ca. 30 km um Hunteburg, auf Anfrage liefern wir auch weiter. Telefon: 05475 1754.'],
    ['Geräte am Lager?', 'Wir halten ständig über 300 Stand- und Einbaugeräte bereit. Fragen Sie einfach an.']],
    ['#planung', '#lager', '#service', '#kontakt'])
S['img'] = {'logo.png': ('willmann/img/i000.jpg', 0, 'trim'), 'h1.jpg': ('willmann/img/i001.jpg', 0), 'h2.jpg': ('willmann/img/i131.jpg', 0), 'h3.jpg': ('willmann/img/i008.jpg', 0),
    'p1.jpg': ('willmann/img/i149.jpg', 1400), 'p2.jpg': ('willmann/img/i051.jpg', 1400), 'p3.jpg': ('willmann/img/i150.jpg', 1400), 'p4.jpg': ('willmann/img/i042.jpg', 1400),
    'lager.jpg': ('willmann/img/i145.jpg', 1400), 'luft.jpg': ('willmann/img/i007.jpg', 0)}
S['body'] = b_willmann

# ───────────── 2. Küchen Center Zwinger, Westerkappeln ─────────────
def b_zwinger(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='1a',
        ubar=[('21 Mal', 'in Folge 1a-Fachhändler'), ('Seit 1995', 'inhabergeführt'), ('Festpreis', 'inkl. Lieferung, Montage, Anschlüsse')],
        ey='Küchen Center Westerkappeln · Ihr Küchenstudio im Raum Osnabrück',
        h1='Ihre Zufriedenheit <em>ist unser Ziel.</em>',
        sub='Küchen verkaufen können viele. Wir begleiten Sie vom ersten Beratungsgespräch bis zur fertigen Küche, ein Küchenleben lang. Mit Markenware zu erschwinglichen Preisen.'))
        + story('auszeichnung', 'Ausgezeichnet von „markt intern“', '21 Mal in Folge <em>1a-Fachhändler.</em>', [
            'Unser Küchen Center wurde vom Branchenmagazin „markt intern“ schon 21 Mal in Folge zum „1a Fachhändler“ ernannt. Das heißt: freundliches und kompetentes Fachpersonal, keine aggressive Rabattwerbung und Markenware zu erschwinglichen Preisen.',
            'Besonderer Dank gilt unseren Kunden, für ihr Vertrauen und ihre langjährige Treue.'], 'award.jpg', 'Auszeichnung zum 1a-Fachhändler 2026', cls='aw')
        + scroller('kuechen', 'Qualitäts-Einbauküchen', 'Die perfekte Küche ist <em>eine Frage des Geschmacks.</em>', 'Design, Landhaus, grifflos oder Classic: Mit unserem Programm lassen sich die unterschiedlichsten Wünsche erfüllen.', [
            ('Design-Küchen', 'k1.jpg', 'Klare Linien und viel Raum.', '50% 50%'),
            ('Landhaus-Küchen', 'k2.jpg', 'Gemütlich mit Charakter.', '50% 50%'),
            ('Grifflose Küchen', 'k3.jpg', 'Ruhige Fronten, reduziert.', '50% 50%'),
            ('Classic-Küchen', 'k4.jpg', 'Zeitlos und bewährt.', '50% 50%'),
            ('Bad-Möbel', 'k5.jpg', 'Auch fürs Bad planen wir passend.', '50% 50%')])
        + ablauf('ablauf', 'Wie wir arbeiten', 'In fünf Schritten <em>zu Ihrer Küche.</em>', 'Die Planung ist für Sie unverbindlich und kostenfrei.', [
            ('Vorbesprechung', 'Erster Termin in unserer Ausstellung oder in Ihrer Küche, etwa eine Stunde. Wir sprechen über Wünsche, Materialien, Geräte und Ihr Budget.'),
            ('Der erste Entwurf', 'Wir präsentieren einen Entwurf für Ihren Raum, stellen Alternativen vor und besprechen Vor- und Nachteile.'),
            ('Weiterentwicklung', 'Wir passen Ihre favorisierte Planung an und zeigen den geänderten Entwurf inklusive Preisangabe.'),
            ('Auftrag und Aufmaß', 'Sie erhalten Elektro- und Wasserinstallationspläne. Vor der Freigabe prüfen wir alle Maße noch einmal vor Ort.'),
            ('Montage', 'Unser eigenes, bestens ausgebildetes Montageteam baut Ihre Küche auf.')], 'alt')
        + promo('bora', 'bora.jpg', 'BORA', 'Das Ende <em>der Dunstabzugshaube.</em>',
                'Mit den Kochfeldabzugssystemen von BORA werden Kochdünste und Gerüche direkt am Kochfeld abgesaugt. Das verändert die Architektur der Küche. Lassen Sie es sich bei uns zeigen.',
                ['BORA Professional, Classic und Basic', 'Live in unserer Ausstellung'], 'BORA-Beratung anfragen')
        + team('team', 'Unser Team', 'Familie Zwinger <em>berät Sie persönlich.</em>', 'Persönlicher Service ganz nach Ihren Vorstellungen ist unsere Devise.', [
            ('t1.jpg', 'Viktor Zwinger', 'Geschäftsführer'), ('t2.jpg', 'Nikolaus Zwinger', 'Verkaufsleiter'), ('t3.jpg', 'Christian Zwinger', 'Einrichtungsberater')], 'dk')
        + reviews(s, ['Von der Planung über die Umsetzung bis zur Ausführung wurden unsere Wünsche sehr gut berücksichtigt. Unser Berater kam während und nach der Montage mehrfach zu uns nach Hause.',
                      'Vom ersten Termin über die Planung bis zu unseren Änderungswünschen lief alles unkompliziert. Die Monteure haben tadellos sauber gearbeitet.',
                      'Die Beratung war top: kompetent, freundlich und voller guter Ideen. Großes Lob an die beiden Küchenmonteure.',
                      'Nach etwa einem Jahr Nutzung: Die Küche ist optisch und funktional hervorragend. Beratung, Montage und Service waren freundlich und kompetent.'])
        + contact(s) + footer(s))

S = SITES['zwinger'] = site(
    slug='kuechen-center-zwinger-westerkappeln', firma='Küchen Center Zwinger e.K.', web='kuechencenter-westerkappeln.de', fonts='r14egg',
    title='Küchen Center Westerkappeln – Ihr Küchenstudio im Raum Osnabrück', desc='Küchen Center Zwinger in Westerkappeln: 21 Mal in Folge 1a-Fachhändler, Qualitäts-Einbauküchen mit Festpreisangebot und eigenem Montageteam.',
    tel='05404 96550', tel_i='+49540496550', mail='info@kuechencenter-westerkappeln.de', adresse='Gartenkamp 212, 49492 Westerkappeln', google=('4,8', 67),
    cta='Beratungstermin vereinbaren', nav=[('Auszeichnung', 'auszeichnung'), ('Küchen', 'kuechen'), ('Ablauf', 'ablauf'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    tbar='Schausonntag: jeden Sonntag 15 bis 18 Uhr (außer an Feiertagen, keine Beratung, kein Verkauf)',
    hours=[('Mo – Fr', '10:00 – 19:00'), ('Sa', '10:00 – 16:00'), ('So', 'Schautag 15:00 – 18:00')],
    form_opts=['Neue Küche', 'Bad-Möbel', 'BORA / Elektrogeräte', 'Finanzierung', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Für die Vorbesprechung nehmen wir uns etwa eine Stunde Zeit. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Testen Sie uns. <em>Sie werden überzeugt sein.</em>', kt_p='Wenn Sie Fragen zu unseren Produkten oder zu Ihrer Küche haben, freuen wir uns auf Ihre Nachricht oder Ihren Anruf.',
    rv_h2='Das sagen <em>unsere Kunden.</em>', social=[('Facebook', 'https://www.facebook.com/K%C3%BCchen-Center-Westerkappeln-462161723930690/')],
    vars=V.format(ink='#1d2a33', mute='#55626b', p='#C8322F', pi='#fff', dk='#1F5F7E', s2='#eef4f7', fh='"Montserrat",system-ui,sans-serif', fb='"Montserrat",system-ui,sans-serif', lh=52, ft='#143f55'),
    css='''.h2{font-weight:800;letter-spacing:-.02em;line-height:1.06}.h2 em{font-style:normal;color:#1F5F7E}.dk .h2 em{color:#9fd3ea}.alt{background:var(--s2)}
.st.aw figure img{aspect-ratio:1920/839;object-fit:cover;height:auto}.st.aw .w{grid-template-columns:1.25fr 1fr}
.tm .grid{grid-template-columns:repeat(3,minmax(0,300px));justify-content:center}.tm .grid figure div{aspect-ratio:4/5}.tm .grid figure div img{object-position:50% 20%}
.rd .road div::before{background:#1F5F7E}.promo .tag{background:#1F5F7E;color:#fff}.ft img{background:#fff;padding:8px 12px;height:60px}
@media(max-width:820px){.st.aw .w{grid-template-columns:1fr}.tm .grid{grid-template-columns:1fr 1fr}}''')
S['css2'] = '.hz{--hz-bg:#1F5F7E;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.85);--hz-stroke:rgba(255,255,255,.16);--hz-line:rgba(255,255,255,.22);--hz-cols:46fr 54fr}.hz h1{font-size:clamp(36px,4.3vw,68px)}.hz h1 em{color:#ffd9d6}.hz .ey{color:#bfe3f3}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}.hz .chip{background:rgba(255,255,255,.12);color:#fff}'
S['bot'] = BOT('Kira', 'Ihre Küchen-Lotsin', 'dem Küchen Center Westerkappeln', S, [
    ['Öffnungszeiten', 'Mo–Fr 10–19 Uhr, Sa 10–16 Uhr. Sonntags Schautag von 15–18 Uhr, ohne Beratung und Verkauf.'],
    ['Was kostet die Planung?', 'Die Planung Ihrer Küche ist unverbindlich und für Sie kostenfrei.'],
    ['Wer baut die Küche auf?', 'Unser eigenes Montageteam. Im Festpreisangebot sind Lieferung, Montage und Anschlüsse enthalten.']],
    ['#auszeichnung', '#kuechen', '#ablauf', '#kontakt'])
S['img'] = {'logo.png': ('zwinger/logo.png', 0), 'h1.jpg': ('zwinger/img/i015.jpg', 0), 'h2.jpg': ('zwinger/img/i016.jpg', 0), 'h3.jpg': ('zwinger/img/i017.jpg', 0),
    'award.jpg': ('zwinger/img/i032.jpg', 0), 'bora.jpg': ('zwinger/img/i022.jpg', 1400),
    'k1.jpg': ('zwinger/img/i025.jpg', 1300), 'k2.jpg': ('zwinger/img/i037.jpg', 1300), 'k3.jpg': ('zwinger/img/i201.jpg', 1300), 'k4.jpg': ('zwinger/img/i019.jpg', 1300), 'k5.jpg': ('zwinger/img/i036.jpg', 1300),
    't1.jpg': ('zwinger/img/i031.jpg', 0, (.40, 0, .76, 1)), 't2.jpg': ('zwinger/img/i030.jpg', 0, (.40, 0, .76, 1)), 't3.jpg': ('zwinger/img/i024.jpg', 0, (.34, 0, .70, 1))}
S['body'] = b_zwinger

# ───────────── 3. Küchen Stegink, Neuenhaus ─────────────
def b_stegink(s):
    return (hd(s, False) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'],
        ey='Küchen Stegink · Neuenhaus in der Grafschaft Bentheim',
        h1='Küchen zum <em>Wohlfühlen.</em>',
        sub='Wir fertigen, liefern und montieren Küchen nach Maß. Seit 1983, mit eigener Tischlerei, deutschlandweit und in den Niederlanden.',
        ubar=[('Seit 1983', 'Qualität, Service, faire Preise'), ('Eigene Tischlerei', 'jedes Möbelstück maßgenau'), ('DE + NL', 'Lieferung und Montage')]))
        + marquee(['Moderne Küchen', 'Landhausküchen', 'Grifflose Küchen', 'Hauswirtschaftsraum', 'Ausstellungsküchen', 'Küchenkonfigurator', 'Eigene Tischlerei'], 'sg')
        + promo('konfigurator', 'konf.jpg', 'Neu', 'Stellen Sie Ihre Traumküche <em>Schritt für Schritt zusammen.</em>',
                'Küchenform, Einbaugeräte, Spüle und Armatur, Sitzplätze, Budget: Mit unserem Küchenkonfigurator sammeln Sie ganz unverbindlich Ihre Wünsche. Wir melden uns mit einem passenden Vorschlag.',
                ['L-Form, U-Form, Küchenzeile oder Insel', 'Grundriss oder Skizze einfach hochladen', 'Ihre Angaben bleiben 14 Tage gespeichert'], 'Küche konfigurieren')
        + scroller('kuechen', 'Bildergalerie', 'Anregungen für <em>Ihre Traumküche.</em>', 'Von der Landhausküche bis zur geradlinigen modernen Küche: Jede Küche wird bei uns an Ihre Wünsche angepasst.', [
            ('Moderne Küchen', 'k1.jpg', 'Geradlinig und wohnlich.', '50% 50%'),
            ('Landhausküchen', 'k2.jpg', 'Rahmenfronten und warme Töne.', '50% 50%'),
            ('Grifflose Küchen', 'k3.jpg', 'Ruhige Flächen ohne Griffe.', '50% 50%'),
            ('Mit Kochinsel', 'k4.jpg', 'Kochen mitten im Raum.', '50% 50%'),
            ('Dunkel und markant', 'k5.jpg', 'Schwarze Fronten, Holz dazu.', '50% 50%'),
            ('Hauswirtschaftsraum', 'k6.jpg', 'Einbauschränke, Regalsysteme, Podeste.', '50% 50%')], 'dk')
        + svc('leistung', 'Qualität ist unser Handwerk', 'Von der Planung <em>bis zur Endmontage.</em>', 'Auch wenn Ihre Räume keine Lösung von der Stange zulassen, haben Sie bei uns den richtigen Ansprechpartner.', [
            ('Beratung und Planung', 'Ihr Partner für individuelle Wünsche, mit zuverlässiger Baubetreuung.'),
            ('Maßgefertigte Küchen', 'Änderungen und Maßanfertigungen sind bei uns kein Problem.'),
            ('Eigene Tischlerei', 'In der hauseigenen Tischlerei stellen wir jedes Möbelstück maßgenau her.'),
            ('Montage vor Ort', 'Wir montieren Ihre Küche in ganz Deutschland und in den Niederlanden.')])
        + gallery('ausstellung', 'Ausstellungsküchen', 'Musterküchen <em>zu reduzierten Preisen.</em>', [
            ('a1.jpg', 'a', '50% 50%'), ('a2.jpg', 'b', '50% 50%'), ('a3.jpg', 'c', '50% 50%')], 'alt')
        + story('ueber', 'Über Stegink', 'Seit 2014 in <em>Neuenhaus-Grasdorf.</em>', [
            'Küchen Stegink wurde 1983 gegründet. Unser Anspruch sind zufriedene Kunden bei Preis, Leistung und Service. In unseren großzügigen Ausstellungsräumen erleben Sie Küchen für jeden Geschmack.',
            'Die eigene Werkstatt liegt direkt am Hauptgebäude. So können wir unmittelbar auf Ihre Wünsche eingehen.'], 'haus.jpg', 'Unser Hauptgeschäft an der Dietrich-Borggreve-Straße', cls='hb')
        + reviews(s, ['Ein Küchentraum ist wahr geworden. Planung, Beratung und Montage auf höchstem Niveau, freundliche und hilfsbereite Mitarbeiter.',
                      'Hervorragende Beratung im Studio, der Preis war absolut fair. Altbau mit schiefen Wänden, und trotzdem wurde alles millimetergenau angepasst.',
                      'Wir hatten schon zwei Angebote. Stegink hat sich viel Zeit genommen und in der Planung viele Tipps gegeben, die unseren Entwurf besser gemacht haben.',
                      'Alle Wünsche wurden berücksichtigt und perfekt umgesetzt. Der Service war von Anfang bis Ende freundlich, kompetent und zuverlässig.'])
        + contact(s) + footer(s))

S = SITES['stegink'] = site(
    slug='kuechen-stegink-neuenhaus', firma='Küchen Stegink GmbH & Co. KG', web='kuechen-stegink.de', fonts='r15kem',
    title='Küchen Stegink – Küchen nach Maß aus Neuenhaus', desc='Küchen Stegink in Neuenhaus: maßgefertigte Küchen seit 1983, eigene Tischlerei, Lieferung und Montage in Deutschland und den Niederlanden.',
    tel='05941 9895540', tel_i='+4959419895540', mail='info@kuechen-stegink.de', adresse='Dietrich-Borggreve-Straße 18, 49828 Neuenhaus', google=('4,8', 77),
    cta='Termin vereinbaren', nav=[('Konfigurator', 'konfigurator'), ('Küchen', 'kuechen'), ('Leistungen', 'leistung'), ('Ausstellung', 'ausstellung'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 12:30, 14:00 – 18:00'), ('Sa', '9:00 – 13:00')],
    form_opts=['Neue Küche', 'Küchenkonfigurator / Planung', 'Ausstellungsküche', 'Hauswirtschaftsraum', 'Service / Reklamation', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Wir beraten Sie gerne und unverbindlich. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Überzeugen Sie sich <em>vor Ort.</em>', kt_p='Kommen Sie vorbei und lassen Sie sich von unseren Fachberatern die neuesten Trends zeigen.',
    rv_h2='Das sagen <em>unsere Kunden.</em>', social=[('Instagram', 'https://www.instagram.com/kuechen_stegink/'), ('Facebook', 'https://www.facebook.com/p/K%C3%BCchen-Stegink-GmbH-Co-KG-100057515557905')],
    vars=V.format(ink='#111', mute='#4d4d4d', p='#D20233', pi='#fff', dk='#0b0b0b', s2='#f3f3f3', fh='"Bebas Neue",Impact,sans-serif', fb='"Roboto",system-ui,sans-serif', lh=58, ft='#000') + ';--hd-bg:#000;--hd-ink:#fff',
    css='''.hs h1,.h2,.sv h3,.sc h3{font-weight:400;letter-spacing:.02em;line-height:.98;text-transform:uppercase}.hs h1{font-size:clamp(60px,10vw,160px)}.h2{font-size:clamp(38px,5vw,72px)}.hs h1 em,.h2 em{font-style:normal;color:#D20233}
.mq.sg span{font-family:var(--fh);font-size:24px;letter-spacing:.06em}.mq.sg{border-block:2px solid #D20233}.alt{background:var(--s2)}.sc.dk{background:#0b0b0b;color:#fff}.sc.dk .lead{color:rgba(255,255,255,.8)}
.sv .row div{border-top:4px solid #D20233}.rv .cd p,.kt h3,.sv .row p{font-family:var(--fb);text-transform:none;letter-spacing:0}.gl .grid{grid-template-columns:repeat(3,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:4/3}
.st.hb figure img{aspect-ratio:4000/1355;object-fit:cover;height:auto}.st.hb .w{grid-template-columns:1.4fr 1fr}.hd .nav a{color:#fff}
@media(max-width:820px){.st.hb .w{grid-template-columns:1fr}.gl .grid{grid-template-columns:1fr}}''')
S['bot'] = BOT('Stina', 'Ihre Küchen-Lotsin', 'Küchen Stegink', S, [
    ['Öffnungszeiten', 'Mo–Fr 9:00–12:30 und 14:00–18:00 Uhr, samstags 9:00–13:00 Uhr.'],
    ['Liefern Sie auch in die Niederlande?', 'Ja, wir liefern und montieren in ganz Deutschland und in den Niederlanden.'],
    ['Gibt es Ausstellungsküchen?', 'Ja, wir tauschen unsere Musterküchen regelmäßig aus. Diese erhalten Sie zu reduzierten Preisen.']],
    ['#konfigurator', '#kuechen', '#ausstellung', '#kontakt'])
S['img'] = {'logo.png': ('stegink/img/i000.jpg', 0), 'h1.jpg': ('stegink/img/i004.jpg', 0), 'h2.jpg': ('stegink/img/i025.jpg', 0), 'h3.jpg': ('stegink/img/i003.jpg', 0),
    'konf.jpg': ('stegink/img/i033.jpg', 1400),
    'k1.jpg': ('stegink/img/i014.jpg', 1200), 'k2.jpg': ('stegink/img/i044.jpg', 1200), 'k3.jpg': ('stegink/img/i036.jpg', 1300), 'k4.jpg': ('stegink/img/i035.jpg', 1300), 'k5.jpg': ('stegink/img/i040.jpg', 1300), 'k6.jpg': ('stegink/img/i052.jpg', 1300),
    'a1.jpg': ('stegink/img/i053.jpg', 1300), 'a2.jpg': ('stegink/img/i054.jpg', 1300), 'a3.jpg': ('stegink/img/i055.jpg', 1300), 'haus.jpg': ('stegink/img/i073.jpg', 2000)}
S['body'] = b_stegink

# ───────────── 4. Feldhaus Küchen Design & Technik, Emstek ─────────────
def b_feldhaus(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], side='l', big='1976', pos={'h1.jpg': '50% 50%', 'h3.jpg': '50% 50%'},
        ubar=[('Seit 1976', 'Familienunternehmen'), ('Mehrfach', 'ausgezeichnet'), ('Aus einer Hand', 'bis zur Montage')],
        ey='Feldhaus Küchen Design & Technik · Emstek',
        h1='Jede Küche <em>ist ein Unikat.</em>',
        sub='Seit 1976 planen wir individuelle, hochwertige Einbauküchen im Oldenburger Münsterland. Mit viel Zeit für Ihr Beratungsgespräch und eigenem Kundendienst.'))
        + marquee(['„Zu Hause wohnen“', '„Feinschmecker Guide“', '„Architektur und Wohnen“', 'Partner der Küchengilde', 'Miele', 'raumplus'], 'fh')
        + story('ueber', 'Wir über uns', 'Eine der besten Adressen <em>für Küchen in Deutschland.</em>', [
            'Unser Familienunternehmen hat sich 1976 auf die komplette Planung individueller Einbauküchen spezialisiert, damals ein Novum im Oldenburger Münsterland. „Zu Hause wohnen“, „Feinschmecker Guide“ und „Architektur und Wohnen“ zählen uns zu den besten Adressen der Küchenspezialisten in Deutschland.',
            'Wir nehmen uns viel Zeit für intensive Beratungsgespräche, auch für Farbgestaltung und Fliesenauswahl.'], 'haus.jpg', 'Unser Haus an der Ostlandstraße in Emstek', cls='hb')
        + ablauf('kodex', 'Unser Kodex zu Ihrem Vorteil', 'So arbeiten <em>wir für Sie.</em>', 'Als Partner der Küchengilde verpflichten wir uns zu hohen Qualitätsstandards.', [
            ('Zuhören', 'Geplant wird ganz individuell: mit Kompetenz, Sachverstand und einem guten Ohr für Ihre Wünsche.'),
            ('Mitdenken', 'Wir bleiben auf dem Boden: Küchen sind zum Leben und für die Kunden da.'),
            ('Weiterdenken', 'Wir planen Raumkonzepte und koordinieren auf Wunsch sämtliche Handwerker.'),
            ('Prüfen', 'Ehrliche Qualität auf allen Ebenen: bei Material, Planung, Mechanik und Geräten.'),
            ('Renovieren', 'Neue Spüle, neue Geräte, neue Arbeitsplatte: Wir realisieren auch kleine Umbauten.')], 'alt')
        + panels('produkte', 'Produkte', 'Küchen, Geräte <em>und Raumlösungen.</em>', 'Neben exklusiven Einbauküchen bieten wir weitere Einrichtungsmöglichkeiten.', [
            ('Küchen', 'p1.jpg', 'Alle Farb- und Stilrichtungen: moderne grifflose Küchen, Landhausstil oder massive Vollholzküchen.', '50% 50%'),
            ('Einbaugeräte', 'p2.jpg', 'Professionelle Geräte von Miele, zum Beispiel Dampfgarer oder Induktions-Wok.', '50% 50%'),
            ('Innenausstattung', 'p3.jpg', 'Auszüge und Ordnungssysteme, ergonomisch geplant.', '50% 50%'),
            ('Raumlösungen', 'p4.jpg', 'Hauswirtschaftsräume, begehbare Kleiderschränke, Wohnwände und Schiebetüren von raumplus.', '50% 50%')])
        + svc('hand', 'Handwerker-Service-Plus', 'Alles <em>aus einer Hand.</em>', 'Auf Wunsch engagieren wir bewährte Fachleute für Sie und koordinieren sämtliche Arbeitsschritte.', [
            ('Boden', 'Fliesen, Parkett, Linoleum oder Stein: Wir haben die passenden Spezialisten.'),
            ('Licht', 'Ein abgestimmtes Konzept aus Grundhelligkeit, Spots am Arbeitsplatz und Stimmungslicht.'),
            ('Finanzieren', 'Wir sind flexibel. Mit uns können Sie über Finanzierungsmöglichkeiten reden.'),
            ('Kundendienst', 'Auch nach dem Kauf sind wir mit unserem hauseigenen Kundendienst für Sie da.')], 'dk')
        + reviews(s, ['Die Beratung war von Anfang an hervorragend: kompetent, ehrlich und auf unsere Bedürfnisse abgestimmt. Besonders überzeugt hat uns das Preis-Leistungs-Verhältnis.',
                      'Wir lieben Familienbetriebe! Von der ersten Planung bis zur Fertigstellung lief alles wunderbar, auch als wir Termine verschieben mussten.',
                      'Herr Feldhaus hat unsere Wünsche perfekt umgesetzt und eigene kreative Ideen eingebracht. Die Handwerker haben gearbeitet, als wäre es ihre eigene Küche.',
                      'Ein toller kleiner Betrieb mit motivierten, freundlichen und gründlichen Mitarbeitern. Jederzeit wieder.'])
        + contact(s) + footer(s))

S = SITES['feldhaus'] = site(
    slug='feldhaus-kuechen-emstek', firma='Feldhaus Küchen Design + Technik GmbH', web='feldhaus-kuechen.de', fonts='r16ellers',
    title='Feldhaus Küchen Design & Technik – Familienunternehmen seit 1976 in Emstek', desc='Feldhaus Küchen in Emstek: individuelle Einbauküchen seit 1976, mehrfach ausgezeichnet, Beratung, Planung und Montage aus einer Hand.',
    tel='04473 947811', tel_i='+494473947811', mail='feldhaus.kuechen@ewetel.net', adresse='Ostlandstraße 1, 49685 Emstek', google=('5,0', 30),
    cta='Termin anfragen', nav=[('Über uns', 'ueber'), ('Kodex', 'kodex'), ('Produkte', 'produkte'), ('Service', 'hand'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '9:00 – 12:00, 14:00 – 17:30'), ('Sa', 'auf Termin 9:00 – 12:00')],
    form_opts=['Neue Küche', 'Einbaugeräte', 'Raumlösung / Schranksystem', 'Umbau / Renovierung', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Gerne vereinbaren wir auch Termine außerhalb der Öffnungszeiten. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Im Herzen des <em>Oldenburger Münsterlands.</em>', kt_p='Sie finden uns zwischen Oldenburg und Osnabrück. Auf Termin sind wir auch samstags von 9 bis 12 Uhr für Sie da.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars=V.format(ink='#2a2624', mute='#5f5a57', p='#796662', pi='#fff', dk='#3a3432', s2='#f4f1ef', fh='"Open Sans",system-ui,sans-serif', fb='"Open Sans",system-ui,sans-serif', lh=58, ft='#2a2624'),
    css='''.h2{font-weight:300;letter-spacing:-.02em;line-height:1.1;font-size:clamp(32px,4.2vw,60px)}.h2 em{font-style:normal;font-weight:700;color:#796662}.dk .h2 em{color:#d9c5bf}
.mq.fh span{font-weight:600;letter-spacing:.04em}.alt{background:var(--s2)}.sv.dk{background:#3a3432;color:#fff}.sv.dk p{color:rgba(255,255,255,.82)}.sv .row div{border-top:2px solid #b89f98}
.ft img{background:#fff;padding:8px 12px;height:60px}.st.hb figure img{aspect-ratio:1400/679;object-fit:cover;height:auto}.st.hb .w{grid-template-columns:1.2fr 1fr}.rd .road div::before{background:#796662}
@media(max-width:820px){.st.hb .w{grid-template-columns:1fr}}''')
S['css2'] = '.hz{--hz-bg:#f4f1ef;--hz-ink:#2a2624;--hz-mute:#5f5a57;--hz-stroke:rgba(121,102,98,.2);--hz-cols:44fr 56fr}.hz h1{font-weight:300;font-size:clamp(38px,4.6vw,74px);letter-spacing:-.025em}.hz h1 em{font-weight:700;color:#796662}.hz .ey{color:#796662}.hz .hz-big{font-weight:800}'
S['bot'] = BOT('Frieda', 'Ihre Küchen-Lotsin', 'Feldhaus Küchen', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–12 und 14–17:30 Uhr. Auf Termin auch samstags von 9–12 Uhr.'],
    ['Koordinieren Sie Handwerker?', 'Ja, auf Wunsch engagieren wir bewährte Fachleute und koordinieren sämtliche Arbeitsschritte.'],
    ['Auch kleine Umbauten?', 'Ja, eine neue Spüle, neue Geräte oder eine neue Arbeitsplatte setzen wir ebenfalls um.']],
    ['#ueber', '#kodex', '#produkte', '#kontakt'])
S['img'] = {'logo.png': ('feldhaus/img/i000.jpg', 0, 'alphacrop'), 'h1.jpg': ('feldhaus/img/i067.jpg', 0), 'h2.jpg': ('feldhaus/img/i112.jpg', 0), 'h3.jpg': ('feldhaus/img/i099.jpg', 0),
    'haus.jpg': ('feldhaus/img/i096.jpg', 0), 'p1.jpg': ('feldhaus/img/i112.jpg', 0), 'p2.jpg': ('feldhaus/img/i115.jpg', 0), 'p3.jpg': ('feldhaus/img/i092.jpg', 0), 'p4.jpg': ('feldhaus/img/i082.jpg', 0)}
S['body'] = b_feldhaus
