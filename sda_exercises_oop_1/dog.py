from python_intermediate_training.sda_exercises_oop_1.animal import Animal

class Dog(Animal):
    def drink(self):
        return f'Dog drinks toilet water'

    def __init__(self, name: str, sound='bark!'):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog makes sound {self.sound}, its name is {self.name} and it looks brave'