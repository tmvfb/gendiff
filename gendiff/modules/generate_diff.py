from gendiff.modules.formatters.return_stylish import stylish
from gendiff.modules.formatters.return_plain import plain
from gendiff.modules.formatters.return_json import to_json


def generate_diff(file1, file2, formatter='stylish'):
    if formatter == 'stylish':
        return stylish(file1, file2)
    if formatter == 'plain':
        return plain(file1, file2)
    if formatter == 'json':
        return to_json(file1, file2)
