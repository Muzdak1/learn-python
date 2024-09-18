from builder import CarBuilder, CarManualBuilder
from director import Director

def main():

    build_automatic_car = CarBuilder()

    director1 = Director(build_automatic_car)

    automatic_sports_car = director1.sports_car()
    automatic_suv_car = director1.automatic_suv()
    
    print(automatic_sports_car.__dict__)
    print(automatic_suv_car.__dict__)

    build_manual_car = CarManualBuilder()
    director2 = Director(build_manual_car)
    manual_suv_car = director2.manual_suv()
    print(manual_suv_car.__dict__)


if __name__ == "__main__":
    main()
