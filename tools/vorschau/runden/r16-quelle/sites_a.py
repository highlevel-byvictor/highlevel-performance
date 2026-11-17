"""Runde 16 · Teil A: Küchen Ellers, Küchengalerie am Dom, Küchen Geyer, Miele Hirnstein."""
from common import *
SITES = {}

# ───────────── 1. Küchen Ellers, Lorup ─────────────
def b_ellers(s):
    return (hd(s, False) + hero_x(s, dict(
        img='h-pic.jpg', pos='50% 60%', bg='emo.jpg',
        ey='Küchen Ellers · Ihr Küchenstudio in Lorup',
        h1='Traumküche gesucht? <em>Hier können Sie sie anfassen.</em>',
        sub='Schauen Sie sich unsere Einbauküchen „zum Anfassen“ an und überzeugen Sie sich selbst von Design, Funktion und Qualität. Beratung, Planung und Aufmaß bei Ihnen vor Ort gehören dazu.',
        g1=('Termin', 'auch außerhalb der Geschäftszeiten'), g2=('Aufmaß', 'bei Ihnen vor Ort')))
        + marquee(['Küchenstudio', 'Musterküchen zum Anfassen', 'Massivholzmöbel', 'Innenausbau', 'Fenster', 'Türen', 'Treppen', 'Ziepelkamp 31 · Lorup'], 'em')
        + gallery('musterkuechen', 'Unsere Musterküchen', 'Kommen Sie vorbei und <em>überzeugen Sie sich selbst.</em>', [
            ('m1.jpg', 'w2', '50% 55%'), ('m2.jpg', '', '50% 50%'), ('m3.jpg', '', '50% 50%'), ('m4.jpg', '', '50% 50%'), ('m5.jpg', '', '50% 50%'),
            ('m6.jpg', 'w2', '50% 50%'), ('m7.jpg', '', '50% 50%'), ('m8.jpg', '', '50% 50%')])
        + ablauf('so-gehts', 'So kommen Sie zur neuen Küche', 'In vier Schritten <em>zur Traumküche.</em>', 'Persönlich, in Ruhe und ganz nach Ihrem Zeitplan.', [
            ('Termin vereinbaren', 'Gern auch außerhalb unserer Geschäftszeiten, wenn es Ihnen besser passt.'),
            ('Musterküchen ansehen', 'Fronten, Arbeitsplatten und Geräte in unserem Küchenstudio in Lorup anfassen und ausprobieren.'),
            ('Planung', 'Wir planen Ihre Küche gemeinsam mit Ihnen, passend zu Raum, Alltag und Wünschen.'),
            ('Aufmaß vor Ort', 'Wir messen bei Ihnen zu Hause, damit am Ende alles passt.')], 'alt')
        + duo('sortiment', 'Mehr als Küchen', 'Alles aus einer Hand <em>in Lorup.</em>', 'Küchenstudio, Möbel und Innenausbau unter einem Dach.', [
            ('Küchenstudio', 'Einbauküchen', 'w-kueche.jpg', 'Unsere Küchenhersteller bieten beste Qualität und eine große Designvielfalt, von modern bis klassisch.', ['Musterküchen zum Ansehen', 'Beratung und Planung', 'Aufmaß vor Ort'], 'Beratung anfragen'),
            ('Möbel', 'Massivholzmöbel', 'w-holz.jpg', 'Holen Sie sich die Natur in Ihre Wohnung: Massivholzmöbel aus unserem Möbelsortiment, dazu Innenausbau, Fenster, Türen und Treppen.', ['Massivholz', 'Innenausbau', 'Fenster, Türen, Treppen'], 'Möbel anfragen')])
        + story('ueber-uns', 'Unser Standort', 'Ziepelkamp 31, <em>mitten in Lorup.</em>', [
            'Bei Küchen Ellers stehen die Küchen nicht im Katalog, sondern in unserer Ausstellung. Kommen Sie vorbei, nehmen Sie sich Zeit und erleben Sie Ihre neue Küche, bevor sie bei Ihnen steht.',
            'Kundinnen und Kunden kommen aus Lorup, Werlte, Sögel, Esterwegen, Friesoythe, Papenburg und dem ganzen Hümmling zu uns.'],
            'haus.jpg', cap='Küchen Ellers GmbH, Ziepelkamp 31 in Lorup', rev=True,
            extra=f'<a class="btn btn-o" style="margin-top:22px" href="https://kuechen-ellers.vprospekt.de/01-22" target="_blank" rel="noopener">Im Prospekt blättern ↗</a>')
        + reviews_ns(s, ['Hervorragende Beratung, und der Preis stimmt. Auch der Service nach dem Kauf ist ausgezeichnet.',
                         'Unsere Küche von Ellers ist einfach klasse. Preis und Leistung passen, die Qualität ist erstklassig und die Montage lief reibungslos.',
                         'Ausführliche Beratung und Küchen der gehobenen Mittelklasse.'], 'alt')
        + contact(s) + footer(s) + pop(dict(img='m1.jpg', ey='Musterküchen zum Anfassen', h='Ihr Termin, wann es Ihnen passt.', p='Auf Wunsch beraten wir Sie auch außerhalb unserer Geschäftszeiten.', btn='Termin anfragen')))

S = SITES['ellers'] = site(
    slug='kuechen-ellers-lorup', firma='Küchen Ellers GmbH', web='kuechen-ellers.de', fonts='r16ellers',
    title='Küchen Ellers – Küchenstudio in Lorup', desc='Küchen Ellers in Lorup: Musterküchen zum Anfassen, Beratung, Planung und Aufmaß vor Ort. Dazu Massivholzmöbel, Innenausbau, Fenster, Türen und Treppen.',
    tel='05954 9105', tel_i='+4959549105', mail='kundenservice@kuechen-ellers.de', adresse='Ziepelkamp 31, 26901 Lorup', google=None,
    cta='Beratungstermin anfragen', nav=[('Musterküchen', 'musterkuechen'), ('So geht’s', 'so-gehts'), ('Sortiment', 'sortiment'), ('Über uns', 'ueber-uns'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:00 – 13:00, 14:00 – 18:00'), ('Sa', '10:00 – 12:00'), ('', 'Termine auch außerhalb dieser Zeiten')],
    form_opts=['Neue Küche', 'Musterküche ansehen', 'Aufmaß vor Ort', 'Massivholzmöbel', 'Innenausbau, Fenster, Türen, Treppen', 'Sonstiges'],
    form_h3='Beratungstermin anfragen', form_p='Wir rufen Sie zurück und finden einen Termin, gern auch nach Feierabend.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Rufen Sie uns an unter 05954 9105 oder schreiben Sie uns. Wir melden uns persönlich.',
    vars='--bg:#fff;--ink:#231c22;--mute:#5a5058;--p:#A9236C;--p-ink:#fff;--a:#A9236C;--a-ink:#fff;--dk:#2a1f27;--s:#fff;--s2:#fbf7ec;--fh:"Open Sans",system-ui,sans-serif;--fb:"Open Sans",system-ui,sans-serif;--r:8px;--r2:12px;--br:6px;--mq-bg:#F8E732;--mq-ink:#2a1f27;--hd-bg:rgba(255,255,255,.97);--hd-ink:#231c22;--logo-h:46px;--ft-bg:#2a1f27;--hx-ar:3/2;--hx-r:12px',
    css=EMO('255,255,255', 'center 30%', pic_w=420, mpos='35% 25%', bgl=42) + '''
.hx h1{font-weight:800;font-style:italic;letter-spacing:-.02em;text-transform:none}.hx h1 em{display:block;font-style:italic;color:#A9236C}
.h2{font-weight:800;letter-spacing:-.02em}.h2 em{font-style:italic;color:#A9236C}.dk .h2 em{color:#F8E732}
.hx .pic{transform:rotate(1.2deg);border:8px solid #fff}.hx .gl{border-left:5px solid #F8E732}
.mq.em span{font-weight:800;font-style:italic}
.alt{background:linear-gradient(180deg,#fbf7ec,#fff)}
.hd .logo img{height:var(--logo-h);width:auto}.ft .logo img,.ft img{background:#fff;padding:6px 8px;border-radius:6px;height:50px}
.gl .grid figure{border-radius:10px}.duo .wd img{object-position:50% 60%}.duo .wd{min-height:430px}.duo .wd small{color:#F8E732}@media(max-width:820px){.duo .wd{min-height:340px}.duo .wd ul{display:none}.duo .wd .tx{padding:24px}}''')
S['bot'] = BOT('Ella', 'Ihre Küchen-Lotsin', 'Küchen Ellers', S, [
    ['Öffnungszeiten', 'Mo–Fr 9–13 und 14–18 Uhr, Sa 10–12 Uhr. Termine gern auch außerhalb dieser Zeiten.'],
    ['Musterküchen?', 'In unserem Küchenstudio in Lorup stehen viele Musterküchen zum Anfassen. Kommen Sie vorbei!'],
    ['Aufmaß vor Ort?', 'Ja, wir messen bei Ihnen zu Hause. Rufen Sie an: 05954 9105.']],
    ['#musterkuechen', '#so-gehts', '#sortiment', '#kontakt'])
S['img'] = {'logo.png': ('logos/ellers_raw.png', 0), 'emo.jpg': (PIX + '1979272.jpg', 0), 'h-pic.jpg': ('ellers/img/i001.jpg', 0),
    'm1.jpg': ('ellers/img/i027.jpg', 0), 'm2.jpg': ('ellers/img/i006.jpg', 0), 'm3.jpg': ('ellers/img/i016.jpg', 0), 'm4.jpg': ('ellers/img/i036.jpg', 0),
    'm5.jpg': ('ellers/img/i046.jpg', 0), 'm6.jpg': ('ellers/img/i060.jpg', 0), 'm7.jpg': ('ellers/img/i066.jpg', 0), 'm8.jpg': ('ellers/img/i031.jpg', 0),
    'w-kueche.jpg': ('ellers/img/i054.jpg', 0), 'w-holz.jpg': ('ellers/img/i215.jpg', 0), 'haus.jpg': ('ellers/img/i221.jpg', 0)}
S['body'] = b_ellers

# ───────────── 2. Küchengalerie am Dom, Haren (Ems) und Rhede (Ems) ─────────────
def b_galerie(s):
    return (hd(s, False) + hero_x(s, dict(
        img='emo.jpg', pos='45% 40%', bg='h-orig.jpg', alt='Familie kocht gemeinsam in der Küche',
        ey='Küchengalerie am Dom · Haren (Ems) und Rhede (Ems)',
        h1='Einfach eine Küche, <em>wie ich sie will.</em>',
        sub='Ein Ort zum Kochen, ein Raum zum Wohlfühlen, in dem sich die ganze Familie trifft. Wir entwickeln mit Ihnen zusammen eine Küche, die wirklich zu Ihnen passt. Persönliche Rundum-Beratung seit 2004.'))
        + promo('angebot', 'p-muster.jpg', 'Musterküchenabverkauf', 'Jetzt zugreifen, <em>solange der Vorrat reicht.</em>',
                'Wir machen Platz für neue Ideen in unserer Ausstellung. Ausgewählte Musterküchen gibt es jetzt zu stark reduzierten Preisen: hochwertige Markenküchen inklusive Elektrogeräten, sofort verfügbar.',
                ['Hochwertige Markenküchen', 'Inklusive Elektrogeräten', 'Sofort verfügbar'], 'Musterküche anfragen', 'alt')
        + tabs('leistungen', 'Mehr als gut. Komplett.', 'Was Sie von uns erwarten können? <em>Einfach alles.</em>', 'Gerne beraten wir Sie auch bei Ihnen zu Hause, auch außerhalb unserer Öffnungszeiten.', [
            ('Beratung & Finanzierung', 'l1.jpg', 'Umfangreiche persönliche Küchenberatung, auf Wunsch inklusive Finanzierung.', ['Persönlich', 'Auch zu Hause']),
            ('3D-Planung', 'l2.jpg', 'Wir planen Ihre Küche am Computer in 3D, dazu die Installationsplanung für Strom und Wasser.', ['3D-Computerplanung', 'Installationsplan']),
            ('Aufmaß vor Ort', 'l3.jpg', 'Wir messen bei Ihnen zu Hause, damit jedes Teil passt.', ['Zentimetergenau']),
            ('Lieferung & Montage', 'l4.jpg', 'Termingerechte Lieferung und Komplett-Montage inklusive Abluft-, Wasser- und Elektroanschluss, bis zur Verlegung der Fliesen.', ['Termingerecht', 'Alles angeschlossen']),
            ('Alte Küche raus', 'l5.jpg', 'Wir bauen Ihre alte Küche ab und entsorgen sie fachgerecht.', ['Demontage', 'Entsorgung'])])
        + gallery('ausstellung', 'Schauen Sie mal', 'Ob Hochglanz, matt oder Eiche: <em>hier ist alles dabei.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%'), ('g7.jpg', '', '50% 50%'), ('g8.jpg', '', '50% 50%')], 'alt')
        + team('team', 'Wir sind das Salz in der Suppe', '…wenn es um <em>Ihre Küche</em> geht.', 'Fachmänner und -frauen, die im Zusammenspiel beste Ergebnisse schaffen, an denen Sie lange Freude haben.', [
            ('t1.jpg', 'Rainer Book', 'Geschäftsführer'), ('t2.jpg', 'Magdalene Book', 'Geschäftsführerin'), ('t3.jpg', 'Andreas Jauer', 'Beratung und Verkauf'),
            ('t4.jpg', 'Herbert Kruse', 'Monteur'), ('t5.jpg', 'Gerrit Tellkamp', 'Monteur')])
        + orte('standorte', 'Zweimal im Emsland', 'Besuchen Sie uns <em>in Haren oder Rhede.</em>', 'Dazu unser reines Ausstellungsstudio in Emmeln, hier bitte immer mit Terminabsprache.', [
            ('Küchengalerie am Dom', 'Emsstraße 2 · 49733 Haren (Ems) · 05932 734280', ''),
            ('Küchengalerie im EDZ', 'Industriestraße 2 · 26899 Rhede (Ems) · 04964 604-554', 'Partner von TEAM 7 Naturholzküchen'),
            ('Ausstellungsstudio Emmeln', 'Nur nach Terminabsprache', '')], 'dk')
        + reviews_ns(s, ['Ich habe 2019 meine Küche bei der Küchengalerie am Dom gekauft und bin bis heute sehr zufrieden. Hochwertige Markenküche zu einem fairen Preis, pünktlich geliefert und sauber montiert.',
                         'Perfekte Küchenplanung: Alle Wünsche wurden berücksichtigt und ideal umgesetzt. Gerrit und Herbert haben die Küche perfekt montiert.',
                         'Toller Service vom Inhaber und seinem Team. Hochwertige Produkte, schnelle Lieferung und Montage.'])
        + contact(s) + footer(s) + pop(dict(img='p-muster.jpg', ey='Musterküchenabverkauf', h='Markenküchen stark reduziert.', p='Inklusive Elektrogeräten und sofort verfügbar, solange der Vorrat reicht.', btn='Jetzt anfragen')))

S = SITES['galerie'] = site(
    slug='kuechengalerie-am-dom-haren', firma='Küchengalerie am Dom', web='kuechengalerie-am-dom.de', fonts='r16galerie',
    title='Küchengalerie am Dom – Küchen in Haren (Ems) und Rhede', desc='Küchengalerie am Dom in Haren (Ems) und im EDZ Rhede: persönliche Küchenberatung seit 2004, 3D-Planung, Komplettmontage und Musterküchenabverkauf.',
    tel='05932 734280', tel_i='+495932734280', mail='info@kuechengalerie-am-dom.de', adresse='Emsstraße 2, 49733 Haren (Ems)', google=None,
    cta='Beratungstermin anfragen', nav=[('Angebot', 'angebot'), ('Leistungen', 'leistungen'), ('Ausstellung', 'ausstellung'), ('Team', 'team'), ('Standorte', 'standorte'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Fr', '09:00 – 18:00'), ('Sa', '09:00 – 13:00'), ('', 'Beratung zu Hause auch außerhalb der Öffnungszeiten')],
    form_opts=['Neue Küche', 'Musterküche aus dem Abverkauf', 'Beratung zu Hause', 'TEAM 7 Naturholzküche (Rhede)', 'Sonstiges'],
    form_lbl='Anliegen', form_orte=['Haren (Ems)', 'Rhede (Ems)', 'Egal'],
    form_h3='Beratungstermin anfragen', form_p='Wir melden uns persönlich und nehmen uns Zeit für Sie.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihre Nachricht.</em>', kt_p='Haren: 05932 734280 · Rhede: 04964 604-554. Oder einfach das Formular nutzen.',
    social=[('Facebook', 'https://www.facebook.com/pages/category/Kitchen-Cooking/K%C3%BCchengalerie-am-Dom-117069746760910/')],
    vars='--bg:#fff;--ink:#241d20;--mute:#5c5357;--p:#AF1F4A;--p-ink:#fff;--a:#AF1F4A;--a-ink:#fff;--dk:#2a1c22;--s:#fff;--s2:#faf3f5;--fh:"Nunito Sans",system-ui,sans-serif;--fb:"Nunito Sans",system-ui,sans-serif;--r:18px;--r2:26px;--br:999px;--mq-bg:#AF1F4A;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.96);--hd-ink:#241d20;--logo-h:54px;--ft-bg:#2a1c22;--hx-ar:3/2;--hx-r:26px',
    css='''.hx{--hx-op:.30;--hx-blur:14px;background:linear-gradient(160deg,#fff,#faf3f5)}.hx .pic{max-width:600px;justify-self:end}.hx{min-height:min(92vh,860px);display:flex;align-items:center}
.hx h1{font-weight:900;letter-spacing:-.02em}.hx h1 em{display:block;font:400 1.02em/1.15 "Pacifico",cursive;color:#AF1F4A;letter-spacing:0;margin-top:.12em}
.h2{font-weight:900;letter-spacing:-.02em}.h2 em{font:400 .98em "Pacifico",cursive;color:#AF1F4A;letter-spacing:0}.dk .h2 em{color:#ff8fb0}
.hx .gl{border-radius:999px;padding:12px 22px}.promo figure{max-width:460px;justify-self:center}.promo figure img{border-radius:26px}
.alt{background:linear-gradient(180deg,#faf3f5,#fff)}
.tm .grid figure div{aspect-ratio:1/1;border-radius:50%;overflow:hidden}.tm .grid figure div img{object-position:50% 25%}.tm .grid{grid-template-columns:repeat(5,1fr)}
@media(max-width:900px){.tm .grid{grid-template-columns:repeat(2,1fr)}}
.ft img{background:#fff;padding:8px 12px;border-radius:12px;height:56px}''')
S['bot'] = BOT('Galina', 'Ihre Küchen-Lotsin', 'der Küchengalerie am Dom', S, [
    ['Musterküchen?', 'Gerade läuft unser Musterküchenabverkauf: Markenküchen inkl. Elektrogeräten stark reduziert, solange der Vorrat reicht.'],
    ['Standorte', 'Haren (Ems), Emsstraße 2, und Rhede (Ems), Industriestraße 2 im EDZ. Dazu das Ausstellungsstudio Emmeln nach Termin.'],
    ['Öffnungszeiten', 'Mo–Fr 9–18 Uhr, Sa 9–13 Uhr. Beratung zu Hause auch außerhalb dieser Zeiten.']],
    ['#angebot', '#leistungen', '#team', '#kontakt'])
S['img'] = {'logo.png': ('galerie/img/i001.jpg', 0, 'alphacrop'), 'h-orig.jpg': ('galerie/img/i190.jpg', 0), 'emo.jpg': (PIX + '9998442.jpg', 0),
    'p-muster.jpg': ('galerie/img/i189.jpg', 0),
    'l1.jpg': ('galerie/img/i180.jpg', 0), 'l2.jpg': ('galerie/img/i194.jpg', 0), 'l3.jpg': ('galerie/img/i183.jpg', 0), 'l4.jpg': ('galerie/img/i182.jpg', 0), 'l5.jpg': ('galerie/img/i179.jpg', 0),
    'g1.jpg': ('galerie/img/i188.jpg', 0), 'g2.jpg': ('galerie/img/i181.jpg', 0), 'g3.jpg': ('galerie/img/i184.jpg', 0), 'g4.jpg': ('galerie/img/i185.jpg', 0),
    'g5.jpg': ('galerie/img/i187.jpg', 0), 'g6.jpg': ('galerie/img/i180.jpg', 0), 'g7.jpg': ('galerie/img/i064.jpg', 0), 'g8.jpg': ('galerie/img/i065.jpg', 0),
    't1.jpg': ('galerie/img/i196.jpg', 0), 't2.jpg': ('galerie/img/i197.jpg', 0), 't3.jpg': ('galerie/img/i198.jpg', 0), 't4.jpg': ('galerie/img/i199.jpg', 0), 't5.jpg': ('galerie/img/i200.jpg', 0)}
S['body'] = b_galerie
S['logo_ft'] = 'logo.png'

# ───────────── 3. Küchenspezialhaus Geyer, Westoverledingen ─────────────
def b_geyer(s):
    return (hd(s, False) + hero_comp(s, dict(
        imgs=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos0='50% 55%',
        ey='Küchen Geyer · das Küchenspezialhaus in Völlenerfehn',
        h1='Ihre 1. Adresse für <em>Qualitätsküchen.</em>',
        sub='Eine Qualitätsküche zum fairen Preis, individuell und ohne Zeitdruck am Computer geplant. Seit über 50 Jahren, und gerne auch bei Ihnen zu Hause.',
        badge=('Über 50 Jahre', 'Küchenspezialhaus in Westoverledingen')))
        + marquee(['Küchenplanung ohne Zeitdruck', 'Beratung bei Ihnen zu Hause', 'Aufmaß und Vollservice', 'Fliesen- und Installationspläne', 'Quooker nachrüsten', 'Hauptstraße 229'], 'gy')
        + scroller('kuechen', 'Küchenideen', 'Finden Sie <em>Ihren Stil.</em>', 'Von der Landhausküche bis zur grifflosen Designküche: Wir planen sie individuell für Ihren Raum.', [
            ('Landhaus, hell und gemütlich', 'k1.jpg', 'Klassische Fronten, warme Töne.', '50% 50%'),
            ('Modern in Weiß', 'k2.jpg', 'Klar, hell und pflegeleicht.', '50% 50%'),
            ('Schwarz mit Charakter', 'k3.jpg', 'Dunkle Fronten, starke Wirkung.', '50% 50%'),
            ('Offen und wohnlich', 'k4.jpg', 'Küche und Wohnraum in einem.', '50% 50%'),
            ('Mit Kochinsel', 'k5.jpg', 'Kochen mitten im Geschehen.', '50% 50%'),
            ('Natürlich in Eiche', 'k6.jpg', 'Holz, das Wärme bringt.', '50% 50%')])
        + svc('service', 'Unser Service für Sie', 'Wir kümmern uns <em>um alles.</em>', 'Nur wenn Sie zufrieden sind, sind wir es auch.', [
            ('Raumausmessung', 'Bauseitiges Aufmaß und Vollservice bei Ihnen vor Ort.'),
            ('Pläne', 'Wir erstellen Fliesenpläne und Installationspläne für Ihren Handwerker.'),
            ('Kostenvoranschläge', 'Im Schadensfall erstellen wir den Kostenvoranschlag für Ihre Versicherung.'),
            ('Gutachten', 'Sachverständigen- und Gutachtenerstellung rund um die Küche.')], 'alt')
        + promo('aktion', 'p-quooker.jpg', 'Aktion', 'Wasserhahn raus, <em>Quooker rein.</em>',
                'Um den Komfort eines Quookers zu genießen, müssen Sie nicht auf Ihre nächste Küche warten. Ein Quooker lässt sich unkompliziert in Ihrer bestehenden Küche nachrüsten. Wir beraten Sie gern.',
                ['Nachrüsten in der bestehenden Küche', 'Beratung bei uns im Haus'], 'Beratung anfragen')
        + team('team', 'Lernen Sie uns kennen', 'Seit über 50 Jahren <em>ist der Kunde bei uns König.</em>', 'Geschäftsführer ist Horst Geyer. Neben einer großen Auswahl legen wir besonderen Wert auf eine fundierte und kompetente Beratung.', [
            ('t1.jpg', 'Susanne Holtermann', 'Team Küchen Geyer'), ('t3.jpg', 'Wilma Geyer', 'Geschäftsführung-Vertretung'), ('t4.jpg', 'Anne Peper', 'Service und Beratung')], 'dk')
        + reviews(s, ['Unsere Küche ist 25 Jahre alt und war von Küchen Geyer. Für neue Geräte wurde die Küche perfekt angepasst. Ein riesiges Dankeschön!',
                      'Herr Geyer ist sehr kompetent und hilfsbereit. Ich hatte ein großes Problem, und er hat schnell und zu einem fairen Preis ein tolles Ergebnis erreicht.',
                      'Herr Geyer gibt sich beim Verkauf viel Mühe, damit am Ende alles perfekt passt. Die Montage läuft ruhig und reibungslos.',
                      'Kompetente und freundliche Leute, schnelle und unkomplizierte Beschaffung. Immer wieder gern.'])
        + contact(s) + footer(s) + pop(dict(img='p-quooker.jpg', ey='Aktion', h='Quooker nachrüsten', p='Kochendes Wasser direkt aus dem Hahn, auch in Ihrer bestehenden Küche.', btn='Jetzt anfragen')))

S = SITES['geyer'] = site(
    slug='kuechen-geyer-westoverledingen', firma='Küchenspezialhaus Geyer GmbH', web='kuechen-geyer.de', fonts='r16geyer',
    title='Küchen Geyer – das Küchenspezialhaus in Westoverledingen', desc='Küchenspezialhaus Geyer in Völlenerfehn: Qualitätsküchen zum fairen Preis seit über 50 Jahren, Planung ohne Zeitdruck, Beratung auch zu Hause.',
    tel='04961 94550', tel_i='+49496194550', mail='geyer.gmbh@ewetel.net', adresse='Hauptstraße 229, 26810 Westoverledingen', google=('4,8', 12),
    cta='Beratungstermin vereinbaren', nav=[('Küchenideen', 'kuechen'), ('Service', 'service'), ('Aktion', 'aktion'), ('Team', 'team'), ('Kontakt', 'kontakt')],
    hours=[('Ausstellung Mo – Fr', '10:00 – 12:00, 14:30 – 18:00'), ('Sa + So', 'nach Termin: 0172 4219423'), ('Lager Mo – Fr', '06:00 – 12:00 nach Absprache')],
    form_opts=['Neue Küche', 'Beratung zu Hause', 'Quooker nachrüsten', 'Kostenvoranschlag / Gutachten', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Wir planen Ihre Küche individuell und ohne Zeitdruck. Wir rufen Sie zurück.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Wir freuen uns <em>auf Ihren Besuch.</em>', kt_p='Rufen Sie an unter 04961 94550 oder mobil 0172 4219423. Samstags und sonntags nach Termin.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars='--bg:#fff;--ink:#16203a;--mute:#525a6c;--p:#2457B8;--p-ink:#fff;--a:#2457B8;--a-ink:#fff;--dk:#14203d;--s:#fff;--s2:#f2f5fb;--fh:"Montserrat",system-ui,sans-serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:6px;--r2:10px;--br:4px;--mq-bg:#14203d;--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:#16203a;--logo-h:62px;--ft-bg:#101a33;--hp-bg:linear-gradient(165deg,#fff 0%,#f2f5fb 60%,#e8eef9 100%)',
    css='''.hp h1,.h2{font-weight:800;letter-spacing:-.025em;line-height:1.05}.hp h1{font-size:clamp(34px,5vw,74px);hyphens:manual}.hp h1 em,.h2 em{font-style:normal;color:#2457B8}.dk .h2 em{color:#8fb2ff}
.hp .comp .badge{background:#2457B8;color:#fff}.hp .comp .badge b{color:#fff}
.mq.gy span{font-family:var(--fh);font-weight:700}.alt{background:var(--s2)}.sv .row div{border-top:4px solid #2457B8}
.tm .grid{grid-template-columns:repeat(3,minmax(0,280px));justify-content:center}.tm .grid figure div{aspect-ratio:1/1}.tm .grid figure div img{object-position:50% 25%}
.promo figure{max-width:440px;justify-self:center}.ft img{background:#fff;padding:8px 12px;border-radius:8px;height:62px}
@media(max-width:820px){.tm .grid{grid-template-columns:1fr 1fr}}''')
S['bot'] = BOT('Greta', 'Ihre Küchen-Lotsin', 'Küchen Geyer', S, [
    ['Öffnungszeiten', 'Ausstellung Mo–Fr 10–12 und 14:30–18 Uhr. Sa und So nach Termin: 0172 4219423.'],
    ['Beratung zu Hause?', 'Ja, gerne beraten wir Sie auch bei Ihnen zu Hause. Rufen Sie an: 04961 94550.'],
    ['Quooker nachrüsten?', 'Ein Quooker lässt sich unkompliziert in Ihrer bestehenden Küche nachrüsten. Wir beraten Sie gern.']],
    ['#kuechen', '#service', '#aktion', '#kontakt'])
S['img'] = {'logo.png': ('geyer/img/i000.jpg', 0, 'trimalpha'), 'h1.jpg': (PIX + '7070676.jpg', 0), 'h2.jpg': ('geyer/img/i001.jpg', 1000), 'h3.jpg': ('geyer/img/i009.jpg', 1000),
    'k1.jpg': ('geyer/img/i001.jpg', 1100), 'k2.jpg': ('geyer/img/i002.jpg', 1100), 'k3.jpg': ('geyer/img/i003.jpg', 1100), 'k4.jpg': ('geyer/img/i006.jpg', 1100), 'k5.jpg': ('geyer/img/i007.jpg', 1100), 'k6.jpg': ('geyer/img/i009.jpg', 1100),
    'p-quooker.jpg': ('geyer/img/i008.jpg', 1100),
    't1.jpg': ('geyer/team0.jpg', 0), 't3.jpg': ('geyer/team2.jpg', 900), 't4.jpg': ('geyer/team3.jpg', 0)}
S['body'] = b_geyer

# ───────────── 4. Miele Hirnstein, Meppen ─────────────
def b_hirnstein(s):
    return (hd(s) + hero_slides(s, dict(
        slides=['h1.jpg', 'h2.jpg', 'h3.jpg'], pos={'h1.jpg': '60% 50%', 'h2.jpg': '60% 50%', 'h3.jpg': '50% 45%'},
        ey='Hirnstein · Küchen & Hausgeräte in Meppen',
        h1='Erleben Sie, was eine Küche ist: <em>wertvoll fürs Leben.</em>',
        sub='Küchenstudio der Marken Schüller und next125, Premium-Händler für Miele-Hausgeräte und autorisierter Kundendienst. Beratung, Planung, Montage und Service aus einer Hand.',
        ubar=[('1971', 'gegründet von Friedrich Hirnstein'), ('2. Generation', 'geführt von Andreas Hirnstein'), ('ca. 90 %', 'aller Reparaturen beim ersten Besuch')]))
        + marquee(['Schüller', 'next125', 'Miele', 'Miele Professional', 'Smeg', 'Rösle', 'Franke', 'Fürstenbergstraße 27'], 'hm')
        + panels('leistungen', 'Unsere Leistungen', 'Alles rund um <em>Küche und Haushalt.</em>', 'Fahren Sie mit der Maus über die Bilder.', [
            ('Küchen', 'l1.jpg', 'Schüller- und next125-Küchen mit wohnlicher Küchenarchitektur und vielen Neuheiten. Dazu passende Tische und Stühle.', '50% 50%'),
            ('Musterküchen', 'l2.jpg', 'Ausgewählte Musterküchen aus unserer Ausstellung zu besonderen Preisen.', '50% 50%'),
            ('Hausgeräte', 'l3.jpg', 'Das gesamte Programm an Miele-Stand- und Einbaugeräten, fachgerecht geliefert und angeschlossen.', '50% 50%'),
            ('Kundendienst', 'l4.jpg', 'Unsere Fahrzeuge haben alle gängigen Miele-Ersatzteile an Bord. So erledigen wir rund 90 % der Reparaturen gleich beim ersten Besuch.', '50% 50%')])
        + promo('musterkuechen', 'p-muster.jpg', 'Musterküchen', 'Ausstellungsküchen <em>zum Sonderpreis.</em>',
                'Schüller- und next125-Musterküchen aus unserer Ausstellung, fertig geplant und sofort zu besichtigen. Für die Details sprechen Sie uns einfach an.',
                ['Schüller und next125', 'In der Ausstellung ansehen', 'Auf Ihren Raum angepasst'], 'Musterküche anfragen', 'alt')
        + gallery('ausstellung', 'Unsere Ausstellung', 'Kommen Sie vorbei, <em>einfach so.</em>', [
            ('g1.jpg', 'w2', '50% 50%'), ('g2.jpg', '', '50% 50%'), ('g3.jpg', '', '50% 50%'), ('g4.jpg', '', '50% 50%'), ('g5.jpg', '', '50% 50%'), ('g6.jpg', 'w2', '50% 50%'), ('g7.jpg', '', '50% 50%'), ('g8.jpg', '', '50% 50%')])
        + story('ueber-uns', 'Familienunternehmen seit 1971', 'Zwei Generationen, <em>ein Anspruch.</em>', [
            'Friedrich Hirnstein hat das Unternehmen 1971 gegründet. Heute führt sein Sohn Andreas Hirnstein es in zweiter Generation weiter.',
            'Im Küchen-Einrichtungshaus an der Fürstenbergstraße bekommen Sie kompetente Beratung, professionelle Planung, fachgerechte Montage und den autorisierten Kundendienst. Alles aus einer Hand.'],
            'haus.jpg', cap='Hirnstein Küchen & Hausgeräte, Fürstenbergstraße 27 in Meppen', tl=[('1971', 'Gründung durch Friedrich Hirnstein'), ('Heute', 'Andreas Hirnstein in 2. Generation')], rev=True, cls='dk')
        + reviews(s, ['Ein tolles Unternehmen, fachlich unschlagbar. Unsere Küche ist 15 Jahre alt, und alle Geräte halten bis heute ohne eine einzige Reparatur.',
                      'Wir hatten Angebote von fünf Küchenstudios. Nirgends waren Fachwissen, Beratung, Auswahl, Ehrlichkeit und Transparenz so gut wie bei Herrn Hirnstein. Auch der Preis war unschlagbar.',
                      'Hervorragende Beratung, tolle Verbesserungsvorschläge und eine schnelle Montage zum fairen Preis. Besser geht es nicht.',
                      'Unsere Traumküche wurde perfekt geplant und einwandfrei montiert. Wir sind rundum zufrieden.'])
        + contact(s) + footer(s) + pop(dict(img='p-muster.jpg', ey='Musterküchen', h='Ausstellungsküchen zum Sonderpreis', p='Schüller und next125, sofort zu besichtigen in Meppen.', btn='Jetzt anfragen')))

S = SITES['hirnstein'] = site(
    slug='hirnstein-kuechen-meppen', firma='Hirnstein GmbH', web='hirnstein-kuechen.de', fonts='r16hirnstein',
    title='Hirnstein – Küchen & Hausgeräte in Meppen', desc='Hirnstein in Meppen seit 1971: Schüller- und next125-Küchen, Miele-Premium-Händler, Musterküchen und autorisierter Kundendienst.',
    tel='05931 12234', tel_i='+49593112234', mail='info@hirnstein-kuechen.de', adresse='Fürstenbergstraße 27, 49716 Meppen', google=('4,8', 26),
    logo_txt='<span class="hl-l"><b>Hirnstein</b><i>Küchen &amp; Hausgeräte</i></span>',
    cta='Beratungstermin vereinbaren', nav=[('Leistungen', 'leistungen'), ('Musterküchen', 'musterkuechen'), ('Ausstellung', 'ausstellung'), ('Über uns', 'ueber-uns'), ('Kontakt', 'kontakt')],
    hours=[('Mo – Do', '09:00 – 13:00, 14:30 – 18:00'), ('Fr', '09:00 – 13:00'), ('Sa', '09:30 – 13:00')],
    form_opts=['Neue Küche', 'Musterküche', 'Miele-Hausgeräte', 'Kundendienst / Reparatur', 'Gewerbegeräte', 'Sonstiges'],
    form_h3='Beratungstermin vereinbaren', form_p='Wir rufen Sie zurück. Oder kommen Sie einfach vorbei.', form_btn='Rückruf anfordern',
    kt_ey='Kontakt', kt_h2='Einfach vorbeikommen <em>oder anrufen.</em>', kt_p='Rufen Sie an unter 05931 12234. Wir freuen uns auf Ihren Besuch in Meppen.',
    rv_h2='Das sagen <em>unsere Kunden.</em>',
    vars='--bg:#fff;--ink:#2a1714;--mute:#5f514d;--p:#B63D32;--p-ink:#fff;--a:#B63D32;--a-ink:#fff;--dk:#3C1D17;--s:#fff;--s2:#f7f2f0;--fh:"Roboto Slab",Georgia,serif;--fb:"Source Sans 3",system-ui,sans-serif;--r:4px;--r2:8px;--br:3px;--hero-ov:linear-gradient(95deg,rgba(40,20,16,.9) 0%,rgba(40,20,16,.55) 52%,rgba(40,20,16,.08) 100%);--mq-bg:#B63D32;--mq-ink:#fff;--hd-bg:rgba(60,29,23,.96);--hd-ink:#fff;--logo-h:46px;--ft-bg:#2a1410',
    css='''.hs h1,.h2{font-weight:600;letter-spacing:-.02em;line-height:1.06}.hs h1{font-size:clamp(38px,4.8vw,72px)}.hs h1 em,.h2 em{font-style:normal;color:#e8705f}.h2 em{color:#B63D32}.dk .h2 em{color:#ff9a8a}
.hl-l{display:inline-flex;flex-direction:column;line-height:1;color:#fff}.hl-l b{font:500 30px/1 var(--fh);letter-spacing:.01em}.hl-l i{font:400 11px/1.4 var(--fb);letter-spacing:.32em;text-transform:uppercase;font-style:normal;opacity:.85;margin-top:4px}
.ft .hl-l{color:#fff}.mq.hm span{font-family:var(--fh)}.alt{background:var(--s2)}.st figure img{object-position:50% 50%}''')
S['bot'] = BOT('Hanno', 'Ihr Küchen-Lotse', 'Hirnstein', S, [
    ['Öffnungszeiten', 'Mo–Do 9–13 und 14:30–18 Uhr, Fr 9–13 Uhr, Sa 9:30–13 Uhr.'],
    ['Miele-Kundendienst?', 'Ja, wir sind autorisierter Miele-Kundendienst. Rund 90 % der Reparaturen erledigen wir beim ersten Besuch.'],
    ['Musterküchen?', 'Schüller- und next125-Musterküchen gibt es zum Sonderpreis. Rufen Sie an: 05931 12234.']],
    ['#leistungen', '#musterkuechen', '#ausstellung', '#kontakt'])
H = 'hirnstein/hi/'
S['img'] = {'h1.jpg': (H + 'i024.jpg', 2200), 'h2.jpg': (H + 'i018.jpg', 2200), 'h3.jpg': (H + 'i000.jpg', 2200),
    'l1.jpg': (H + 'i025.jpg', 1400), 'l2.jpg': (H + 'i020.jpg', 1400), 'l3.jpg': (H + 'i033.jpg', 1400), 'l4.jpg': (H + 'i047.jpg', 1400),
    'p-muster.jpg': (H + 'i011.jpg', 1200),
    'g1.jpg': (H + 'i006.jpg', 1400), 'g2.jpg': (H + 'i012.jpg', 900), 'g3.jpg': (H + 'i027.jpg', 900), 'g4.jpg': (H + 'i030.jpg', 900),
    'g5.jpg': (H + 'i026.jpg', 900), 'g6.jpg': (H + 'i009.png', 1400), 'g7.jpg': (H + 'i021.jpg', 900), 'g8.jpg': (H + 'i034.jpg', 900),
    'haus.jpg': (H + 'i000.jpg', 1400)}
S['body'] = b_hirnstein
