from singelton import Singelton

def main():
    
    obj1 =  Singelton.get_instance()
    obj2 = Singelton.get_instance()

    duplicate_obj1 = obj1

    if obj1 == obj2:
        print("obj1 == obj2")

    if obj1 is obj2:
        print("obj1 is obj2")

    print(duplicate_obj1 == obj1)
    print(duplicate_obj1 is obj1)

if __name__ == "__main__":
    main()
