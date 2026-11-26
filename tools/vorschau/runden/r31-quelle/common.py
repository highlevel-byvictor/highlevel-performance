"""Akquise DM 26.11.2026 (Do, Handwerk): gemeinsame Helfer."""
from lib import *

def site(**kw):
    s = dict(kw); s.setdefault('du', False); s.setdefault('branche', 'Handwerksbetrieb'); s.setdefault('runde', 'Akquise DM 26.11.2026'); return s

def BOT(name, tag, firma, s, qa, tour):
    return dict(name=name, tag=tag, hello=f'Guten Tag! Ich bin <b>{name}</b>. Soll ich Ihnen kurz zeigen, was Sie bei {firma} erwartet?',
                hi=f'Guten Tag, ich bin {name} von {firma}. Wobei darf ich helfen?', qa=[list(x) for x in qa], tour=[[t] for t in tour])

def EMO(rgb, pos='center 50%', dark=False, pic_w=420, flip=False, mpos='50% 30%', mh=44, bgl=0):
    """Beinke-Hero: Emotionsbild scharf im Hintergrund, Verlauf in Markenfarbe von links, Text links, eigenes Foto rechts unten.
    Handy: Bild als Band oben (mh vh), Text darunter, damit nie Text über Gesichtern liegt."""
    c = rgb; fl = 'transform:scaleX(-1);' if flip else ''
    return (f".hx.hasbg::before{{inset:0!important;filter:none!important;opacity:1!important;background-position:{pos}!important;{fl}left:{bgl}%!important}}"
            f".hx.hasbg::after{{content:'';position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,rgba({c},1) 0%,rgba({c},.95) {max(bgl,36)}%,rgba({c},.25) {max(bgl,36)+(12 if bgl else 24)}%,rgba({c},0) {max(bgl,36)+(20 if bgl else 38)}%)}}"
            f".hx.hasbg>.w{{position:relative;z-index:1}}.hx .pic{{max-width:{pic_w}px;justify-self:end;align-self:end}}.hx.hasbg{{min-height:min(94vh,880px);display:flex;align-items:center}}"
            + (".hx h1,.hx .sub,.hx .ey{color:#fff}.hx .sub{opacity:.9}" if dark else '')
            + f"@media(max-width:820px){{.hx.hasbg{{display:block;padding-top:calc({mh}vh + 14px)}}.hx.hasbg::before{{height:{mh}vh;bottom:auto!important;background-position:{mpos}!important;left:0!important;transform:none}}"
            f".hx.hasbg::after{{background:linear-gradient(0deg,rgba({c},1) calc(100% - {mh}vh),rgba({c},0) calc(100% - {mh}vh + 120px))}}.hx .pic{{justify-self:stretch;max-width:none}}.hx h1{{hyphens:manual}}}}")
PIX = '/home/claude/pixa16/'
HI = '/home/claude/r31raw/'

def BOTDU(name, tag, firma, s, qa, tour):
    return dict(name=name, tag=tag, hello=f'Hallo! Ich bin <b>{name}</b>. Soll ich dir kurz zeigen, was dich bei {firma} erwartet?',
                hi=f'Hallo, ich bin {name} von {firma}. Wobei darf ich helfen?', qa=[list(x) for x in qa], tour=[[t] for t in tour])

V = '--bg:#fff;--ink:{ink};--mute:{mute};--p:{p};--p-ink:{pi};--a:{p};--a-ink:{pi};--dk:{dk};--s:#fff;--s2:{s2};--fh:{fh};--fb:{fb};--r:0px;--r2:0px;--br:2px;--mq-bg:{dk};--mq-ink:#fff;--hd-bg:rgba(255,255,255,.97);--hd-ink:{ink};--logo-h:{lh}px;--ft-bg:{ft};--hp-bg:{s2}'
DKHD = ';--hd-bg:{c};--hd-ink:#fff'
RUND = '.btn{border-radius:999px}.chip{border-radius:999px}.play span{border-radius:50%}.tag{border-radius:999px}.mcall a{border-radius:999px}'

import glob as _g
def I(k, n, w=1600, *m):
    f = [x for x in _g.glob(f'{HI}{k}/img/i{int(n):03d}.*') if not x.endswith('.src')]
    assert f, (k, n)
    return (f[0], w) + tuple(m)
def css_hw(p, dk, extra=''):
    return (f'''.h2,.hz h1{{font-weight:800;letter-spacing:-.015em}}.h2 em,.hz h1 em{{font-style:normal;color:{p}}}.dk .h2 em{{color:#fff;text-decoration:underline;text-decoration-color:{p};text-underline-offset:.12em}}
.mq.wm span{{font-weight:700;font-size:15px}}.alt{{background:var(--s2)}}.sv .row div{{border-top:4px solid {p}}}.st.dk{{background:{dk};color:#fff}}.st.dk .lead{{color:rgba(255,255,255,.86)}}.st.dk .tl b{{color:#fff}}.rd .road div h3{{color:{p}}}
.sec.gl{{display:block!important}}.gl .grid{{grid-auto-flow:dense}}.gl .grid figure{{border-radius:0!important}}.btn{{border-radius:999px!important}}.kt .info i{{border-radius:50%!important}}
@media(max-width:820px){{.hz h1{{font-size:31px!important;hyphens:none!important;overflow-wrap:normal!important;word-break:normal!important}}.gl .grid{{grid-auto-rows:150px}}}}''' + extra)
def hz(s2, p, ink='#161616', mute='#444'):
    return f'.hz{{--hz-bg:{s2};--hz-ink:{ink};--hz-mute:{mute};--hz-stroke:rgba(0,0,0,.07);--hz-cols:46fr 54fr}}.hz h1{{font-size:clamp(34px,4.2vw,64px)}}.hz .ey{{color:{p}}}'
ABL = [('Anliegen schicken', 'Über das Formular oder direkt per Telefon. Sagen Sie kurz, worum es geht.'),
       ('Termin vor Ort', 'Wir schauen uns alles bei Ihnen an und beraten Sie persönlich.'),
       ('Saubere Ausführung', 'Wir arbeiten zuverlässig, sorgfältig und termintreu.')]
