import json
import os

print("=" * 60)
print("VALIDAÇÃO DE AMBIENTE")
print("=" * 60)
print()

# ==================================================
# CONFIG
# ==================================================

try:

    with open(
        "config/config.json",
        "r",
        encoding="utf-8"
    ) as f:

        config = json.load(f)

    print("[OK] config/config.json encontrado")

except Exception as erro:

    print(
        "[ERRO] Não foi possível carregar config.json"
    )

    print(erro)

    quit()

# ==================================================
# AF SDK
# ==================================================

print()
print("Validando AF SDK...")

afsdk = config.get(
    "afsdk_dll"
)

if not afsdk:

    print(
        "[ERRO] afsdk_dll não encontrado"
    )

    quit()

if not os.path.exists(afsdk):

    print(
        "[ERRO] AF SDK não encontrada"
    )

    print(afsdk)

    quit()

print("[OK] AF SDK encontrada")
print(afsdk)

# ==================================================
# SERVIDORES
# ==================================================

print()
print("Validando servidores...")

servidores = config.get(
    "pi_servers",
    []
)

if not servidores:

    print(
        "[ERRO] Nenhum servidor encontrado"
    )

    quit()

print(
    f"[OK] {len(servidores)} servidores encontrados"
)

print()

for i, servidor in enumerate(
    servidores,
    start=1
):

    print(
        f"{i} - {servidor}"
    )

# ==================================================
# FINAL
# ==================================================

print()
print("=" * 60)
print("VALIDAÇÃO CONCLUÍDA")
print("=" * 60)