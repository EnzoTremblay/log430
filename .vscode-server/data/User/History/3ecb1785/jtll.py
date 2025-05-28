import pytest
import unittest
from app import main, init_db, search_product, record_sale, view_stock

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_main_output_format(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello World"

class TestApp(unittest.TestCase):
    def setUp(self):
        # Initialize the database for testing
        init_db()

    def test_search_product(self):
        # Test searching for an existing product
        result = search_product("Product1")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Product1")

    def test_record_sale(self):
        # Test recording a sale
        initial_stock = view_stock("Product1")
        record_sale("Product1", 1)
        updated_stock = view_stock("Product1")
        self.assertEqual(updated_stock, initial_stock - 1)

    def test_view_stock(self):
        # Test viewing stock for a product
        stock = view_stock("Product1")
        self.assertGreaterEqual(stock, 0)

if __name__ == "__main__":
    unittest.main()
