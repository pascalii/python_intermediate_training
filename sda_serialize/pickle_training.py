import pickle


def pickle_write(items: list):
    print('pickle_write start')
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format info: {e.args}')
    print('pickle_write finish')


def pickle_read():
    print('pickle_read start')
    string_list = []
    try:
        with open('./data.pickle', 'rb') as fd:
            string_list = pickle.load(fd)
    except (IOError, Exception) as e:
        print(f'Exception while reading pickle format info: {e.args}')
    print('pickle_read finish')
    return string_list


def main():
    abc = ['bread', 'butter', 'cola']
    pickle_write(abc)
    list_of_strings = pickle_read()
    print(list_of_strings)


if __name__ == "__main__":
    main()
