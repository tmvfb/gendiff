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
            yield dict(compare_pairs({key: value}, sign='+'))  # returns pair

    for key, value in dict1.items():
        if key not in dict2.keys():  # checks if key in 2nd dict
            yield dict(compare_pairs({key: value}, sign='-'))
        # checks if at least one value (child) is not dict
        # if true, no need to go deeper (no nested dict)
        elif not all(isinstance(i, dict) for i in [value, dict2[key]]):
            yield dict(compare_pairs({key: value}, {key: dict2[key]}))

# if key in both dicts + can go deeper (=values are dicts): go deep recursively
# child is a dict in this case, use dict comprehension to define it correctly
# tree_diff in dict comp will generate all {key: value} pairs for nested dict
        else:
            child = dict((k, v)
                         for pair in tree_diff(value, dict2[key])
                         for k, v in pair.items()
                         )
            yield {key: child}


# compare 2 {key: value} pairs if at least 1 value is not dict
# or if one pair is empty
def compare_pairs(pair1, pair2={}, sign='-'):
    key = list(pair1.keys())[0]
    value = pair1[key]
    if key[:2] in ['- ', '+ ']:
        raise Exception('''Incorrect key.
                        Keyname can't begin with "+ " or "- "''')
    if pair1 == pair2:
        yield (key, value)
    elif pair2:
        yield (' '.join(['-', key]), value)
        yield (' '.join(['+', key]), pair2[key])
    else:
        yield (' '.join([sign, key]), value)
