import json
import os

print("\nVALIDAÇÃO DE AMBIENTE\n")

try:

    with open(
        "config/config.json",
        "r",
        encoding="utf-8"
    ) as f:

        config = json.load(f)

    print("[OK] config.json")

except:

    print("[ERRO] config.json não encontrado")
    quit()

afsdk = config["afsdk_dll"]

if os.path.exists(afsdk):

    print("[OK] AF SDK")

else:

    print("[ERRO] AF SDK não encontrada")

print(f"[OK] PI Server: {config['pi_server']}")