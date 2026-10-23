import csv
from datetime import datetime

import clr

from lib.config_manager import carregar_config
from lib.pi_connection import selecionar_servidor

# ==========================================
# INÍCIO
# ==========================================

inicio = datetime.now()

print("=" * 60)
print("BUSCA DE TAGS")
print("=" * 60)
print()

# ==========================================
# CARREGAR CONFIGURAÇÃO
# ==========================================

print("Carregando configuração...")

cfg = carregar_config()

print("[OK] Configuração carregada")

# ==========================================
# CARREGAR AF SDK
# ==========================================

print()
print("Carregando AF SDK...")

clr.AddReference(
    cfg["afsdk_dll"]
)

print("[OK] AF SDK carregada")

# ==========================================
# IMPORTAR PI
# ==========================================

from OSIsoft.AF.PI import PIPoint

# ==========================================
# ESCOLHER SERVIDOR
# ==========================================

server = selecionar_servidor()

print()
print(f"[OK] Conectado em: {server.Name}")
print()

# ==========================================
# CARREGAR EQUIPAMENTOS
# ==========================================

print("Carregando equipamentos...")

with open(
    "templates/equipamentos.txt",
    "r",
    encoding="utf-8"
) as arquivo:

    equipamentos = [
        linha.strip()
        for linha in arquivo
        if linha.strip()
    ]

total = len(equipamentos)

print(
    f"[OK] {total} equipamentos carregados"
)

print()

# ==========================================
# PROCESSAMENTO
# ==========================================

total_tags = 0

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

    for i, equipamento in enumerate(
        equipamentos,
        start=1
    ):

        print("-" * 60)

        print(
            f"[{i}/{total}] "
            f"Pesquisando: {equipamento}"
        )

        try:

            tags = list(
                PIPoint.FindPIPoints(
                    server,
                    f"{equipamento}*"
                )
            )

            qtd = len(tags)

            total_tags += qtd

            print(
                f"Encontradas: {qtd} | "
                f"Acumulado: {total_tags}"
            )

            for tag in tags:

                writer.writerow([
                    equipamento,
                    tag.Name
                ])

        except Exception as erro:

            print(
                f"[ERRO] {equipamento}"
            )

            print(erro)

# ==========================================
# FINAL
# ==========================================

fim = datetime.now()

print()
print("=" * 60)
print("PROCESSAMENTO CONCLUÍDO")
print("=" * 60)

print(
    f"Equipamentos processados : {total}"
)

print(
    f"Tags encontradas        : {total_tags}"
)

print(
    "Arquivo gerado          : resultado_tags.csv"
)

print(
    f"Tempo total             : {fim - inicio}"
)

print("=" * 60)