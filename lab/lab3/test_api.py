import unittest
from api import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_stock_magasin(self):
        response = self.app.get('/api/v1/stores/1/stock')
        self.assertEqual(response.status_code, 200)
        self.assertIn('stock', response.get_json())

    def test_get_rapport(self):
        response = self.app.get('/api/v1/report')
        self.assertEqual(response.status_code, 200)
        self.assertIn('rapport', response.get_json())

    def test_update_produit(self):
        data = {'nom': 'Outil', 'prix': 12.0, 'categorie': 'Bricolage'}
        response = self.app.put('/api/v1/products/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('produit', response.get_json())

    def test_get_dashboard(self):
        response = self.app.get('/api/v1/dashboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn('indicateurs', response.get_json())

if __name__ == '__main__':
    unittest.main()
