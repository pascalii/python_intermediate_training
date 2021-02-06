from python_intermediate_training.sda_exercises_oop_1.figures.figures_entities import *

def main():
    circle1 = Circle(5)
    circle2 = Circle(10)
    circle3 = Circle(15)

    triangle1 = Triangle(15,5)
    triangle2 = Triangle(12,25)
    triangle3 = Triangle(15,20)

    rectangle1 = Rectangle(35, 5)
    rectangle2 = Rectangle(5, 5)
    rectangle3 = Rectangle(25, 15)

    print(circle1.get_area())
    print(triangle1.get_area())
    print(rectangle1.get_area())


if __name__ == "__main__":
    main()