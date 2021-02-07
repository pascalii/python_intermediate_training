import csv


def csv_write(users_list):
    try:
        with open('./data.csv', 'w') as fd:
            writer = csv.writer(fd)
            for user_tuple in users_list:
                writer.writerow(user_tuple)

    except (IOError, Exception) as e:
        print(f'Exception while writing csv format info: {e.args}')


def main():
    users = [
        ('John', 'Smith', 765438),
        ('Samuel', 'Jackson', 660438)
    ]
    csv_write(users)


if __name__ == "__main__":
    main()
