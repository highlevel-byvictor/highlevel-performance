"""Akquise DM 25.11.2026: Kosmetikstudios (Instagram aktiv, Website schwach)."""
SITES = {}
for _m in ("sites_a", "sites_b"):
    try:
        SITES.update(__import__(_m).SITES)
    except ModuleNotFoundError as e:
        if e.name != _m: raise
