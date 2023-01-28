from gendiff import generate_diff


def test_generate_diff_flat_json():
    with open('tests/fixtures/diff_flat.txt', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == test_file


def test_generate_diff_flat_yaml():
    with open('tests/fixtures/diff_flat.txt', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yml') == test_file


def test_generate_diff_tree_json():
    with open('tests/fixtures/diff_tree.txt', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/tree1.json',
                         'tests/fixtures/tree2.json') == test_file


def test_generate_diff_tree_yaml():
    with open('tests/fixtures/diff_tree.txt', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/tree1.yaml',
                         'tests/fixtures/tree2.yaml') == test_file
