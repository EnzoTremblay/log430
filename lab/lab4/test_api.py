import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
from cache import get_stock_magasin_cached

class CacheTestCase(unittest.TestCase):
    def test_cache_stock(self):
        result1 = get_stock_magasin_cached(1)
        result2 = get_stock_magasin_cached(1)
        self.assertEqual(result1, result2)
        # Le second appel doit être plus rapide (cache hit)

if __name__ == '__main__':
    unittest.main()
