from abc import ABC, abstractmethod

class Shape(ABC):
    

    @abstractmethod
    def clone(self, deep):
        pass
