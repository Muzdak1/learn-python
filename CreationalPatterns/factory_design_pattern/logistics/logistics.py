from abc import ABC, abstractmethod
# make this class modular
# Abstract class
class Logistics(ABC):
    # snake case plan_delivery
    def plan_delivery(self):
        transport = self.create_transport()
        return transport

    @abstractmethod
    def create_transport(self):
        pass

# pascal case RoadLogistics