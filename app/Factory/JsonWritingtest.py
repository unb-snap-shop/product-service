import unittest
import os
import json
from componentManager import ComponentManager
from component import CPU, GPU, Motherboard, RAM, Storage

class TestComponentManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file = 'testproducts.json'
        ComponentManager.products_file = cls.test_file  # Override the file path to use a test file

    # @classmethod
    # def tearDownClass(cls):
    #     if os.path.exists(cls.test_file):
    #         os.remove(cls.test_file)  # Clean up the test file

    def test_create_component_and_write_to_json(self):
        cpu_data = {
            "brand": "TestBrand",
            "model": "TestModel",
            "cores": 4,
            "threads": 4,
            "base_clock": 3.5,
            "boost_clock": 3.9,
            "tdp": 65,
            "price": 100.00
        }
        cpu = ComponentManager.create_component('CPU', **cpu_data)
        self.assertIsInstance(cpu, CPU)

        # Check that the JSON file was updated
        self.assertTrue(os.path.exists(self.test_file))

        with open(self.test_file, 'r') as json_file:
            data = json.load(json_file)
            self.assertIsInstance(data, list)  # Ensure it's a list
            self.assertGreater(len(data), 0)  # Ensure there's at least one product
            # Verify the last product matches what we created
            self.assertEqual(data[-1]['brand'], cpu_data['brand'])
            self.assertEqual(data[-1]['model'], cpu_data['model'])

if __name__ == '__main__':
    unittest.main()
