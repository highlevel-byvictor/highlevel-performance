"""Runde 19 · Musterseite: Schornsteinfeger-Meisterbetrieb Michael Höckelmann, Bersenbrück."""
from common import *
SITES = {}

def b_hoeckelmann(s):
    return (hd(s, False) + hero_split(s, dict(
        imgs=['h1.jpg', 'h2.jpg'], big='',
        ubar=[('Meister', 'Schornsteinfegermeister'), ('Energieberater', 'für Gebäude, HWK'), ('DIN 14676', 'Fachkraft Rauchwarnmelder')],
        ey='Schornsteinfeger-Meisterbetrieb Michael Höckelmann · Bersenbrück',
        h1='Ihr Experte für Sicherheit, <em>Umwelt und Energie.</em>',
        sub='Als Schornsteinfeger sind wir Ihr Ansprechpartner rund ums Haus: Brandschutz, Emissionsschutz und neutrale Beratung zur Energieeinsparung. Sauber, pünktlich und mit größter Sorgfalt.'))
        + marquee(['Schornsteinfegerarbeiten', 'Energieausweis', 'Rauchwarnmelder', 'Gashausschau', 'Feuerungstechnische Beratung', 'Energieberatung'], 'wm')
        + svc('leistungen', 'Dienstleistungen', 'Weit mehr als <em>Schornsteinreinigung.</em>', 'Das Berufsbild des Schornsteinfegers hat sich gewandelt. Wir sind heute auch neutraler und unabhängiger Berater.', [
            ('Schornsteinfegerarbeiten', 'Reinigen, Messen und Überprüfen. Seit vielen Jahrhunderten sorgen Schornsteinfeger mit ihrer Arbeit für Sicherheit.'),
            ('Energieausweis', 'Die verbriefte Verbrauchsangabe Ihres Gebäudes. Jeder kennt den Verbrauch seines Pkw, kaum jemand den seines Eigenheims.'),
            ('Rauchwarnmelder', 'Als Fachkraft für Rauchwarnmelder nach DIN 14676 planen, installieren und prüfen wir Ihre Melder.'),
            ('Gashausschau', 'Wir kontrollieren Ihre Gasleitung und geben Ihnen ein sicheres Gefühl.'),
            ('Feuerungstechnische Beratung', 'Moderne Feuerungsanlagen stellen hohe Ansprüche an Messtechnik und Know-how. Wir beraten vor dem Kauf.'),
            ('Energieberatung', 'Wo lässt sich bei Ihnen Energie sparen, und mit welchem Aufwand? Wir zeigen es Ihnen neutral.')])
        + promo('ausweis', 'dach.jpg', 'Energieausweis', 'Was verbraucht <em>Ihr Haus wirklich?</em>',
                'Ein Energieausweis ist die verbriefte Verbrauchsangabe Ihres Gebäudes. Als Gebäudeenergieberater (HWK) erstellen wir ihn und sagen Ihnen ehrlich, wo Energie verloren geht.',
                ['Vom Gebäudeenergieberater im Handwerk', 'Neutral und unabhängig', 'Termin direkt bei Ihnen zu Hause'], 'Energieausweis anfragen', 'alt')
        + ablauf('weg', 'So einfach geht es', 'Anfragen, Termin, <em>erledigt.</em>', 'Sprechen Sie Ihre persönlichen Wünsche und Anregungen gerne an.', [
            ('Anliegen schicken', 'Über das Formular oder direkt per Telefon. Sagen Sie kurz, worum es geht.'),
            ('Termin abstimmen', 'Wir melden uns bei Ihnen und finden einen Termin, der passt.'),
            ('Arbeit vor Ort', 'Alle Arbeiten führen wir sauber, pünktlich und mit größter Sorgfalt aus.')])
        + story('ueber', 'Über uns', 'Ein kompetentes und <em>freundliches Team.</em>', [
            'Als Schornsteinfeger-Betrieb sind wir für Sie der richtige Ansprechpartner, wenn es um Brandschutz, Umweltschutz, Energieeinsparung oder neutrale Beratung geht.',
            'Mit Michael Höckelmann und seinem Mitarbeiter Jan Plagge entscheiden Sie sich für ein Team, das seine Arbeit ernst nimmt.'], 'team.jpg', 'Michael Höckelmann (links) und Jan Plagge', cls='dk',
            tl=[('Michael Höckelmann', 'Schornsteinfegermeister, Gebäudeenergieberater HWK'), ('Jan Plagge', 'Mitarbeiter')])
        + contact(s) + footer(s))

S = SITES['hoeckelmann'] = site(
    slug='schornsteinfeger-hoeckelmann-bersenbrueck', firma='Schornsteinfeger-Meisterbetrieb Michael Höckelmann', web='schornsteinfeger-hoeckelmann.de', fonts='r18rec',
    title='Schornsteinfeger Michael Höckelmann – Meisterbetrieb in Bersenbrück', desc='Schornsteinfeger-Meisterbetrieb Michael Höckelmann in Bersenbrück: Schornsteinfegerarbeiten, Energieausweis, Rauchwarnmelder, Gashausschau und Energieberatung.',
    tel='05439 6075861', tel_i='+4954396075861', mail='mail@schornsteinfeger-hoeckelmann.de', adresse='Priggenhagener Straße 108, 49593 Bersenbrück', google=None,
    cta='Termin anfragen', nav=[('Leistungen', 'leistungen'), ('Energieausweis', 'ausweis'), ('Ablauf', 'weg'), ('Über uns', 'ueber'), ('Kontakt', 'kontakt')],
    hours=[('Termine', 'nach Vereinbarung'), ('Mobil', '0160 4444960')],
    form_opts=['Schornsteinfegerarbeiten', 'Energieausweis', 'Rauchwarnmelder', 'Gashausschau', 'Beratung neue Feuerstätte', 'Energieberatung', 'Sonstiges'],
    form_h3='Termin anfragen', form_p='Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Zum Glück gibt es <em>den Schornsteinfeger.</em>', kt_p='Rufen Sie an oder schreiben Sie uns. Wir kümmern uns.',
    vars=V.format(ink='#171715', mute='#575757', p='#E3000B', pi='#fff', dk='#171715', s2='#f5f4f2', fh='"Noto Sans",system-ui,sans-serif', fb='"Noto Sans",system-ui,sans-serif', lh=64, ft='#171715'),
    css='''.h2,.hz h1{font-weight:800;letter-spacing:-.025em}.h2 em,.hz h1 em{font-style:normal;color:#E3000B}.dk .h2 em{color:#ff6b72}.mq.wm span{font-weight:700;font-size:15px}
.alt{background:var(--s2)}.sv .row div{border-top:4px solid #E3000B}.st.dk{background:#171715;color:#fff}.st.dk .lead{color:rgba(255,255,255,.86)}.st.dk .tl b{color:#fff}.rd .road div h3{color:#E3000B}
#ueber figure{max-width:440px;justify-self:center}.ft img{background:#fff;padding:8px 12px;height:70px}''')
S['css2'] = '.hz{--hz-bg:#fff;--hz-ink:#171715;--hz-mute:#575757;--hz-stroke:rgba(227,0,11,.13);--hz-cols:46fr 54fr}.hz h1{font-size:clamp(36px,4.3vw,68px)}.hz .ey{color:#E3000B}@media(max-width:820px){.hz h1{font-size:33px;hyphens:none}}'
S['bot'] = BOT('Ruß', 'Ihr Schornsteinfeger-Lotse', 'Höckelmann', S, [
    ['Was machen Sie alles?', 'Schornsteinfegerarbeiten, Energieausweis, Rauchwarnmelder, Gashausschau, feuerungstechnische Beratung und Energieberatung.'],
    ['Wie bekomme ich einen Termin?', 'Am schnellsten per Telefon: 05439 6075861 oder mobil 0160 4444960. Oder Sie nutzen das Formular.'],
    ['Brauche ich einen Energieausweis?', 'Bei Verkauf oder Vermietung in der Regel ja. Wir beraten Sie dazu und erstellen ihn.']],
    ['#leistungen', '#ausweis', '#ueber', '#kontakt'])
S['img'] = {'logo.png': I('hoeckelmann', 3, 0), 'h1.jpg': (PIX19 + '2792895.jpg', 0), 'h2.jpg': (PIX19 + '8114188.jpg', 0),
    'dach.jpg': (PIX19 + '7313645.jpg', 0), 'team.jpg': ('/home/claude/r19raw/hoeckelmann/team2x.jpg', 0)}
S['body'] = b_hoeckelmann
