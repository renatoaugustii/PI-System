import json
from pathlib import Path

CONFIG_FILE = Path("config/config.json")

def carregar_config():

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            "Arquivo config/config.json não encontrado."
        )

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)
