import unittest
from src.product_catalogue import ProductCatalogue 

class service_singleton_test(unittest.TestCase):
    def test_singleton_instance(self):
        # Create an instance of the Singleton class
        instance1 = ProductCatalogue()
        # Create another instance of the Singleton class
        instance2 = ProductCatalogue()
        
        # Test if both instances are the same object
        self.assertIs(instance1, instance2, "Both instances should be the same object")

    def test_singleton_inherits_object(self):
        # Test if the Singleton class correctly inherits from the object class
        self.assertTrue(issubclass(ProductCatalogue, object), "Singleton should inherit from object")

if __name__ == '__main__':
    unittest.main()
