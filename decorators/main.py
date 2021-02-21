from decorators.case_2 import read_file
from functools import wraps

def catch_io_error_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f'IOError caught {e.args}')
            return None

    return inner

def catch_io_error_with_wraps(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f'IOError caught {e.args}')
            return None

    return inner

@catch_io_error_decorator
def throw_exception_file():
    raise IOError('Test error')

@catch_io_error_with_wraps
def read_file_does_not_exist():
    with open('./training.training.training', 'r') as fd:
        fd.read()

def main():
    read_file_does_not_exist()


#     a, b = print_hello_yall(1, 2)
#     print(f'In main: {a} {b}')
#
#
# def wrap_before_and_after(func):
#     def wrapper(*args, **kwargs):
#         print('Before')
#         result = func(*args, **kwargs)
#         print('After')
#         return result
#
#     return wrapper

# read_file(file_path='./abc')

# @wrap_before_and_after
# def print_hello_yall(a, b):
#     print('Hello yall!')
#     print(f'{a, b}')
#     return a, b


if __name__ == '__main__':
    main()
