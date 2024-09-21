from abc import ABC, abstractmethod


class Colors(ABC):
    
    @abstractmethod
    def color(self):
        pass

class RedColor(Colors):

    def color(self):
        return "Red Color"
    
class BlueColor(Colors):

    def color(self):
        return "Blue Color"