from logistics.logistics import Logistics
from transport import Ship


class ShipLogistics(Logistics):

    def create_transport(self):
        return Ship()