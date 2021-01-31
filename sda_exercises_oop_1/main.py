from python_intermediate_training.sda_exercises_oop_1.cat import Cat


def main():
    cat_object = Cat("Tom")
    cat_object_1 = Cat("Curt")
    cat_object_2 = Cat("Wojtek", "Mial")
    cat_object_3 = Cat("Lazy", "I don't meow")

    # cats = [cat_object_1, cat_object_2, cat_object_3, cat_object]
    cats = []
    cats.append(cat_object)
    cats.append(cat_object_1)
    cats.append(cat_object_2)
    cats.append(cat_object_3)
    for cat in cats:
        sound = cat.make_sound()
        print(sound)
    
if __name__ == "__main__":
    main()
