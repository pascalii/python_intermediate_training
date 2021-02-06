from typing import List
from python_intermediate_training.sda_exercises_oop_1.cat import Cat
from python_intermediate_training.sda_exercises_oop_1.dog import Dog

# """ #1 it works """
#
#
# class Cat:
#     def __init__(self, cat_name: str):
#         self.cat_name = cat_name
#
#     def make_sound(self, sound: str):
#         return f'My cat {self.cat_name} says {sound}'
#
#
# my_cat1 = Cat('Grisza')
# my_cat2 = Cat('Indira')
# print(my_cat1.make_sound("Miauu"))
# print(my_cat2.make_sound("Mrrrr"))

# class Cat:
#     """2 another trial( working) shows the same sound to every cat"""
#
#     def __init__(self):
#         self.cat_list = []
#
#     def add_cat(self, cat_name: str) -> List[str]:
#         self.cat_list.append(cat_name)
#         return self.cat_list
#
#     def make_sound(self, sound: str):
#         for cats in self.cat_list:
#             print(f"Cat named {cats} says {sound}")
#
#     def get_cat_list(self) -> List[str]:
#         return self.cat_list
#
#     def eat_mousse(self, number: int):
#         for cats in self.cat_list:
#             print(f"{cats} ate {number} mousse/mousses.")
#
#
# kitty = Cat()
# kitty.add_cat("Grisza")
# kitty.add_cat("Indira")
# print(kitty.make_sound("miau"))
# print(kitty.eat_mousse(5))
# print(kitty.get_cat_list())

"""another one:) I was just checking something(some modifications in def add_cat comparing to the previous solution)
it works!!!, I wanted to assign different sound to different cats and also different numbers of eaten mouses
"""


class CatContainer:

    def __init__(self):
        self.cat_list = []

    def add_cat(self, cat_name: str, cat_sound: str, eaten_mouse: int) -> list:
        cat1 = Cat(cat_name, cat_sound, eaten_mouse)
        self.cat_list.append(cat1)
        return self.cat_list

    def make_sound(self):
        for cat in self.cat_list:
            print(cat.make_sound())

    def eat_mouse(self):
        for cat in self.cat_list:
            print(cat.eat_mouse())

    def get_cat_list(self) -> list:
        return self.cat_list


class Dog:

    def __init__(self):
        self.dog_list = []

    def add_dog(self, dog_name: str, dog_sound: str) -> List[str]:
        self.dog_list.append({"dog_name": dog_name, "dog_sound": dog_sound})
        return self.dog_list

    def make_sound(self):
        for dogs in self.dog_list:
            print(f"Dog named {dogs['dog_name']} says {dogs['dog_sound']}")

    def get_dog_list(self) -> List[str]:
        return self.dog_list

Dog.add_dog(dog_name="Boss", dog_sound="woofs")