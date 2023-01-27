from gendiff import generate_diff


def test_plain_generate_diff():
    with open('tests/fixtures/plain_diff.txt', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/tree1.json',
                         'tests/fixtures/tree2.json', 'plain') == test_file


def test_json_generate_diff():
    with open('tests/fixtures/json_diff.json', 'r') as test_file:
        test_file = test_file.read()
    assert generate_diff('tests/fixtures/tree1.json',
                         'tests/fixtures/tree2.json', 'json') == test_file
