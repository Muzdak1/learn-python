from abc import ABC,abstractmethod

class FurnitureFactory(ABC):


    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_coffee_table(self):
        pass


class VictorianFurniture(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()

    def create_coffee_table(self):
        return VictorianCoffeTable()


class ModernFurniture(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()
    
    def create_coffee_table(self):
        return ModernCoffeeTable()


class Chair(ABC):

    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class VictorianChair(Chair):

    def has_legs(self):
        return ("Victorian Chair legs")


    def sit_on(self):
        return ("Sit on Victorian Chair")


class ModernChair(Chair):

    def has_legs(self):
        return ("Modern Chair Legs")

    def sit_on(self):
        return ("Sit on Modern Chair")




class Sofa(ABC):

    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class VictorianSofa(Sofa):

    def has_legs(self):
        return ("Victorian Sofa Legs")

    def sit_on(self):
        return ("Sit on Victorian Sofa")


class ModernSofa(Sofa):

    def has_legs(self):
        return ("Modern Sofa Legs")

    def sit_on(self):
        return ("Sit on Modern Sofa")
    



class CoffeTable(ABC):

    @abstractmethod
    def has_legs(self):
        pass

class VictorianCoffeTable(Sofa):

    def has_legs(self):
        return ("Victorian CoffeTable")
    
class ModernCoffeeTable(CoffeTable):
    
    def has_legs(self):
        return ("Modern CoffeTable")






def main():
    furniture_factory: FurnitureFactory;

    furniture_factory = VictorianFurniture()
    victorian_chair = furniture_factory.create_chair()
    print(victorian_chair.has_legs())

    furniture_factory = ModernFurniture()
    modern_chair = furniture_factory.create_chair()
    print(modern_chair.has_legs())


   
if __name__ == "__main__":
    main()