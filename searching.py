import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data = json.load(data_file)
    print(data)

    if field in data.keys():
        return data[field]
    else:
        return None
    #teoreticky tam to none nemusi byt protoze kdyby to tam nebylo, tak to stejne vyhodi none


def main():
    unordered_numbers = read_data('sequential.json', 'unordered_numbers')
    pass


if __name__ == '__main__':
    main()

