import abc
from math import pi

<<<<<<< Updated upstream

def count_area_func(*args):
    area = 0.0
    for arg in args:
        area += arg.get_area()
    return area


=======
>>>>>>> Stashed changes
class Figure(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass

<<<<<<< Updated upstream
    @staticmethod
    def count_area(figures: list) -> float:
        area = 0.0
        for figure in figures:
            area += figure.get_area()
        return area

    @staticmethod
    def check_area(some_area: float, figures: list) -> bool:
        figure_area = Figure.count_area(figures)
        return some_area > figure_area


=======
>>>>>>> Stashed changes
class Circle(Figure):

    def __init__(self, r):
        self.r = r

    def get_area(self):
<<<<<<< Updated upstream
        return round(pi * self.r ** 2, 3)

=======
        return pi * self.r ** 2
>>>>>>> Stashed changes

class Triangle(Figure):

    def __init__(self, a, h):
        self.a = a
        self.h = h

    def get_area(self):
        return (self.a * self.h) / 2

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
<<<<<<< Updated upstream
        return (self.a * self.b) / 2
=======
        return (self.a * self.b) / 2
>>>>>>> Stashed changes
