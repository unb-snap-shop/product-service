import random
from app.factory.concrete_factory import CPUFactory, GPUFactory, MotherboardFactory, RAMFactory, StorageFactory
from ..utils.product_catalogue import ProductCatalogue


class ComponentManager:
    factory_registry = {
        'CPU': CPUFactory(),
        'GPU': GPUFactory(),
        'Motherboard': MotherboardFactory(),
        'RAM': RAMFactory(),
        'Storage': StorageFactory()
    }

    @staticmethod
    def create_component(component_type, **data):
        if component_type in ComponentManager.factory_registry:
            factory = ComponentManager.factory_registry[component_type]
            data["id"] = ComponentManager.generate_random_id()
            component = factory.create_component(**data)
            catalog = ProductCatalogue()
            catalog.add_product(component)
            return component
        else:
            raise ValueError(f"Component type {component_type} not registered")

    @staticmethod
    def generate_random_id():
        return random.randint(1, 1000000)
