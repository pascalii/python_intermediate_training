from sda_exercises_oop_1.car import Car
from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog
from sda_exercises_oop_1.vet import Vet


def main():
    cat_object = Cat("Tom", "niauuu")
    cat_object_1 = Cat("Curt", "pszszsz")
    cat_object_2 = Cat("Wojtek", "mial")
    cat_object_3 = Cat("Lazy", "I don't meow")

    dog_object = Dog("Bernard", "woof")
    dog_object_1 = Dog("Sammy","peep")

    animal_list = []
    animal_list.append(dog_object)
    animal_list.append(dog_object_1)

    animal_list.append(cat_object)
    animal_list.append(cat_object_1)
    animal_list.append(cat_object_2)
    animal_list.append(cat_object_3)
    #
    # for animal in animal_list:
    #     print(animal.make_sound())
    # cat_object.eat_mouse()
    # cat_object.eat_mouse()
    # cat_object.eat_mouse()
    #
    # print('Now other cat will eat')
    #
    # cat_object_2.eat_mouse()
    #
    # car_object = Car()
    # print(car_object.move())
    #
    # cat = Cat("mniau")
    # print(cat.move())

    print(Vet.sayCatHello(cat_object))
    print(Vet.sayCatHello(cat_object_1))
    print(Vet.sayDogHello(dog_object))


    vet = Vet()
    vet.sayCatHello(cat_object_2)
    print(vet.sayCatHello(cat_object_2))

    print(Vet.sayAnimalHello(cat_object_3))



if __name__ == "__main__":
    main()
