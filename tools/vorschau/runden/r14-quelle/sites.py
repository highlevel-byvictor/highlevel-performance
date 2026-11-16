"""Runde 14: 20 Fahrschulen im Umkreis von ca. 40 km um Bersenbrück. Nur Material der Originalseiten und belegte Fakten."""
SITES = {}
for _m in ('sites_a', 'sites_b', 'sites_c', 'sites_d'):
    try:
        SITES.update(__import__(_m).SITES)
    except ModuleNotFoundError as e:
        if e.name != _m: raise
