"""Runde 15: Fahrschulen im Emsland rund um Werlte (ca. 50 km). Nur veraltete Seiten ohne Call-to-Action. Nur Material der Originalseiten und belegte Fakten."""
SITES = {}
for _m in ('sites_a', 'sites_b'):
    try:
        SITES.update(__import__(_m).SITES)
    except ModuleNotFoundError as e:
        if e.name != _m: raise
