from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    

    @abstractmethod
    def clone(self, deep):
        pass


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

def main():
    width_value = [20]
    height_value = [30]
    rectangle1 = Rectangle(width_value, height_value)
    
     #Shallow copy
    rectangle2 = rectangle1.clone(deep=False)
    rectangle2._width.append(100)

    #Deep copy
    rectangle3 = rectangle1.clone(deep=True)
    rectangle3._width.append(100)

    
    print("Memory Addresses:")
    print(f"Rectangle 1 address: {id(rectangle1._width)}")
    print(f"Rectangle 2 (Shallow Copy) address: {id(rectangle2._width)}")
    print(f"Rectangle 3 (Deep Copy) address: {id(rectangle3._width)}\n")

    print("Rectangle 1:", rectangle1)
    print("Rectangle 2 (Shallow Copy):", rectangle2)
    print("Rectangle 3 (Deep Copy):", rectangle3)
    

    print("\nComparisons:")
    print(f"rectangle1 is rectangle2: {rectangle1 is rectangle2}")  
    print(f"rectangle1 == rectangle2: {rectangle1 == rectangle2}")  
    print(f"rectangle1 is rectangle3: {rectangle1 is rectangle3}")  
    print(f"rectangle1 == rectangle3: {rectangle1 == rectangle3}")  

    print("\nInternal attribute memory addresses:")
    print(f"rectangle1._width address: {id(rectangle1._width)}")
    print(f"rectangle2._width address: {id(rectangle2._width)}")
    print(f"rectangle3._width address: {id(rectangle3._width)}")

if __name__ == "__main__":
    main()

# Testing

# class Rectangle:
#     def __init__(self, _width, _height, _value):
#         self._width = _width
#         self._height = _height
#         self._value = _value

#     def __repr__(self):
#         return f"Rectangle(width={self._width}, height={self._height})"

# # Create an instance of Rectangle
# values = [200]
# original = Rectangle(10, 5, values)

# # Shallow copy
# shallow_copied = copy.copy(original)
# shallow_copied._width = [500]
# # Deep copy
# deep_copied = copy.deepcopy(original)
# deep_copied._width = [500]
# # Modify the original object


# print("Original:", original, id(original._width))
# print("Shallow Copied:", shallow_copied, id(shallow_copied._width))
# print("Original:", original, id(original._width))
# print("Deep Copied:", deep_copied, id(deep_copied._width))