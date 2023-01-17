from gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/file3.json', 'r') as file3:
        file3 = file3.read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == file3

    with open('tests/fixtures/file3.yaml', 'r') as file4:
        file4 = file4.read()
    assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml') == file4
