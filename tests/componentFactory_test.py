import sys
import os
import unittest

# Get the directory of the test script
test_dir = os.path.dirname(__file__)
# Get the parent directory (the root of your project)
project_dir = os.path.dirname(test_dir)
# Add the project directory to sys.path
sys.path.append(project_dir)

# Now you can import your module
from app.factory.componentFactory import ComponentFactory, CPU, GPU

# The rest of your test code follows...

class TestComponentFactory(unittest.TestCase):
    def test_create_component_valid_data(self):
        # Test creating a CPU component
        cpu_data = {'type': 'CPU', 'brand': 'Intel', 'model': 'Core i7', 'cores': 8, 'threads': 16 }
        cpu_component = ComponentFactory.create_component(cpu_data)
        self.assertIsInstance(cpu_component, CPU)

        # Test creating a GPU component
        gpu_data = {'type': 'GPU', 'brand': 'NVIDIA', 'model': 'GeForce RTX', 'memory': '8GB GDDR6'}
        gpu_component = ComponentFactory.create_component(gpu_data)
        self.assertIsInstance(gpu_component, GPU)

    def test_create_component_invalid_data(self):
        # Test creating a component with missing type
        invalid_data = {'brand': 'Intel', 'model': 'Core i7', 'cores': 8, 'threads': 16 }
        with self.assertRaises(ValueError):
            ComponentFactory.create_component(invalid_data)

        # Test creating a component with unknown type
        unknown_data = {'type': 'UnknownType', 'brand': 'Intel', 'model': 'Core i7', 'cores': 8, 'threads': 16 }
        with self.assertRaises(ValueError):
            ComponentFactory.create_component(unknown_data)