
class Director:

    def __init__(self, builder):
        self.builder = builder


    def automatic_suv(self):
        return self.builder.set_seats(7).set_engine("V8").set_gps("GPS: Yes").get_result()
        
    
    def sports_car(self):
        return self.builder.set_seats(2).set_engine("1.8").set_gps("GPS: Yes").get_result()
    
    def manual_suv(self):
        return self.builder.set_seats(7).set_engine("V8").set_gps("GPS: Yes").set_manual_gear("Yes").get_result()