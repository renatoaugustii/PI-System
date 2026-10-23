import json
import os
from pathlib import Path
from datetime import datetime

# ==================================================
# INÍCIO
# ==================================================

inicio = datetime.now()

print("=" * 60)
print("CONFIGURAÇÃO INICIAL DO PI SYSTEM")
print("=" * 60)
print()

# ==================================================
# PROCURAR AF SDK
# ==================================================

print("[ETAPA 1] Procurando AF SDK...")
print()

possiveis_caminhos = [
    r"C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
    r"C:\Program Files\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
]

afsdk_dll = None

for caminho in possiveis_caminhos:

    print(f"Verificando: {caminho}")

    if os.path.exists(caminho):
        afsdk_dll = caminho
        break

if afsdk_dll is None:

    print()
    print("[ERRO] AF SDK não encontrada.")
    quit()

print()
print("[OK] AF SDK encontrada")
print(afsdk_dll)

# ==================================================
# CARREGAR AF SDK
# ==================================================

print()
print("[ETAPA 2] Carregando AF SDK...")

try:

    import clr

    clr.AddReference(afsdk_dll)

    print("[OK] AF SDK carregada")

except Exception as erro:

    print()
    print("[ERRO] Falha ao carregar AF SDK")
    print(erro)

    quit()

# ==================================================
# LISTAR SERVIDORES
# ==================================================

print()
print("[ETAPA 3] Obtendo lista de servidores PI...")

try:

    from OSIsoft.AF.PI import PIServers

    servidores = PIServers()

    print("[OK] PIServers carregado")

except Exception as erro:

    print()
    print("[ERRO] Falha ao carregar lista de servidores")
    print(erro)

    quit()

lista_servidores = []

print()
print("Enumerando servidores disponíveis...")
print()

for i, servidor in enumerate(servidores, start=1):

    try:

        nome = servidor.Name

        lista_servidores.append(nome)

        print(f"{i} - {nome}")

    except Exception as erro:

        print(
            f"[ERRO] Falha ao obter servidor {i}"
        )

print()
print(
    f"[OK] {len(lista_servidores)} servidores encontrados"
)

# ==================================================
# CRIAR CONFIG
# ==================================================

print()
print("[ETAPA 4] Gerando configuração...")

config = {
    "afsdk_dll": afsdk_dll,
    "pi_servers": lista_servidores
}

Path("config").mkdir(
    parents=True,
    exist_ok=True
)

with open(
    "config/config.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        config,
        f,
        indent=4,
        ensure_ascii=False
    )

print("[OK] config/config.json criado")

# ==================================================
# RESUMO FINAL
# ==================================================

fim = datetime.now()

print()
print("=" * 60)
print("CONFIGURAÇÃO FINALIZADA")
print("=" * 60)
print()

print("AF SDK:")

print(
    afsdk_dll
)

print()

print(
    f"Servidores encontrados: "
    f"{len(lista_servidores)}"
)

print()

print(
    f"Tempo total: "
    f"{fim - inicio}"
)

print()

print(
    "Arquivo criado:"
)

print(
    "config/config.json"
)

print()
print("=" * 60)