from gendiff.modules.diff import diff
from gendiff.modules.formatters.return_stylish import custom_sort
import json


def to_json(file1, file2):
    result = diff(file1, file2)
    result = sort_keys(result)
    return json.dumps(result)


def sort_keys(node):
    return {k: sort_keys(v) if isinstance(v, dict) else v
            for k, v in sorted(node.items(), key=custom_sort)}
