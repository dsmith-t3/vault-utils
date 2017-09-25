import os
import yaml


def load_config():
    with open("config.yml") as f:
        data = yaml.safe_load(f)
    missing = [opt for opt in ("vault_url", "token") if data.get(opt, None) is None]
    if missing:
        raise Exception("%s not set" % ", ".join(missing))
    return data
