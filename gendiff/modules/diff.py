from gendiff.modules.files_open import files_open


def diff(file1, file2):
    file1 = files_open(file1)
    file2 = files_open(file2)
    result = dict((k, v)  # converting generator to dict of dicts
                  for pair in tree_diff(file1, file2)
                  for k, v in pair.items()
                  )
    return result


def tree_diff(dict1, dict2):  # returns a generator (of nested dicts)

    for key, value in dict2.items():
        if key not in dict1.keys():  # checks if key in 1st dict
            yield {''.join(['- ', key]): value}  # returns dict element

    for key, value in dict1.items():
        if key not in dict2.keys():  # checks if key in 2nd dict
            yield {''.join(['+ ', key]): value}

        # checks if at least one value (child) is not dict
        # if true, no need to go deeper (no nested dict)
        elif not all(isinstance(i, dict) for i in [value, dict2[key]]):
            yield compare({key: value}, {key: dict2[key]})

# if key in both dicts + can go deeper (=values are dicts): go deep recursively
# child is a dict in this case, use dict comprehension to define it correctly
# tree_diff in dict comp will generate all {key: value} pairs for nested dict
        else:
            child = dict((k, v)
                         for pair in tree_diff(value, dict2[key])
                         for k, v in pair.items()
                         )
            yield {key: child}


# compares 2 {key: value} pairs if at least 1 value is not dict
def compare(pair1, pair2):
    for key, value in pair1.items():
        if pair1 == pair2:
            return {k: v for k, v in pair1.items()}
        else:
            return {''.join(['- ', key]): value}
            return {''.join(['+ ', key]): pair2[key]}
