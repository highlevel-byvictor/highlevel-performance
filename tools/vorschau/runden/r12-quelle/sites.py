"""Runde 12: Küchenstudios im Umkreis von 15 km um Bersenbrück. Nur echtes Material und belegte Fakten der Originalseiten."""
from lib import *
SITES = {}

# ───────────────────────── 1. Bersenbrücker Küchenstudio ─────────────────────────
def b_bsb(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h-show.jpg', 'h-kat.jpg', 'h-front.jpg'], pos0='50% 55%',
        ey='Küchenstudio in Bersenbrück · seit 1997',
        h1='14 Musterküchen. <em>Eine davon wird Ihre.</em>',
        sub='Auf rund 400 m² zeigen wir Ihnen Küchen von nobilia, Ballerina, Burger und Häcker. Persönliche Beratung, computergestützte Planung und Montage aus einer Hand, zu transparenten Preisen.',
        badge=('400 m²', 'Ausstellung in der Robert-Bosch-Straße')))
        + marquee(['nobilia', 'Ballerina Küchen', 'Burger Küchen', 'Häcker Küchen', 'BORA', 'Miele', 'Bosch', 'AEG', 'Badmöbel'])
        + promo('angebote', 'p-muster.jpg', 'Ausstellung wird erneuert', 'Musterküchen stark <em>reduziert.</em>',
                'Wir aktualisieren unsere Ausstellung und brauchen Platz. Deshalb geben wir ausgewählte Ausstellungsküchen zum Abholpreis ab, ehrlich kalkuliert und ohne Scheinrabatte.',
                ['nobilia XENO in Fjordblau', 'nobilia XENO in Grauschiefer', 'Ballerina Schneeweiß Lack Hochglanz'], 'Musterküche ansehen', 'alt')
        + tabs('leistungen', 'Küchenkauf aus einer Hand', 'Von der Idee bis zur <em>Einweisung.</em>', 'Wir nehmen uns Zeit für Ihre Wünsche und kümmern uns um alles, was dazugehört.', [
            ('Beratung & Planung', 'l-plan.jpg', 'Jede Küche planen wir nach Ihren Bedürfnissen: am Computer, mit großer Auswahl an Fronten, Dekoren, Arbeitsplatten und Griffen.', ['Computergestützte Planung', 'Große Auswahl an Fronten']),
            ('Aufmaß', 'l-aufmass.jpg', 'Auf Wunsch ermitteln wir zentimetergenau das Raummaß und die Lage der Elektro- und Wasseranschlüsse. Medienpläne erstellen wir gleich mit.', ['Zentimetergenau', 'Medienpläne inklusive']),
            ('Lieferung & Montage', 'l-montage.jpg', 'Termingerechte Lieferung und präzise Montage aus einer Hand. Alle nötigen Handwerkerleistungen koordinieren wir für Sie.', ['Termintreu', 'Handwerker koordiniert']),
            ('Geräte & Austausch', 'l-geraete.jpg', 'Neue Geräte oder vorhandene Altgeräte: Wir bauen sie effizient und optisch passend ein. Die Herstellergarantie können Sie auf Wunsch auf 5 Jahre verlängern.', ['5 Jahre Garantie möglich', 'Finanzierung auf Wunsch']),
            ('Badmöbel', 'l-bad.jpg', 'Neu bei uns: Badmöbel von nobilia. Die gleiche Qualität und Planung, jetzt auch für Ihr Badezimmer.', ['nobilia Bad'])])
        + gallery('ausstellung', 'Unsere Musterküchen', 'Kommen Sie vorbei und <em>fassen Sie alles an.</em>', [
            ('g1.jpg', '', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', '', '50% 50%'), ('g7.jpg', '', '50% 50%'), ('g8.jpg', '', '50% 50%')])
        + story('team', 'Familie Hüdepohl und Team', 'Persönlich beraten <em>statt verkauft.</em>', [
            'Seit Oktober 1997 sind wir in Bersenbrück für Sie da. Angefangen haben wir an der Bramscher Straße, 2009 sind wir in die größeren Ausstellungsräume an der Robert-Bosch-Straße gezogen.',
            'Eine neue Küche kauft man nicht alle Tage. Deshalb nehmen wir uns Zeit, hören zu und lassen Ihren Küchentraum Wirklichkeit werden.'],
            'team.jpg', cap='Das Verkaufsteam vom Bersenbrücker Küchenstudio', tl=[('1997', 'Gründung an der Bramscher Straße'), ('2009', 'Umzug in die Robert-Bosch-Straße'), ('Heute', '14 Musterküchen auf rund 400 m²')], rev=True)
        + vgrid('filme', 'Marken in Bewegung', 'Sehen, was in Ihrer <em>Küche steckt.</em>', 'Die Filme unserer Partner zeigen, wie die Küchen und Geräte entstehen und funktionieren.', [
            ('nobilia Werksfilm', 'yt', '1Zc6efEMAqk', 'v-nobilia.jpg'), ('Miele: Faszination Küche', 'yt', 'CwRfzNMcZwY', 'v-miele.jpg'), ('BORA Kochfeldabzug', 'mp4', 'bora.mp4', 'v-bora.jpg')])
        + reviews(s, ['Sehr freundliche und kompetente Beratung, hier wird einem nichts aufgeschwatzt. Beim Angebotsvergleich gehörte das Küchenstudio zu den besten.',
                      'Toller Ausstellungsraum mit riesiger Auswahl und allen Top-Marken. Faire Beratung, und auch nach der Montage ist der Service super.',
                      'Herr Hüdepohl hat sich sehr viel Zeit genommen. Die Beratung war um Welten besser als in den Möbelhäusern, die wir verglichen haben.',
                      'Hervorragende Beratung von Herrn Hüdepohl. Absolut empfehlenswert.'])
        + steps('So einfach geht es', 'In drei Schritten <em>zur neuen Küche.</em>', [('Termin vereinbaren', 'Rufen Sie an unter 05439 902808 oder nutzen Sie das Formular.'), ('Planen', 'Wir planen gemeinsam am Computer und zeigen Ihnen Fronten, Platten und Geräte.'), ('Einziehen', 'Wir liefern, montieren und erklären Ihnen jedes Gerät.')], 'dk')
        + contact(s) + footer(s) + pop(dict(img='p-muster.jpg', ey='Ausstellung wird erneuert', h='Musterküchen zum Abholpreis', p='Ausgewählte Ausstellungsküchen stark reduziert, solange sie da sind.', btn='Jetzt anfragen')))

SITES['bsb'] = dict(
    slug='bersenbruecker-kuechenstudio', firma='Bersenbrücker Küchenstudio', web='kueche-bersenbrueck.de', fonts='r12bsb',
    title='Bersenbrücker Küchenstudio – Küchen in Bersenbrück', desc='Küchenstudio in Bersenbrück seit 1997: 14 Musterküchen auf 400 m², nobilia, Ballerina, Burger, Häcker. Beratung, Planung und Montage aus einer Hand.',
    tel='05439 902808', tel_i='+495439902808', mail='info@kueche-bersenbrueck.de', adresse='Robert-Bosch-Straße 6–8, 49593 Bersenbrück', google=('4,6', 17),
    cta='Beratungstermin vereinbaren', nav=[('Angebote', 'angebote'), ('Leistungen', 'leistungen'), ('Ausstellung', 'ausstellung'), ('Über uns', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:30 – 18:00'), ('Sa', '09:30 – 13:00'), ('', 'sowie nach Vereinbarung')],
    form_opts=['Beratung & Planung', 'Musterküche zum Abholpreis', 'Geräteaustausch', 'Badmöbel', 'Sonstiges'], form_h3='Beratungstermin anfragen', form_p='Wir rufen Sie zurück und finden einen Termin, der Ihnen passt.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns auf <em>Ihren Besuch.</em>', kt_p='Kommen Sie in unsere Ausstellung oder vereinbaren Sie vorab einen Termin.',
    social=[('Facebook', 'https://www.facebook.com/bersenbruecker.kuechenstudio')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Kira', tag='Ihre Küchen-Lotsin', hello='Hallo! Ich bin Kira. Soll ich Ihnen kurz zeigen, was Sie im Bersenbrücker Küchenstudio erwartet?', hi='Hallo! Ich bin Kira vom Bersenbrücker Küchenstudio. Wobei darf ich helfen?',
             qa=[['Welche Marken?', 'nobilia, Ballerina, Burger und Häcker, dazu Geräte von AEG, Bosch, Miele und BORA.'], ['Musterküchen?', 'Ausgewählte Ausstellungsküchen gibt es gerade zum Abholpreis. Rufen Sie an: 05439 902808.'], ['Öffnungszeiten', 'Mo–Fr 9:30–18 Uhr, Sa 9:30–13 Uhr und nach Vereinbarung.']],
             tour=[['#angebote'], ['#leistungen'], ['#ausstellung'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#1d1d1f;--mute:#5b5b60;--p:#D4141A;--a:#D4141A;--a-ink:#fff;--dk:#1d1d1f;--s:#fff;--s2:#f4f2ef;--fh:"Sora",system-ui,sans-serif;--fb:"Inter",system-ui,sans-serif;--r:14px;--r2:20px;--br:999px;--mq-bg:#1d1d1f;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.94);--hd-ink:#1d1d1f;--logo-h:34px;--ft-bg:#141416;--hp-bg:linear-gradient(160deg,#fff 0%,#f4f2ef 60%,#efe9e2 100%)',
    css='''.hp h1,.h2{font-weight:700;letter-spacing:-.025em;line-height:1.04}.hp h1{font-size:clamp(42px,5vw,74px)}.hp h1 em,.h2 em{font-style:normal;color:var(--p)}
.hp .comp .badge{background:#1d1d1f;color:#fff}.hp .comp .badge b{color:#F1D600}
.mq span{font-family:var(--fh);font-weight:600}.promo figure{max-width:440px}
.alt{background:var(--s2)}.ft img{background:#fff;padding:8px 12px;border-radius:10px;height:46px}
.hd .logo img{height:var(--logo-h)}
#team figure{max-width:400px;justify-self:center}
#leistungen .pv figure{aspect-ratio:940/400;height:auto}''',
    img={'logo.png': ('logos/bsb.png', 0), 'h-show.jpg': ('bsb/img/i021.jpg', 0), 'h-kat.jpg': ('bsb/img/i004.jpg', 0, (.25, 0, .75, 1)), 'h-front.jpg': ('bsb/img/i022.jpg', 0),
         'p-muster.jpg': ('bsb/gal/fjordblau_5.jpg', 0), 'team.jpg': ('bsb/img/i028.jpg', 0),
         'l-plan.jpg': ('bsb/img/i003.png', 0), 'l-aufmass.jpg': ('bsb/img/i007.jpg', 0), 'l-montage.jpg': ('bsb/img/i009.jpg', 0), 'l-geraete.jpg': ('bsb/img/i010.png', 0), 'l-bad.jpg': ('bsb/img/i011.png', 0),
         'g1.jpg': ('bsb/gal/grauschiefer_2.jpg', 0), 'g2.jpg': ('bsb/gal/grauschiefer_9.jpg', 0), 'g3.jpg': ('bsb/gal/fjordblau_6.jpg', 0), 'g4.jpg': ('bsb/gal/grauschiefer_3.jpg', 0), 'g7.jpg': ('bsb/gal/grauschiefer_6.jpg', 0), 'g8.jpg': ('bsb/gal/grauschiefer.jpg', 0), 'g5.jpg': ('bsb/gal/fjordblau_1.jpg', 0), 'g6.jpg': ('bsb/gal/grauschiefer_4.jpg', 0),
         'v-nobilia.jpg': ('/home/claude/r12raw/vid/yt-1Zc6efEMAqk.jpg', 1280), 'v-miele.jpg': ('/home/claude/r12raw/vid/yt-CwRfzNMcZwY.jpg', 1280), 'v-bora.jpg': ('/home/claude/r12raw/vid/bora-poster.jpg', 1280), 'bora.mp4': ('/home/claude/r12raw/vid/bora-720.mp4', 0)},
    body=b_bsb)

# ───────────────────────── 2. Küche + Design, Peters + Kuhlmann ─────────────────────────
def b_pk(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='K+D', pos={'h1.jpg': '60% 50%'},
        ey='Küche + Design · Bersenbrück · seit 2014',
        h1='Von Handwerkern geplant. <em>Von Handwerkern gebaut.</em>',
        sub='Alexander Peters berät, Tischlermeister Leon Kuhlmann baut. Ihre Einbauküche aus einer Hand: vom ersten Aufmaß bei Ihnen zu Hause bis zum letzten Handgriff.',
        ubar=[('Wir kommen zu Ihnen', 'Erstberatung bei Ihnen zu Hause'), ('Küche in 3D erleben', 'Mit VR-Brille durch Ihre neue Küche'), ('Ein Ansprechpartner', 'Auch beim kompletten Umbau')]))
        + story('ueber-uns', 'Alexander Peters & Leon Kuhlmann', 'Zwei Handwerker, <em>eine Leidenschaft.</em>', [
            '2014 haben wir uns in Bersenbrück zusammengetan, mit einer klaren Überzeugung: Wer Küchen plant und baut, muss sein Handwerk von Grund auf verstehen.',
            'Alexander Peters ist gelernter Schreiner und berät Sie im Verkauf. Leon Kuhlmann ist Tischlermeister und sorgt mit seinem Montageteam dafür, dass jede Küche millimetergenau sitzt.'],
            'peters.jpg', cap='Alexander Peters, Schreiner und Berater', tl=[('2014', 'Gründung in Bersenbrück'), ('6', 'Köpfe im Team'), ('5,0', 'Sterne aus 84 Google-Bewertungen')])
        + panels('leistungen', 'Unsere Leistungen', 'Alles, was zu <em>Ihrer Küche</em> gehört.', 'Fahren Sie mit der Maus über die Bereiche.', [
            ('Hausbesuch', 'l-haus.jpg', 'Wir kommen zu Ihnen. In Ihrem Raum sehen wir Dinge, die kein Grundriss zeigt: das Licht am Morgen, den Boden, die Atmosphäre.', '50% 50%'),
            ('Küche in 3D', 'l-vr.jpg', 'Mit der VR-Brille gehen Sie durch Ihre neue Küche, bevor sie gebaut ist. So sehen Sie, wie alles wirkt.', '50% 50%'),
            ('Generalumbau', 'l-umbau.jpg', 'Boden, Licht, Wasser, Elektro und Farbe: Wir koordinieren alle Gewerke. Sie haben nur einen Ansprechpartner.', '50% 50%'),
            ('Montage vom Meister', 'l-montage.jpg', 'Unser eigenes Montageteam unter Tischlermeister Leon Kuhlmann baut Ihre Küche sauber und präzise ein.', '50% 50%')], 'dk')
        + scroller('inspiration', 'Kücheninspiration', 'Ideen für <em>Ihre Traumküche.</em>', 'Kompakt, für die Familie oder als Designstück: Einbauküchen für jeden Geschmack und jedes Budget.', [
            ('Wohnküche mit Insel', 'i1.jpg', 'Kochen und Leben in einem Raum, mit viel Platz für alle.', '50% 50%'),
            ('Natürlich warm', 'i2.jpg', 'Holz, Stein und weiche Farben für eine ruhige Atmosphäre.', '50% 50%'),
            ('Designküche', 'i3.jpg', 'Klare Linien, grifflose Fronten und starke Geräte.', '50% 50%'),
            ('Familienküche', 'i4.jpg', 'Stauraum, Ordnung und Arbeitsflächen, die den Alltag leichter machen.', '50% 50%'),
            ('Durchdachte Details', 'i5.jpg', 'Auszüge, Licht und Armaturen, die Sie jeden Tag gern benutzen.', '50% 50%')])
        + team('team', 'Das Team hinter Ihrer Küche', 'Persönlich. Erfahren. <em>Handwerklich stark.</em>', 'Gemeinsam betreuen wir Kundinnen und Kunden von Ankum, Quakenbrück und Bramsche über Osnabrück und Damme bis nach Neuenkirchen, Merzen und Gehrde.', [
            ('t-peters.jpg', 'Alexander Peters', 'Schreiner, Beratung & Verkauf'), ('t-kuhlmann.jpg', 'Leon Kuhlmann', 'Tischlermeister, Montage'), ('t-team.jpg', 'Unser Team', 'Planung & Montage')])
        + steps('Küche kaufen in 10 Schritten', 'Der Weg zu <em>Ihrer neuen Küche.</em>', [('Ihre Wünsche', 'Großfamilie oder Single, Hobbykoch oder Designfan: Erzählen Sie uns, wie Sie leben.'), ('Das Konzept', 'Wir hören zu, messen auf und entwickeln erste Ideen für Ihren Raum.'), ('Planung & Zahlen', 'Farben, Materialien, Geräte und eine klare Kalkulation, alles transparent.'), ('Montage', 'Detail- und Ablaufpläne, dann baut unser Team Ihre Küche millimetergenau ein.')])
        + reviews(s, ['Die Planung in der Software war erstaunlich realistisch. Beratung top, Qualität fantastisch, und die Monteure haben schnell, sauber und professionell gearbeitet.',
                      'Vom Erstgespräch bei uns zu Hause über die Planung im Studio bis zur Montage lief alles reibungslos und genau wie besprochen.',
                      'Man hat sich viel Zeit genommen, auf Details geachtet und gemeinsam mit uns gute Lösungen entwickelt.',
                      'Besonders der Installationsplan für Elektriker und andere Handwerker war hervorragend und hat alles sehr vereinfacht.'])
        + contact(s, 'dk') + footer(s) + pop(dict(img='l-vr.jpg', ey='Neu: Virtual Reality', h='Gehen Sie durch Ihre Küche, bevor sie gebaut ist.', p='Mit der VR-Brille erleben Sie Ihre Planung in 3D, bei uns im Studio.', btn='Termin vereinbaren')))

SITES['pk'] = dict(
    slug='kueche-design-peters-kuhlmann', firma='Küche + Design, Peters + Kuhlmann', web='kuechen-bsb.de', fonts='r12pk',
    title='Küche + Design, Peters + Kuhlmann – Küchenstudio in Bersenbrück', desc='Küchenplanung und Montage aus einer Hand in Bersenbrück: Hausbesuch, Küche in 3D mit VR-Brille, Generalumbau und Montage vom Tischlermeister.',
    tel='05439 6029140', tel_i='+4954396029140', mail='info@kuechen-bsb.de', adresse='Ankumer Straße 19, 49593 Bersenbrück', google=('5,0', 84),
    cta='Beratungstermin vereinbaren', nav=[('Über uns', 'ueber-uns'), ('Leistungen', 'leistungen'), ('Inspiration', 'inspiration'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '10:00 – 17:30'), ('Sa', 'nach Terminvereinbarung')],
    form_opts=['Beratung im Studio', 'Hausbesuch', 'Küche in 3D (VR)', 'Generalumbau', 'Sonstiges'], form_h3='Beratungstermin anfragen', form_p='Kommen Sie vorbei, oder wir kommen zu Ihnen. Wir melden uns zeitnah.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kommen Sie vorbei, <em>oder wir kommen zu Ihnen.</em>', kt_p='Ihre neue Küche beginnt mit einem Gespräch, nicht mit einem Katalog.',
    social=[('Instagram', 'https://www.instagram.com/kueche_design/'), ('Facebook', 'https://www.facebook.com/kuecheunddesign/')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Kalle', tag='Ihr Küchen-Lotse', hello='Hallo! Ich bin Kalle. Soll ich Ihnen zeigen, wie Ihre Küche bei Küche + Design entsteht?', hi='Hallo! Ich bin Kalle von Küche + Design. Wobei darf ich helfen?',
             qa=[['Kommen Sie zu mir?', 'Ja, die Erstberatung kann bei Ihnen zu Hause stattfinden. So sehen wir Ihren Raum, wie er wirklich ist.'], ['Küche in 3D?', 'Mit der VR-Brille gehen Sie im Studio durch Ihre geplante Küche.'], ['Öffnungszeiten', 'Mo–Fr 10–17:30 Uhr, samstags nach Terminvereinbarung.']],
             tour=[['#ueber-uns'], ['#leistungen'], ['#inspiration'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#22222f;--mute:#5d6070;--p:#6FAE22;--a:#7AB929;--a-ink:#141a0a;--dk:#2A2A3D;--s:#fff;--s2:#f3f5ef;--fh:"Outfit",system-ui,sans-serif;--fb:"Karla",system-ui,sans-serif;--r:12px;--r2:18px;--br:10px;--hero-ov:linear-gradient(95deg,rgba(26,26,40,.88) 0%,rgba(26,26,40,.55) 50%,rgba(26,26,40,.1) 100%);--mq-bg:#7AB929;--mq-ink:#141a0a;--hd-bg:rgba(42,42,61,.94);--hd-ink:#fff;--logo-h:52px;--ft-bg:#1e1e2c',
    css='''.hs h1,.h2{font-weight:600;letter-spacing:-.02em;line-height:1.04}.hs h1{font-size:clamp(42px,5.4vw,82px)}.hs h1 em,.h2 em{font-style:normal;color:var(--a)}
.hs .big{-webkit-text-stroke:2px rgba(122,185,41,.35)}
.hd .logo img{background:#fff;padding:6px 10px;border-radius:8px}.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:56px}
.tm .grid figure div{aspect-ratio:3/4}.st figure img{object-position:50% 20%}''',
    img={'logo.png': ('logos/pk.png', 640), 'h1.jpg': ('pk/img/i039.webp', 0), 'h2.jpg': ('pk/img/i020.webp', 0), 'h3.jpg': ('pk/img/i021.webp', 0),
         'peters.jpg': ('pk/img/t-alexander-peters.webp', 900), 't-peters.jpg': ('pk/img/t-alexander-peters.webp', 700), 't-kuhlmann.jpg': ('pk/img/t-leon-kuhlmann.webp', 700), 't-team.jpg': ('pk/img/t-mitarbeiter.webp', 700),
         'l-haus.jpg': ('pk/img/i006.webp', 0), 'l-vr.jpg': ('pk/img/i016.webp', 0), 'l-umbau.jpg': ('pk/img/i018.webp', 1200), 'l-montage.jpg': ('pk/img/i055.webp', 1200),
         'i1.jpg': ('pk/img/i042.webp', 1100), 'i2.jpg': ('pk/img/i052.webp', 1100), 'i3.jpg': ('pk/img/i045.webp', 1100), 'i4.jpg': ('pk/img/i048.webp', 1100), 'i5.jpg': ('pk/img/i054.webp', 1100)},
    body=b_pk)

# ───────────────────────── 3. ORTLAND Küche + Design ─────────────────────────
def b_ortland(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='1960', pos={'h1.jpg': '50% 50%'},
        ey='Ortland Küche + Design · Quakenbrück',
        h1='Küchen einzig<em>ART</em>ig. <em>Made im Artland.</em>',
        sub='Individual-Küchen, die Sie in keinem Katalog finden. Geplant mit der Hand, gebaut von unseren Tischlern, für genau Ihr Leben.',
        ubar=[('Seit 1960', 'Holzhandwerk über Generationen'), ('Ausstellung auf zwei Etagen', 'Materialien und Arbeitshöhen ausprobieren'), ('Fast nur Empfehlungen', 'So kommen unsere Neukunden zu uns')]))
        + story('philosophie', 'Die Ortland-Philosophie', 'So einmalig <em>wie Sie selbst.</em>', [
            'Mit einer Individual-Küche von Ortland bekommen Sie eine hochwertige Küchenwelt mit Charakter. Wir schneiden sie auf Ihre ganz eigene Lebenssituation zu, sozusagen höchst persönlich.',
            'Fast alle unsere Neukunden kommen über eine Weiterempfehlung zu uns. Darauf sind wir stolz.'],
            'team.jpg', cap='Familienbetrieb. Mit Liebe zur Küche.')
        + panels('handwerk', 'Handarbeit von Anfang an', 'Vom ersten Strich <em>bis zur Montage.</em>', 'Bei jeder Ortland-Küche stehen zwei Dinge im Vordergrund: der Mensch und der Raum.', [
            ('Gespräch', 'p-plan.jpg', 'Welche Ansprüche haben Sie? Welchen Stil mögen Sie, natürlich und mediterran oder cool und funktional? Alles beginnt mit einem persönlichen Gespräch.', '50% 50%'),
            ('Entwurf', 'p-skizze.jpg', 'Wir planen mit unseren Händen: Der Vorentwurf beginnt mit dem ersten Strich auf Papier.', '50% 50%'),
            ('Tischlerhandwerk', 'p-tischler.jpg', 'Unsere gelernten Tischler setzen Ihren Küchentraum um. Keine Küche ist wie die andere.', '50% 40%'),
            ('Ausprobieren', 'p-ausst.jpg', 'Welche Arbeitshöhe passt? Welche Front fühlt sich gut an? In unserer Ausstellung erfahren Sie es wortwörtlich.', '50% 50%')], 'dk')
        + gallery('referenzen', 'Referenzen', 'So schön <em>kann Küche sein.</em>', [
            ('r1.jpg', 'w2 h2r', '50% 50%'), ('r2.jpg', '', '50% 50%'), ('r3.jpg', '', '50% 50%'), ('r4.jpg', '', '50% 50%'), ('r5.jpg', '', '50% 50%')])
        + story('geschichte', 'Holzhandwerk seit Generationen', 'Die Liebe zum Holz <em>liegt uns in den Genen.</em>', [
            'Schon im 19. Jahrhundert kauft Tischlermeister Heinrich Ortland ein Grundstück an der St. Annenstraße 12. Nach dem 1. Weltkrieg führen seine Söhne den Betrieb als Gebrüder Ortland Bau- und Möbeltischlerei.',
            'Willi Ortland, Tischlermeister und Innenarchitekt, macht sich 1960 mit seiner Frau Hildegard selbstständig. Seit 1972 ist die Küchenausstellung an der St. Annenstraße zu Hause.'],
            'alt.jpg', cap='Die St. Annenstraße in Quakenbrück, damals', tl=[('19. Jh.', 'Heinrich Ortland kauft die St. Annenstraße 12'), ('1960', 'Gründung der Möbeltischlerei'), ('1972', 'Küchenausstellung an der St. Annenstraße'), ('Heute', 'Familienbetrieb mit eigenem Team')], rev=True)
        + reviews(s, ['Sehr freundliches Personal, exzellente Beratung und viele Musterküchen, um sich Ideen zu holen.',
                      'Ich kann Ortland Küchen uneingeschränkt empfehlen. Das Preis-Leistungs-Verhältnis ist hervorragend.',
                      'Alle Vorschläge und Lösungen wurden umgesetzt, sie waren schnell vor Ort. Jederzeit gern wieder.',
                      'Hier trifft man auf Kompetenz und Qualität, und die Beratung ist unglaublich kreativ und flexibel.'], 'alt')
        + contact(s) + footer(s) + pop(dict(img='kaffee.jpg', ey='Einladung', h='Einen Kaffee bekommen Sie bei uns auch.', p='Nehmen Sie sich Zeit für Ihre Küche. Wir nehmen sie uns für Sie.', btn='Beratungstermin vereinbaren')))

SITES['ortland'] = dict(
    slug='ortland-kueche-design-quakenbrueck', firma='ORTLAND Küche + Design', web='ortland-kuechen.de', fonts='r12ortland',
    title='ORTLAND Küche + Design – Individual-Küchen in Quakenbrück', desc='Ortland Küche + Design in Quakenbrück: Individual-Küchen aus echtem Tischlerhandwerk, Familienbetrieb seit 1960, Ausstellung auf zwei Etagen.',
    tel='05431 3541', tel_i='+4954313541', mail='info@ortland-kuechen.de', adresse='St. Annenstraße 12, 49610 Quakenbrück', google=('4,8', 18),
    cta='Beratungstermin vereinbaren', nav=[('Philosophie', 'philosophie'), ('Handwerk', 'handwerk'), ('Referenzen', 'referenzen'), ('Geschichte', 'geschichte'), ('Kontakt', 'kontakt')],
    hours=[('Beratung', 'nach Terminvereinbarung'), ('Telefon', '05431 3541')],
    form_opts=['Beratung & Planung', 'Ausstellung besuchen', 'Umbau / Modernisierung', 'Sonstiges'], form_h3='Beratungstermin anfragen', form_p='Wir nehmen uns Zeit für Sie und melden uns persönlich.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir nehmen uns <em>Zeit für Sie.</em>', kt_p='Rufen Sie an, schreiben Sie uns oder besuchen Sie unsere Ausstellung in Quakenbrück.',
    social=[('Instagram', 'https://www.instagram.com/ortlandkuechen/'), ('Facebook', 'https://www.facebook.com/profile.php?id=61555694387612')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Ole', tag='Ihr Küchen-Lotse', hello='Hallo! Ich bin Ole. Soll ich Ihnen zeigen, wie eine Ortland-Küche entsteht?', hi='Hallo! Ich bin Ole von Ortland Küche + Design. Wobei darf ich helfen?',
             qa=[['Was ist eine Individual-Küche?', 'Eine Küche, die auf Ihre Lebenssituation zugeschnitten ist und von unseren Tischlern umgesetzt wird.'], ['Ausstellung?', 'Unsere Ausstellung in Quakenbrück zeigt auf zwei Etagen vom Landhausstil bis zur modernen Küche.'], ['Kontakt', 'Telefon 05431 3541 oder info@ortland-kuechen.de']],
             tour=[['#philosophie'], ['#handwerk'], ['#referenzen'], ['#kontakt']]),
    vars='--bg:#fbf9f6;--ink:#2b2a28;--mute:#62605b;--p:#A23A2C;--a:#A23A2C;--a-ink:#fff;--dk:#2f2e2c;--s:#fff;--s2:#f1ece5;--fh:"Josefin Sans",system-ui,sans-serif;--fb:"Lora",Georgia,serif;--r:4px;--r2:6px;--br:2px;--hero-ov:linear-gradient(90deg,rgba(28,27,25,.85) 0%,rgba(28,27,25,.45) 55%,rgba(28,27,25,.05) 100%);--mq-bg:#2f2e2c;--mq-ink:#f1ece5;--hd-bg:rgba(251,249,246,.95);--hd-ink:#2b2a28;--logo-h:58px;--ft-bg:#232220',
    css='''.hs h1,.h2{font-weight:300;text-transform:uppercase;letter-spacing:.04em;line-height:1.05}.hs h1{font-size:clamp(40px,5.2vw,80px)}.hs h1 em,.h2 em{font-style:normal;font-weight:600;color:#d9806f}.h2 em{color:var(--p)}
.ey{font-family:var(--fh);letter-spacing:.2em}.btn{font-family:var(--fh);text-transform:uppercase;letter-spacing:.12em;font-weight:600}
.alt{background:var(--s2)}.ft img{filter:brightness(0) invert(1)}.st figure img{filter:sepia(.15)}
.hd.lt:not(.scr) .logo img{filter:brightness(0) invert(1)}
@media(max-width:600px){.btn{letter-spacing:.06em;font-size:14px}}''',
    img={'logo.png': ('logos/ortland.png', 700), 'h1.jpg': ('ortland/img/i046.png', 0), 'h2.jpg': ('ortland/img/i048.png', 0), 'h3.jpg': ('ortland/img/i043.png', 0),
         'team.jpg': ('ortland/img/i059.jpg', 0), 'p-plan.jpg': ('ortland/img/i056.jpg', 0), 'p-skizze.jpg': ('ortland/img/i044.png', 1200), 'p-tischler.jpg': ('ortland/img/i045.png', 1200), 'p-ausst.jpg': ('ortland/img/i041.png', 1200),
         'r1.jpg': ('ortland/img/i047.png', 1400), 'r2.jpg': ('ortland/img/i028.jpg', 0), 'r3.jpg': ('ortland/img/i034.jpg', 0), 'r4.jpg': ('ortland/img/i035.jpg', 0), 'r5.jpg': ('ortland/img/i057.jpg', 0),
         'alt.jpg': ('ortland/img/i051.jpeg', 0), 'kaffee.jpg': ('ortland/img/i060.jpg', 0)},
    body=b_ortland)

# ───────────────────────── 4. TS-Möbel Design (Thomas Steinkamp) ─────────────────────────
def b_ts(s):
    return (hd(s) + hero_comp(s, dict(
        imgs=['h-kueche.jpg', 'h-muster.jpg', 'h-haus.jpg'], pos0='50% 50%',
        ey='Tischlerei & Küchenstudio · Alfhausen',
        h1='Wohnkultur <em>&amp; Lebensart.</em>',
        sub='Tradition und Technik im modernen Handwerksbetrieb. Wir nehmen Maß bei Ihnen, entwickeln mit Ihnen Ideen und fertigen Küchen und Möbel, die genau passen.',
        badge=('Seit 2000', 'Tischlerei, seit 2008 mit Küchenstudio')))
        + marquee(['Küchen', 'Wohnzimmer', 'Schlafzimmer', 'Esszimmer', 'Badmöbel', 'Ladeneinrichtungen', 'Einzelstücke'])
        + duo('welten', 'Zwei Werkstätten, ein Anspruch', 'Beratung, Planung und <em>Fertigung aus einer Hand.</em>', 'Ob neue Küche oder Möbel nach Maß: Bei uns bekommen Sie beides vom selben Team.', [
            ('Küchenstudio', 'Küchen', 'w-kueche.jpg', 'Musterküchen in vielen Stilen, vom warmen Holz bis zur grifflosen Designküche. Wir planen sie in Ihren Raum und bauen sie selbst ein.', ['Planung vor Ort', 'Eigene Montage', 'Viele Fronten zur Auswahl'], 'Küche planen'),
            ('Tischlerei', 'Möbel nach Maß', 'w-moebel.jpg', 'Wohnzimmer, Schlafzimmer, Bad und Einzelstücke aus hochwertigen Hölzern, gefertigt mit modernen Maschinen in Alfhausen.', ['Hochwertige Hölzer', 'Maß vor Ort', 'Ladeneinrichtungen'], 'Möbel anfragen')])
        + gallery('galerie', 'Küchengalerie', 'Lassen Sie sich <em>inspirieren.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')])
        + story('ueber-uns', 'Über uns', 'Zuverlässig und pünktlich. <em>Ganz selbstverständlich.</em>', [
            'Die Tischlerei TS-Möbel Design wurde im Jahr 2000 gegründet. Mit modernen Maschinen und einem gut ausgebildeten Team fertigen wir Qualitätsmöbel nach Ihren Wünschen.',
            'Wir verwenden ausschließlich hochwertige Hölzer und achten auch bei allen anderen Werkstoffen auf Qualität und Langlebigkeit.'],
            'werkstatt.jpg', cap='Muster und Materialien in unserer Ausstellung', tl=[('2000', 'Gründung der Tischlerei'), ('2008', 'Eröffnung des Küchenstudios'), ('Heute', 'Küchen und Möbel aus Alfhausen')], rev=True)
        + reviews(s, ['Wir haben fast alles bei Thomas maßanfertigen lassen: Küche, Wohnzimmer, Hauswirtschaftsraum und Bäder. Preise und Qualität sind unschlagbar, und er hat immer eine gute Idee.',
                      'Unsere Küche wurde bis nach Leipzig geliefert und in zwei Tagen montiert. Freundlich, zuverlässig und in hervorragender Qualität.'], 'alt')
        + steps('So arbeiten wir', 'Von der Idee <em>zum fertigen Möbel.</em>', [('Maß nehmen', 'Wir kommen zu Ihnen und nehmen alles vor Ort auf.'), ('Ideen & Material', 'Gemeinsam entwickeln wir Ideen und wählen die passenden Materialien.'), ('Fertigung & Montage', 'Wir fertigen in Alfhausen und bauen pünktlich bei Ihnen ein.')], 'dk')
        + contact(s) + footer(s))

SITES['ts'] = dict(
    slug='ts-moebel-design-alfhausen', firma='Tischlerei TS-Möbel Design & Küchenstudio', web='ts-möbel-design.de', fonts='r12ts',
    title='TS-Möbel Design – Tischlerei & Küchenstudio in Alfhausen', desc='Tischlerei und Küchenstudio in Alfhausen: Küchen, Möbel nach Maß und Einzelstücke aus hochwertigen Hölzern. Beratung, Planung und Fertigung aus einer Hand.',
    tel='05464 1539', tel_i='+4954641539', mail='info@ts-moebel-design.de', adresse='Bahnhofstraße 5a, 49594 Alfhausen', google=('4,8', 6),
    cta='Beratung anfragen', nav=[('Küche & Möbel', 'welten'), ('Galerie', 'galerie'), ('Über uns', 'ueber-uns'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '07:00 – 12:00 · 13:00 – 16:30'), ('Fr', '07:00 – 13:30')],
    form_opts=['Neue Küche', 'Möbel nach Maß', 'Badmöbel', 'Ladeneinrichtung', 'Sonstiges'], form_h3='Beratung anfragen', form_p='Wir rufen Sie zurück und vereinbaren einen Termin vor Ort.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir setzen Ihre Ideen <em>in die Wirklichkeit um.</em>', kt_p='Rufen Sie an oder schreiben Sie uns, gern auch mit Fotos oder Maßen Ihres Raumes.',
    social=[], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Tom', tag='Ihr Werkstatt-Lotse', hello='Hallo! Ich bin Tom. Soll ich Ihnen kurz zeigen, was TS-Möbel Design für Sie fertigt?', hi='Hallo! Ich bin Tom von TS-Möbel Design. Wobei darf ich helfen?',
             qa=[['Was fertigen Sie?', 'Küchen, Wohn-, Schlaf- und Esszimmer, Badmöbel, Ladeneinrichtungen und Einzelstücke.'], ['Kommen Sie zu mir?', 'Ja, wir nehmen Maß vor Ort und beraten Sie zu den Materialien.'], ['Öffnungszeiten', 'Mo–Do 7–12 und 13–16:30 Uhr, Fr 7–13:30 Uhr.']],
             tour=[['#welten'], ['#galerie'], ['#ueber-uns'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#16213a;--mute:#555c6b;--p:#C8202F;--a:#C8202F;--a-ink:#fff;--dk:#16213a;--s:#fff;--s2:#f3f1ec;--fh:"Vidaloka",Georgia,serif;--fb:"Mulish",system-ui,sans-serif;--r:8px;--r2:14px;--br:6px;--mq-bg:#16213a;--mq-ink:#f3f1ec;--hd-bg:rgba(22,33,58,.96);--hd-ink:#fff;--logo-h:60px;--ft-bg:#0f1729;--hp-bg:linear-gradient(170deg,#f6f3ee 0%,#fff 55%)',
    css='''.hp h1,.h2{font-weight:400;letter-spacing:-.005em;line-height:1.05}.hp h1{font-size:clamp(46px,5.6vw,86px)}.hp h1 em,.h2 em{font-style:normal;color:var(--p)}
.mq span{font-family:var(--fh)}.alt{background:var(--s2)}.hp .comp .badge{background:var(--dk);color:#fff}
.hd{background:var(--hd-bg);color:#fff}''',
    img={'logo.png': ('logos/ts.png', 520, 'alphacrop'), 'h-kueche.jpg': ('ts/img/i099.jpg', 0), 'h-muster.jpg': ('ts/img/i090.jpg', 1100), 'h-haus.jpg': ('ts/img/i096.jpg', 900),
         'w-kueche.jpg': ('ts/img/i089.jpg', 0), 'w-moebel.jpg': ('ts/img/i104.jpg', 1200), 'werkstatt.jpg': ('ts/img/i091.jpg', 1200),
         'g1.jpg': ('ts/img/i062.jpg', 0), 'g2.jpg': ('ts/img/i100.jpg', 0), 'g3.jpg': ('ts/img/i086.jpg', 0), 'g4.jpg': ('ts/img/i045.jpg', 0), 'g5.jpg': ('ts/img/i070.jpg', 0), 'g6.jpg': ('ts/img/i033.jpg', 0)},
    body=b_ts)

# ───────────────────────── 5. Tischlerei Beckermann ─────────────────────────
def b_beckermann(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg'], big='HOLZ', pos={'h1.jpg': '50% 60%'},
        ey='beckermann · Wohnen mit Holz · Niedersachsenpark',
        h1='Wer selbst kocht, <em>plant die bessere Küche.</em>',
        sub='Küchen, Massivholzmöbel und Raumlösungen aus der eigenen Tischlerei in Neuenkirchen-Vörden. Geplant von Köchen und Tischlern, gefertigt nach Ihren Maßen.',
        ubar=[('Seit über 30 Jahren', 'Hochwertige, überwiegend massive Möbel'), ('Showroom im Niedersachsenpark', 'Möbel, Küchen, Betten und Böden'), ('Rundum-Service', 'Von der Beratung bis zur Montage')]))
        + story('chef', 'Kochen aus Leidenschaft', 'Der Chef <em>versteht sein Handwerk.</em>', [
            'Vincenz Beckermann ist Unternehmensgründer und leidenschaftlicher Koch. Seit 2022 führt Tischlermeister Frederick Sommerei den Betrieb und setzt die Beckermann-Tradition fort.',
            'Unser Leitsatz: „Wer selbst kocht, weiß, wie eine Küche ausgestattet sein muss.“ Deshalb steht bei uns immer ein ausführliches Vorgespräch am Anfang, denn jede Küche wird im Detail auf ihre Nutzer abgestimmt.'],
            'chef.jpg', cap='Vincenz Beckermann, Projektleitung und Kundenberatung', tl=[('30+', 'Jahre hochwertige Massivholzmöbel'), ('2022', 'Frederick Sommerei übernimmt'), ('Heute', 'Showroom im Niedersachsenpark')])
        + tabs('kuechen', 'Die Küche, das Herz des Hauses', 'Küchen mit <em>vielen Gesichtern.</em>', 'Von klassisch bis modern: Bei Beckermann ist für jeden Geschmack etwas dabei.', [
            ('Massivholzküchen', 'k-massiv.jpg', 'Echtes Holz aus der eigenen Fertigung: warm, langlebig und mit Charakter.', ['Eigene Tischlerei', 'Nach Maß']),
            ('Designküchen', 'k-design.jpg', 'Klare Linien, edle Oberflächen und starke Geräte von BORA, Miele und Quooker.', ['BORA', 'Miele', 'Quooker']),
            ('Landhausküchen', 'k-land.jpg', 'Gemütlich und zeitlos, mit Kassettenfronten und viel Stauraum.', ['Zeitlos', 'Viel Stauraum']),
            ('Ausstattung', 'k-aus.jpg', 'Damit auch Extrembelastungen kein Problem sind, statten wir jede Küche hochwertig aus.', ['Hochwertige Auszüge', 'Durchdachte Innenaufteilung'])])
        + duo('wohnen', 'Mehr als Küche', 'Schlafen, wohnen, <em>wohlfühlen.</em>', 'In unserem Showroom finden Sie auch Betten, Wohnmöbel, Böden und Türen, alles mit dem gleichen Anspruch.', [
            ('Schlafen', 'Betten & RELAX Bettsysteme', 'w-schlafen.jpg', 'Schlafkomfort aus Massivholz, dazu die RELAX Bettsysteme unserer Partner.', ['Massivholzbetten', 'RELAX Bettsysteme'], 'Beraten lassen'),
            ('Wohnen', 'Einrichten & Möbelbau', 'w-wohnen.jpg', 'Einzelmöbel oder komplette Raumlösungen für Wohnen und Arbeiten, mit Raumplus-Schranksystemen, Sitzmöbeln, Tischen und Böden.', ['Möbelbau', 'Raumplus', 'Fußböden & Türen'], 'Termin vereinbaren')], 'alt')
        + gallery('showroom', 'Showroom im Niedersachsenpark', 'Sich informieren <em>und alles ausprobieren.</em>', [
            ('s1.jpg', 'w2 h2r', '50% 50%'), ('s2.jpg', '', '50% 50%'), ('s3.jpg', '', '50% 50%'), ('s4.jpg', '', '50% 50%'), ('s5.jpg', '', '50% 50%')])
        + reviews(s, ['Von der ersten Beratung bis zur Planung fühlten wir uns bestens aufgehoben. Sehr persönlich, und alle Wünsche wurden möglich gemacht.',
                      'Küche, Hauswirtschaftsraum und Schiebetür: Alles lief reibungslos, und eine Reklamation wurde schnell und kundenfreundlich gelöst.',
                      'Im Showroom wurden uns die Vor- und Nachteile von Materialien und Geräten geduldig erklärt, sogar mit ersten Skizzen.',
                      'Hervorragende Qualität, sehr gute Beratung und zuverlässiger Service.'])
        + steps('Unser Arbeitsprozess', 'So entsteht <em>Ihre Einrichtung.</em>', [('Vorgespräch', 'Wir hören zu und lernen, wie Sie leben und kochen.'), ('Entwurf', 'Wir zeichnen und planen bis ins Detail.'), ('Fertigung & Montage', 'Aus der eigenen Werkstatt, fachgerecht bei Ihnen montiert.')], 'dk')
        + contact(s) + footer(s) + pop(dict(img='s2.jpg', ey='Rabatt-Aktionen', h='Ausstellungsmöbel mit attraktiven Rabatten', p='Wir bieten immer wieder Einzelmöbel aus Sonderaktionen an. Sprechen Sie uns an.', btn='Jetzt anfragen')))

SITES['beckermann'] = dict(
    slug='tischlerei-beckermann', firma='Tischlerei Beckermann', web='tischlerei-beckermann.de', fonts='r12beckermann',
    title='beckermann Wohnen mit Holz – Küchen & Möbel in Neuenkirchen-Vörden', desc='Tischlerei Beckermann im Niedersachsenpark: Küchen, Massivholzmöbel, Betten und Raumlösungen aus eigener Fertigung. Showroom in Neuenkirchen-Vörden.',
    tel='05493 992466', tel_i='+495493992466', mail='info@tischlerei-beckermann.de', adresse='Braunschweiger Straße 3, 49434 Neuenkirchen-Vörden', google=('4,8', 6),
    cta='Beratungstermin vereinbaren', nav=[('Über uns', 'chef'), ('Küchen', 'kuechen'), ('Wohnen', 'wohnen'), ('Showroom', 'showroom'), ('Kontakt', 'kontakt')],
    hours=[('Mo, Di, Do', '08:00 – 12:30 · 13:00 – 17:00'), ('Mi, Fr', '08:00 – 14:00'), ('Sa', 'Termine nach Vereinbarung')],
    form_opts=['Neue Küche', 'Möbel nach Maß', 'Betten & Schlafsysteme', 'Showroom-Besuch', 'Sonstiges'], form_h3='Beratungstermin anfragen', form_p='Wir melden uns persönlich und nehmen uns Zeit für Ihr Vorgespräch.', form_btn='Rückruf anfordern',
    kt_ey='Besuchen Sie uns', kt_h2='Büro und Showroom <em>im Niedersachsenpark.</em>', kt_p='Kommen Sie vorbei oder rufen Sie an, samstags gern nach Vereinbarung.',
    social=[('Instagram', 'https://www.instagram.com/tischlerei_beckermann/')], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Benno', tag='Ihr Holz-Lotse', hello='Hallo! Ich bin Benno. Soll ich Ihnen zeigen, was Sie bei beckermann erwartet?', hi='Hallo! Ich bin Benno von beckermann Wohnen mit Holz. Wobei darf ich helfen?',
             qa=[['Was bieten Sie?', 'Küchen, Massivholzmöbel, Betten, Raumlösungen, Böden und Türen, aus eigener Fertigung.'], ['Wo ist der Showroom?', 'Braunschweiger Straße 3 im Niedersachsenpark, 49434 Neuenkirchen-Vörden.'], ['Öffnungszeiten', 'Mo, Di, Do 8–12:30 und 13–17 Uhr, Mi und Fr 8–14 Uhr, samstags nach Vereinbarung.']],
             tour=[['#chef'], ['#kuechen'], ['#showroom'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#26231d;--mute:#5f5a52;--p:#E8790C;--a:#F08A00;--a-ink:#1d1708;--dk:#26231d;--s:#fff;--s2:#f6f2ec;--fh:"Fira Sans",system-ui,sans-serif;--fb:"Fira Sans",system-ui,sans-serif;--r:10px;--r2:16px;--br:8px;--hero-ov:linear-gradient(100deg,rgba(30,26,20,.88) 0%,rgba(30,26,20,.5) 52%,rgba(30,26,20,.08) 100%);--mq-bg:#F08A00;--mq-ink:#1d1708;--hd-bg:rgba(255,255,255,.96);--hd-ink:#26231d;--logo-h:50px;--ft-bg:#1d1a15',
    css='''.hs h1,.h2{font-weight:300;letter-spacing:-.015em;line-height:1.05}.hs h1{font-size:clamp(42px,5.4vw,82px)}.hs h1 em,.h2 em{font-style:normal;font-weight:600;color:var(--a)}
.hs .big{-webkit-text-stroke:2px rgba(240,138,0,.35)}#chef figure{max-width:400px;justify-self:center}.hd .logo img{background:#fff;padding:5px 10px;border-radius:8px}.alt{background:var(--s2)}.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:54px}''',
    img={'logo.png': ('logos/beckermann.png', 0), 'h1.jpg': ('beckermann/img/i009.jpg', 0), 'h2.jpg': ('beckermann/img/i040.jpg', 0), 
         'chef.jpg': ('beckermann/img/i034.jpg', 0), 'k-massiv.jpg': ('beckermann/img/i016.jpg', 0), 'k-design.jpg': ('beckermann/img/i027.jpg', 0), 'k-land.jpg': ('beckermann/img/i028.jpg', 0), 'k-aus.jpg': ('beckermann/img/i011.jpg', 0),
         'w-schlafen.jpg': ('beckermann/img/i032.jpg', 0), 'w-wohnen.jpg': ('beckermann/img/i025.jpg', 0),
         's1.jpg': ('beckermann/img/i021.jpg', 0), 's2.jpg': ('beckermann/img/i013.jpg', 0), 's3.jpg': ('beckermann/img/i029.jpg', 0), 's4.jpg': ('beckermann/img/i036.jpg', 0), 's5.jpg': ('beckermann/img/i058.jpg', 0)},
    body=b_beckermann)

# ───────────────────────── 6. Meyer Möbelwerkstätten ─────────────────────────
def raum(id, ey, h2, lead, items):
    c = ''.join(f'<article><figure><img src="img/{i}" alt="{t}" loading="lazy"></figure><h3>{t}</h3><p>{x}</p></article>' for t, i, x in items)
    return f'<section class="sec rl dk" id="{id}"><div class="w"><div data-r><p class="ey">{ey}</p><h2 class="h2">{h2}</h2><p class="lead">{lead}</p></div><div class="rg" data-r="2">{c}</div></div></section>'

def b_meyer(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='EICHE', pos={'h1.jpg': '50% 50%'},
        ey='Meyer Möbelwerkstätten · Eggermühlen',
        h1='Mehr als <em>eine Küche.</em>',
        sub='Individuelle Küchen, Möbelunikate und Raumlösungen aus eigener Fertigung. Nachhaltig gebaut, mit Holz aus heimischen Wäldern.',
        ubar=[('1.000 m² Ausstellung', 'Küchen und Massivholzmöbel in allen Stilen'), ('Holz aus 70 km Umkreis', 'Eiche, Buche, Ahorn, Erle, Kirsche'), ('Sonntags Schautag', '14 bis 18 Uhr, ohne Verkauf')]))
        + story('holz', 'Wir & Holz', 'Eine gute <em>Verbindung.</em>', [
            'Aus den Wäldern im Umkreis von etwa 70 km um Eggermühlen beziehen wir unser Holz, hauptsächlich Eiche. Mit Unterstützung des Försters wählen wir die Stämme sorgfältig aus.',
            'In unserer Tischlerei bereiten wir das Holz mit viel Liebe auf und fertigen daraus millimetergenaue, langlebige Möbel und Küchen für Ihren Stil.'],
            'tischler.jpg', cap='Eigene Fertigung in Eggermühlen', tl=[('70 km', 'Holz aus heimischen Wäldern'), ('2.', 'Generation Familienbetrieb'), ('1.000 m²', 'Ausstellung')])
        + tabs('kuechen', 'Tischlerküchen', 'Ihre Küche, <em>passend gebaut.</em>', 'Mit eigener Fertigung, computergestützter Planung und Leidenschaft für Küchen planen wir Ihren ganzen Wohn- und Essbereich.', [
            ('Tischlerküche', 'k1.jpg', 'Küchenschränke passend für Ihre Raumform und Ihre Arbeitsweise, gefertigt in unserer Werkstatt.', ['Eigene Fertigung', 'CAD-3D-Planung']),
            ('Essbereich', 'k2.jpg', 'Wir sehen die Küche als Lebensraum und planen Essbereiche zum Wohlfühlen gleich mit.', ['Tische & Bänke', 'Aus einer Hand']),
            ('Geräte', 'k3.jpg', 'Kochen, backen, dampfen, spülen: mit unseren Partnern BORA, Siemens, Miele und berbel immer auf dem neuesten Stand.', ['BORA', 'Siemens', 'Miele', 'berbel']),
            ('Stauraum', 'k4.jpg', 'Durchdachte Auszüge und Innenaufteilungen, damit alles seinen Platz hat.', ['Mm-genau gefertigt'])])
        + raum('raumloesungen', 'Raumlösungen & Möbelunikate', 'Für jede <em>Raumsituation.</em>', 'Dachschrägen, Drempel, begehbare Kleiderschränke oder Stauraum unter der Treppe: Wir finden die Lösung.', [
            ('Wohnen', 'r1.jpg', 'Wohnmöbel aus Massivholz, die zu Ihrem Stil passen und lange halten.'),
            ('Essen', 'r2.jpg', 'Massive Tische und Stühle für den Mittelpunkt Ihres Hauses.'),
            ('Schlafen', 'r3.jpg', 'Betten und Schränke aus heimischem Holz, auf Maß gebaut.'),
            ('Unikate', 'r4.jpg', 'Formvollendete Einzelstücke in unterschiedlichsten Stilrichtungen.')])
        + gallery('showroom', 'Showroom in Eggermühlen', 'Sehen. Fühlen. <em>Erleben.</em>', [
            ('s1.jpg', 'w2 h2r', '50% 50%'), ('s2.jpg', '', '50% 50%'), ('s3.jpg', '', '50% 50%'), ('s4.jpg', '', '50% 50%'), ('s5.jpg', '', '50% 50%')])
        + reviews(s, ['Wir haben schon mehrfach Möbel bestellt und waren mit Planung und Montage immer sehr zufrieden.',
                      'Küche und Zweitküche sind täglich in Benutzung und funktionieren perfekt. Herr Meyer hat uns hervorragend beraten.',
                      'Unsere maßgefertigte Küche sieht fantastisch aus. Toller Preis, saubere und hochwertige Verarbeitung.',
                      'Top Qualität, hervorragende Beratung, alle Wünsche wurden berücksichtigt. Note: 1.'], 'alt')
        + steps('Planung & Montage aus einer Hand', 'So entsteht <em>Ihr Möbel.</em>', [('Beratung zu Hause', 'Persönliche Beratung mit Stil- und Bedarfsanalyse in Ihren eigenen vier Wänden.'), ('3D-Planung', 'Schon vor der Fertigung sehen Sie alles maßstabsgetreu in 3D.'), ('Fertigung & Aufbau', 'Mm-genau gefertigt und von unserem Team fachgerecht aufgebaut.')])
        + contact(s, 'dk') + footer(s) + pop(dict(img='s1.jpg', ey='Sonntags Schautag', h='1.000 m² Ausstellung, sonntags von 14 bis 18 Uhr', p='In Ruhe schauen, ganz ohne Verkauf. Beratung gern unter der Woche.', btn='Beratung vereinbaren')))

SITES['meyer'] = dict(
    slug='meyer-moebelwerkstaetten-eggermuehlen', firma='Meyer Möbelwerkstätten', web='meyer-moebel.de', fonts='r12meyer',
    title='Meyer Möbelwerkstätten – Küchen & Massivholzmöbel in Eggermühlen', desc='Meyer Möbelwerkstätten in Eggermühlen: individuelle Tischlerküchen, Möbelunikate und Raumlösungen aus heimischem Holz. 1.000 m² Ausstellung.',
    tel='05462 504', tel_i='+495462504', mail='info@meyer-moebel.de', adresse='Am Cordtskamp 1, 49577 Eggermühlen', google=('5,0', 12),
    cta='Beratungstermin vereinbaren', nav=[('Holz', 'holz'), ('Küchen', 'kuechen'), ('Raumlösungen', 'raumloesungen'), ('Showroom', 'showroom'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 12:30 · 14:00 – 18:00'), ('Sa', '08:00 – 13:00'), ('So', 'Schautag 14:00 – 18:00 (kein Verkauf)')],
    form_opts=['Tischlerküche', 'Raumlösung', 'Möbelunikat', 'Beratung zu Hause', 'Sonstiges'], form_h3='Beratungstermin anfragen', form_p='Ansprechpartner: Carl Meyer und Udo Lömker. Wir melden uns persönlich.', form_btn='Rückruf anfordern',
    kt_ey='Besuchen Sie uns', kt_h2='Wir zeigen Ihnen <em>live, was wir können.</em>', kt_p='Besuchen Sie uns in Eggermühlen oder vereinbaren Sie gleich einen Beratungstermin.',
    social=[], rv_h2='Das sagen unsere <em>Kunden.</em>',
    bot=dict(name='Mats', tag='Ihr Werkstatt-Lotse', hello='Hallo! Ich bin Mats. Soll ich Ihnen zeigen, was die Meyer Möbelwerkstätten für Sie bauen?', hi='Hallo! Ich bin Mats von den Meyer Möbelwerkstätten. Wobei darf ich helfen?',
             qa=[['Woher kommt das Holz?', 'Aus den Wäldern im Umkreis von etwa 70 km um Eggermühlen, vor allem Eiche.'], ['Sonntags geöffnet?', 'Sonntags ist von 14 bis 18 Uhr Schautag, ohne Verkauf.'], ['Öffnungszeiten', 'Mo–Fr 8–12:30 und 14–18 Uhr, Sa 8–13 Uhr.']],
             tour=[['#holz'], ['#kuechen'], ['#showroom'], ['#kontakt']]),
    vars='--bg:#fff;--ink:#2a2826;--mute:#615d59;--p:#8A6A43;--a:#A67C4E;--a-ink:#fff;--dk:#3a3633;--s:#fff;--s2:#f4f1ec;--fh:"Montserrat",system-ui,sans-serif;--fb:"Source Serif 4",Georgia,serif;--r:2px;--r2:4px;--br:0px;--hero-ov:linear-gradient(90deg,rgba(32,30,28,.85) 0%,rgba(32,30,28,.45) 55%,rgba(32,30,28,.05) 100%);--mq-bg:#3a3633;--mq-ink:#f4f1ec;--hd-bg:rgba(255,255,255,.96);--hd-ink:#3a3633;--logo-h:40px;--ft-bg:#2a2826',
    css='''.hs h1,.h2{font-weight:300;text-transform:uppercase;letter-spacing:.08em;line-height:1.08}.hs h1{font-size:clamp(40px,5vw,78px)}.hs h1 em,.h2 em{font-style:normal;font-weight:600;color:#d8b48a}.h2 em{color:var(--p)}
.ey,.btn{letter-spacing:.18em;text-transform:uppercase}
.hd.lt:not(.scr) .logo img{filter:brightness(0) invert(1)}
@media(max-width:600px){.btn{letter-spacing:.06em;font-size:14px}}
.rl .rg{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:40px}.rl figure{margin:0;aspect-ratio:4/3;overflow:hidden;max-width:300px}.rl figure img{width:100%;height:100%;object-fit:cover}.rl h3{font-family:var(--fh);font-weight:600;text-transform:uppercase;letter-spacing:.12em;font-size:17px;margin:16px 0 6px}.rl p{font-size:17px;line-height:1.55;opacity:.85}
@media(max-width:800px){.rl .rg{grid-template-columns:1fr 1fr;gap:16px}.rl p{font-size:16px}}.alt{background:var(--s2)}.ft img{filter:brightness(0) invert(1)}''',
    img={'logo.png': ('logos/meyer.png', 0), 'h1.jpg': ('meyer/img/i002.jpg', 2200), 'h2.jpg': ('meyer/img/i120.jpg', 0), 'h3.jpg': ('meyer/img/i042.jpg', 0),
         'tischler.jpg': ('meyer/img/i009.jpg', 0), 'k1.jpg': ('meyer/img/i040.jpg', 1200), 'k2.jpg': ('meyer/img/i107.jpg', 0), 'k3.jpg': ('meyer/img/i036.jpeg', 1200), 'k4.jpg': ('meyer/img/i064.jpg', 1200),
         'r1.jpg': ('meyer/img/i123.jpg', 0), 'r2.jpg': ('meyer/img/i048.jpg', 0), 'r3.jpg': ('meyer/img/i053.jpg', 0), 'r4.jpg': ('meyer/img/i122.jpg', 0),
         's1.jpg': ('meyer/img/i012.jpg', 0), 's2.jpg': ('meyer/img/i021.jpg', 0), 's3.jpg': ('meyer/img/i015.jpg', 0), 's4.jpg': ('meyer/img/i018.jpg', 0), 's5.jpg': ('meyer/img/i023.jpg', 0)},
    body=b_meyer)
