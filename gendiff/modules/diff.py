from gendiff.modules.files_open import files_open


def diff(file1, file2):
    file1 = files_open(file1)
    file2 = files_open(file2)

    for key, value in file1.items():
        if key in file2.keys():
            if file2[key] == file1[key]:
                yield f'  {key}: {value}'
            else:
                yield f'- {key}: {value}'
                yield f'+ {key}: {file2[key]}'
        else:
            yield f'- {key}: {value}'

    for key, value in file2.items():
        if key not in file1.keys():
            yield f'+ {key}: {value}'
