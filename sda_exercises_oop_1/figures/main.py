from python_intermediate_training.sda_exercises_oop_1.figures.figures_entities import *


def main():
    circle1 = Circle(20)
    circle2 = Circle(10)
    circle3 = Circle(5)

    triangle1 = Triangle(15, 5)
    triangle2 = Triangle(12, 25)
    triangle3 = Triangle(15, 20)

    rectangle1 = Rectangle(35, 5)
    rectangle2 = Rectangle(5, 5)
    rectangle3 = Rectangle(25, 15)

    print(circle1.get_area())
    print(triangle1.get_area())
    print(rectangle1.get_area())

    # area = Figure.count_area([triangle2, rectangle2, circle2])
    # print(area)

    # area = count_area_func(triangle2, rectangle2, circle2)
    # print(area)

    result = Figure.check_area(300.00, [circle3])
    print(result)

    print(Figure.count_area([circle3]))

if __name__ == "__main__":
    main()
