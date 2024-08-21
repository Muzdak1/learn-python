class ManualCar:
     def __init__(self, builder):
        self.seat = builder.seats
        self.engine =builder.engine
        self.gps = builder.gps
        self.manual_gear = builder.manual_gear