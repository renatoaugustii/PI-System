import csv

from lib.pi_connection import conectar_pi

import clr

from lib.config_manager import carregar_config

cfg = carregar_config()

clr.AddReference(
    cfg["afsdk_dll"]
)

from OSIsoft.AF.PI import PIPoint

server = conectar_pi()

print(f"Conectado em: {server.Name}")

with open(
    "templates/equipamentos.txt",
    "r",
    encoding="utf-8"
) as f:

    equipamentos = [
        linha.strip()
        for linha in f
        if linha.strip()
    ]

with open(
    "resultado_tags.csv",
    "w",
    newline="",
    encoding="utf-8-sig"
) as csvfile:

    writer = csv.writer(
        csvfile,
        delimiter=";"
    )

    writer.writerow([
        "Equipamento",
        "Tag"
    ])

    for equipamento in equipamentos:

        print(
            f"\nPesquisando: {equipamento}"
        )

        tags = list(
            PIPoint.FindPIPoints(
                server,
                f"{equipamento}*"
            )
        )

        print(
            f"Encontradas: {len(tags)}"
        )

        for tag in tags:

            writer.writerow([
                equipamento,
                tag.Name
            ])

print("\nConcluído!")
print("Arquivo gerado: resultado_tags.csv")