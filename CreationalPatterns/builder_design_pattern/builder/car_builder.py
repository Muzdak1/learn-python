from builder import Builder
from car import AutomaticCar

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