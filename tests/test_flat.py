from gendiff import generate_diff


def test_generate_diff_json():
    with open('tests/fixtures/diff_flat.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == file3


def test_generate_diff_yaml():
    with open('tests/fixtures/diff_flat.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yml') == file3
