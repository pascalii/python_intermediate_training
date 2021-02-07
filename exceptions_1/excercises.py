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
