from app.factory.component import CPU, GPU, Motherboard, RAM, Storage
from app.factory.componentFactoryInterface import ComponentFactoryInterface


class CPUFactory(ComponentFactoryInterface):
    def create_component(self, **data):
        return CPU(**data)


class GPUFactory(ComponentFactoryInterface):
    def create_component(self, **data):
        return GPU(**data)


class MotherboardFactory(ComponentFactoryInterface):
    def create_component(self, **data):
        return Motherboard(**data)


class RAMFactory(ComponentFactoryInterface):
    def create_component(self, **data):
        return RAM(**data)


class StorageFactory(ComponentFactoryInterface):
    def create_component(self, **data):
        return Storage(**data)
