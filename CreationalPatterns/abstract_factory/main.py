from furniture_factory import FurnitureFactory, VictorianFurniture, ModernFurniture


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