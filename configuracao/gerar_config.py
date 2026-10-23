import json
import os

print()
print("=" * 50)
print("GERADOR DE CONFIGURAÇÃO")
print("=" * 50)
print()

dll_encontrada = None

caminhos_comuns = [
    r"C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
    r"C:\Program Files\PIPC\AF\PublicAssemblies\4.0\OSIsoft.AFSDK.dll",
]

for caminho in caminhos_comuns:

    if os.path.exists(caminho):
        dll_encontrada = caminho
        break

if dll_encontrada is None:

    print("AF SDK não encontrado.")
    print()

    dll_encontrada = input(
        "Informe o caminho da DLL: "
    )

pi_server = input(
    "Informe o PI Server (ex: pisystem-vitoria): "
).strip()

config = {
    "afsdk_dll": dll_encontrada,
    "pi_server": pi_server
}

os.makedirs(
    "config",
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
        indent=4
    )

print()
print("Configuração salva em:")
print("config/config.json")
