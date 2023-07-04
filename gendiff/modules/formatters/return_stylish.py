from gendiff.modules.diff import diff


def stylish(file1, file2):
    result = diff(file1, file2)
    result = make_stylish(result)
    # last symbol of result is '\n', don't need it
    return '\n'.join(['{', result[:-1], '}'])


def make_stylish(node, memory='', indent='    '):
    node = dict(sorted(node.items(), key=custom_sort))

    for key, value in node.items():
        key_indent = indent_checker(key, indent)
        memory += ''.join([key_indent, key, ': '])
        if not isinstance(value, dict):
            memory += ''.join([prettify(value), '\n'])
        else:
            memory += '{\n'
            memory = make_stylish(value, memory, indent + '    ')
            memory += ''.join([indent, '}', '\n'])
    return memory


def indent_checker(dict_key, indent):
    # every new nesting level is 4 spaces indented
    # + and - signs should be a part of the indentation
    if dict_key[:2] in ['- ', '+ ']:
        key_indent = indent[2:]
    else:
        key_indent = indent
    return key_indent


def custom_sort(items):
    if items[0][:2] in ['- ', '+ ']:
        return items[0][2:]
    else:
        return items[0]


def prettify(val):
    val = str(val)
    return val.replace('None', 'null')\
              .replace('True', 'true')\
              .replace('False', 'false')
