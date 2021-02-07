import sys


def task_1():
    list_of_numbers = [1, 5, 8, 12, 33]
    print('task_1 before')
    try:
        result = list_of_numbers[5]
    except IndexError as ie:
        print(f'Exception caught {ie.args}')
    except Exception as ex:
        print(f'Exception caught {ex.args}')
    print('task_1 after')
    try:
        result = list_of_numbers[5]
    except (IndexError, Exception) as e:
        print(f'Exception caught by tuple{e.args}')


def task_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty')
    print(f'Given name is: {name}')


def task_3(number: int, divisor: int):
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as zde:
        print(f'Dont divide by zero, dogg')
        result = sys.float_info.max
        # result = float(sys.maxsize)
    return result


def task_4(dictionary: dict):
    key = 'items'
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as ke:
        print(f'Key {key} not found, more info {ke.args}')


def task_4_p_2(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if item not in items:
        print('Key does not exist or list is empty')


def task_6():
    raise NotImplementedError('Solved feature')


def task_7():
    fd = None
    try:
        fd = open(
            'C:\\Users\HP\PycharmProjects\Python_intermediate\python_intermediate_training\exceptions_1\booger.txt')
    except IOError as i:
        print(f'Exception caught {i.args}')

    finally:
        if fd:
            print("File descriptor closing")
            fd.close()
