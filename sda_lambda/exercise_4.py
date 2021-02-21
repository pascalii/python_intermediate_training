from random import randint


def exercise_4():
    randoms_list = [randint(0, 101) for item in range(10)]
    print("Before")
    print(randoms_list)
    print("After")
    print(list(map(lambda number: number * 2, randoms_list)))