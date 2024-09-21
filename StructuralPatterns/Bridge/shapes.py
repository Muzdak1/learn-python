from abc import ABC, abstractmethod

class Shapes(ABC):
    
    @abstractmethod
    def shape(self):
        pass 


class Rectangle(Shapes):

    def shape(self, color=None):
        if color:
            return f"Rectangle is {color.color()}"
        else:
            return "Rectangle with no color"
    
class Circle(Shapes):

    def shape(self, color=None):
        if color:
            return f"Circle is {color.color()}"
        else:
            return "Circle with no color"

    
