import re


def exercise_1():
    print('Write number here: ')
    value = input()

    expression = '[0-9]+'
    if re.fullmatch(expression, value):
        print('Found number')
        if int(value) % 2 == 0:
            print('Even number')
        else:
            print('Odd number')
    else:
        print('Incorrect input')

def exercise_2():
    print('Write postal code here: ')
    value = input()
    expression = '[0-9]{2}-[0-9]{3}'
    if re.fullmatch(expression, value):
        print("Correct postal code")
    else:
        print("Incorrect postal code")