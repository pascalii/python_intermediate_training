class Dog:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Dog makes sound {self.sound}, its name is {self.name} and it looks brave'