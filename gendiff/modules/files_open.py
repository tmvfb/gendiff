import json
from os import getcwd
from pathlib import Path

import yaml


def files_open(filepath):
    extension = Path(filepath).suffix

    def load(path):
        if extension == ".json":
            return json.load(path)
        elif extension in [".yaml", ".yml"]:
            return yaml.load(path, Loader=yaml.SafeLoader)
        else:
            raise Exception(
                "Wrong file format. Possible formats are json or yaml."
            )

    try:
        with open(filepath) as f:
            return load(f)
    except FileNotFoundError:
        with open("/".join([getcwd(), filepath])) as f:
            return load(f)
