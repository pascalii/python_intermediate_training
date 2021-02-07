from sda_exercises_oop_1.figures import pytest
from sda_exercises_oop_1.figures.figures_entities import Figure, Circle, Triangle, Rectangle


def test_check_area():
    # given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    # when
    result = Figure.check_area([circle1, triangle1, rectangle1])
    # then
    assert result == 8.1416
