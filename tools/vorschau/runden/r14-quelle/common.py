"""Runde 14: gemeinsame Helfer für die Fahrschul-Seiten."""
from lib import *

def BOT(name, tag, firma, s, cls, usp, qa=(), tour=(), du=True, ex=None, fin=None):
    """Fahrschul-Lotse: Führerschein-Check (Klasse + Alter + Wunsch) füllt die Anmeldung vor."""
    if du:
        hello = f'Hey! Ich bin <b>{name}</b> von {firma}. In 30 Sekunden finden wir raus, welcher Führerschein zu dir passt.'
        hi = f'Hey, ich bin {name}! Drei kurze Fragen, dann weißt du, welche Klasse du brauchst, und deine Anmeldung ist schon vorausgefüllt.'
    else:
        hello = f'Guten Tag! Ich bin <b>{name}</b> von {firma}. In 30 Sekunden finden wir heraus, welcher Führerschein zu Ihnen passt.'
        hi = f'Guten Tag, ich bin {name}! Drei kurze Fragen, dann wissen Sie, welche Klasse Sie brauchen, und Ihre Anmeldung ist schon vorausgefüllt.'
    return dict(name=name, tag=tag, hello=hello, hi=hi, du=du, cls=cls, usp=usp, qa=[list(x) for x in qa], tour=[list(x) for x in tour],
                tel=s['tel'], tel_i=s['tel_i'], ex=ex, finBtn=fin)

def site(**kw):
    s = dict(kw)
    s.setdefault('du', True)
    return s
