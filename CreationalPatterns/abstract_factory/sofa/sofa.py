from abc import ABC, abstractmethod
class Sofa(ABC):

    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass
