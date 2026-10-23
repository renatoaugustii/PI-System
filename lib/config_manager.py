import json

def carregar_config():

    with open(
        "config/config.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)