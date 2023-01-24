from gendiff import generate_diff


def test_generate_diff_tree():
    with open('tests/fixtures/tree3.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/tree1.json', 'tests/fixtures/tree2.json') == file3
