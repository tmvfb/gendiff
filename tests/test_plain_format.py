from gendiff import generate_diff


def test_plain_generate_diff():
    with open('tests/fixtures/plain_diff.txt', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/tree1.json',
                         'tests/fixtures/tree2.json', 'plain') == file3
