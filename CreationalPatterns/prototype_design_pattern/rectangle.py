from shape import Shape
import copy


class Rectangle(Shape):
    
    def __init__(self,_width,_height):
        self._width = _width
        self._height = _height
     
    def clone(self, deep):
        if deep:
            return copy.deepcopy(self)
        else:
            return copy.copy(self)

    def __repr__(self):
        return (f"width={self._width}, height={self._height})")