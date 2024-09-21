from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    

    @abstractmethod
    def clone(self, deep):
        pass
