# PI-System

Repositório para automações e consultas em sistemas PI.

## Estrutura

configuracao/
- Scripts de configuração inicial.

lib/
- Funções compartilhadas.

scripts/
- Scripts de negócio.

templates/
- Arquivos modelo.

config/
- Configuração local (não versionada).

## Primeira utilização

Execute:

    python configuracao/gerar_config.py

Depois valide:

    python configuracao/validar_pi.py

## Buscar Tags

Edite:

    templates/equipamentos.txt

Execute:

    python scripts/buscar_tags.py

Resultado:

    resultado_tags.csv
