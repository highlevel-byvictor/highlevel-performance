"""Runde 16: Küchenstudios rund um Werlte (bis ca. 35 km). Nur veraltete Seiten bzw. schwaches Marketing. Eigenes Material der Firmen, Pixabay nur für Emotionsbilder."""
SITES = {}
for _m in ('sites_a', 'sites_b'):
    try:
        SITES.update(__import__(_m).SITES)
    except ModuleNotFoundError as e:
        if e.name != _m: raise
