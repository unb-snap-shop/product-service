import random
from concreteFactory import CPUFactory, GPUFactory, MotherboardFactory, RAMFactory, StorageFactory

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
            return factory.create_component(**data)
        else:
            raise ValueError(f"Component type {component_type} not registered")

    @staticmethod
    def generate_random_id():
        return random.randint(1, 1000000)
