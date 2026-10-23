import clr

from lib.config_manager import carregar_config

def conectar_pi():

    cfg = carregar_config()

    clr.AddReference(
        cfg["afsdk_dll"]
    )

    from OSIsoft.AF.PI import PIServers

    server = PIServers()[
        cfg["pi_server"]
    ]

    server.Connect()

    return server
