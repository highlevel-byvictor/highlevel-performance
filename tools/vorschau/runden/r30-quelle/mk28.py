PL = '<span><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></span>'

def bewerten(s, du=False):
    """Band unter den Stimmen: zufriedene Patienten zur Google-Bewertung bitten (mehr Vertrauen für Neue)."""
    t = ('Warst du zufrieden?', 'Eine kurze Bewertung hilft anderen bei der Suche nach einer guten Praxis. Danke dir!', 'Jetzt bewerten') if du else \
        ('Waren Sie zufrieden?', 'Eine kurze Bewertung bei Google hilft anderen Patienten bei der Suche nach einer guten Praxis. Herzlichen Dank!', 'Jetzt bewerten')
    return (f'<section class="bw28"><div class="w"><div><b>{t[0]}</b><span>{t[1]}</span></div>'
            f'<a class="btn" href="{gurl(s)}" target="_blank" rel="noopener">★ {t[2]}</a></div></section>')

def team28(people, ey, h2, lead, cls=''):
    p = ''.join(f'<figure data-r><div><img src="img/{i}" alt="{E(n)}" loading="lazy"></div><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for i, n, r in people)
    return f'<section class="sec tg28 {cls}" id="team"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="grid">{p}</div></div></section>'

def vids28(id, ey, h2, lead, items, cls=''):
    on = "var f=this.parentNode,m=f.querySelector('video');this.remove();m.controls=true;m.play()"
    f = ''.join(f'<div class="it" data-r><div class="frame"><video src="img/{v}" poster="img/{p}" preload="none" playsinline></video><button class="play" aria-label="Video abspielen" onclick="{on}">{PL}</button></div><h3>{t}</h3></div>' for v, p, t in items)
    return f'<section class="sec vg {cls}" id="{id}"><div class="w"><div data-r>{head(ey, h2, lead)}</div><div class="grid">{f}</div></div></section>'

CSS28 = '''.bw28{background:var(--s2);padding:26px 0;border-top:1px solid rgba(0,0,0,.06)}.bw28 .w{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}.bw28 b{display:block;font:800 22px var(--fh);color:var(--ink)}.bw28 span{color:var(--mute);font-size:17px}
.bw28 .btn{background:#fff;color:#161616;border:1.5px solid rgba(0,0,0,.15);border-radius:999px!important;padding:13px 22px;font-weight:700}.bw28 .btn:hover{background:var(--p);color:var(--p-ink);border-color:var(--p)}
.tg28 .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:22px;margin-top:34px}.tg28 figure{margin:0}.tg28 figure>div{aspect-ratio:3/4;overflow:hidden;background:var(--s2)}.tg28 figure:nth-child(3n+1)>div{border-radius:18px}
.tg28 img{width:100%;height:100%;object-fit:cover;object-position:50% 8%}.tg28 figcaption{margin-top:10px}.tg28 b{display:block;font:700 17px var(--fh)}.tg28 span{font-size:14.5px;color:var(--mute)}
.vg .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin-top:30px}.vg .frame{position:relative;aspect-ratio:16/9;background:#000;border-radius:18px;overflow:hidden}.vg video,.vg .frame img{width:100%;height:100%;object-fit:cover}.vg h3{font:700 17px var(--fh);margin-top:10px}
.hz-img{position:relative}.hv28{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
#jobs figure img,#zwei figure img{aspect-ratio:auto!important;height:auto!important;width:100%}
@media(max-width:900px){.tg28 .grid{grid-template-columns:1fr 1fr;gap:14px}.bw28 b{font-size:19px}}'''

def mk(k, d):
    g = d.get
    ort = d['ort']; top = d['top']; fam = d['fam']; p = d['p']; dk = d['dk']; s2 = d['s2']; pi = g('pi', '#fff')
    svcs = d['svcs']; cats = d['cats']; rec = d['rec']; du = g('du', False)
    Sie = (lambda a, b: b if du else a)
    def body(s):
        hero = d['hero']
        ub = ''.join(f'<div><b>{x}</b>{y}</div>' for x, y in d['ubar'])
        if hero == 'team':
            t = hd(s, False) + (f'<section class="ht20" id="top"><figure><img src="img/h1.jpg" alt="{E(d["hcap"])}"></figure><div class="w"><div data-r>{chip(s)}<p class="ey">{d["ey"]}</p><h1>{d["h1"]}</h1></div>'
                 f'<div data-r="2"><p class="sub">{d["sub"]}</p><div class="ctas"><a class="btn btn-a" href="#kontakt">{s["cta"]} {AR}</a><a class="btn btn-o" href="tel:{s["tel_i"]}">{PH} {s["tel"]}</a></div><div class="ub">{ub}</div></div></div></section>')
        elif hero == 'slides':
            t = hd(s) + hero_slides(s, dict(slides=['h1.jpg', 'h2.jpg'], pos=g('hpos', {}), ey=d['ey'], h1=d['h1'], sub=d['sub'], ubar=d['ubar']))
        else:
            t = hd(s, False) + hero_split(s, dict(imgs=(['h1.jpg', 'h2.jpg'] if d['himgs'][0] != d['himgs'][1] else ['h1.jpg']), cls=('card' if g('card') else ''), pos=g('hpos', {}), side=hero, big='', ubar=d['ubar'], ey=d['ey'], h1=d['h1'], sub=d['sub']))
        if g('hvid'): t = t.replace('<div class="sl">', '<video class="hv28" src="img/hv.mp4" poster="img/hv.jpg" autoplay muted loop playsinline></video><div class="sl" style="display:none">', 1)
        b = t + anliegen(s, cats).replace('Worum geht es bei Ihnen?', Sie('Worum geht es bei Ihnen?', 'Worum geht es bei dir?')) + marquee([a for a, _ in svcs] + [d.get('mq_end', f'Physiotherapie in {ort}')], 'wm')
        if g('video_first'): b += d['video_first']
        if g('stimmen'):
            b += (reviews(s, d['stimmen'], cls='alt') if g('google') else reviews_ns(s, d['stimmen'], cls='alt', h2=Sie('Das sagen <em>unsere Patienten.</em>', 'Das sagen <em>unsere Patienten.</em>')))
        b += bewerten(s, du)
        b += svc('leistungen', 'Leistungen', d['sv_h2'], d['sv_lead'], svcs[:6])
        b += promo('fokus', 'pr.jpg', top['tag'], top['h2'], top['txt'], top['pts'], top['btn'], 'alt')
        if g('zwei'):
            z = d['zwei']; b += eltern('zwei', 'el.jpg', z['ey'], z['h2'], z['txt'], z['pts'], z['btn'], rev=True)
        b += ablauf('weg', 'So läuft es ab', Sie('Anrufen, ankommen, <em>loslegen.</em>', 'Anrufen, ankommen, <em>loslegen.</em>'), Sie('So einfach kommen Sie zu uns.', 'So einfach kommst du zu uns.'), [
            ('Termin vereinbaren', Sie(f'Rufen Sie an unter {s["tel"]} oder schreiben Sie uns über das Formular. Halten Sie Ihr Rezept bereit, wenn Sie eins haben.', f'Ruf an unter {s["tel"]} oder schreib uns über das Formular. Halte dein Rezept bereit, wenn du eins hast.')),
            ('Befund und Gespräch', d.get('ab2', Sie('Beim ersten Termin hören wir zu und schauen uns genau an, wo es hakt. Danach planen wir Ihre Behandlung.', 'Beim ersten Termin hören wir zu und schauen uns genau an, wo es hakt. Danach planen wir deine Behandlung.'))),
            ('Behandlung und Übungen', d.get('ab3', Sie('Wir behandeln Sie und zeigen Ihnen Übungen, die Sie zu Hause weitermachen können.', 'Wir behandeln dich und zeigen dir Übungen für zu Hause.')))])
        tm = d['team']
        b += teamsec('ueber', tm['ey'], tm['h2'], tm['paras'], 'tm.jpg', tm['cap'], tm['tl'], cls='dk', mw=tm.get('mw'))
        if g('people'): b += team28([(f'p{i+1}.jpg', n, r) for i, (_, n, r) in enumerate(d['people'])], 'Team', d.get('people_h2', 'Die Menschen <em>hinter der Praxis.</em>'), d.get('people_lead', ''))
        if g('gal'): b += gal20('praxis', 'Einblicke', d.get('gal_h2', 'Ein Blick in <em>unsere Praxis.</em>'), [(f'g{i+1}.jpg', pos) for i, (_, pos) in enumerate(d['gal'])])
        if g('vids'): b += vids28('videos', 'Videos', d.get('vids_h2', 'Schauen Sie <em>uns zu.</em>'), d.get('vids_lead', ''), [(f'v{i+1}.mp4', f'v{i+1}.jpg', t) for i, (_, _, t) in enumerate(d['vids'])])
        if g('job'):
            j = d['job']; b += eltern('jobs', 'jb.jpg', 'Karriere', j['h2'], j['txt'], j['pts'], 'Jetzt melden', rev=False)
        b += notfall(s, d['notfall']) + contact(s)
        b += pops20([('pr.jpg', 'Aus der Praxis', top['tag'], top['pop'], s['cta'])] + [(im, 'Aus der Praxis', a, tx, s['cta']) for im, a, tx in d['pops']])
        return b + footer(s)
    opts = [a for a, _ in svcs] + (['Bewerbung'] if g('job') else []) + ['Sonstiges']
    nav = [('Leistungen', 'leistungen'), (top['nav'], 'fokus'), ('Team', 'team' if g('people') else 'ueber')] + ([('Jobs', 'jobs')] if g('job') else []) + [('Kontakt', 'kontakt')]
    S = SITES[k] = site(
        slug=d['slug'], firma=d['firma'], web=d['web'], fonts=d['fonts'], branche=d.get('branche', 'Physiotherapie'), du=du,
        title=f'{d["firma"]} – {d.get("tt", "Physiotherapie")} in {ort}', desc=f'{d["firma"]} in {ort}: ' + ', '.join(a for a, _ in svcs[:5]) + '.',
        tel=d['tel'], tel_i=d['tel_i'], mail=g('mail', ''), adresse=f'{d["strasse"]}, {d["plz"]} {ort}', google=g('google'),
        cta=d.get('cta', 'Termin anfragen'), nav=nav,
        hours=d['hours'], form_opts=opts, form_h3=d.get('cta', 'Termin anfragen'), form_p=Sie('Sagen Sie uns kurz, worum es geht. Wir melden uns bei Ihnen.', 'Sag uns kurz, worum es geht. Wir melden uns bei dir.'), form_btn='Rückruf anfordern',
        kt_ey='Kontakt', kt_h2=Sie('Wir sind <em>für Sie da.</em>', 'Wir sind <em>für dich da.</em>'), kt_p=Sie('Rufen Sie an oder schreiben Sie uns. Wir melden uns so schnell wie möglich.', 'Ruf an oder schreib uns. Wir melden uns so schnell wie möglich.'),
        vars=V.format(ink='#1b1d22', mute='#4d535c', p=p, pi=pi, dk=dk, s2=s2, fh=fam[0], fb=fam[1], lh=g('lh', 58), ft=dk),
        css=f'''.h2,.hz h1,.hs h1{{font-weight:800;letter-spacing:-.02em}}.h2 em,.hz h1 em,.ht20 h1 em{{font-style:normal;color:{g('em', p)}}}.hs h1 em{{font-style:normal;color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.rd .road div h3{{color:{g('em', p)}}}.hs .ubar b{{color:#fff}}.hs .ey{{color:#fff!important}}.ft img{{background:#fff;padding:8px 12px;height:66px}}
.promo .tag{{background:{p};color:{pi}}}.el .ey,.ht20 .ey{{color:{g('em', p)}}}
@media(max-width:820px){{.hz h1,.hs h1{{font-size:31px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}}}''' + CSS20 + CSS28)
    card = (f'@media(min-width:901px){{.hz.card{{min-height:min(90vh,800px)}}.hz.card .hz-img{{align-self:center;min-height:0;aspect-ratio:{g("card")};margin:130px clamp(24px,4vw,64px) 60px;border-radius:18px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.18)}}.hz.card .sl img{{animation:none}}}}@media(max-width:900px){{.hz.card .hz-img{{height:auto!important;min-height:0!important;aspect-ratio:{g("card")};margin-top:72px}}}}' if g('card') else '')
    S['css2'] = (f'.promo{{--prmw:{g("prmw")}px}}' if g('prmw') else '') + (f'#zwei figure{{max-width:{g("elmw")}px;justify-self:center}}' if g('elmw') else '') + (f'#jobs figure{{max-width:{g("jbmw")}px;justify-self:center}}' if g('jbmw') else '') + (f'.tg28 figure>div{{aspect-ratio:{g("par")}}}.tg28 img{{object-position:50% 30%}}' if g('par') else '') + card + f'.hz{{--hz-bg:{s2};--hz-ink:#1b1d22;--hz-mute:#4d535c;--hz-stroke:rgba(0,0,0,.07);--hz-cols:{g("cols", "46fr 54fr")}}}.hz h1{{font-size:clamp(34px,4.1vw,64px)}}.hz .ey{{color:{g("em", p)}}}' + g('css2', '')
    S['rv_h2'] = 'Das sagen unsere <em>Patienten.</em>'
    if g('logo_txt'): S['logo_txt'] = d['logo_txt']
    if g('stimmen') and not g('google'): S['voices'] = True
    if g('gr'): S['gr'] = g('gr')
    S['nf_t'] = d.get('nf_t', Sie('Schnell einen Termin?', 'Schnell einen Termin?'))
    hl = Sie('Guten Tag', 'Hallo')
    S['bot'] = dict(auto=False, say=Sie(f'Hallo, ich bin <b>{d["bot"]}</b>, Ihr KI-Assistent. Ich führe Sie durch die Website.', f'Hallo, ich bin <b>{d["bot"]}</b>, dein KI-Assistent. Ich führe dich durch die Website.'),
        name=d['bot'], tag=d.get('bot_tag', 'Ihr Praxis-Lotse' if not du else 'Dein Praxis-Lotse'), du=du, tel=d['tel'], tel_i=d['tel_i'], notfall=d['notfall'], finBtn=d.get('cta', 'Termin anfragen'),
        hello=Sie(f'{hl}! Ich bin <b>{d["bot"]}</b>, der digitale Lotse von {d["kurz"]}. Soll ich Ihnen helfen, schnell das Richtige zu finden?', f'{hl}! Ich bin <b>{d["bot"]}</b>, der digitale Lotse von {d["kurz"]}. Soll ich dir helfen, schnell das Richtige zu finden?'),
        hi=Sie(f'{hl}, ich bin {d["bot"]}. Ich stelle Ihnen drei kurze Fragen und zeige Ihnen, was hier zu Ihrem Anliegen passt.', f'{hl}, ich bin {d["bot"]}. Ich stelle dir drei kurze Fragen und zeige dir, was hier zu deinem Anliegen passt.'),
        cats=[[CATL[c], c] for c in cats], rec=rec, usp=USP, ex='Öffnungszeiten, Leistungen oder Terminen',
        qa=[['zeit|geöffnet|sprech|offen|öffnung', 'Die Öffnungszeiten: ' + ', '.join(f'{a} {b}' for a, b in d['hours']) + '.'],
            ['wo|adresse|anfahrt|park', f'Die Praxis findest du hier: {d["strasse"]}, {d["plz"]} {ort}.' if du else f'Sie finden uns hier: {d["strasse"]}, {d["plz"]} {ort}.'],
            ['leistung|angebot|macht ihr|bieten', 'Zum Beispiel: ' + ', '.join(a for a, _ in svcs[:6]) + '.'],
            ['rezept|verordnung|kasse|krankenkasse|zuzahlung|privat', Sie('Mit ärztlicher Verordnung rechnen wir mit Ihrer Krankenkasse ab. Alles Weitere klären wir gern am Telefon.', 'Mit ärztlicher Verordnung rechnen wir mit deiner Krankenkasse ab. Alles Weitere klären wir gern am Telefon.')],
            ['job|stelle|bewerb|arbeiten|karriere', (Sie('Wir freuen uns über Verstärkung! Melden Sie sich einfach über das Formular oder per Telefon.', 'Wir freuen uns über Verstärkung! Melde dich einfach über das Formular oder per Telefon.') if g('job') else 'Fragen Sie gern direkt in der Praxis nach.')],
            ['kosten|preis', Sie('Das hängt von der Behandlung ab. Am besten fragen Sie direkt in der Praxis, dort bekommen Sie eine ehrliche Auskunft.', 'Das hängt von der Behandlung ab. Frag am besten direkt in der Praxis nach.')]],
        tour=[['#leistungen', 'Das finden Sie hier.' if not du else 'Das findest du hier.'], ['#fokus', f'Ein Schwerpunkt: {top["tag"]}.'], ['#weg', 'So läuft Ihr Termin ab.' if not du else 'So läuft dein Termin ab.'], ['#ueber', 'Hier lernen Sie das Team kennen.' if not du else 'Hier lernst du das Team kennen.'], ['#kontakt', 'Und hier fragen Sie Ihren Termin an.' if not du else 'Und hier fragst du deinen Termin an.']])
    im = {'h1.jpg': (d['himgs'][0], 1800), 'h2.jpg': (d['himgs'][1], 1800), 'pr.jpg': (top['img'], 1400), 'tm.jpg': (d['team']['img'], 1400)}
    if g('logo'): im['logo.png'] = d['logo']
    if g('zwei'): im['el.jpg'] = (d['zwei']['img'], 1400)
    if g('job'): im['jb.jpg'] = (d['job']['img'], 1400)
    for i, (src, _) in enumerate(g('gal', [])): im[f'g{i+1}.jpg'] = (src, 1200)
    for i, (src, _, _) in enumerate(g('people', [])): im[f'p{i+1}.jpg'] = (src, 700)
    for i, (v, po, _) in enumerate(g('vids', [])): im[f'v{i+1}.mp4'] = (v, 0); im[f'v{i+1}.jpg'] = (po, 1000)
    for x in g('extra_img', {}).items(): im[x[0]] = x[1]
    S['img'] = im; S['body'] = body

def J(k, n):
    import glob
    f = glob.glob(f'{R}{k}/img/i{n}.*'); assert f, (k, n); return f[0]

OS = ('"Open Sans",system-ui,sans-serif',) * 2; LATO = ('"Lato",system-ui,sans-serif',) * 2; SSANS = ('"Source Sans 3",system-ui,sans-serif',) * 2
TIT = ('"Titillium Web",system-ui,sans-serif',) * 2; POP = ('"Poppins",system-ui,sans-serif',) * 2; MON = ('"Montserrat",system-ui,sans-serif',) * 2
MAN = ('"Manrope",system-ui,sans-serif',) * 2; NUN = ('"Nunito",system-ui,sans-serif',) * 2; RUB = ('"Rubik",system-ui,sans-serif',) * 2
ROB = ('"Roboto",system-ui,sans-serif',) * 2; FIRA = ('"Fira Sans",system-ui,sans-serif',) * 2; SORA = ('"Sora",system-ui,sans-serif', '"Nunito Sans",system-ui,sans-serif')
JOS = ('"Josefin Sans",system-ui,sans-serif', '"Lato",system-ui,sans-serif'); ARCH = ('"Archivo",system-ui,sans-serif',) * 2
NF = 'Rufen Sie an, wir finden schnell einen passenden Termin. Mit Rezept rechnen wir direkt mit Ihrer Kasse ab.'
NF_DU = 'Ruf an, wir finden schnell einen passenden Termin. Mit Rezept rechnen wir direkt mit deiner Kasse ab.'
