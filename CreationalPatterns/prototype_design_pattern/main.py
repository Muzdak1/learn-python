from rectangle import Rectangle



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
