"""Akquise DM 25.11.2026 · Teil A: Beauty Sisters (Bielefeld), Auszeit Kosmetik (Münster), Kosmetikinstitut Marita Gehrmann (Marl)."""
from common import *
SITES = {}

# ───────────── 1. Beauty Sisters Kosmetik-Institut, Bielefeld ─────────────
def b_bs(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg'], pos={'h1.jpg': '50% 35%'}, big='2002',
        ubar=[('Seit 2002', 'in Bielefeld'), ('Seit 2011', 'Ausbildungsbetrieb'), ('City', 'Bahnhofstraße 24')],
        ey='Beauty Sisters · Kosmetik-Institut in Bielefeld',
        h1='Permanent Make-up, Haut und Wimpern <em>vom Fach.</em>',
        sub='Gesichtsbehandlungen, Permanent Make-up, Wimpern- und Hairextensions, Nägel und Körperbehandlungen: alles in einem Institut, mitten in der Bielefelder Fußgängerzone.'))
        + ytvideo('film', 'Unser Film', 'Willkommen <em>bei den Beauty Sisters.</em>', 'Ein kurzer Einblick in unser Institut an der Bahnhofstraße.', 'fGHkhltqz6w', 'film.jpg', 'vdk')
        + scroller('behandlungen', 'Unsere Behandlungen', 'Von Kopf bis Fuß <em>in einem Institut.</em>', 'Wählen Sie Ihre Behandlung. Wir beraten Sie gern persönlich, was zu Ihrer Haut passt.', [
            ('Permanent Make-up', 'pmu.jpg', 'Brauen, Lidstrich und Lippen. Permanent Make-up Artist bei Purebeau seit 2006.', '50% 50%'),
            ('Gesichtsbehandlungen', 'gesicht.jpg', 'A.N.D. Fruchtsäure, Hydra Glow, Craith, Ultraschall und O2 Intraceuticals.', '50% 40%'),
            ('Micro Needling', 'needling.jpg', 'Anti-Aging-Anwendungen für ein feineres, frischeres Hautbild.', '50% 40%'),
            ('Wimpernextensions', 'wimpern.jpg', 'Volumenwimpern 3D/6D und Megavolumen für einen wachen Blick.', '50% 50%'),
            ('Hairextensions', 'haare.jpg', 'Zertifiziert für Invisible Bead Extensions®: flach, natürlich und bequem.', '50% 50%'),
            ('Hände und Nägel', 'naegel.jpg', 'Maniküre, Gel und Nageldesign, gepflegt bis in die Spitzen.', '50% 50%'),
            ('Körper und Haarentfernung', 'koerper.jpg', 'MDL 4G Haarentfernung, Waxing, Kryolipolyse und Body Wrapping.', '50% 50%')])
        + gallery('studio', 'Unser Studio', 'Hell, ruhig und <em>mitten in der Stadt.</em>', [
            ('st1.jpg', 'a', '50% 50%'), ('st2.jpg', 'b', '50% 50%'), ('st3.jpg', 'c', '50% 50%'), ('st4.jpg', 'd', '50% 50%')])
        + story('geschichte', 'Unsere Geschichte', 'Vom Sonnenstudio <em>zum Kosmetik-Institut.</em>', [
            'Die Erfolgsgeschichte von BEAUTY SISTERS beginnt im September 2002 mit der Eröffnung des Sonnenstudios WELCOME SUN. Seitdem haben wir unser Angebot ständig erweitert und verbessert.',
            'Da Qualität bei uns an oberster Stelle steht, bilden wir unsere Mitarbeiterinnen stets weiter und besuchen regelmäßig Fachmessen. Seit 2011 bilden wir außerdem zur geprüften Kosmetikerin aus.'],
            'st5.jpg', 'Beauty Sisters, Bahnhofstraße 24 in Bielefeld',
            tl=[('2006', 'Permanent Make-up Artist'), ('2017', 'Umzug in die Fußgängerzone'), ('2022', 'Craith Lab und Invisible Bead Extensions')], cls='alt')
        + svc('ausbildung', 'Ausbildung und Akademie', 'Wir geben unser Wissen <em>weiter.</em>', 'Junge Frauen, die ihr Hobby zum Beruf machen möchten, können sich jederzeit bei uns bewerben.', [
            ('Duale Ausbildung', 'Dreijährige Ausbildung zur geprüften Kosmetikerin, eingetragene Betriebsstätte bei der Handwerkskammer.'),
            ('Beauty Sisters Akademie', 'Hochwertige und innovative Fort- und Weiterbildungen für Kosmetikerinnen.'),
            ('Zertifiziert', 'A.N.D.-Institut, Craith Lab, Invisible Bead Extensions, Phibrows Artist.')], 'dk')
        + promo('gutschein', 'gutschein.jpg', 'Gutschein', 'Schönheit <em>zum Verschenken.</em>',
                'Ob Gesichtsbehandlung, Wimpern oder Nägel: Mit einem Gutschein der Beauty Sisters schenken Sie eine Auszeit in der Bielefelder City.',
                ['Für alle Behandlungen', 'Direkt im Institut erhältlich'], 'Gutschein anfragen')
        + contact(s) + footer(s))

S = SITES['bs'] = site(
    slug='beauty-sisters-bielefeld', firma='BeautySisters² GmbH', web='beautysisters-bielefeld.de', fonts='r28bs',
    title='Beauty Sisters – Kosmetik-Institut in Bielefeld', desc='Beauty Sisters Kosmetik-Institut in Bielefeld seit 2002: Permanent Make-up, Gesichtsbehandlungen, Wimpern- und Hairextensions, Nägel, Ausbildungsbetrieb.',
    tel='0521 770 90 355', tel_i='+4952177090355', mail='mail@beautysisters-bielefeld.de', adresse='Bahnhofstraße 24, 33602 Bielefeld',
    cta='Termin anfragen', nav=[('Film', 'film'), ('Behandlungen', 'behandlungen'), ('Studio', 'studio'), ('Geschichte', 'geschichte'), ('Ausbildung', 'ausbildung'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:00 – 19:00'), ('Sa', '09:00 – 18:00')],
    form_opts=['Permanent Make-up', 'Gesichtsbehandlung', 'Wimpern / Brauen', 'Hairextensions', 'Nägel', 'Gutschein', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Sagen Sie uns kurz, welche Behandlung Sie interessiert. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Mitten in der City. <em>Wir freuen uns auf Sie.</em>', kt_p='Sie finden uns in der Bielefelder Fußgängerzone an der Bahnhofstraße 24.',
    social=[('Instagram', 'https://www.instagram.com/beautysistersbielefeld/')],
    vars=V.format(ink='#1b1a18', mute='#5e5a53', p='#B8913F', pi='#fff', dk='#141311', s2='#f6f2ea', fh='"Cormorant Garamond",Georgia,serif', fb='"Montserrat",system-ui,sans-serif', lh=54, ft='#111') + DKHD.format(c='#111'),
    css='''.h2{font-weight:600;letter-spacing:-.005em;line-height:1.05}.h2 em{font-style:italic;color:#B8913F}.dk .h2 em,.vdk .h2 em{color:#e0bd6e}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.sv.dk{background:#141311;color:#fff}.sv.dk .lead{color:rgba(255,255,255,.82)}.sv .row div{border-top:3px solid #B8913F}.vd.vdk{background:#111;color:#fff}.vd.vdk .lead,.vd.vdk .note{color:rgba(255,255,255,.75)}
.promo .tag{background:#B8913F;color:#fff}.gl .grid{grid-template-columns:repeat(4,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:3/4}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr 1fr}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#111;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(184,145,63,.35);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:600;font-size:clamp(40px,4.6vw,74px)}.hz h1 em{color:#e0bd6e;font-style:italic}.hz .ey{color:#e0bd6e}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['bot'] = BOT('Lia', 'Ihre Beauty-Lotsin', 'den Beauty Sisters', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–19 Uhr, Sa 9–18 Uhr. Telefon: 0521 770 90 355.'],
    ['Bieten Sie Permanent Make-up an?', 'Ja, für Brauen, Lidstrich und Lippen. Wir arbeiten seit 2006 als Permanent Make-up Artist.'],
    ['Bilden Sie aus?', 'Ja, seit 2011 bieten wir die dreijährige duale Ausbildung zur geprüften Kosmetikerin an.']],
    ['#film', '#behandlungen', '#studio', '#kontakt'])
S['logo'] = 'logo.png'
S['img'] = {'logo.png': ('beautysisters/img/i000.png', 0), 'h1.jpg': ('beautysisters/img/i001.jpg', 0), 'film.jpg': ('/home/claude/r28raw/bs_yt.jpg', 0),
    'pmu.jpg': ('beautysisters/img/i002.jpg', 0), 'gesicht.jpg': ('beautysisters/img/i005.jpg', 0), 'needling.jpg': ('beautysisters/img/i007.jpg', 0),
    'wimpern.jpg': ('beautysisters/img/i014.jpg', 0), 'haare.jpg': ('beautysisters/img/i053.jpg', 0), 'naegel.jpg': ('beautysisters/img/i094.jpg', 0),
    'koerper.jpg': ('beautysisters/img/i009.jpg', 0),
    'st1.jpg': ('beautysisters/img/i026.jpg', 0), 'st2.jpg': ('beautysisters/img/i028.jpg', 0), 'st3.jpg': ('beautysisters/img/i033.jpg', 0), 'st4.jpg': ('beautysisters/img/i047.jpg', 0),
    'st5.jpg': ('beautysisters/img/i048.jpg', 0), 'gutschein.jpg': ('beautysisters/img/i056.jpg', 0)}
S['body'] = b_bs

# ───────────── 2. Auszeit Kosmetik, Münster ─────────────
def b_az(s):
    return (hd(s) + hero_split(s, dict(
        imgs=['h1.jpg'], pos={'h1.jpg': '50% 25%'}, big='2006', side='l',
        ubar=[('Seit 2006', 'in Münster'), ('Neu', 'Ostmarkstraße 58'), ('Online', 'Mo – Fr bis 20 Uhr')],
        ey='Auszeit Kosmetik · Jana Hölker · Münster',
        h1='Ihre Auszeit <em>ist unser Mittelpunkt.</em>',
        sub='Medical Beauty, Permanent Make-up und Fineline Tattoo, Hände und Füße: Seit 2006 kümmert sich das Team rund um Jana Hölker um Ihre Haut. Jetzt in neuen Räumen an der Ostmarkstraße 58.'))
        + facts([('07.11.2026', 'Neueröffnung an der Ostmarkstraße 58'), ('7', 'Spezialistinnen für Kosmetik, Fußpflege, Nägel und PMU'), ('Zertifiziert', 'Aesthetico active³ peel concept')], 'nx')
        + panels('leistungen', 'Unsere Leistungen', 'Von Kopf bis Fuß <em>in guten Händen.</em>', 'Gönnen Sie sich eine Auszeit bei einer verwöhnenden Gesichtsbehandlung und vergessen Sie Ihren Alltag.', [
            ('Medical Beauty', 'l1.jpg', 'Microneedling, Peelings und Hautpflege auf höchstem Niveau, individuell für Ihre Hautbedürfnisse. Mit Produkten von Aesthetico.', '35% 40%'),
            ('Permanent Make-up', 'l4.jpg', 'Puderbrows, Härchenzeichnung, Softliner, Wimpernkranzverdichtung und Aquarelllips: natürlich, langanhaltend und typgerecht.', '50% 50%'),
            ('Hände und Füße', 'l3.jpg', 'Maniküre, StripLac, Shellac und Gelmodellage. Dazu medizinische Fußpflege im nicht heilkundlichen Bereich.', '50% 50%'),
            ('Lashlift und Browlift', 'l2.jpg', 'Für einen offenen Blick und gepflegte Brauen, ohne tägliches Schminken.', '50% 50%')])
        + gallery('pmu', 'Permanent Make-up', 'Abgeheilte Ergebnisse <em>von Jana Hölker.</em>', [
            ('p1.jpg', 'a', '50% 50%'), ('p2.jpg', 'b', '50% 50%'), ('p3.jpg', 'c', '50% 50%'), ('p4.jpg', 'd', '50% 50%')], 'alt')
        + team('team', 'Das Auszeit-Team', 'Ein Team junger Frauen <em>mit Herz und Leidenschaft.</em>', 'Rund um Geschäftsinhaberin Jana Hölker widmen wir uns mit Leib und Seele der Beautywelt.', [
            ('t1.jpg', 'Jana Hölker', 'Inhaberin · med. Kosmetik, Fineline Tattoos'), ('t2.jpg', 'Maria Schullert', 'med. und kosm. Fußpflege, Visagistik'),
            ('t3.jpg', 'Natalie Busch', 'Nagelpflege, Kosmetik'), ('t4.jpg', 'Natalie Paul', 'kosm. und med. Fußpflege'),
            ('t5.jpg', 'Alla Eppinger', 'In der Auszeit seit 2018'), ('t6.jpg', 'Elisha Korkus', 'Auszubildende Kosmetik (IHK)'), ('t7.jpg', 'Julia Draht', 'Nageldesign')])
        + promo('gutschein', 'gutschein.jpg', 'Gutscheine', 'Verschenken Sie <em>eine Auszeit!</em>',
                'Unsere Gutscheine sind Wertgutscheine und können für alle Behandlungen und sogar Produkte eingesetzt werden. Auf Wunsch senden wir sie Ihnen gegen Vorkasse auch per Post.',
                ['Gesicht, Fußpflege, Maniküre oder PMU', 'Auch per Post erhältlich'], 'Gutschein bestellen', 'alt')
        + contact(s) + footer(s))

S = SITES['az'] = site(
    slug='auszeit-kosmetik-muenster', firma='Auszeit Kosmetik', web='auszeit-kosmetik-muenster.de', fonts='r28az',
    title='Auszeit Kosmetik Münster – Jana Hölker', desc='Auszeit Kosmetik in Münster seit 2006: Medical Beauty, Permanent Make-up, Fineline Tattoo, Nägel und med. Fußpflege. Neu an der Ostmarkstraße 58.',
    tel='0251 162 46 66', tel_i='+492511624666', mail='info@auszeit-kosmetik-muenster.de', adresse='Ostmarkstraße 58, 48145 Münster',
    cta='Termin buchen', nav=[('Leistungen', 'leistungen'), ('Permanent Make-up', 'pmu'), ('Team', 'team'), ('Gutscheine', 'gutschein'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 20:00'), ('Sa', '08:00 – 14:00'), ('Kernzeit', 'Mo – Fr 10:00 – 18:00')],
    form_opts=['Medical Beauty / Gesicht', 'Permanent Make-up', 'Fineline Tattoo', 'Maniküre / Nägel', 'Fußpflege', 'Gutschein', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Ihr Wunschtermin ist online nicht frei? Schreiben Sie uns, wir rufen zurück. WhatsApp: 0172 773 45 17.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Neue Räume. <em>Gleiches Team.</em>', kt_p='Seit dem 07.11.2026 finden Sie uns an der Ostmarkstraße 58 in Münster.',
    social=[('Instagram', 'https://www.instagram.com/auszeitkosmetikmuenster/')],
    vars=V.format(ink='#3a1f33', mute='#6d5867', p='#8E2470', pi='#fff', dk='#5a1747', s2='#fbf0f6', fh='"Playfair Display",Georgia,serif', fb='"Nunito Sans",system-ui,sans-serif', lh=58, ft='#3a1f33'),
    css='''.h2{font-weight:600;letter-spacing:-.01em;line-height:1.08}.h2 em{font-style:italic;color:#8E2470}.alt{background:var(--s2)}
.ft16.nx{background:#5a1747;color:#fff}.ft16.nx .nb>div{background:rgba(255,255,255,.07)!important;border-color:rgba(255,255,255,.18)!important}.ft16.nx b{color:#f7c6e3!important;font-size:clamp(24px,2.6vw,36px)!important}.ft16.nx span{color:rgba(255,255,255,.88)!important}
.promo .tag{background:#8E2470;color:#fff}.gl .grid{grid-template-columns:repeat(4,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:1/1}
.tm .grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}.tm figure div{aspect-ratio:2/3!important}.tm figure img{object-position:50% 0!important}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr 1fr}}''' + RUND)
S['css2'] = '.hd .logo img{max-width:min(190px,44vw);height:auto;width:auto;max-height:var(--logo-h)}.hz h1{hyphens:manual!important}@media(max-width:820px){.hz .sl img{object-position:50% 8%!important}}.hz{--hz-bg:#fbf0f6;--hz-ink:#3a1f33;--hz-mute:#6d5867;--hz-stroke:rgba(142,36,112,.18);--hz-line:rgba(58,31,51,.16)}.hz h1{font-weight:600;font-size:clamp(40px,4.6vw,74px)}.hz h1 em{color:#8E2470;font-style:italic}.hz .ey{color:#8E2470}'
S['bot'] = BOT('Ella', 'Ihre Auszeit-Lotsin', 'Auszeit Kosmetik', S, [
    ['Wo finde ich Sie jetzt?', 'Seit dem 07.11.2026 an der Ostmarkstraße 58, 48145 Münster.'],
    ['Öffnungszeiten', 'Online buchbar Mo–Fr 8–20 Uhr, Sa 8–14 Uhr. Kernöffnungszeit Mo–Fr 10–18 Uhr.'],
    ['Gibt es Gutscheine?', 'Ja, Wertgutscheine für alle Behandlungen und Produkte, auf Wunsch auch per Post.']],
    ['#leistungen', '#pmu', '#team', '#kontakt'])
S['logo'] = 'logo.png'
A = 'auszeit/img/'
S['img'] = {'logo.png': (A + 'i000.png', 0), 'h1.jpg': (A + 'i002.jpg', 1400), 'h2.jpg': (A + 'i046.jpg', 1400),
    'l1.jpg': (A + 'i011.jpg', 1600), 'l2.jpg': (A + 'i012.jpg', 1600), 'l3.jpg': (A + 'i013.jpg', 1600), 'l4.jpg': (A + 'i014.jpg', 1600),
    'p1.jpg': (A + 'i061.png', 900), 'p2.jpg': (A + 'i066.png', 900), 'p3.jpg': (A + 'i086.png', 900), 'p4.jpg': (A + 'i062.png', 900),
    't1.jpg': (A + 'i002.jpg', 700), 't2.jpg': (A + 'i003.jpg', 700), 't3.jpg': (A + 'i004.jpg', 700), 't4.jpg': (A + 'i005.jpg', 700),
    't5.jpg': (A + 'i006.jpg', 700), 't6.jpg': (A + 'i007.jpg', 700), 't7.jpg': (A + 'i008.jpg', 700), 'gutschein.jpg': (A + 'i017.jpg', 0)}
S['body'] = b_az

# ───────────── 3. Kosmetikinstitut Marita Gehrmann, Marl ─────────────
def b_mg(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 30%', 'h2.jpg': '50% 30%'}, big='Sothys',
        ubar=[('Sothys', 'Experte 2025/26'), ('Zertifiziert', 'Digiesthéticienne'), ('After Work', 'ohne Aufpreis')],
        ey='Kosmetikinstitut Marita Gehrmann · Marl',
        h1='Schönheit beginnt <em>mit Wohlbefinden.</em>',
        sub='Exklusive Gesichtsbehandlungen, die Sothys-Massage Digi-Esthétique und Make-up-Beratung: persönlich, ruhig und mit der französischen Luxuskosmetik von SOTHYS Paris.'))
        + story('ich', 'Das bin ich', 'Kosmetikerin, Visagistin <em>und examinierte Krankenschwester.</em>', [
            'Aus meiner jahrelangen Erfahrung als Krankenschwester ist mir der Kontakt zu Menschen sehr wichtig. Einem Menschen Zeit und Aufmerksamkeit zu schenken, gibt mir jeden Tag das Gefühl der Dankbarkeit.',
            'Fühlen Sie sich wohl bei mir, entfliehen Sie dem Alltag! Lassen Sie sich mit allen Sinnen verwöhnen. Sowohl Frauen als auch Männer.'], 'marita.jpg', 'Marita Gehrmann, Kosmetikerin und Visagistin',
            tl=[('Staatl. examiniert', 'Krankenschwester'), ('Mo – Sa', 'Termine nach Vereinbarung'), ('After Work', 'ohne Aufpreis')])
        + panels('behandlungen', 'Meine Leistungen', 'Exklusive Pflege <em>für höchste Ansprüche.</em>', 'Behandlungen mit wertvollen Wirkstoffen sorgen für Wohlgefühl, Geschmeidigkeit und Schutz.', [
            ('Gesichtsbehandlung', 'g1.jpg', 'Von der Doppel-Peeling-Behandlung (95 €) bis zum Ritual Secrets de Sothys (145 €): abgestimmt auf Ihre Haut.', '50% 30%'),
            ('Digi-Esthétique', 'g2.jpg', 'Die speziell von Sothys entwickelte Massagemethode. Ein richtiges Wohlfühlkonzept für Körper und Geist.', '50% 40%'),
            ('Apparative Kosmetik', 'g3.jpg', 'Mikrodermabrasion, Aqua Peeling, Oxygen Facial und Microneedling, ganz ohne Spritzen.', '50% 30%'),
            ('Make-up', 'g4.jpg', 'Sie möchten sich schminken, wissen aber nicht wie? Kommen Sie gern zur Make-up-Beratung.', '50% 25%')], 'dk')
        + svc('preise', 'Auszug aus der Preisliste', 'Gönnen Sie sich <em>etwas Besonderes.</em>', 'Alle Behandlungen und Preise erhalten Sie gern persönlich oder in meiner Preisliste.', [
            ('DX Glow · 130 €', 'Verteidigt und stärkt müde, gestresste Haut und stellt das Gleichgewicht wieder her.'),
            ('Mikrodermabrasion / Aqua Peeling / Oxygen · 139 €', 'Peeling, Tiefenreinigung und Feuchtigkeits-Booster in einer Behandlung.'),
            ('Microneedling · 125 €', 'Regt die Haut an, sich von innen zu erneuern. Falten werden gemildert, Poren verfeinert.'),
            ('Behandlung für Ihn · 82 €', 'Abgestimmt auf die männliche Haut: Anti-Stress, Hydrierung und gegen Falten.')])
        + gallery('auszeichnung', 'Expertenstatus', 'Ausgezeichnet <em>von SOTHYS Paris.</em>', [
            ('a1.jpg', 'a', '50% 50%'), ('a2.jpg', 'b', '50% 50%'), ('a3.jpg', 'c', '50% 30%'), ('a4.jpg', 'd', '50% 50%')], 'alt')
        + contact(s) + footer(s))

S = SITES['mg'] = site(
    slug='kosmetikinstitut-gehrmann-marl', firma='Kosmetikinstitut Marita Gehrmann', web='kosmetikinstitut-gehrmann.de', fonts='r28mg',
    title='Kosmetikinstitut Marita Gehrmann – Sothys Kosmetik in Marl', desc='Kosmetikinstitut Marita Gehrmann in Marl: Sothys Gesichtsbehandlungen, Digi-Esthétique Massage, apparative Kosmetik und Make-up-Beratung.',
    tel='02365 2966933', tel_i='+4923652966933', mail='marita_gehrmann@web.de', adresse='Riegestraße 5, 45768 Marl',
    cta='Termin anfragen', nav=[('Das bin ich', 'ich'), ('Leistungen', 'behandlungen'), ('Preise', 'preise'), ('Expertenstatus', 'auszeichnung'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Sa', 'nach Vereinbarung'), ('After Work', 'ohne Aufpreis'), ('Handy', '0151 24078950')],
    form_opts=['Gesichtsbehandlung', 'Digi-Esthétique Massage', 'Apparative Kosmetik', 'Make-up-Beratung', 'Gutschein', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Nennen Sie mir Ihre Wunschzeit, ich rufe Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ich freue mich <em>auf Ihren Besuch.</em>', kt_p='Sie finden mein Kosmetikinstitut an der Riegestraße 5 in Marl.',
    social=[('Instagram', 'https://www.instagram.com/maritagehrmann/')],
    vars=V.format(ink='#1c1c1c', mute='#5d5a56', p='#A8844A', pi='#fff', dk='#1c1c1c', s2='#f4f1ec', fh='"Bodoni Moda",Georgia,serif', fb='"Jost",system-ui,sans-serif', lh=40, ft='#141414') + DKHD.format(c='#141414'),
    css='''.h2{font-weight:500;letter-spacing:-.01em;line-height:1.08}.h2 em{font-style:italic;color:#A8844A}.dk .h2 em{color:#d8b878}.alt{background:var(--s2)}.hd .nav a{color:#fff}
.ap.dk{background:#1c1c1c;color:#fff}.ap.dk .lead{color:rgba(255,255,255,.82)}.sv .row div{border-top:3px solid #A8844A}
.lt-logo{font:500 21px "Bodoni Moda",Georgia,serif;letter-spacing:.02em;color:#fff;white-space:nowrap}.ft .lt-logo{color:#fff}
.gl .grid{grid-template-columns:repeat(4,1fr)}.gl .grid figure{grid-column:auto!important;grid-row:auto!important;aspect-ratio:3/4}
@media(max-width:820px){.gl .grid{grid-template-columns:1fr 1fr}.lt-logo{font-size:17px}}''' + RUND)
S['css2'] = '.hz{--hz-bg:#141414;--hz-ink:#fff;--hz-mute:rgba(255,255,255,.84);--hz-stroke:rgba(168,132,74,.3);--hz-line:rgba(255,255,255,.2)}.hz h1{font-weight:500;font-size:clamp(40px,4.6vw,74px)}.hz h1 em{color:#d8b878;font-style:italic}.hz .ey{color:#d8b878}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.6)}'
S['logo_txt'] = 'Marita Gehrmann <small style="display:block;font:400 11px Jost,sans-serif;letter-spacing:.24em;text-transform:uppercase;opacity:.75">Kosmetikinstitut</small>'
S['bot'] = BOT('Marie', 'Ihre Beauty-Lotsin', 'Marita Gehrmann', S, [
    ['Wann kann ich kommen?', 'Termine nach Vereinbarung von Montag bis Samstag, After-Work-Termine ohne Aufpreis. Telefon: 02365 2966933.'],
    ['Mit welcher Kosmetik arbeiten Sie?', 'Mit SOTHYS Paris. Ich bin Sothys Experte für Gesichtspflege, Körperpflege und Make-up 2025/26.'],
    ['Behandeln Sie auch Männer?', 'Ja, es gibt eine eigene Behandlung für die männliche Haut (82 €).']],
    ['#ich', '#behandlungen', '#preise', '#kontakt'])
G = 'gehrmann/img/'
S['img'] = {'h1.jpg': (G + 'i016.jpg', 1600), 'h2.jpg': (G + 'i021.jpg', 1600), 'marita.jpg': (G + 'i060.jpg', 0),
    'g1.jpg': (G + 'i046.jpg', 1400), 'g2.jpg': (G + 'i076.jpg', 1400), 'g3.jpg': (G + 'i066.jpg', 1400), 'g4.jpg': (G + 'i080.jpg', 1080, (0, 0.04, 1, 0.56)),
    'a1.jpg': (G + 'i091.jpg', 0), 'a2.jpg': (G + 'i096.jpg', 0), 'a3.jpg': (G + 'i106.jpg', 0), 'a4.jpg': (G + 'i086.jpg', 0)}
S['body'] = b_mg
