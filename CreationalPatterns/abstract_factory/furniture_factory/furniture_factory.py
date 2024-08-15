from abc import ABC,abstractmethod

class FurnitureFactory(ABC):


    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_coffee_table(self):
        pass