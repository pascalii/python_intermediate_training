from python_intermediate_training.sda_exercises_oop_1.cat import Cat
from python_intermediate_training.sda_exercises_oop_1.dog import Dog

def main():
    cat_object = Cat("Tom")
    cat_object_1 = Cat("Curt")
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
    for animal in animal_list:
        print(animal.make_sound())
    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()

    print('Now other cat will eat')

    cat_object_2.eat_mouse()

if __name__ == "__main__":
    main()
