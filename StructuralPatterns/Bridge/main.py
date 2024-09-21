
from shapes import Circle
from colors import RedColor

def main():
    red_color = RedColor()
    red_circle = Circle(red_color)
    print(red_circle.shape())       

if __name__ == "__main__":
    main()
