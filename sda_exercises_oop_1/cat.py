class Cat:
    def __init__(self, name: str, sound='meeeooooww', eatean_mice = 0):
        self.name = name
        self.sound = sound
        self.eaten_mice = eatean_mice

    def make_sound(self) -> str:
        return f'Name is {self.name} sound is {self.sound}'

    def eat_mouse(self):
        self.eaten_mice += 1
        print(f'Ive eaten {self.eaten_mice} mouse/mice')
        return self.eaten_mice
