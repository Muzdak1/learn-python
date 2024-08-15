from furniture_factory import FurnitureFactory
from chair import ModernChair
from sofa import ModernSofa
from coffee_table import ModernCoffeeTable


class ModernFurniture(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()
    
    def create_coffee_table(self):
        return ModernCoffeeTable()
