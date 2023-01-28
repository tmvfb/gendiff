from gendiff.modules.diff import diff
from gendiff.modules.formatters.return_stylish import custom_sort


def plain(file1, file2):
    result = diff(file1, file2)
    result = make_plain(result).strip()  # delete \n at the end
    return result


def make_plain(node, memory='', folder=''):  # folder stores current path
    node = dict(sorted(node.items(), key=custom_sort))

    for key, value in node.items():
        path, nested_path = path_builder(folder, key)
        is_modified_item, comparison_outcome = compare(key, node, path)
        if is_modified_item:
            memory += comparison_outcome
        if isinstance(value, dict):
            memory = make_plain(value, memory, nested_path)
    return memory


def compare(dict_key, node, path):
    is_modified_item = True
    indicator = dict_key[:2]  # catch plus/minus sign
    val_list = [prettify_plain(value)
                for key, value in node.items()
                if str(key)[2:] == str(dict_key)[2:]
                ]
    if len(val_list) == 2:
        if indicator == '+ ':
            return False, None  # avoid duplicates
        outcome =\
            f'Property {path} was updated. From {val_list[0]} to {val_list[1]}\n'  # noqa
    elif indicator not in ['- ', '+ ']:
        return False, None
    elif indicator == '- ':
        outcome =\
            f'Property {path} was removed\n'
    elif indicator == '+ ':
        outcome =\
            f'Property {path} was added with value: {val_list[0]}\n'
    return is_modified_item, outcome


def prettify_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in [None, False, True]:
        return str(value).replace('None', 'null')\
                         .replace('False', 'false')\
                         .replace('True', 'true')
    return "'".join(['', str(value), ''])


def path_builder(folder, key):
    stripped_keyname = key[2:]  # no need for length check!
    if folder:
        path = '.'.join([folder, stripped_keyname])
        nested_path = '.'.join([folder, key])
    elif key[:2] in ['- ', '+ ']:
        path = stripped_keyname
        nested_path = stripped_keyname
    else:
        path = key
        nested_path = key

    path = "'" + path + "'"
    return path, nested_path
