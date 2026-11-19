"""Akquise-Agent 19.11.2026 (Donnerstag, Handwerk): 5 Betriebe mit Instagram und schwacher Website.
Texte, Leistungen, Bilder und Logos stammen von den Originalseiten. Keine erfundenen Preise oder Stimmen."""
from common import *
SITES = {}
R = '/home/claude/r20raw/'

def css_base(p, dk, extra=''):
    return (f'''.h2,.hz h1{{font-weight:800;letter-spacing:-.02em}}.h2 em,.hz h1 em{{font-style:normal;color:{p}}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.st.dk{{background:{dk};color:#fff}}.st.dk .lead{{color:rgba(255,255,255,.86)}}.st.dk .tl b{{color:#fff}}.rd .road div h3{{color:{p}}}
.sec.gl{{display:block!important}}.gl .grid{{grid-auto-flow:dense}}.gl .grid figure{{border-radius:0!important}}.btn{{border-radius:999px!important}}.hz .ey,.sv .row div h3::before{{}}.kt .info i{{border-radius:50%!important}}
.ft img{{background:#fff;padding:8px 12px;height:66px}}
@media(max-width:820px){{.hz h1{{font-size:31px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}.gl .grid{{grid-auto-rows:150px}}}}''' + extra)

def hz(s2, p, ink='#161616'):
    return f'.hz{{--hz-bg:{s2};--hz-ink:{ink};--hz-mute:#555;--hz-stroke:rgba(0,0,0,.07);--hz-cols:46fr 54fr}}.hz h1{{font-size:clamp(34px,4.2vw,64px)}}.hz .ey{{color:{p}}}'

ABL = [('Anliegen schicken', 'Über das Formular oder direkt per Telefon. Sagen Sie kurz, worum es geht.'),
       ('Termin vor Ort', 'Wir schauen uns alles bei Ihnen an und beraten Sie persönlich.'),
       ('Saubere Ausführung', 'Wir arbeiten zuverlässig, sorgfältig und termintreu.')]

# ─────────────────────────── 1 · Malerbetrieb Vehrenkamp, Nienburg ───────────────────────────
def b_vehrenkamp(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '50% 60%'}, big='',
        ubar=[('Seit 1984', 'Familienunternehmen'), ('Meisterbetrieb', 'Malerinnung Nienburg'), ('ca. 30', 'Mitarbeiter')],
        ey='Malerbetrieb Vehrenkamp · Nienburg/Weser',
        h1='Wir helfen Ihnen, <em>schöner zu wohnen.</em>',
        sub='Malerarbeiten, Fassadengestaltung und Wärmedämmung vom Meisterbetrieb. Seit über 30 Jahren mit Expertise und Erfahrung für Sie da, privat wie gewerblich.'))
        + marquee(['Malerarbeiten', 'Fassadengestaltung', 'Wärmedämmverbundsysteme', 'Fußbodenarbeiten', 'Tapezierarbeiten', 'Schimmelpilzsanierung', 'Sandstrahlarbeiten', 'Objektbeschriftungen'], 'wm')
        + promo('fassade', 'fa.jpg', 'Fassade & Wärmedämmung', 'Dämmen, verputzen, <em>neu gestalten.</em>',
                'Von der Wärmedämmung mit Putz und Anstrich bis zu Klinkerriemchen, Kratzputz oder dem Firmenlogo im Putz: Wir geben Ihrer Fassade ein neues Gesicht und senken gleichzeitig die Energiekosten.',
                ['Wärmedämmverbundsysteme (WDVS)', 'Hubsteiger bis 18 Meter Höhe', 'Wärmebildkamera zeigt, wo Energie verloren geht'], 'Fassade anfragen', 'alt')
        + svc('leistungen', 'Leistungsangebot', 'Weit mehr als <em>streichen.</em>', 'Unser Leistungsspektrum reicht weit über die klassischen Maler- und Fußbodenarbeiten hinaus.', [
            ('Maler- und Lackierarbeiten', 'Anstrich- und Lackierarbeiten im privaten, öffentlichen und gewerblichen Bereich.'),
            ('Raumgestaltung', 'Wisch- und Schablonentechnik, italienische Glättetechnik (Stucco-Lustro) und großflächige Fototapeten.'),
            ('Fußbodenarbeiten', 'Neue Böden aus einer Hand, passend zu Wand und Raum.'),
            ('Schimmelpilzsanierung', 'Wir finden die Ursache und sanieren fachgerecht.'),
            ('Restaurierung', 'Mit Restaurator im Handwerk im Team: Altes erhalten und neu zur Geltung bringen.'),
            ('Sandstrahlen & Graffiti-Entfernung', 'Sandstrahlarbeiten, z. B. am Kipper, und die Entfernung von Graffiti.')])
        + gallery('referenzen', 'Referenzen', 'Ein Blick auf <em>unsere Arbeit.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 40%')])
        + ablauf('weg', 'So einfach geht es', 'Anfragen, beraten, <em>fertig.</em>', 'Sie müssen sich um nichts kümmern.', ABL)
        + story('ueber', 'Über uns', 'Ein Familienbetrieb <em>seit 1984.</em>', [
            'Thomas Vehrenkamp gründete den Malerbetrieb 1984 in Erichshagen/Nienburg. Seit 1992 sind wir an der Celler Straße 94 zu Hause.',
            'Seit 2015 führen Thomas und Tim Vehrenkamp das Unternehmen gemeinsam. Wir bilden aus und freuen uns über jeden, der unser Handwerk lernen möchte.'],
            'ab.jpg', 'Unser Firmengebäude an der Celler Straße 94', cls='dk',
            tl=[('Thomas Vehrenkamp', 'Firmengründer, Geschäftsführer'), ('Tim Vehrenkamp', 'Maler- und Lackierermeister, Geschäftsführer')])
        + contact(s) + footer(s))

P1, D1 = '#c8102e', '#20376a'
S = SITES['vehrenkamp'] = site(
    slug='malerbetrieb-vehrenkamp-nienburg', firma='Malerbetrieb Vehrenkamp GmbH & Co. KG', web='malerbetrieb-vehrenkamp.de', fonts='r14bec', branche='Malerbetrieb',
    runde='Akquise DM 19.11.2026',
    title='Malerbetrieb Vehrenkamp – Meisterbetrieb in Nienburg/Weser', desc='Malerbetrieb Vehrenkamp in Nienburg: Malerarbeiten, Fassadengestaltung, Wärmedämmung, Fußböden, Schimmelpilzsanierung.',
    tel='05021 912591', tel_i='+495021912591', mail='info@malerbetrieb-vehrenkamp.de', adresse='Celler Straße 94, 31582 Nienburg', google=None,
    cta='Angebot anfragen', nav=[('Fassade', 'fassade'), ('Leistungen', 'leistungen'), ('Referenzen', 'referenzen'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung')],
    form_opts=['Malerarbeiten', 'Fassade / Wärmedämmung', 'Raumgestaltung', 'Fußboden', 'Schimmelpilzsanierung', 'Sonstiges'],
    form_h3='Angebot anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns auf <em>Ihre Anfrage.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    vars=V.format(ink='#161616', mute='#555', p=P1, pi='#fff', dk=D1, s2='#f3f5f9', fh='"Barlow Condensed",system-ui,sans-serif', fb='"Heebo",system-ui,sans-serif', lh=46, ft=D1),
    css=css_base(P1, D1, '.h2,.hz h1{text-transform:uppercase;font-weight:700;letter-spacing:0}'))
S['css2'] = hz('#fff', P1)
S['bot'] = BOT('Pinsel', 'Ihr Maler-Lotse', 'Vehrenkamp', S, [
    ['Was machen Sie alles?', 'Malerarbeiten, Fassadengestaltung, Wärmedämmverbundsysteme, Fußböden, Tapezierarbeiten, Schimmelpilzsanierung, Sandstrahlen und mehr.'],
    ['Wie bekomme ich ein Angebot?', 'Am schnellsten per Telefon: 05021 912591. Oder Sie nutzen das Formular.'],
    ['Bilden Sie aus?', 'Ja, wir bilden Maler und Lackierer aus. Sprechen Sie uns gern an.']],
    ['#fassade', '#leistungen', '#referenzen', '#kontakt'])
S['img'] = {'logo.png': (R + 'vehrenkamp/i01.png', 600), 'h1.jpg': (R + 'vehrenkamp/i62.jpg', 1600), 'h2.jpg': (R + 'vehrenkamp/i40.jpg', 1600), 'h3.jpg': (R + 'vehrenkamp/i66.jpg', 1600),
    'fa.jpg': (R + 'vehrenkamp/i60.jpg', 1400), 'g1.jpg': (R + 'vehrenkamp/i42.jpg', 1200), 'g2.jpg': (R + 'vehrenkamp/i55.jpg', 900), 'g3.jpg': (R + 'vehrenkamp/i47.jpg', 900),
    'g4.jpg': (R + 'vehrenkamp/i24.jpg', 900), 'g5.jpg': (R + 'vehrenkamp/i68.jpg', 1200), 'g6.jpg': (R + 'vehrenkamp/i37.jpg', 900), 'ab.jpg': (R + 'vehrenkamp/i11.jpg', 1200)}
S['body'] = b_vehrenkamp
S['social'] = [('Instagram', 'https://www.instagram.com/malerbetrieb_vehrenkamp/')]

# ─────────────────────────── 2 · Malermeister Christian Hilbk, Münster-Sprakel ───────────────────────────
def b_hilbk(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], side='l', big='',
        ubar=[('Seit 1995', 'meistergeführt'), ('Innungsbetrieb', 'Malerinnung Münster'), ('Termintreu', 'zuverlässig, sorgfältig')],
        ey='Malermeister Christian Hilbk · Münster-Sprakel',
        h1='Wir bringen Farbe <em>in Ihren Alltag.</em>',
        sub='Frische Farben bringen ein Wohlgefühl in Ihre eigenen vier Wände. Spachteln, wischen, tupfen oder einfach streichen: Bei Malermeister Christian Hilbk sind Sie in den besten Händen.'))
        + marquee(['Innenraumgestaltung', 'Innenanstrich', 'Farbberatung', 'Tapezieren', 'Bodenbeläge', 'Fassadengestaltung', 'Wärmedämmung'], 'wm')
        + promo('innen', 'pr.jpg', 'Innenraumgestaltung', 'Vom Boden bis zur Decke: <em>Ihre Räume.</em>',
                'Die Gestaltung von Wänden und Böden prägt Ihr Zuhause oder Ihre Firmenräume. Christian Hilbk hat das Gespür für Licht, Raumaufteilung und Farbwirkung, für die passende Tapete und die Details, die das Wohlfühlen ausmachen.',
                ['Maßgeschneiderte Profiberatung', 'Farbkonzepte, die zusammenpassen', 'Saubere, haltbare Verarbeitung'], 'Beratung anfragen', 'alt')
        + svc('leistungen', 'Leistungen', 'Auf diese Leistungen <em>können Sie zählen.</em>', 'Vom Innenanstrich bis zur gedämmten Fassade.', [
            ('Innenanstrich', 'Die Decke tropffrei streichen, im Treppenhaus sicher stehen, die richtige Farbe für Funktionsräume: Wir machen das.'),
            ('Farbberatung', 'Wir stimmen Farben passend aufeinander ab. Unsere Farbkarte ist die Kur für Ihr Wohlbefinden.'),
            ('Tapezieren', 'Von klassisch bis Designtapete, sauber verklebt und auf Stoß.'),
            ('Bodenbeläge', 'Neue Böden, passend zur Wand und zum Raum.'),
            ('Fassadengestaltung', 'Der Putz bröckelt? Graffiti? Wir kümmern uns darum.'),
            ('Wärmedämmung', 'Wärmebrücken, Schimmel und Energiekosten eindämmen, verbunden mit einer gelungenen Farbgestaltung.')])
        + gallery('referenzen', 'Referenzen', 'Ein neues Wohngefühl <em>entsteht.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%')])
        + ablauf('weg', 'So einfach geht es', 'Anfragen, beraten, <em>fertig.</em>', 'Sie müssen sich um nichts kümmern.', ABL)
        + story('ueber', 'Über mich', 'Unsere Arbeit <em>macht uns Spaß.</em>', [
            'Wir sind ein meistergeführter Innungsbetrieb seit 1995. Wir arbeiten zuverlässig, sorgfältig und termintreu.',
            '„Ich habe die Firma Hilbk mit allen Angestellten und Auszubildenden als sehr umgängliche Handwerker kennengelernt.“ (Saskia Löwenkamp, Café Nordcup Münster, Kundenstimme von hilbk.de)'],
            'ab.jpg', 'Malermeister Christian Hilbk', cls='dk',
            tl=[('Christian Hilbk', 'Malermeister'), ('Mo – Fr', '08:00 – 17:00 Uhr')])
        + contact(s) + footer(s))

P2, D2 = '#c4161c', '#1f2d5c'
S = SITES['hilbk'] = site(
    slug='malermeister-hilbk-muenster', firma='Ch. Hilbk Malerbetrieb', web='malermeister-hilbk.de', fonts='r16geyer', branche='Malerbetrieb',
    runde='Akquise DM 19.11.2026',
    title='Malermeister Christian Hilbk – Malerbetrieb in Münster-Sprakel', desc='Malermeister Christian Hilbk in Münster: Innenraumgestaltung, Innenanstrich, Farbberatung, Tapezieren, Bodenbeläge, Fassade und Wärmedämmung.',
    tel='0251 216914', tel_i='+49251216914', mail='info@hilbk.de', adresse='Am Hangkamp 19, 48157 Münster', google=None,
    cta='Beratung anfragen', nav=[('Innenräume', 'innen'), ('Leistungen', 'leistungen'), ('Referenzen', 'referenzen'), ('Über mich', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '08:00 – 17:00 Uhr')],
    form_opts=['Innenanstrich', 'Farbberatung', 'Tapezieren', 'Bodenbeläge', 'Fassade', 'Wärmedämmung', 'Sonstiges'],
    form_h3='Beratung anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns über <em>Ihre Nachricht.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    vars=V.format(ink='#161616', mute='#555', p=P2, pi='#fff', dk=D2, s2='#f6f4f1', fh='"Montserrat",system-ui,sans-serif', fb='"Source Sans 3",system-ui,sans-serif', lh=58, ft=D2),
    css=css_base(P2, D2))
S['css2'] = hz('#f6f4f1', P2)
S['bot'] = BOT('Farbe', 'Ihr Maler-Lotse', 'Hilbk', S, [
    ['Was machen Sie alles?', 'Innenraumgestaltung, Innenanstrich, Farbberatung, Tapezieren, Bodenbeläge, Fassadengestaltung und Wärmedämmung.'],
    ['Wie erreiche ich Sie?', 'Telefon 0251 216914, Mo – Fr 08:00 – 17:00 Uhr. Oder Sie nutzen das Formular.'],
    ['Wo sind Sie tätig?', 'In Münster und Umgebung.']],
    ['#innen', '#leistungen', '#referenzen', '#kontakt'])
S['img'] = {'logo.png': (R + 'hilbk/i02.png', 0), 'h1.jpg': (R + 'hilbk/i06.webp', 0), 'h2.jpg': (R + 'hilbk/i25.webp', 1600), 'h3.jpg': (R + 'hilbk/i09.webp', 1400),
    'pr.jpg': (R + 'hilbk/i12.webp', 1400), 'g1.jpg': (R + 'hilbk/i24.webp', 1200), 'g2.jpg': (R + 'hilbk/i08.webp', 900), 'g3.jpg': (R + 'hilbk/i19.webp', 900),
    'g4.jpg': (R + 'hilbk/i10.webp', 900), 'g5.jpg': (R + 'hilbk/i11.webp', 1200), 'g6.jpg': (R + 'hilbk/i16.webp', 900), 'ab.jpg': (R + 'hilbk/i30.webp', 900)}
S['body'] = b_hilbk
S['social'] = [('Instagram', 'https://www.instagram.com/malerbetrieb_ch_hilbk/')]

# ─────────────────────────── 3 · Malerfachbetrieb Wunderlin, Münster ───────────────────────────
def b_wunderlin(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], big='',
        ubar=[('Meisterin', 'Maler und Lackierer'), ('Münster', 'und Umgebung'), ('Öko-Farben', 'ohne Konservierung')],
        ey='Malerfachbetrieb Wunderlin · Münster',
        h1='Farbe. Gestaltung. <em>Freude.</em>',
        sub='Ihr Spezialist für Maler- und Tapezierarbeiten, individuelle Wandgestaltung, Fassadenanstriche und Wärmedämm-Verbundsysteme. Persönlich beraten von Malermeisterin Désirée Wunderlin.'))
        + marquee(['Maler- und Lackierarbeiten', 'Tapezierarbeiten', 'Dekorative Wohnraumgestaltung', 'Farb- und Stilberatung', 'Fassadenrenovierung', 'WDVS', 'Ökologische Farben'], 'wm')
        + promo('fassade', 'pr.jpg', 'Fassade', 'Vom Innenanstrich bis zur <em>Fassadensanierung.</em>',
                'Ob Großbaustelle, gewerbliches Projekt oder Ihr privates Zuhause: Wir sanieren und streichen Fassaden und bringen Wärmedämm-Verbundsysteme an. Durch unsere langjährige Erfahrung gewährleisten wir Ihnen eine saubere Ausführung.',
                ['Fassadenrenovierung und -anstriche', 'Wärmedämm-Verbundsysteme (WDVS)', 'Energie- und Architektenberatung'], 'Fassade anfragen', 'alt')
        + svc('leistungen', 'Unsere Leistungen', 'Die Liebe <em>zum Detail.</em>', 'Kreative Farbgestaltungen in enger Abstimmung mit Ihnen, dazu anspruchsvolle Maler- und Putztechniken.', [
            ('Maler- und Lackierarbeiten', 'Innen und außen, inklusive Fensterbeschichtung und Beschichtung von Bauteilen.'),
            ('Tapezierarbeiten', 'Sauber verarbeitet, von klassisch bis Design.'),
            ('Dekorative Wohnraumgestaltung', 'Individuelle Wandgestaltung, die zu Ihnen passt.'),
            ('Farb- und Stilberatung', 'Wir finden mit Ihnen die Farben, die Ihren Räumen guttun.'),
            ('Wohngesundheit & Baubiologie', 'Ökologische Farben ohne Konservierungsstoffe.'),
            ('Wärmedämm-Verbundsysteme', 'Fassade dämmen, Energie sparen, neu gestalten.')])
        + gallery('projekte', 'Projekte', 'Überzeugen Sie sich <em>selbst.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', 'w2', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + ablauf('weg', 'So einfach geht es', 'Anfragen, beraten, <em>fertig.</em>', 'Bei uns erwartet Sie eine persönliche und individuelle Beratung.', ABL)
        + story('ueber', 'Über uns', 'Unsere Kunden schätzen die <em>fachkundige Beratung.</em>', [
            'Die Liebe zum Detail und die Freude an der Ausführung sind ein wichtiger Teil unseres Erfolgsgeheimnisses.',
            'Unabhängig davon, ob Großbaustelle, gewerbliches Projekt oder Neuerung in Ihrem Zuhause: Bei uns erwartet Sie eine persönliche Beratung zu allen Fragen rund um die Malerarbeiten.'],
            'ab.jpg', 'Malerfachbetrieb Wunderlin', cls='dk',
            tl=[('Désirée Wunderlin', 'Maler- und Lackierermeisterin'), ('Münster', 'und Umgebung')])
        + contact(s) + footer(s))

P3, D3 = '#e2007a', '#2b2b2b'
S = SITES['wunderlin'] = site(
    slug='malerfachbetrieb-wunderlin-muenster', firma='Malerfachbetrieb Wunderlin', web='wunderlin-maler.de', fonts='r9medifit', branche='Malerfachbetrieb',
    runde='Akquise DM 19.11.2026',
    title='Malerfachbetrieb Wunderlin – Farbe. Gestaltung. Freude. | Münster', desc='Malerfachbetrieb Wunderlin in Münster: Maler- und Tapezierarbeiten, Wandgestaltung, Fassadenanstriche, Wärmedämm-Verbundsysteme.',
    tel='0251 20805779', tel_i='+4925120805779', mail='info@wunderlin-maler.de', adresse='Kolbergstraße 3, 48147 Münster', google=None,
    cta='Beratung anfragen', nav=[('Fassade', 'fassade'), ('Leistungen', 'leistungen'), ('Projekte', 'projekte'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung'), ('Mobil', '0152 32753435')],
    form_opts=['Malerarbeiten', 'Tapezierarbeiten', 'Wohnraumgestaltung', 'Farbberatung', 'Fassade / WDVS', 'Sonstiges'],
    form_h3='Beratung anfragen', form_p='Stellen Sie uns gerne Ihre Fragen. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Kontaktieren <em>Sie uns!</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    vars=V.format(ink='#1d1d1d', mute='#555', p=P3, pi='#fff', dk=D3, s2='#f7f7e8', fh='"Poppins",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=0, ft=D3),
    css=css_base(P3, D3, '.lt-logo{font:700 30px/1 Poppins,sans-serif;color:#e2007a;letter-spacing:-.02em}.lt-logo small{display:block;font:500 11px/1.4 Inter,sans-serif;color:#555;letter-spacing:.12em;text-transform:uppercase}.ft .lt-logo{color:#fff}.ft .lt-logo small{color:#ccc}'))
S['logo_txt'] = 'wunderlin<small>Malerfachbetrieb</small>'
S['css2'] = hz('#f7f7e8', P3)
S['bot'] = BOT('Rolli', 'Ihr Maler-Lotse', 'Wunderlin', S, [
    ['Was machen Sie alles?', 'Maler- und Lackierarbeiten, Tapezierarbeiten, Wohnraumgestaltung, Farb- und Stilberatung, Fassadenrenovierung, WDVS und ökologische Farben.'],
    ['Wie erreiche ich Sie?', 'Telefon 0251 20805779 oder mobil 0152 32753435. Oder Sie nutzen das Formular.'],
    ['Wo sind Sie tätig?', 'In Münster und Umgebung.']],
    ['#fassade', '#leistungen', '#projekte', '#kontakt'])
S['img'] = {'h1.jpg': (R + 'wunderlin/i05.jpg', 0), 'h2.jpg': (R + 'wunderlin/i04.jpg', 0), 'h3.jpg': (R + 'wunderlin/i06.jpg', 0),
    'pr.jpg': (R + 'wunderlin/i07.jpg', 0), 'g1.jpg': (R + 'wunderlin/i08.jpg', 0), 'g2.jpg': (R + 'wunderlin/i10.jpg', 0), 'g3.jpg': (R + 'wunderlin/i03.jpg', 0),
    'g4.jpg': (R + 'wunderlin/i04.jpg', 0), 'g5.jpg': (R + 'wunderlin/i09.jpg', 0), 'ab.jpg': (R + 'wunderlin/i02.jpg', 0)}
S['body'] = b_wunderlin
S['social'] = [('Instagram', 'https://www.instagram.com/wunderlin_malerfachbetrieb/')]

# ─────────────────────────── 4 · Elektro Brockmann, Ahlen ───────────────────────────
def b_brockmann(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 45%'}, big='',
        ubar=[('Seit 1952', 'Meisterfachbetrieb'), ('KNX-Partner', 'Smart Home'), ('3 Generationen', 'Familie Brockmann')],
        ey='Elektro Brockmann · Ihr Elektriker in Ahlen',
        h1='Wir haben den <em>Strom im Griff.</em>',
        sub='Smart Home, Reparatur oder Großbaustelle: Unser Team plant und installiert Ihre Elektrotechnik. Innovativ. Zuverlässig. Kundenfreundlich.'))
        + marquee(['Elektroinstallation & Planung', 'Anlageninstallation', 'Netzwerktechnik', 'KNX-Partner', 'Smart Home', 'PV-Anlagen', 'Kreis Warendorf'], 'wm')
        + promo('smarthome', 'pr.jpg', 'KNX & Smart Home', 'Ihr Zuhause, <em>intelligent vernetzt.</em>',
                'Sensoren wie Bewegungsmelder und Thermostate geben Befehle an Aktoren, die Beleuchtung, Heizung oder Klima steuern. Wir verknüpfen und programmieren alles nach Ihren Wünschen. Bedienung über Schalter, Touchpanel, Fernbedienung oder Telefon.',
                ['KNX erfüllt die Normen EN 50090 und ISO/IEC 14543', 'Visualisierung für Sie als Endkunde', 'Strukturierte Netzwerke inklusive'], 'Smart Home anfragen', 'alt')
        + svc('leistungen', 'Leistungen', 'Privat, Gewerbe <em>und Industrie.</em>', 'Unsere Mitarbeiter bilden sich regelmäßig fort, um immer auf dem neuesten Stand der Energie- und Gebäudetechnik zu sein.', [
            ('Elektroinstallation & Planung', 'Vom Neubau bis zur Reparatur: Wir planen und installieren Ihre Elektrik.'),
            ('Anlageninstallation', 'Großbaustellen auch außerorts, mit dem passenden Equipment und genug Fachkräften.'),
            ('Netzwerktechnik', 'Strukturierte Netzwerke für Haus und Firma.'),
            ('KNX-Partner', 'Gebäudeautomation nach Norm, mit langfristiger Planungssicherheit.'),
            ('Smart Home', 'Licht, Heizung und Geräte bequem steuern.'),
            ('PV-Anlagen', 'Wir sind Ihr Partner für Photovoltaik, von der Planung bis zum Anschluss.')])
        + gallery('einblicke', 'Einblicke', 'Unser Betrieb <em>an der Westenmauer.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 50%'), ('g3.jpg', 'h2r', '50% 50%'), ('g4.jpg', 'w2', '50% 50%'), ('g5.jpg', 'w2', '50% 50%')])
        + ablauf('weg', 'So einfach geht es', 'Anrufen, planen, <em>Strom an.</em>', 'Alle Mitarbeiter sind im Umgang mit Kunden besonders geschult.', ABL)
        + story('ueber', 'Unsere Geschichte', 'Meisterbetrieb <em>seit 1952.</em>', [
            '1952 gründete Ferdinand Brockmann den Meisterfachbetrieb für Elektroinstallation an der Westenmauer in Ahlen.',
            '2001 übergab er die Firma an seinen Sohn Peter Brockmann, der sie gemeinsam mit seiner Frau Annegret führt. Seit 2017 ist auch die nächste Generation fest im Betrieb.'],
            'ab.jpg', 'Handwerklicher Meisterbetrieb Ferdinand Brockmann, gegründet 1953', cls='dk',
            tl=[('Peter Brockmann', 'Geschäftsleitung'), ('Annegret Brockmann', 'Geschäftsleitung')])
        + contact(s) + footer(s))

P4, D4 = '#2f6bff', '#0b1530'
S = SITES['brockmann'] = site(
    slug='elektro-brockmann-ahlen', firma='Elektro Brockmann', web='elektro-brockmann.de', fonts='r13opel', branche='Elektro-Meisterbetrieb',
    runde='Akquise DM 19.11.2026',
    title='Elektro Brockmann – Ihr Elektriker in Ahlen seit 1952', desc='Elektro Brockmann in Ahlen: Elektroinstallation und Planung, Anlageninstallation, Netzwerktechnik, KNX-Partner, Smart Home.',
    tel='02382 2057', tel_i='+4923822057', mail='info@elektro-brockmann.de', adresse='Westenmauer 7, 59227 Ahlen', google=None,
    cta='Termin anfragen', nav=[('Smart Home', 'smarthome'), ('Leistungen', 'leistungen'), ('Einblicke', 'einblicke'), ('Geschichte', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Büro', 'Mo – Fr, siehe Telefon')],
    form_opts=['Elektroinstallation', 'Reparatur', 'Smart Home / KNX', 'Netzwerktechnik', 'Rauchmelder', 'Gewerbe / Großbaustelle', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns auf die <em>Zusammenarbeit.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    vars=V.format(ink='#121621', mute='#555', p=P4, pi='#fff', dk=D4, s2='#eef2fb', fh='"Outfit",system-ui,sans-serif', fb='"Inter",system-ui,sans-serif', lh=48, ft=D4),
    css=css_base(P4, D4))
S['css2'] = hz(D4, '#7fa6ff', '#fff') + '.hz .sub,.hz .hz-ub div{color:rgba(255,255,255,.85)}.hz .hz-ub b{color:#fff}.hz .btn-o{color:#fff;border-color:rgba(255,255,255,.5)}.hz h1 em{color:#7fa6ff}'
S['bot'] = BOT('Volt', 'Ihr Elektro-Lotse', 'Brockmann', S, [
    ['Was machen Sie alles?', 'Elektroinstallation und Planung, Anlageninstallation, Netzwerktechnik, KNX und Smart Home, Rauchmelder.'],
    ['Wie bekomme ich einen Termin?', 'Am schnellsten per Telefon: 02382 2057. Oder Sie nutzen das Formular.'],
    ['Arbeiten Sie auch für Firmen?', 'Ja, für Privatkunden, Gewerbe und Industrie, auch auf Großbaustellen außerorts.']],
    ['#smarthome', '#leistungen', '#ueber', '#kontakt'])
S['img'] = {'logo.png': (R + 'brockmann/i07.jpg', 600), 'h1.jpg': (R + 'brockmann/i01.jpg', 0), 'h2.jpg': (R + 'brockmann/i158.jpg', 0),
    'pr.jpg': (R + 'brockmann/i154.jpg', 0), 'g1.jpg': (R + 'brockmann/i167.jpg', 0), 'g2.jpg': (R + 'brockmann/i149.jpg', 900), 'g3.jpg': (R + 'brockmann/i145.jpg', 900),
    'g4.jpg': (R + 'brockmann/i163.jpg', 900), 'g5.jpg': (R + 'brockmann/i177.jpg', 0), 'ab.jpg': (R + 'brockmann/i172.jpg', 900)}
S['body'] = b_brockmann
S['social'] = [('Instagram', 'https://www.instagram.com/elektrobrockmann/')]

# ─────────────────────────── 5 · Dachdeckermeisterbetrieb Münnich, Münster ───────────────────────────
MB = R + 'muennich/big/'
def b_muennich(s):
    return (hd(s, False) + hero_split(s, dict(imgs=['h1.jpg', 'h2.jpg'], pos={'h1.jpg': '50% 50%'}, big='',
        ubar=[('Meisterbetrieb', 'Dachdecker'), ('Steil & Flach', 'Neubau und Sanierung'), ('Münster', 'und Umgebung')],
        ey='Dachdeckermeisterbetrieb Münnich · Münster',
        h1='Ihr Dachdecker in <em>Münster und Umgebung.</em>',
        sub='Neubauten, Dachsanierungen, Flachdach, Gründach, Balkonsanierung, Fassadenverkleidung und Bauklempnerei. Persönlich beraten von Patrick und Marcel Münnich.'))
        + marquee(['Steildach', 'Flachdach', 'Gründach', 'Balkonsanierung', 'Fassadenverkleidung', 'Bauklempnerei', 'PV-Montage', 'Dachfenster'], 'wm')
        + promo('sanierung', 'pr.jpg', 'Dachsanierung', 'Steil- und Flachdach <em>in besten Händen.</em>',
                'Wir sind Ihr zuverlässiger Partner für die Sanierung von Steil- und Flachdächern sowie für Neubauten. Setzen Sie auf unsere Expertise für hochwertige Ergebnisse.',
                ['Steil-, Grün- und Flachdachsanierungen', 'Neubauten', 'Persönliche Beratung vor Ort'], 'Dachsanierung anfragen', 'alt')
        + svc('leistungen', 'Unsere Leistungen', 'Alles rund <em>ums Dach.</em>', 'Vom ersten Ziegel bis zur Wartung.', [
            ('Fassadenverkleidungen & Bauklempnerei', 'Lösungen, die ästhetisch ansprechend und funktional sind.'),
            ('Sturmschäden & Reparaturen', 'Wir beseitigen Sturmschäden und allgemeine Schäden an Ihrem Dach schnell und professionell.'),
            ('PV-Anlagen Montage', 'Wir sind spezialisiert auf die Installation von PV-Anlagen.'),
            ('Dachwartungen', 'Regelmäßige Inspektionen erkennen Schäden früh und verlängern die Lebensdauer Ihres Daches.'),
            ('Dachfensterlösungen', 'Mehr Licht und Frischluft für Ihre Räume.'),
            ('Gründächer & Balkone', 'Gründach anlegen, Balkon abdichten und sanieren.')])
        + gallery('arbeiten', 'Arbeiten', 'Ein Blick <em>aufs Dach.</em>', [
            ('g1.jpg', 'w2 h2r', '50% 50%'), ('g2.jpg', 'h2r', '50% 40%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%')])
        + ablauf('weg', 'So einfach geht es', 'Anfragen, prüfen, <em>dicht.</em>', 'Kontaktieren Sie uns gerne für eine persönliche Beratung.', ABL)
        + contact(s) + footer(s))

P5, D5 = '#b8651c', '#2a2522'
S = SITES['muennich'] = site(
    slug='dachdecker-muennich-muenster', firma='Dachdeckermeisterbetrieb Münnich GmbH', web='muennich-bedachung.de', fonts='r14alb', branche='Dachdecker-Meisterbetrieb',
    runde='Akquise DM 19.11.2026',
    title='Dachdeckermeisterbetrieb Münnich – Ihr Dachdecker in Münster', desc='Dachdeckermeisterbetrieb Münnich in Münster: Steil- und Flachdachsanierung, Gründach, Fassadenverkleidung, Bauklempnerei, PV-Montage, Dachfenster.',
    tel='0251 14905388', tel_i='+4925114905388', mail='info@muennich-bedachung.de', adresse='Heeremansweg 23, 48167 Münster', google=None,
    cta='Dach anfragen', nav=[('Sanierung', 'sanierung'), ('Leistungen', 'leistungen'), ('Arbeiten', 'arbeiten'), ('Ablauf', 'weg'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '7:00 – 16:30 Uhr'), ('Freitag', '7:00 – 13:30 Uhr')],
    form_opts=['Steildach', 'Flachdach', 'Gründach', 'Sturmschaden / Reparatur', 'PV-Montage', 'Dachfenster', 'Sonstiges'],
    form_h3='Dach anfragen', form_p='Gern auch mit Foto vom Dach. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Ihr Dach ist bei uns <em>in guten Händen.</em>', kt_p='Rufen Sie an oder schreiben Sie uns.',
    vars=V.format(ink='#1b1a19', mute='#555', p=P5, pi='#fff', dk=D5, s2='#f4efe9', fh='"Bitter",system-ui,serif', fb='"Source Sans 3",system-ui,sans-serif', lh=60, ft=D5),
    css=css_base(P5, D5))
S['css2'] = hz('#f4efe9', P5)
S['bot'] = BOT('Ziegel', 'Ihr Dach-Lotse', 'Münnich', S, [
    ['Was machen Sie alles?', 'Steil-, Flach- und Gründächer, Balkonsanierung, Fassadenverkleidung, Bauklempnerei, Sturmschäden, PV-Montage, Dachwartung und Dachfenster.'],
    ['Wie erreiche ich Sie?', 'Telefon 0251 14905388, Mo – Do 7:00 – 16:30 Uhr, Fr 7:00 – 13:30 Uhr.'],
    ['Wo sind Sie tätig?', 'In Münster und Umgebung.']],
    ['#sanierung', '#leistungen', '#arbeiten', '#kontakt'])
S['img'] = {'logo.png': (MB + 'afede5_4d60fb95d8194d5aa3b3fdd404d56eff~mv2.png', 500, 'trim'), 'h1.jpg': (MB + 'afede5_95b12c353d0e45c5ba398902d6cad1a6~mv2.jpeg', 0),
    'h2.jpg': (MB + 'afede5_ea157ad4a5e74c809730635853a9bd77~mv2.jpeg', 0), 'pr.jpg': (MB + 'afede5_1b83eea4dd26479b87263447bf8978cc~mv2.jpeg', 0),
    'g1.jpg': (MB + 'afede5_95b12c353d0e45c5ba398902d6cad1a6~mv2.jpeg', 0), 'g2.jpg': (MB + 'afede5_6f72f6eb487f4f08b8a97e1c6ae8ec4b~mv2.jpg', 0),
    'g3.jpg': (MB + 'afede5_5c5f3b088ee94c33881194a7e228c1de~mv2.jpg', 0), 'g4.jpg': (MB + 'afede5_ea157ad4a5e74c809730635853a9bd77~mv2.jpeg', 0)}
S['body'] = b_muennich
S['social'] = [('Instagram', 'https://www.instagram.com/dachdecker_muennich_gmbh/')]
