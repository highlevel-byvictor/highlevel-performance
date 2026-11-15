"""Runde 11: Modul-Bausteine. Jede Firma setzt ihre Seite aus diesen Bausteinen zusammen (eigene Reihenfolge, Farben, Schriften, CSS)."""
import html as H
E = H.escape
PH = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2a1 1 0 011-.25 11.4 11.4 0 003.6.6 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1c0 1.25.2 2.45.57 3.57a1 1 0 01-.25 1z"/></svg>'
AR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def stars(r):
    return '★' * round(float(str(r).replace(',', '.')))

def logo(s, ft=False):
    if s.get('logo_txt'): return f'<span class="lt-logo">{s["logo_txt"]}</span>'
    return f'<img src="img/{s.get("logo_ft","logo.png") if ft else "logo.png"}" alt="{E(s["firma"])}">'

def svc(id, ey, h2, lead, items, cls=''):
    r = ''.join(f'<div data-r><h3>{a}</h3><p>{b}</p></div>' for a, b in items)
    return f'<section class="sec sv {cls}" id="{id}"><div class="w">{head(ey,h2,lead)}<div class="row">{r}</div></div></section>'

def faces(id, ey, h2, lead, imgs, cls=''):
    f = ''.join(f'<figure data-r><img src="img/{i}" alt="{E(c)}" loading="lazy"><figcaption>{c}</figcaption></figure>' for i, c in imgs)
    return f'<section class="sec fc {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{f}</div></div></section>'

def hd(s, light=True):
    nav = ''.join(f'<a href="#{a}">{t}</a>' for t, a in s['nav'])
    return f'''<header class="hd{' lt' if light else ''}" data-hd><div class="w"><a class="logo" href="#">{logo(s)}</a><nav class="nav">{nav}</nav><a class="btn btn-a" href="#kontakt">{s['cta']}</a><button class="burger" data-nav aria-label="Menü">☰</button></div></header>'''

def chip(s):
    g = s.get('google')
    if not g: return ''
    return f'<div class="chip"><b>{g[0]}</b><span class="st">{stars(g[0])}</span>{g[1]} Google-Bewertungen</div>'

def hero_slides(s, h):
    sl = ''
    for i, x in enumerate(h['slides']):
        on = ' on' if i == 0 else ''
        if x.endswith('.mp4'):
            sl += f'<div data-slide class="{on.strip()}"><video src="img/{x}" autoplay muted loop playsinline poster="img/{h.get("poster","")}"></video></div>'
        else:
            sl += f'<div data-slide class="{on.strip()}"><img src="img/{x}" alt="{E(h.get("alt", s["firma"]))}" style="object-position:{h.get("pos",{}).get(x,"50% 50%")}"></div>'
    dots = ''.join(f'<button data-dot class="{"on" if i==0 else ""}" aria-label="Bild {i+1}"></button>' for i in range(len(h['slides']))) if len(h['slides']) > 1 else ''
    ub = ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in h.get('ubar', []))
    big = f'<div class="big">{h["big"]}</div>' if h.get('big') else ''
    return f'''<section class="hs" data-slider="6000" id="top"><div class="sl">{sl}</div><div class="ov"></div>{big}<div class="w">{chip(s)}<p class="ey" style="color:var(--a)">{h['ey']}</p><h1>{h['h1']}</h1><p class="sub">{h['sub']}</p><div class="ctas"><a class="btn btn-a" href="#kontakt">{s['cta']} {AR}</a><a class="btn btn-g" href="tel:{s['tel_i']}">{PH} {s['tel']}</a></div><div class="dots">{dots}</div>{'<div class="ubar">'+ub+'</div>' if ub else ''}</div></section>'''

def hero_comp(s, h):
    c = h['imgs']
    figs = f'<figure class="c1"><img src="img/{c[0]}" alt="{E(h.get("alt",""))}" style="object-position:{h.get("pos0","50% 50%")}"></figure>'
    if len(c) > 1: figs += f'<figure class="c2"><img src="img/{c[1]}" alt=""></figure>'
    if len(c) > 2: figs += f'<figure class="c3"><img src="img/{c[2]}" alt=""></figure>'
    badge = f'<div class="badge"><b>{h["badge"][0]}</b>{h["badge"][1]}</div>' if h.get('badge') else ''
    return f'''<section class="hp" id="top"><div class="w"><div data-r>{chip(s)}<p class="ey">{h['ey']}</p><h1 style="margin-top:14px">{h['h1']}</h1><p class="sub">{h['sub']}</p><div class="ctas"><a class="btn btn-a" href="#kontakt">{s['cta']} {AR}</a><a class="btn btn-o" href="tel:{s['tel_i']}">{PH} {s['tel']}</a></div></div><div class="comp" data-r="2">{figs}{badge}</div></div></section>'''

def marquee(items, cls=''):
    t = ''.join(f'<span>{x}</span>' for x in items) * 2
    return f'<div class="mq {cls}"><div class="t">{t}</div></div>'

def head(ey, h2, lead='', center=False):
    st = ' style="text-align:center;margin-inline:auto"' if center else ''
    return f'<div{st}><p class="ey">{ey}</p><h2 class="h2">{h2}</h2>{f"<p class=lead{st}>{lead}</p>" if lead else ""}</div>'

def tabs(id, ey, h2, lead, items, cls=''):
    btn = ''.join(f'<button class="{"on" if i==0 else ""}" data-tab="{i}"><i>{i+1:02d}</i>{t}</button>' for i, (t, *_ ) in enumerate(items))
    pv = ''
    for i, (t, img, txt, chips) in enumerate(items):
        ch = ''.join(f'<li>{c}</li>' for c in chips)
        pv += f'<div class="pv{" on" if i==0 else ""}"><figure><img src="img/{img}" alt="{E(t)}" loading="lazy"></figure><p>{txt}</p>{"<ul>"+ch+"</ul>" if ch else ""}</div>'
    return f'<section class="sec tb {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}<div class="lst">{btn}</div></div><div class="pane" data-r="2">{pv}</div></div></section>'

def panels(id, ey, h2, lead, items, cls=''):
    p = ''.join(f'<div class="pn{" on" if i==0 else ""}" data-pn><img src="img/{img}" alt="{E(t)}" loading="lazy" style="object-position:{pos}"><div class="tx"><h3>{t}</h3><p>{txt}</p></div></div>' for i, (t, img, txt, pos) in enumerate(items))
    return f'<section class="sec ap {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="row" data-r="2">{p}</div></div></section>'

def scroller(id, ey, h2, lead, items, cls=''):
    c = ''.join(f'<article class="cd"><figure><img src="img/{img}" alt="{E(t)}" loading="lazy" style="object-position:{pos}"></figure><div><h3>{t}</h3><p>{txt}</p></div></article>' for t, img, txt, pos in items)
    return f'<section class="sec sc {cls}" id="{id}"><div class="w top" data-r>{head(ey,h2,lead)}<div class="arr"><button data-sc="-1" aria-label="zurück">←</button><button data-sc="1" aria-label="weiter">→</button></div></div><div class="trk">{c}</div></section>'

def duo(id, ey, h2, lead, worlds, cls=''):
    w = ''
    for small, t, img, txt, chips, btn in worlds:
        ch = ''.join(f'<li>{c}</li>' for c in chips)
        w += f'<div class="wd" data-r><img src="img/{img}" alt="{E(t)}" loading="lazy"><div class="tx"><small>{small}</small><h3>{t}</h3><p>{txt}</p><ul>{ch}</ul><a class="btn btn-a" href="#kontakt">{btn} {AR}</a></div></div>'
    return f'<section class="sec duo {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="row">{w}</div></div></section>'

def story(id, ey, h2, paras, img, cap='', tl=(), rev=False, cls='', extra=''):
    ps = ''.join(f'<p class="lead">{p}</p>' for p in paras)
    t = ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in tl)
    fc = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<section class="sec st{" rev" if rev else ""} {cls}" id="{id}"><div class="w"><figure data-r><img src="img/{img}" alt="{E(cap or h2)}" loading="lazy">{fc}</figure><div data-r="2"><p class="ey">{ey}</p><h2 class="h2">{h2}</h2>{ps}{"<div class=tl>"+t+"</div>" if t else ""}{extra}</div></div></section>'

def numbers(items):
    return '<div class="nb">' + ''.join(f'<div data-r><b>{a}</b><span>{b}</span></div>' for a, b in items) + '</div>'

def gallery(id, ey, h2, imgs, cls=''):
    f = ''.join(f'<figure class="{c}"><img src="img/{i}" alt="" loading="lazy" style="object-position:{p}"></figure>' for i, c, p in imgs)
    return f'<section class="sec gl {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2)}</div><div class="grid" data-r="2">{f}</div></div></section>'

def video(id, ey, h2, lead, src, poster, cls=''):
    return f'<section class="sec vd {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="frame" data-r="2"><video src="img/{src}" poster="img/{poster}" preload="none" playsinline controls></video><button class="play" aria-label="Video abspielen"><span><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></span></button></div></div></section>'

def ytvideo(id, ey, h2, lead, yt, poster, cls=''):
    return f'<section class="sec vd {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="frame yt" data-r="2" data-yt="{yt}"><img src="img/{poster}" alt="" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover"><button class="play" aria-label="Video abspielen" onclick="var f=this.parentNode;f.innerHTML=\'<iframe src=&quot;https://www.youtube-nocookie.com/embed/\'+f.dataset.yt+\'?autoplay=1&amp;rel=0&quot; allow=&quot;autoplay; encrypted-media; fullscreen&quot; allowfullscreen style=&quot;position:absolute;inset:0;width:100%;height:100%;border:0&quot;></iframe>\'"><span><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></span></button></div><p class="note" style="margin-top:12px">Video von YouTube. Erst beim Klick wird eine Verbindung zu YouTube aufgebaut.</p></div></section>'

def vgrid(id, ey, h2, lead, items, cls=''):
    PL = '<span><svg viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z"/></svg></span>'
    f = ''
    for t, kind, src, poster in items:
        if kind == 'yt':
            on = "var f=this.parentNode;f.innerHTML='<iframe src=&quot;https://www.youtube-nocookie.com/embed/'+f.dataset.yt+'?autoplay=1&amp;rel=0&quot; allow=&quot;autoplay; encrypted-media; fullscreen&quot; allowfullscreen></iframe>'"
            f += f'<div class="it" data-r><div class="frame" data-yt="{src}"><img src="img/{poster}" alt="" loading="lazy"><button class="play" aria-label="Video abspielen" onclick="{on}">{PL}</button></div><h3>{t}</h3><small>YouTube, lädt erst beim Klick</small></div>'
        else:
            on = "var f=this.parentNode,m=f.querySelector('video');this.remove();m.controls=true;m.play()"
            f += f'<div class="it" data-r><div class="frame"><video src="img/{src}" poster="img/{poster}" preload="none" playsinline></video><button class="play" aria-label="Video abspielen" onclick="{on}">{PL}</button></div><h3>{t}</h3></div>'
    return f'<section class="sec vg {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{f}</div></div></section>'

def reviews(s, items, cls=''):
    g = s['google']
    c = ''.join(f'<div class="cd"><div class="st">★★★★★</div><p>„{t}“</p><small>Google-Rezension, sinngemäß</small></div>' for t in items) * 2
    return f'<section class="sec rv {cls}" id="stimmen" style="overflow:hidden"><div class="w"><div class="sum" data-r><b>{g[0]}</b><div><div class="st">{stars(g[0])}</div><span>{g[1]} Bewertungen bei Google</span></div></div><h2 class="h2" style="margin-top:20px">{s.get("rv_h2","Das sagen unsere <em>Mitglieder.</em>")}</h2></div><div class="trk">{c}</div><div class="w"><p class="note">Auszüge aus echten Google-Rezensionen, gekürzt und sinngemäß wiedergegeben.</p></div></section>'

def steps(ey, h2, items, cls=''):
    r = ''.join(f'<div data-r><h3>{a}</h3><p>{b}</p></div>' for a, b in items)
    return f'<section class="sec sp {cls}"><div class="w">{head(ey,h2)}<div class="row">{r}</div></div></section>'

def team(id, ey, h2, lead, people, cls=''):
    p = ''.join(f'<figure data-r><div><img src="img/{i}" alt="{E(n)}" loading="lazy"></div><figcaption><b>{n}</b><span>{r}</span></figcaption></figure>' for i, n, r in people)
    return f'<section class="sec tm {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="grid">{p}</div></div></section>'

def faq(ey, h2, items, cls='', id='vorteile'):
    q = ''.join(f'<div class="it"><button data-acc>{a}</button><p>{b}</p></div>' for a, b in items)
    return f'<section class="sec fq {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2)}</div><div data-r="2">{q}</div></div></section>'

def contact(s, cls=''):
    hrs = ''.join(f'<span>{a}</span><span>{b}</span>' for a, b in s['hours'])
    opts = ''.join(f'<option>{o}</option>' for o in s['form_opts'])
    du = s.get('du')
    nm, tl, ms = ('Dein Name', 'Deine Telefonnummer', 'Deine Nachricht (optional)') if du else ('Ihr Name', 'Ihre Telefonnummer', 'Ihre Nachricht (optional)')
    ok = 'Danke! Wir melden uns schnellstmöglich bei dir.' if du else 'Vielen Dank! Wir melden uns schnellstmöglich bei Ihnen.'
    return f'''<section class="sec kt {cls}" id="kontakt"><div class="w"><div data-r><p class="ey">{s['kt_ey']}</p><h2 class="h2">{s['kt_h2']}</h2><p class="lead">{s['kt_p']}</p>
<div class="info"><div><i>☎</i><div><b><a href="tel:{s['tel_i']}">{s['tel']}</a></b>{s.get('mail','')}</div></div><div><i>⌖</i><div><b>{s['firma']}</b>{s['adresse']}</div></div><div><i>◷</i><div><b>Öffnungszeiten</b><div class="hrs">{hrs}</div></div></div></div>
<div class="map"><img src="img/karte.webp" alt="Karte: {E(s['adresse'])}" loading="lazy"><a href="https://www.openstreetmap.org/search?query={E(s['adresse'])}" target="_blank" rel="noopener">Route planen →</a></div></div>
<div class="bx" data-r="2"><h3 style="font-size:28px">{s['form_h3']}</h3><p style="color:var(--mute);margin:8px 0 22px">{s['form_p']}</p><form class="fm"><div class="two"><label>Name<input required autocomplete="name" placeholder="{nm}"></label><label>Telefon<input required type="tel" autocomplete="tel" placeholder="{tl}"></label></div><label>Anliegen<select>{opts}</select></label><label>Nachricht<textarea placeholder="{ms}"></textarea></label><button class="btn btn-a">{s['form_btn']} {AR}</button><small>Grober Entwurf: Das Formular verschickt noch nichts.</small><div class="ok">{ok}</div></form></div></div></section>'''

def footer(s):
    nav = ''.join(f'<a href="#{a}">{t}</a>' for t, a in s['nav'])
    soc = ''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in s.get('social', []))
    return f'''<footer class="ft"><div class="w"><div>{logo(s, True)}<p>{s['firma']}<br>{s['adresse']}<br><a href="tel:{s['tel_i']}">{s['tel']}</a></p></div><div><b>Seite</b>{nav}</div>{'<div><b>Folgen</b>'+soc+'</div>' if soc else ''}<div class="cp">Grober Entwurf von High Level Performance mit Bildern und Texten von {s['web']}. Bei einer Zusammenarbeit wird alles viel intensiver ausgearbeitet.</div></div></footer>'''

def pop(p):
    return f'<div class="pop" id="pop"><button class="x" aria-label="Schließen">×</button><img src="img/{p["img"]}" alt=""><div><small>{p["ey"]}</small><b>{p["h"]}</b><p>{p["p"]}</p><a class="btn btn-a" href="#kontakt">{p["btn"]}</a></div></div>'

JS = r'''<script>(function(){
document.querySelectorAll('.tb').forEach(function(t){var b=t.querySelectorAll('[data-tab]'),p=t.querySelectorAll('.pv'),i=0,iv;function go(n){b[i].classList.remove('on');p[i].classList.remove('on');i=n;b[i].classList.add('on');p[i].classList.add('on')}b.forEach(function(x,k){x.addEventListener('click',function(){go(k);clearInterval(iv)})});iv=setInterval(function(){go((i+1)%b.length)},7000)});
document.querySelectorAll('.ap .row').forEach(function(r){var ps=r.querySelectorAll('[data-pn]');ps.forEach(function(p){function on(){ps.forEach(function(q){q.classList.remove('on')});p.classList.add('on')}p.addEventListener('click',on);p.addEventListener('mouseenter',function(){if(matchMedia('(hover:hover)').matches)on()})})});
document.querySelectorAll('.sc').forEach(function(s){var t=s.querySelector('.trk');s.querySelectorAll('[data-sc]').forEach(function(b){b.addEventListener('click',function(){t.scrollBy({left:+b.dataset.sc*t.clientWidth*.6,behavior:'smooth'})})})});
document.querySelectorAll('.vd').forEach(function(v){var b=v.querySelector('.play'),m=v.querySelector('video');if(b&&m)b.addEventListener('click',function(){v.classList.add('playing');m.play()})});
var pp=document.getElementById('pop');if(pp){var sh=0;function show(){if(sh>=2)return;sh++;pp.classList.add('in');setTimeout(function(){pp.classList.remove('in');if(sh<2)setTimeout(show,60000)},15000)}var armed=0;addEventListener('scroll',function(){if(!armed&&scrollY>innerHeight*.9){armed=1;setTimeout(show,2500)}},{passive:true});pp.querySelector('.x').onclick=function(){sh=2;pp.classList.remove('in')};pp.querySelector('a').onclick=function(){sh=2;pp.classList.remove('in')}}
})();</script>'''

def page(s, body):
    note = '<div class="hlp-note"><b>Grober Entwurf</b> · Erstellt von High Level Performance. Bei einer Zusammenarbeit arbeiten wir jede Seite viel intensiver aus.<button aria-label="Hinweis schließen">×</button></div>'
    mcall = f'<div class="mcall"><a href="tel:{s["tel_i"]}">{PH}Anrufen</a><a href="#kontakt">{s["cta"]}</a></div>'
    bot = s['bot']
    import json
    botjs = '<script>window.BOT=' + json.dumps(bot, ensure_ascii=False) + '</script>'
    return f'''<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{E(s['title'])}</title><meta name="description" content="{E(s['desc'])}"><style><!--FONTS-->
<!--KIT_CSS-->
<!--LIB_CSS-->
:root{{{s['vars']}}}
{s.get('css','')}</style></head><body>{body}{note}{mcall}{botjs}<script><!--KIT_JS--></script>{JS}</body></html>'''

def promo(id, img, tag, h2, txt, pts, btn, cls=''):
    li = ''.join(f'<li>{p}</li>' for p in pts)
    return f'<section class="sec {cls}" id="{id}"><div class="w promo"><figure data-r><img src="img/{img}" alt="" loading="lazy"></figure><div data-r="2"><span class="tag">{tag}</span><h2 class="h2" style="margin-top:18px">{h2}</h2><p class="lead">{txt}</p><ul>{li}</ul><a class="btn btn-a" href="#kontakt">{btn} {AR}</a></div></div></section>'
