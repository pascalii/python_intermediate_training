from python_intermediate_training.sda_exercises_oop_1.movable import Movable
from python_intermediate_training.sda_exercises_oop_1.animal import Animal

class Cat(Animal, Movable):
    def __init__(self, name: str, sound='meeeooooww', eatean_mice = 0):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound
        self.eaten_mice = eatean_mice

    def make_sound(self) -> str:
        return f'Name is {self.name} sound is {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mice += 1
        print(f'Ive eaten {self.eaten_mice} mouse/mice')
        return self.eaten_mice

    def move(self):
        return 'I walk'