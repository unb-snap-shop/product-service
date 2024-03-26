from abc import ABC, abstractmethod

class ComponentFactoryInterface(ABC):
    @abstractmethod
    def create_component(self, **data):
        pass