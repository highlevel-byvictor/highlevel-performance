"""Akquise 20.11.2026 (Freitag, Gastro r32): gemeinsame Helfer."""
from lib import *

R = '/home/claude/r32raw/'

def site(**kw):
    s = dict(kw); s.setdefault('du', False); s.setdefault('branche', 'Restaurant / Gastronomie'); s.setdefault('runde', 'Akquise DM 27.11.2026')
    s.setdefault('form_lbl', 'Personen'); s.setdefault('form_opts', ['2 Personen', '3–4 Personen', '5–8 Personen', 'Größere Gruppe'])
    s.setdefault('form_h3', 'Tisch anfragen'); s.setdefault('form_btn', 'Reservierung anfragen')
    s.setdefault('form_p', 'Schreiben Sie uns Wunschtag, Uhrzeit und Anlass. Wir rufen Sie zurück und bestätigen Ihre Reservierung.')
    s.setdefault('cta', 'Tisch reservieren')
    return s

def BOT(name, tag, firma, qa, tour):
    return dict(name=name, tag=tag, hello=f'Guten Tag! Ich bin <b>{name}</b>. Soll ich Ihnen kurz zeigen, was Sie bei {firma} erwartet?',
                hi=f'Guten Tag, ich bin {name} von {firma}. Wobei darf ich helfen?', qa=[list(x) for x in qa], tour=[[t] for t in tour])

V = '--bg:{bg};--ink:{ink};--mute:{mute};--p:{p};--p-ink:#fff;--a:{p};--a-ink:#fff;--dk:{dk};--s:#fff;--s2:{s2};--fh:{fh};--fb:{fb};--r:0px;--r2:0px;--br:2px;--mq-bg:{dk};--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:{ink};--logo-h:{lh}px;--ft-bg:{dk};--hp-bg:{s2}'

STEAM = '<span class="steam" aria-hidden="true"><i></i><i></i><i></i></span>'

def hero_g(s, h):
    """Gastro-Hero: geteilter Slider mit Beschriftung je Bild (Gericht/Ort), optional Dampf über warmen Gerichten."""
    sl = ''
    for i, (x, cap, warm) in enumerate(h['imgs']):
        st = f'<span class="steam" style="left:{h.get("steam",{}).get(x,"50%")}" aria-hidden="true"><i></i><i></i><i></i></span>' if warm else ''
        c = f'<span class="cap"><small>{cap[0]}</small>{cap[1]}</span>' if cap else ''
        sl += f'<div data-slide class="{"on" if i==0 else ""}"><img src="img/{x}" alt="{E(cap[1] if cap else s["firma"])}" style="object-position:{h.get("pos",{}).get(x,"50% 50%")}"{"" if i==0 else " loading=lazy"}>{st}{c}</div>'
    dots = ''.join(f'<button data-dot class="{"on" if i==0 else ""}" aria-label="Bild {i+1}"></button>' for i in range(len(h['imgs']))) if len(h['imgs']) > 1 else ''
    ub = ''.join(f'<div><b>{a}</b>{b}</div>' for a, b in h.get('ubar', []))
    ctas = f'<div class="ctas"><a class="btn btn-a" href="#kontakt">{s["cta"]} {AR}</a><a class="btn btn-o" href="tel:{s["tel_i"]}">{PH} {s["tel"]}</a></div>'
    return (f'<section class="hz {"rev " if h.get("side")=="l" else ""}{h.get("cls","")}" id="top" data-slider="5500">'
            f'<div class="hz-img"><div class="sl">{sl}</div><div class="dots">{dots}</div></div>'
            f'<div class="hz-tx"><div class="in" data-r>{chip(s)}<p class="ey">{h["ey"]}</p><h1>{h["h1"]}</h1><p class="sub">{h["sub"]}</p>{ctas}'
            f'{"<div class=hz-ub>"+ub+"</div>" if ub else ""}</div></div></section>')

def cards(id, ey, h2, lead, items, cls=''):
    """Karten mit Bild: (img, titel, text, pos)."""
    c = ''.join(f'<article class="gc" data-r><figure><img src="img/{i}" alt="{E(t)}" loading="lazy" style="object-position:{p}"></figure><div><h3>{t}</h3><p>{x}</p></div></article>' for i, t, x, p in items)
    return f'<section class="sec gk {cls}" id="{id}"><div class="w"><div data-r>{head(ey,h2,lead)}</div><div class="gcs">{c}</div></div></section>'

def moment(img, text, sig='', pos='50% 50%'):
    return f'<section class="gm"><img src="img/{img}" alt="" loading="lazy" style="object-position:{pos}"><div class="w"><p data-r>{text}</p>{"<small data-r>"+sig+"</small>" if sig else ""}</div></section>'

def css_g(p, dk, extra=''):
    return ('''.h2 em,.hz h1 em{font-style:italic;color:var(--p)}.dk .h2 em{color:#fff}
.hz .sl>div{overflow:hidden}.hz .cap{position:absolute;right:22px;bottom:22px;z-index:3;background:rgba(0,0,0,.55);color:#fff;padding:12px 18px;font:600 17px/1.25 var(--fh);border-left:4px solid var(--p);max-width:70%;backdrop-filter:blur(4px)}
.hz .sl>div:not(.on) .cap,.hz .sl>div:not(.on) .steam{visibility:hidden}.hz .cap small{display:block;font:600 11px/1.4 var(--fb);letter-spacing:.14em;text-transform:uppercase;opacity:.8;margin-bottom:3px}
.steam{position:absolute;top:30%;width:120px;height:160px;transform:translateX(-50%);z-index:2;pointer-events:none}
.steam i{position:absolute;bottom:0;left:50%;width:34px;height:110px;border-radius:50%;background:radial-gradient(ellipse at center,rgba(255,255,255,.55),rgba(255,255,255,0) 70%);filter:blur(8px);animation:stm 4.2s ease-in infinite;opacity:0}
.steam i:nth-child(2){left:30%;animation-delay:1.4s}.steam i:nth-child(3){left:66%;animation-delay:2.8s}
@keyframes stm{0%{transform:translateY(30px) scaleX(.6);opacity:0}25%{opacity:.85}100%{transform:translateY(-110px) scaleX(1.4);opacity:0}}
@media(prefers-reduced-motion:reduce){.steam{display:none}}
.gcs{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;margin-top:34px}
.gc{background:#fff;border:1px solid rgba(0,0,0,.07);overflow:hidden;border-radius:0 0 18px 0}.gc figure{margin:0;aspect-ratio:4/3;overflow:hidden}.gc img{width:100%;height:100%;object-fit:cover;transition:transform .6s}.gc:hover img{transform:scale(1.05)}
.gc div{padding:20px 22px 24px}.gc h3{font:600 22px/1.2 var(--fh);margin:0 0 8px;color:var(--ink)}.gc p{margin:0;color:var(--mute);line-height:1.6}
.gm{position:relative;min-height:62vh;display:flex;align-items:center;overflow:hidden;color:#fff;text-align:center}.gm>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.gm::after{content:'';position:absolute;inset:0;background:rgba(0,0,0,.48)}
.gm .w{position:relative;z-index:1}.gm p{font:500 clamp(26px,3.4vw,46px)/1.25 var(--fh);max-width:900px;margin:0 auto}.gm p em{color:var(--p2,#fff);font-style:italic}.gm small{display:block;margin-top:18px;letter-spacing:.12em;text-transform:uppercase;font-size:12px;opacity:.85}
.btn{border-radius:999px!important}.sec.gl{display:block!important}.gl .grid{grid-auto-flow:dense}.gl .grid figure{border-radius:0!important}.kt .info i{border-radius:50%!important}.ft img{background:#fff;padding:8px 12px;height:66px}
.lt-logo{font:700 22px/1.05 var(--fh);color:var(--ink);letter-spacing:-.01em}.lt-logo small{display:block;font:600 10px/1.4 var(--fb);letter-spacing:.16em;text-transform:uppercase;color:var(--p)}.ft .lt-logo{color:#fff}
@media(max-width:820px){.hz h1{font-size:34px!important;hyphens:none!important}.hz .cap{right:12px;bottom:12px;font-size:14px;padding:9px 12px}.gl .grid{grid-auto-rows:150px}.steam{top:22%}}''' + extra)

def hz(s2, ink='#1c1714'):
    return f'.hz{{--hz-bg:{s2};--hz-ink:{ink};--hz-mute:#5b524a;--hz-stroke:rgba(0,0,0,.07);--hz-cols:46fr 54fr}}.hz h1{{font-size:clamp(36px,4.3vw,66px)}}.hz .ey{{color:var(--p)}}'

ABL = [('Tisch anfragen', 'Rufen Sie an oder schreiben Sie uns Ihren Wunschtermin.'),
       ('Ankommen', 'Wir empfangen Sie herzlich und nehmen uns Zeit für Sie.'),
       ('Genießen', 'Frisch zubereitet, mit Liebe serviert.'),
       ('Wiederkommen', 'Wir freuen uns schon auf Ihren nächsten Besuch.')]
