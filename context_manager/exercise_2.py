class OpenFileManager:
    def __init__(self, path: str = '', mode = 'a'):
        self.__source = path
        self.__mode = mode
        self.__fd = None

    @property
    def source(self):
        return self.__source

    def get_source(self):
        return self.__source

    @source.setter
    def source(self, path: str):
        self.__source = path

    def set_source(self, path: str):
        self.__source = path

    def __enter__(self):
        print("Opening file")
        self.__fd = open(self.__source, self.__mode)
        return self.__fd

    def __exit__(self, *args):
        print('Closing file')
        self.__fd.close()

def exercise_2():
    manager = OpenFileManager()
    manager_source = manager.source #getter
    print(manager_source)
    manager.source = './test_file.txt' #setter
    manager_source = manager.source  #getter
    print(manager_source)

    try:
        with manager as fd:
            print('Writing')
            fd.write('Text')
    except IOError as e:
        print(f'Error found: {e.args}')
