import json
import yaml
from os import getcwd


def files_open(filepath):
    def loader(path):
        if filepath.endswith('.json'):
            return json.load(path)
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            return yaml.load(path, Loader=yaml.SafeLoader)
    try:
        with open('filepath') as working_file:
            working_file = loader(working_file)
    except FileNotFoundError:
        with open('/'.join([getcwd(), filepath])) as working_file:
            working_file = loader(working_file)

    return working_file
