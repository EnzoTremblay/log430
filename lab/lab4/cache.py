import time
from functools import lru_cache

@lru_cache(maxsize=128)
def get_stock_magasin_cached(magasin_id):
    # Simule une requête lente
    time.sleep(0.2)
    # À remplacer par la vraie logique métier
    return {'produit': 'Outil', 'quantite': 100}
