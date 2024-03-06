import unittest
from src.product_catalogue import ProductCatalogue

class TestProductCatalogue(unittest.TestCase):
    
    def test_singleton_instance(self):
        catalogue1 = ProductCatalogue()
        catalogue2 = ProductCatalogue()
        self.assertIs(catalogue1, catalogue2)

    def test_add_and_list_product(self):
        catalogue = ProductCatalogue()
        
        catalogue.products = []

        mock_product = {
            "id": 11,
            "type": "CPU",
            "brand": "TestBrand",
            "model": "TestModel",
            "specifications": {
                "cores": 4,
                "threads": 4,
                "baseClock": "3.6 GHz",
                "boostClock": "4.0 GHz",
                "tdp": "65W"
            },
            "price": 123.45
        }

        catalogue.add_product(mock_product)
        print(catalogue.list_products(),[])

        self.assertIn(mock_product, catalogue.list_products())

    def test_list_products_empty(self):
        catalogue = ProductCatalogue()
        
        catalogue.products = []
        self.assertEqual(catalogue.list_products(), [])

if __name__ == '__main__':
    unittest.main()