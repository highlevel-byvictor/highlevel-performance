"""Runde 17: Küchenstudios im Umkreis von 80 km um Bersenbrück. Eigenes Material der Firmen, Pixabay nur als Ergänzung."""
SITES = {}
for _m in ('sites_a', 'sites_b', 'sites_c'):
    try:
        SITES.update(__import__(_m).SITES)
    except ModuleNotFoundError as e:
        if e.name != _m: raise
