import clr

from lib.config_manager import carregar_config

def selecionar_servidor():

    cfg = carregar_config()

    clr.AddReference(
        cfg["afsdk_dll"]
    )

    from OSIsoft.AF.PI import PIServers

    servidores = PIServers()

    print()
    print("=" * 60)
    print("SELEÇÃO DE SERVIDOR")
    print("=" * 60)
    print()

    for i, nome in enumerate(
        cfg["pi_servers"],
        start=1
    ):

        print(f"{i} - {nome}")

    print()

    escolha = int(
        input(
            "Escolha o servidor: "
        )
    )

    nome_servidor = cfg[
        "pi_servers"
    ][
        escolha - 1
    ]

    print()
    print(
        f"Conectando em: "
        f"{nome_servidor}"
    )

    server = servidores[
        nome_servidor
    ]

    server.Connect()

    print(
        f"[OK] Conectado em: "
        f"{nome_servidor}"
    )

    return server