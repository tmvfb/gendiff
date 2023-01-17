#!/usr/bin/env/python3
from gendiff.modules.return_json import return_json


def generate_diff(file1, file2):
    return return_json(file1, file2)


if __name__ == '__main__':
    generate_diff()
