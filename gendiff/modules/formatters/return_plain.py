from gendiff.modules.diff import diff
from gendiff.modules.formatters.return_stylish import custom_sort


def plain(file1, file2):
    result = diff(file1, file2)
    result = make_plain(result).strip()  # delete \n at the end
    return result


def make_plain(node, memory='', folder=''):  # folder stores current path
    node = dict(sorted(node.items(), key=custom_sort))

    for key, value in node.items():
        # path describes current nested object e.g. key1.key2
        path_name, path = build_path(folder, key)
        is_modified_item, comparison_outcome = compare(key, node, path_name)
        if is_modified_item:
            memory += comparison_outcome
        elif isinstance(value, dict):
            memory = make_plain(value, memory, path)
    return memory


def compare(dict_key, node, path):
    """
    Checks if a passed key was modified in the new file.
    """
    is_modified_item = True
    indicator = dict_key[:2]  # catch plus/minus sign

    # val_list stores all value entries with the passed key in the passed node
    # 1 entry if the object wasn't modified or was added/removed
    # 2 entries if the object was modified (one with + and one with - key)
    val_list = [prettify_plain(value)
                for key, value in node.items()
                if str(key)[2:] == str(dict_key)[2:]]
    if len(val_list) == 2:
        if indicator == '+ ':
            return False, None  # avoid duplicates
        outcome =\
            f'Property {path} was updated. From {val_list[0]} to {val_list[1]}\n'  # noqa: E501
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


def build_path(folder, key):
    stripped_keyname = key[2:]
    # no need for length check!
    # if key has + or - then len(key) >= 3
    # else key wasn't modified and stripped_keyname won't be used anywhere

    if folder:
        # if key wasn't changed only path variable is used
        # else only path_name variable is used
        path = '.'.join([folder, key])
        path_name = '.'.join([folder, stripped_keyname])

    # cases for highest nesting level
    elif key[:2] in ['- ', '+ ']:
        path = stripped_keyname
        path_name = stripped_keyname
    else:
        path = key
        path_name = key

    path_name = "'" + path_name + "'"
    return path_name, path
