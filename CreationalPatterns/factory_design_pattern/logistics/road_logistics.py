from logistics.logistics import Logistics
from transport import Truck


class RoadLogistics(Logistics):

    def create_transport(self):
        return Truck()