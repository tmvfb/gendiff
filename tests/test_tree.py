from gendiff import generate_diff


def test_tree_json():
    with open('tests/fixtures/diff_tree.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/tree1.json',
                         'tests/fixtures/tree2.json') == file3


def test_tree_yaml():
    with open('tests/fixtures/diff_tree.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/tree1.yaml',
                         'tests/fixtures/tree2.yaml') == file3
