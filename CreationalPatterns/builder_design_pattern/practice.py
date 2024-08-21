from abc import ABC,abstractmethod



class AutomaticCar:
    def __init__(self, builder):
        self.seat = builder.seats
        self.engine =builder.engine
        self.gps = builder.gps


class ManualCar:
     def __init__(self, builder):
        self.seat = builder.seats
        self.engine =builder.engine
        self.gps = builder.gps
        self.manual_gear = builder.manual_gear


class Builder(ABC):
    

    
    @abstractmethod
    def set_seats():
        pass

    @abstractmethod
    def set_engine():
        pass

    @abstractmethod
    def set_gps():
        pass


class CarBuilder(Builder):

    def __init__(self):
        self.seats = None
        self.engine = None
        self.gps = None


    def set_seats(self, seats):
        self.seats = seats
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self


    def set_gps(self, gps):
        self.gps = gps
        return self


    def get_result(self):
        return AutomaticCar(self)



class CarManualBuilder(Builder):

    def __init__(self):
        self.seats = None
        self.engine = None
        self.gps = None
        self.manual_gear = None


    def set_seats(self, seats):
        self.seats = seats
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self


    def set_gps(self, gps):
        self.gps = gps
        return self


    def set_manual_gear(self, manual_gear):
        self.manual_gear = manual_gear
        return self

    def get_result(self):
        return ManualCar(self)


class Director:

    def __init__(self, builder):
        self.builder = builder


    def automatic_suv(self):
        return self.builder.set_seats(7).set_engine("V8").set_gps("GPS: Yes").get_result()
        
    
    def sports_car(self):
        return self.builder.set_seats(2).set_engine("1.8").set_gps("GPS: Yes").get_result()
    
    def manual_suv(self):
        return self.builder.set_seats(7).set_engine("V8").set_gps("GPS: Yes").set_manual_gear("Yes").get_result()
        
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
