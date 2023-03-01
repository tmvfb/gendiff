import pytest
from gendiff import generate_diff


parameters = [('flat_json_1', 'flat_json_2', 'stylish', 'test_file_flat'),
              ('flat_yaml_1', 'flat_yaml_2', 'stylish', 'test_file_flat'),
              ('tree_json_1', 'tree_json_2', 'stylish', 'test_file_tree'),
              ('tree_json_1', 'tree_json_2', 'stylish', 'test_file_tree'),
              ('tree_yaml_1', 'tree_yaml_2', 'stylish', 'test_file_tree'),
              ('tree_json_1', 'tree_json_2', 'plain', 'test_file_plain'),
              ('tree_json_1', 'tree_json_2', 'json', 'test_file_json')
              ]


@pytest.mark.parametrize('file1, file2, format, test_file', parameters)
def test_generate_diff(file1, file2, format, test_file, request):
    file1 = request.getfixturevalue(file1)
    file2 = request.getfixturevalue(file2)
    expected = request.getfixturevalue(test_file)
    result = generate_diff(file1, file2, format)
    assert result == expected


def test_generate_diff_default(tree_json_1, tree_json_2, test_file_tree):
    assert generate_diff(tree_json_1, tree_json_2) == test_file_tree
