class Cat:
    def __init__(self, name: str, sound='meeeooooww'):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Name is {self.name} sound is {self.sound}'
