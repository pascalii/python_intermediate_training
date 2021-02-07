from exceptions_1.excercises import task_2, task_3


def main():
    print('start app')
    # try:
    #     task_2('')
    # # except ValueError as ve:
    # #     print(f'{ve.args} returned')
    # except Exception as e:
    #     print(f"Exception {e.args}")

    result = task_3(11, 0)
    print(result)

    print('finish')

if __name__ == "__main__":
    main()
