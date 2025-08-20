import unittest
from .api import create_app
from .models import initialiser_donnees, consulter_stock_central, generer_rapport_consolide, synchroniser_stock


class Lab2TestCase(unittest.TestCase):
	def setUp(self):
		initialiser_donnees()
		app = create_app()
		self.client = app.test_client()

	def test_core_functions(self):
		stock = consulter_stock_central()
		self.assertTrue("Outil" in stock)
		synchroniser_stock(1, 1, 123)
		stock2 = consulter_stock_central()
		self.assertTrue(stock2["Outil"] >= stock["Outil"])  # total central augmente/égale

	def test_api_endpoints(self):
		r = self.client.get("/api/v1/stores/1/stock")
		self.assertEqual(r.status_code, 200)
		self.assertIn("stock", r.get_json())

		r2 = self.client.get("/api/v1/report")
		self.assertEqual(r2.status_code, 200)
		self.assertIn("rapport", r2.get_json())

		r3 = self.client.put("/api/v1/products/1", json={"magasin_id": 1, "quantite": 111})
		self.assertEqual(r3.status_code, 200)
		self.assertIn("produit", r3.get_json())

		r4 = self.client.get("/api/v1/dashboard")
		self.assertEqual(r4.status_code, 200)
		self.assertIn("indicateurs", r4.get_json())


if __name__ == "__main__":
	unittest.main()

