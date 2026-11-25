"""Akquise DM 25.11.2026 · Teil B: Ludmilla Giebler Cosmetics (Osnabrück), ALMA Kosmetik & Wellness (Nordhorn)."""
from common import *
SITES = {}

# ───────────── 4. Ludmilla Giebler Cosmetics, Osnabrück ─────────────
def b_lg(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '45% 40%', 'h2.jpg': '50% 40%', 'h3.jpg': '50% 40%'}, big='25',
        ubar=[('Seit 2001', 'eigenes Hautinstitut'), ('Über 25 Jahre', 'Berufserfahrung'), ('Hydrafacial', 'das Original in Osnabrück')],
        ey='Ludmilla Giebler Cosmetics · Hautinstitut in Osnabrück',
        h1='Ihre Haut <em>in besten Händen.</em>',
        sub='Individuelle Hautkonzepte, moderne apparative Kosmetik und Anti-Aging ohne OP: Hydrafacial, RF-Microneedling, Dermadrop TDA und mehr. Persönlich, diskret und mit Zeit für Ihre Haut.'))
        + scroller('behandlungen', 'Behandlungen', 'Für jede Haut <em>das passende Konzept.</em>', 'Die Technologien werden nicht nach festem Schema eingesetzt, sondern gezielt ausgewählt und kombiniert.', [
            ('Hydrafacial™ das Original', 'b1.jpg', 'Sofort sichtbarer Glow und ein ebenmäßiges Hautbild. Empfohlen im Abstand von vier Wochen.', '50% 50%'),
            ('RF-Microneedling', 'b2.jpg', 'Strafft die Haut und mildert Narben und Unebenheiten.', '50% 50%'),
            ('Laser-Haarentfernung', 'b4.jpg', 'Neue Diodenlaser-Technologie für dauerhaft glatte Haut.', '50% 40%'),
            ('Rosacea und Couperose', 'b5.jpg', 'Beruhigende, entzündungshemmende Wirkstoffbehandlungen.', '40% 50%'),
            ('Akne und Narben', 'b6.jpg', 'Individuelle Kombination aus Mikrodermabrasion, Needling und Wirkstoffen.', '50% 30%'),
            ('Wimpern und Brauen', 'b7.jpg', 'Wimpernlifting und Augenbrauenkorrektur für den perfekten Ausdruck.', '50% 50%')])
        + story('ueber', 'Über mich', 'Kein anonymes Studio, <em>sondern Ihr Hautinstitut.</em>', [
            'Seit 2001 verbinde ich in meinem privaten Kosmetikinstitut in Osnabrück langjährige kosmetische Expertise, moderne Technologien und hochwertige Wirkstoffkosmetik mit einer besonders persönlichen Betreuung.',
            'Gemeinsam entwickeln wir ein Behandlungskonzept, das auf Ihren Hautzustand und Ihre Hautziele abgestimmt ist. Unter meinem Motto „Zeit für Schönheit – Zeit für Dich“.'], 'ludmilla.jpg', 'Ludmilla Giebler, staatl. geprüfte Kosmetikerin, B.Sc. Ökotrophologie',
            tl=[('Seit 2001', 'in Osnabrück'), ('Staatl. geprüft', 'Kosmetikerin'), ('Skin Longevity', 'Anti-Aging ohne OP')], cls='alt')
        + svc('konzept', 'So arbeite ich', 'Schöne Haut <em>ist kein Zufall.</em>', 'Statt einzelner Standardbehandlungen erhalten Sie ein auf Ihre Haut abgestimmtes Konzept.', [
            ('1 · Hautanalyse', 'Ausführliche Beratung und Beurteilung Ihres Hautzustandes.'),
            ('2 · Behandlungsplan', 'Professionelle Anwendungen und apparative Kosmetik, gezielt kombiniert.'),
            ('3 · Heimpflege', 'Hochwertige Wirkstoffkosmetik für zu Hause, damit das Ergebnis bleibt.'),
            ('4 · Langfristig', 'Qualität, Festigkeit und Ausstrahlung der Haut möglichst lange erhalten.')], 'dk')
        + marquee(['Osnabrück', 'Belm', 'Wallenhorst', 'Georgsmarienhütte', 'Melle', 'Bramsche', 'Ibbenbüren', 'Bad Iburg', 'Münster', 'Hannover', 'und sogar Hamburg'])
        + gallery('institut', 'Das Institut', 'Ruhe, Diskretion <em>und Zeit für Ihre Haut.</em>', [
            ('i1.jpg', 'a', '50% 50%'), ('i2.jpg', 'b', '50% 50%'), ('i3.jpg', 'c', '50% 50%')])
        + contact(s) + footer(s))

S = SITES['lg'] = site(
    slug='ludmilla-giebler-cosmetics-osnabrueck', firma='Ludmilla Giebler Cosmetics', web='lg-cosmetics.de', fonts='r28lg',
    title='Ludmilla Giebler Cosmetics – Hautinstitut in Osnabrück', desc='Ludmilla Giebler Cosmetics in Osnabrück: Hydrafacial, RF-Microneedling, Dermadrop TDA, Laser-Haarentfernung und individuelle Hautkonzepte seit 2001.',
    tel='0170 9666704', tel_i='+491709666704', mail='info@lg-cosmetics.de', adresse='Reinhold-Schneider-Str. 6, 49088 Osnabrück',
    cta='Termin vereinbaren', nav=[('Behandlungen', 'behandlungen'), ('Über mich', 'ueber'), ('Konzept', 'konzept'), ('Institut', 'institut'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung'), ('WhatsApp', '0170 9666704'), ('Online', 'Termin online buchen')],
    form_opts=['Hydrafacial', 'RF-Microneedling', 'Dermadrop TDA', 'Laser-Haarentfernung', 'Akne / Rosacea / Narben', 'Hautanalyse', 'Sonstiges'],
    form_h3='Termin vereinbaren', form_p='Sagen Sie mir kurz, worum es geht. Ich rufe Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Zeit für Schönheit. <em>Zeit für Dich.</em>', kt_p='Mein privates Hautinstitut liegt nahe der Osnabrücker Innenstadt.',
    social=[('Instagram', 'https://www.instagram.com/ludmilla_giebler_cosmetics/')],
    vars=V.format(ink='#1a1a1a', mute='#5c5856', p='#A27B5C', pi='#fff', dk='#161616', s2='#f5f1ed', fh='"Marcellus",Georgia,serif', fb='"Raleway",system-ui,sans-serif', lh=50, ft='#111') + DKHD.format(c='#111'),
    css='''.h2{font-weight:400;letter-spacing:.005em;line-height:1.1}.h2 em{font-style:normal;color:#A27B5C}.dk .h2 em{color:#d9b48f}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.sv.dk{background:#161616;color:#fff}.sv.dk .lead{color:rgba(255,255,255,.82)}.sv .row div{border-top:3px solid #A27B5C}.mq{background:#A27B5C}
.gl .grid{grid-template-columns:repeat(3,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:4/3}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#111;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(162,123,92,.3);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:400;font-size:clamp(40px,4.6vw,74px)}.hz h1 em{color:#d9b48f;font-style:normal}.hz .ey{color:#d9b48f}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['bot'] = BOT('Lara', 'Ihre Haut-Lotsin', 'Ludmilla Giebler Cosmetics', S, [
    ['Wie bekomme ich einen Termin?', 'Online, telefonisch oder per WhatsApp unter 0170 9666704.'],
    ['Was ist Hydrafacial?', 'Eine Tiefenreinigung mit Feuchtigkeitspflege für sofortigen Glow. Empfohlen im Abstand von vier Wochen.'],
    ['Behandeln Sie Rosacea und Akne?', 'Ja, mit individuell abgestimmten Konzepten für Rosacea, Couperose, Akne und Narben.']],
    ['#behandlungen', '#ueber', '#konzept', '#kontakt'])
S['logo'] = 'logo.png'
L = 'giebler/img/'
S['img'] = {'logo.png': (L + 'i001.png', 0), 'h1.jpg': (L + 'i000.jpg', 0), 'h2.jpg': (L + 'i019.jpg', 0), 'h3.jpg': (L + 'i018.jpg', 0),
    'b1.jpg': (L + 'i033.jpg', 0), 'b2.jpg': (L + 'i036.jpg', 0), 'b4.jpg': (L + 'i039.jpg', 0),
    'b5.jpg': (L + 'i044.jpg', 0), 'b6.jpg': (L + 'i051.jpg', 0), 'b7.jpg': (L + 'i041.jpg', 0),
    'ludmilla.jpg': (L + 'i000.jpg', 0), 'i1.jpg': (L + 'i020.jpg', 1600, (0, 0, .5, 1)), 'i2.jpg': (L + 'i019.jpg', 0), 'i3.jpg': (L + 'i020.jpg', 1600, (.5, 0, 1, 1))}
S['body'] = b_lg

# ───────────── 5. ALMA Kosmetik & Wellness, Nordhorn ─────────────
def b_al(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 30%', 'h2.jpg': '50% 50%'}, big='ALMA', side='l',
        ubar=[('1 Jahr', 'ALMA in Nordhorn'), ('Online', 'Termin buchen'), ('Mi bis 20 Uhr', 'für den Feierabend')],
        ey='ALMA Kosmetik & Wellness · Nordhorn',
        h1='Pflege für deine Haut, <em>Wellness für deine Seele.</em>',
        sub='Gesichtsbehandlungen, Pediküre und Maniküre, Massagen, Wimpern und Brauen: Jeder Termin ist persönlich auf dich abgestimmt, damit du dich von Kopf bis Fuß wohlfühlst.'))
        + scroller('behandlungen', 'Behandlungen im Überblick', 'Deine Auszeit <em>vom Alltag.</em>', 'Ob Gesichtsbehandlung, Fußpflege oder entspannende Massage: Bei ALMA findest du alles für deine Schönheit und dein Wohlbefinden.', [
            ('Gesichtsbehandlungen', 'b1.jpg', 'Classic Gesichtsbehandlung ab 69,50 € (50 Min.): Reinigung, Peeling, Ausreinigung und Pflege.', '50% 40%'),
            ('Pediküre und Maniküre', 'b2.jpg', 'Von klassisch bis Shellac, ganz nach deinem Wunsch. Klassische Maniküre 34,50 €.', '50% 50%'),
            ('Massagen', 'b3.jpg', 'Wohltuende Massagen für tiefe Entspannung und Balance.', '50% 50%'),
            ('Wimpern und Brauen', 'b4.jpg', 'Färben, Korrektur, Lash- und Brow Lifting für einen natürlich schönen Look.', '50% 50%'),
            ('Waxing', 'b5.jpg', 'Schonend und hygienisch, z. B. Achseln 19,50 €, Beine komplett 47,50 €.', '50% 50%'),
            ('Make-up', 'b6.jpg', 'Vom Tages-Make-up bis zum Braut-Make-up inklusive Probe.', '50% 30%')])
        + duo('wellness', 'Wellnesspakete', 'Perfekt kombiniert <em>für Körper und Seele.</em>', 'Deine Auszeit vom Alltag: zum Entspannen oder zum Verschenken.', [
            ('Für dich', 'Wellness Balance · Lumière · Luxe', 'p1.jpg', 'Drei Pakete von 64,50 € bis 144,50 €, mit kombinierten Behandlungen für Haut und Seele.', ['Wellness Balance 64,50 €', 'Wellness Lumière 99,50 €', 'Wellness Luxe 144,50 €'], 'Paket anfragen'),
            ('Zum Verschenken', 'Gutscheine', 'p2.jpg', 'Schenk eine Auszeit bei ALMA: für eine Behandlung deiner Wahl oder ein ganzes Wellnesspaket.', ['Für alle Behandlungen', 'Direkt im Studio erhältlich'], 'Gutschein anfragen')], 'alt')
        + story('ueber', 'Lerne mich kennen', 'Ich bin Sara. <em>Willkommen bei ALMA.</em>', [
            'Ich bin Kosmetikerin und Fußpflegerin mit Erfahrung in der professionellen Hautpflege. Mit ALMA Kosmetik & Wellness habe ich einen Ort für Qualität, Ruhe und individuelle Behandlungen geschaffen.',
            'Parkmöglichkeiten findest du direkt an der Straße in unmittelbarer Nähe des Instituts, für eine entspannte und unkomplizierte Anreise.'], 'sara.jpg', 'Sara, Inhaberin von ALMA Kosmetik & Wellness',
            tl=[('Persönlich', 'individuelle Beratung'), ('Hochwertig', 'nachhaltige Pflege'), ('Zentral', 'mitten in Nordhorn')], rev=True)
        + contact(s) + footer(s))

S = SITES['al'] = site(
    slug='alma-kosmetik-nordhorn', firma='ALMA Kosmetik & Wellness', web='alma-kosmetik.de', fonts='r28al', du=True,
    title='ALMA Kosmetik & Wellness – Kosmetikstudio in Nordhorn', desc='ALMA Kosmetik & Wellness in Nordhorn: Gesichtsbehandlungen, Pediküre und Maniküre, Massagen, Wimpern und Brauen, Waxing, Make-up und Wellnesspakete.',
    tel='05921 7817111', tel_i='+4959217817111', mail='info@alma-kosmetik.de', adresse='Lingener Straße 25, 48531 Nordhorn',
    cta='Termin buchen', nav=[('Behandlungen', 'behandlungen'), ('Wellness', 'wellness'), ('Über mich', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Di', '09:00 – 18:00'), ('Mi', '10:00 – 20:00'), ('Do – Fr', '09:00 – 18:00'), ('Sa – So', 'geschlossen')],
    form_opts=['Gesichtsbehandlung', 'Pediküre / Maniküre', 'Massage', 'Wimpern & Brauen', 'Waxing', 'Make-up', 'Wellnesspaket / Gutschein'],
    form_h3='Termin anfragen', form_p='Schreib mir kurz, was du dir wünschst. Ich rufe dich zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Zentral in Nordhorn. <em>Dein Weg zu schöner Haut.</em>', kt_p='Du findest ALMA an der Lingener Straße 25, Parkplätze direkt an der Straße.',
    social=[('Instagram', 'https://www.instagram.com/alma.kosmetik/')],
    vars=V.format(ink='#2f2a25', mute='#6b625a', p='#8C7B66', pi='#fff', dk='#5f544a', s2='#f4f0ea', fh='"Gilda Display",Georgia,serif', fb='"Karla",system-ui,sans-serif', lh=56, ft='#3d362f') + DKHD.format(c='#8C7B66'),
    css='''.h2{font-weight:400;letter-spacing:-.005em;line-height:1.1}.h2 em{font-style:italic;color:#8C7B66}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.gl .grid{grid-template-columns:repeat(2,1fr);align-items:start;max-width:900px}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:auto!important;height:auto!important}.gl .grid figure img{height:auto!important;aspect-ratio:auto!important}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#f4f0ea;--hz-ink:#2f2a25;--hz-mute:#6b625a;--hz-stroke:rgba(140,123,102,.22);--hz-line:rgba(47,42,37,.16)}.hz h1{font-weight:400;font-size:clamp(38px,4.4vw,70px)}.hz h1 em{color:#8C7B66;font-style:italic}.hz .ey{color:#8C7B66}'
S['bot'] = BOTDU('Ava', 'Deine Wohlfühl-Lotsin', 'ALMA Kosmetik & Wellness', S, [
    ['Öffnungszeiten', 'Mo–Di 9–18 Uhr, Mi 10–20 Uhr, Do–Fr 9–18 Uhr. Am Wochenende geschlossen.'],
    ['Was kostet eine Gesichtsbehandlung?', 'Die Classic Gesichtsbehandlung (50 Min.) kostet 69,50 €.'],
    ['Gibt es Gutscheine?', 'Ja, für Behandlungen und Wellnesspakete, perfekt zum Verschenken.']],
    ['#behandlungen', '#wellness', '#ueber', '#kontakt'])
S['logo'] = 'logo.png'
M = 'alma/img/'
S['img'] = {'logo.png': (M + 'i001.png', 0), 'h1.jpg': (M + 'i002.jpg', 0), 'h2.jpg': (M + 'i003.jpg', 1600),
    'b1.jpg': (M + 'i020.jpg', 0), 'b2.jpg': (M + 'i014.jpg', 0), 'b3.jpg': (M + 'i015.jpg', 0), 'b4.jpg': (M + 'i016.jpg', 0), 'b5.jpg': (M + 'i017.jpg', 0), 'b6.jpg': (M + 'i023.jpg', 0),
    'p1.jpg': (M + 'i013.jpg', 0), 'p2.jpg': (M + 'i018.jpg', 0), 'sara.jpg': (M + 'i025.jpg', 0),
   }
S['body'] = b_al
