import json
from os import getcwd


def files_open(file1, file2):
    try:
        with open('file1') as first_file:
            first_file = json.load(first_file)
    except FileNotFoundError:
        with open('/'.join([getcwd(), file1])) as first_file:
            first_file = json.load(first_file)

    try:
        with open('file2') as second_file:
            second_file = json.load(second_file)
    except FileNotFoundError:
        with open('/'.join([getcwd(), file2])) as second_file:
            second_file = json.load(second_file)
    return first_file, second_file


def diff(file1, file2):
    first_file, second_file = files_open(file1, file2)
    for key, value in first_file.items():
        if key in second_file.keys():
            if second_file[key] == first_file[key]:
                yield f'  {key}: {value}'
            else:
                yield f'- {key}: {value}'
                yield f'+ {key}: {second_file[key]}'
        else:
            yield f'- {key}: {value}'

    for key, value in second_file.items():
        if key not in first_file.keys():
            yield f'+ {key}: {value}'


def generate_diff(file1, file2):
    result = list(diff(file1, file2))
    result.sort(key=lambda x: x[2])
    return '\n'.join(result).replace('True', 'true').replace('False', 'false')


# if __name__ == '__main__':
#     generate_diff(file1, file2)
