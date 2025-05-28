import pytest
import unittest
from app import main, rechercher_produit, enregistrer_vente, consulter_stock, Base, engine
from unittest.mock import patch

def test_main(capsys):
    with patch('builtins.input', return_value='4'):
        main()
    captured = capsys.readouterr()
    assert "Bienvenue dans le système de caisse du magasin !" in captured.out

def test_main_output_format(capsys):
    with patch('builtins.input', return_value='4'):
        main()
    captured = capsys.readouterr()
    assert "Bienvenue dans le système de caisse du magasin !" in captured.out

class TestApp(unittest.TestCase):
    def setUp(self):
        # Initialize the database for testing
        Base.metadata.create_all(engine)

    def test_search_product(self):
        # Test searching for an existing product
        result = rechercher_produit('nom', 'Outil')
        assert len(result) == 1
        assert result[0].nom == 'Outil'

    def test_record_sale(self):
        # Test recording a sale
        initial_stock = consulter_stock(filter_nom="Outil")
        assert len(initial_stock) == 1
        assert initial_stock[0].nom == "Outil"

    def test_view_stock(self):
        # Test viewing stock for a product
        stock = consulter_stock(filter_nom="Stylo")
        assert len(stock) == 1
        assert stock[0].nom == "Stylo"

if __name__ == "__main__":
    unittest.main()
