from python_intermediate_training.sda_exercises_oop_1.animal import Animal

class Dog(Animal):
    def __init__(self, name: str, sound: str):
        super().__init__(name, sound)
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog makes sound {self.sound}, its name is {self.name} and it looks brave'