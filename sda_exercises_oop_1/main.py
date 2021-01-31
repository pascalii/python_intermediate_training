from python_intermediate_training.sda_exercises_oop_1.cat import Cat
from python_intermediate_training.sda_exercises_oop_1.dog import Dog

def main():
    cat_object = Cat("Tom")
    cat_object_1 = Cat("Curt")
    cat_object_2 = Cat("Wojtek", "mial")
    cat_object_3 = Cat("Lazy", "I don't meow")
    dog_object = Dog("Bernard", "woof")
    # cats = [cat_object_1, cat_object_2, cat_object_3, cat_object]
    print(dog_object.make_sound())

    cats = []
    cats.append(cat_object)
    cats.append(cat_object_1)
    cats.append(cat_object_2)
    cats.append(cat_object_3)
    for cat in cats:
        sound = cat.make_sound()
        print(sound)
    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()

    print('Now other cat will eat')

    cat_object_2.eat_mouse()

if __name__ == "__main__":
    main()
