import json
import os
from pathlib import Path

# ==================================================
# PROCURAR AF SDK
# ==================================================

possiveis_caminhos = [
    r"C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
    r"C:\Program Files\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
]

afsdk_dll = None

for caminho in possiveis_caminhos:

    if os.path.exists(caminho):
        afsdk_dll = caminho
        break

if afsdk_dll is None:

    print("\n[ERRO]")
    print("OSIsoft.AFSDK.dll não encontrada.")
    quit()

print(f"\n[OK] AF SDK encontrada:")
print(afsdk_dll)

# ==================================================
# CARREGAR SDK
# ==================================================

try:

    import clr

    clr.AddReference(afsdk_dll)

    print("\n[OK] AF SDK carregada")

except Exception as erro:

    print("\n[ERRO] Falha ao carregar AF SDK")
    print(erro)
    quit()

# ==================================================
# LISTAR SERVIDORES PI
# ==================================================

from OSIsoft.AF.PI import PIServers

servidores = PIServers()

print("\nServidores encontrados:\n")

lista_servidores = []

for servidor in servidores:

    lista_servidores.append(servidor.Name)

for i, nome in enumerate(lista_servidores, start=1):

    print(f"{i} - {nome}")

# ==================================================
# TESTAR CONEXÃO
# ==================================================

pi_server = None

for nome in lista_servidores:

    try:

        servidor = servidores[nome]

        servidor.Connect()

        pi_server = nome

        print(f"\n[OK] Conectado em: {nome}")

        break

    except:
        pass

if pi_server is None:

    print("\n[ERRO]")
    print("Nenhum PI Server acessível.")
    quit()

# ==================================================
# CRIAR CONFIG
# ==================================================

config = {
    "afsdk_dll": afsdk_dll,
    "pi_server": pi_server
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

print("\n[OK] Configuração criada:")
print("config/config.json")