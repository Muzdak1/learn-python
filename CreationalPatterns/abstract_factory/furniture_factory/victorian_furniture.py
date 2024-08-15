from furniture_factory import FurnitureFactory
from chair import VictorianChair
from sofa import VictorianSofa
from coffee_table import VictorianCoffeTable


class VictorianFurniture(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

    def create_coffee_table(self):
        return VictorianCoffeTable()