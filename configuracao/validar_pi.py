import json
import os

print()

try:

    with open(
        "config/config.json",
        "r",
        encoding="utf-8"
    ) as f:

        cfg = json.load(f)

    print("[OK] Arquivo config")

    if os.path.exists(
        cfg["afsdk_dll"]
    ):
        print("[OK] AF SDK")
    else:
        print("[ERRO] AF SDK não encontrado")

except Exception as erro:

    print("[ERRO]", erro)
