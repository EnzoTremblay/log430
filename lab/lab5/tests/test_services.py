import unittest
from importlib import import_module


class ServicesTests(unittest.TestCase):
    def _client(self, module_name: str):
        mod = import_module(f"lab.lab5.services.{module_name}")
        app = getattr(mod, "app")
        return app.test_client()

    def test_products(self):
        c = self._client("produits")
        r = c.get("/api/v1/products")
        self.assertEqual(r.status_code, 200)
        r2 = c.put("/api/v1/products/1", json={"nom": "Outil", "prix": 11.5})
        self.assertEqual(r2.status_code, 200)

    def test_sales(self):
        c = self._client("ventes")
        r = c.get("/api/v1/sales")
        self.assertEqual(r.status_code, 200)

    def test_stock(self):
        c = self._client("stock")
        r = c.get("/api/v1/stock")
        self.assertEqual(r.status_code, 200)

    def test_clients(self):
        c = self._client("clients")
        r = c.post("/api/v1/clients", json={"nom": "Alice"})
        self.assertEqual(r.status_code, 201)

    def test_panier(self):
        c = self._client("panier")
        r = c.post("/api/v1/cart", json={"id": 1, "qty": 2})
        self.assertEqual(r.status_code, 201)

    def test_commande(self):
        c = self._client("commande")
        r = c.post("/api/v1/checkout", json={"cart_id": 1})
        self.assertEqual(r.status_code, 201)


if __name__ == "__main__":
    unittest.main()
