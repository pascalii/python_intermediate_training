from abc import ABC


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def animal_name(self):
        return self.name