import os

import pytest


def get_path(filename):
    return os.path.join('tests/fixtures/', filename)


def open_file(filename):
    filepath = get_path(filename)
    with open(filepath, 'r') as f:
        test_file = f.read()
        return test_file


@pytest.fixture
def test_file_flat():
    return open_file('diff_flat.txt')


@pytest.fixture
def flat_json_1():
    return get_path('file1.json')


@pytest.fixture
def flat_json_2():
    return get_path('file2.json')


@pytest.fixture
def flat_yaml_1():
    return get_path('file1.yaml')


@pytest.fixture
def flat_yaml_2():
    return get_path('file2.yml')


@pytest.fixture
def test_file_tree():
    return open_file('diff_tree.txt')


@pytest.fixture
def tree_json_1():
    return get_path('tree1.json')


@pytest.fixture
def tree_json_2():
    return get_path('tree2.json')


@pytest.fixture
def tree_yaml_1():
    return get_path('tree1.yaml')


@pytest.fixture
def tree_yaml_2():
    return get_path('tree2.yml')


@pytest.fixture
def test_file_plain():
    return open_file('plain_diff.txt')


@pytest.fixture
def test_file_json():
    return open_file('json_diff.json')
