import os
import yaml


def load_config():
    config_file = "config.yml"

    if not os.path.isfile(config_file):
        raise Exception(config_file + " does not exist")

    file = open(config_file)
    data = yaml.safe_load(file)
    file.close()

    options = ["vault_url", "token"]

    for option in options:
        if data[option] is None:
            raise Exception(option + " is not set")

    return data
