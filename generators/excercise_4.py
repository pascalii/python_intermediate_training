from time import sleep


def lazy_read_generator(fd, text_size=1024):
    while True:
        data = fd.read(text_size)
        if not data:
            break
        yield data


def excercise_4():
    print("excercise 4")
    with open("./lorem_ipsum.txt", "r") as fd:
        for part_line in lazy_read_generator(fd):
            print(part_line)
            sleep(2)
