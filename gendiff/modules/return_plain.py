from gendiff.modules.diff import diff
from gendiff.modules.return_stylish import custom_sort


def plain(file1, file2):
    result = diff(file1, file2)
    result = make_plain(result).strip()  # delete \n at the end
    return result


def make_plain(node, memory='', folder=''):
    node = dict(sorted(node.items(), key=custom_sort))

    for key, value in node.items():
        path, nested_path = path_builder(folder, key)
        is_updated, is_added, is_removed, old, new = compare(key, node)
        if is_updated and\
           f'Property {path} was updated. From {old} to {new}' not in memory:
            memory += f'Property {path} was updated. From {old} to {new}\n'
        if is_added:
            memory += f'Property {path} was added with value: {new}\n'
        if is_removed:
            memory += f'Property {path} was removed\n'
        if isinstance(value, dict):
            memory = make_plain(value, memory, nested_path)
    return memory


def compare(dict_key, node):  # this won't work if key is '-', consider refactor
    if str(dict_key[0]) not in ['-', '+']:
        return False, False, False, None, None

    val_list = [prettify_plain(value)
                for key, value in node.items()
                if str(key)[2:] == str(dict_key)[2:]
                ]
    if len(val_list) == 2:
        return True, False, False, val_list[0], val_list[1]
    elif str(dict_key)[0] == '-':
        return False, False, True, val_list[0], None
    elif str(dict_key)[0] == '+':
        return False, True, False, None, val_list[0]


def prettify_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in [None, False, True]:
        return str(value).replace('None', 'null')\
                         .replace('False', 'false')\
                         .replace('True', 'true')
    return "'".join(['', str(value), ''])


def path_builder(folder, key):
    try:
        stripped_keyname = str(key)[2:]
    except IndexError:
        stripped_keyname = str(key)
    if folder:
        path = '.'.join([folder, stripped_keyname])
        nested_path = '.'.join([folder, key])
    elif str(key)[0] in ['-', '+']:
        path = stripped_keyname
        nested_path = stripped_keyname
    else:
        path = key
        nested_path = key

    path = "'" + path + "'"
    return path, nested_path
