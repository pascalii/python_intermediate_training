from python_intermediate_training.sda_exercises_oop_1.cat import Cat


def main():
    cat_object = Cat("Tom")
    sound: str = cat_object.make_sound()
    print(sound)
    
    
    
if __name__ == "__main__":
    main()
