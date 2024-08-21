from builder import Builder
from car import ManualCar

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
