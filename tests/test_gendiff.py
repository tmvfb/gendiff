from gendiff import generate_diff


def test_generate_diff():
    with open('/home/tmvfb/python-project-50/tests/fixtures/file3.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == file3
