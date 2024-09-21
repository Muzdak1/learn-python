from abc import ABC, abstractmethod

class Shapes(ABC):
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def shape(self):
        pass 


class Rectangle(Shapes):

    def shape(self):
        return f"Rectangle is {self.color.color()}"


class Circle(Shapes):

    def shape(self):
        return f"Circle is {self.color.color()}"