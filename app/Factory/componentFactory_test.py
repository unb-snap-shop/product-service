import unittest
from componentFactory import ComponentFactory
from component import CPU, GPU, Motherboard, RAM, Storage

# Ensure components are registered with the factory.
# This is typically done outside of tests in the actual application initialization,
# but for standalone tests, it may be necessary to ensure registration.
ComponentFactory.register_component('CPU', CPU)
ComponentFactory.register_component('GPU', GPU)
ComponentFactory.register_component('Motherboard', Motherboard)
ComponentFactory.register_component('RAM', RAM)
ComponentFactory.register_component('Storage', Storage)

class TestComponentCreation(unittest.TestCase):
    def test_cpu_creation(self):
        cpu_data = {
            
            "brand": "AMD",
            "model": "Ryzen 5 5600X",
            "price": 299.99,
            **{
                "cores": 6,
                "threads": 12,
                "base_clock": "3.7 GHz",  # Use 'base_clock' instead of 'baseClock'
                "boost_clock": "4.6 GHz",  # Use 'boost_clock' instead of 'boostClock'
                "tdp": "65W"
            }
        }
        cpu = ComponentFactory.create_component('CPU', cpu_data)
        self.assertIsInstance(cpu, CPU)
        self.assertEqual(cpu.brand, "AMD")
        self.assertEqual(cpu.specifications["cores"], 6)


    def test_cpu2_creation(self):
        cpu2_data = {
            
            "brand": "Intel",
            "model": "Core i7-11700K",
            "price": 399.99,
            **{
                "cores": 8,
                "threads": 16,
                "base_clock": "3.6 GHz",  # Use 'base_clock' instead of 'baseClock'
                "boost_clock": "5.0 GHz",  # Use 'boost_clock' instead of 'boostClock'
                "tdp": "125W"
            }
        }
        cpu2 = ComponentFactory.create_component('CPU', cpu2_data)
        self.assertIsInstance(cpu2, CPU)
        self.assertEqual(cpu2.brand, "Intel")
        self.assertEqual(cpu2.specifications["tdp"], "125W")



    def test_gpu_creation(self):
        gpu_data = {
           
            "brand": "NVIDIA",
            "model": "GeForce RTX 3080",
            "price": 699.99,
            "memory": "10 GB GDDR6X",
            "boost_clock": "1.71 GHz",
            "tdp": "320W"
        }
        gpu = ComponentFactory.create_component('GPU', gpu_data)
        self.assertIsInstance(gpu, GPU)
        self.assertEqual(gpu.brand, "NVIDIA")
        self.assertEqual(gpu.specifications["memory"], "10 GB GDDR6X")

    def test_motherboard_creation(self):
        motherboard_data = {
            
            "brand": "ASUS",
            "model": "ROG Strix B550-F Gaming",
            "price": 179.99,
            "chipset": "AMD B550",
            "memory": "128GB DDR4",
            "formFactor": "ATX"
        }
        motherboard = ComponentFactory.create_component('Motherboard', motherboard_data)
        self.assertIsInstance(motherboard, Motherboard)
        self.assertEqual(motherboard.brand, "ASUS")
        self.assertEqual(motherboard.specifications["chipset"], "AMD B550")

    def test_ram_creation(self):
        ram_data = {
            
            "brand": "Corsair",
            "model": "Vengeance LPX 16GB",
            "price": 89.99,
            "memory_type": "DDR4",
            "speed": "3200MHz",
            "modules": "2 x 8GB",
            "latency": "CL16"
        }
        ram = ComponentFactory.create_component('RAM', ram_data)
        self.assertIsInstance(ram, RAM)
        self.assertEqual(ram.brand, "Corsair")
        self.assertEqual(ram.specifications["memoryType"], "DDR4")

    def test_storage_creation(self):
        storage_data = {
           
            "brand": "Samsung",
            "model": "970 EVO Plus 1TB",
            "price": 189.99,
            "storage_type": "SSD",
            "formFactor": "M.2",
            "interface": "NVMe",
            "rpm": "3500MB/s",
            "cache": "3300MB/s"
        }
        storage = ComponentFactory.create_component('Storage', storage_data)
        self.assertIsInstance(storage, Storage)
        self.assertEqual(storage.brand, "Samsung")
        self.assertEqual(storage.specifications["storageType"], "SSD")

    def test_cpu3_creation(self):
        cpu3_data = {
            
            "brand": "Intel",
            "model": "Core i7-11700K",
            "price": 399.99,
            **{
                "cores": 8,
                "threads": 16,
                "base_clock": "3.6 GHz",  # Use 'base_clock' instead of 'baseClock'
                "boost_clock": "5.0 GHz",  # Use 'boost_clock' instead of 'boostClock'
                "tdp": "125W"
            }
        }
        cpu3 = ComponentFactory.create_component('CPU', cpu3_data)
        self.assertIsInstance(cpu3, CPU)
        self.assertEqual(cpu3.brand, "Intel")
        self.assertEqual(cpu3.specifications["tdp"], "125W")

if __name__ == '__main__':
    unittest.main()