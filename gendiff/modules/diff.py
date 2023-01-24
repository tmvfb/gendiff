from gendiff.modules.files_open import files_open


def diff(file1, file2):
    file1 = files_open(file1)
    file2 = files_open(file2)
    return list(tree_diff(file1, file2))


def tree_diff(dict1, dict2):
    for key, value in dict1.items():
        try:
            if key not in dict2.keys():
                yield f'- {key}: {value}'
            elif not isinstance(value, dict):
                yield compare({key: value}, {key: dict2[key]})
            else:
                yield f'{key}: '
                yield list(tree_diff(value, dict2[key]))
        except AttributeError:
            pass


def compare(pair1, pair2):
    for key, value in pair1.items():
        if pair1 == pair2:
            return f'{key}: {value}'
        else:
            return f'+ {key}: {value} \n {key}: {pair2[key]}'
