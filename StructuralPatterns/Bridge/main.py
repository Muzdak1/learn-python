
from shapes import Circle
from colors import RedColor

def main():
    circle = Circle()
    red_color = RedColor()
    red_color_circle = circle.shape(red_color)
    print(red_color_circle)
  

if __name__ == "__main__":
    main()
