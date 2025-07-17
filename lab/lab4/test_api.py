import unittest
from cache import get_stock_magasin_cached

class CacheTestCase(unittest.TestCase):
    def test_cache_stock(self):
        result1 = get_stock_magasin_cached(1)
        result2 = get_stock_magasin_cached(1)
        self.assertEqual(result1, result2)
        # Le second appel doit être plus rapide (cache hit)

if __name__ == '__main__':
    unittest.main()
