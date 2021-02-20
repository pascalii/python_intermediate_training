from sda_serialize.human import Human, json_human_to_file, json_human_from_file

# from serialize.csv_training import csv_writer, csv_read
# from serialize.pickle_training import pickle_write, pickle_read

# from serialize.json_training import json_to_file, json_from_file

from sda_serialize.json_training import write_json_to_file


def main():
    # abc = ['bread', 'butter', 'cola']
    # pickle_write(abc)
    # print(pickle_read())

    # users = [
    #     ('John', "Smith", 765438),
    #     ('Samuel', "Jackson", 668438)
    # ]
    #
    # # csv_writer(users)
    # print(csv_read())

    # write_json_to_file()
    # print(json_from_file())



    # h1 = Human(30, "Sebastian", "Daop")
    # h2 = Human(39, "Valeria", "Zippo")
    # h3 = Human(22, "Amadeus", "Kaku")
    #
    # humans = [h1, h2, h3]
    #
    # json_human_to_file(humans)

    humans = json_human_from_file()
    for human in humans:
        print(human)

if __name__ == "__main__":
    main()