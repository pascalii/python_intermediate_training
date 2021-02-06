from python_intermediate_training.sda_exercises_oop_1.cat import Cat
from python_intermediate_training.sda_exercises_oop_1.dog import Dog
from python_intermediate_training.sda_exercises_oop_1.animal import Animal

class Vet:

    @staticmethod
    def sayCatHello(cat: Cat) -> str:
        return f'Hi {cat.name}'

    @staticmethod
    def sayDogHello(dog: Dog) -> str:
        return f'Hi {dog.name}'

    @staticmethod
    def sayAnimalHello(animal: Animal):
        return f'Hi {animal.name}'