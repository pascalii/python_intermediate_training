import json


def write_json_to_file():
    json_list = [
        {'name': 'Bart'},
        {'name': 'Dick'}
    ]

    try:
        with open("./training.json", "w") as fd:
            json.dump(json_list, fd, indent=2)

    except (IOError, Exception) as e:
        print(f'Problem writing to file, more info: {e.args}')

def json_from_file():
    json_list = []

    try:
        with open("./training.json", "r") as fd:
            json_list = json.load(fd)

    except (IOError, Exception) as e:
        print(f'Problem with writing to file, more info: {e.args}')

    return json_list