from abc import ABC, abstractmethod
class CoffeTable(ABC):

    @abstractmethod
    def has_legs(self):
        pass