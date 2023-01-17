import json
import yaml
from os import getcwd


def files_open(filepath):
    if filepath.endswith('.json'):
        format = json
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        format = yaml
    try:
        with open('filepath') as working_file:
            working_file = format.load(working_file)
    except FileNotFoundError:
        with open('/'.join([getcwd(), filepath])) as working_file:
            working_file = format.load(working_file)

    return working_file
