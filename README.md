# PI-System

Coleção de automações e utilitários para consulta, extração e processamento de informações em ambientes PI System.

O objetivo deste repositório é centralizar scripts reutilizáveis, reduzir atividades manuais repetitivas e fornecer uma base padronizada para o desenvolvimento de novas automações.

---

# Estrutura do Projeto

```text
PI-System/
│
├── configuracao/
├── docs/
├── lib/
├── scripts/
├── templates/
├── config/
├── logs/
│
├── README.md
└── .gitignore
```

---

# Pré-requisitos

Antes de utilizar qualquer script, verifique:

- Python 3.10 ou superior
- PythonNet instalado
- AF SDK instalado
- Permissão de acesso ao ambiente PI

---

# Configuração Inicial

Na primeira utilização execute:

```bash
python configuracao/gerar_config.py
```

O script irá:

- Localizar automaticamente o AF SDK
- Identificar os servidores PI disponíveis
- Gerar o arquivo local de configuração

---

# Validação do Ambiente

Para validar a configuração atual execute:

```bash
python configuracao/validar_ambiente.py
```

A validação verifica:

- Arquivo de configuração local
- AF SDK
- Lista de servidores PI identificados

---

# Arquivo de Configuração

Após a configuração inicial será criado:

```text
config/config.json
```

O arquivo armazena informações necessárias para execução das automações, como:

- Caminho do AF SDK
- Lista de servidores PI disponíveis

Exemplo:

```json
{
    "afsdk_dll": "C:\\Caminho\\Para\\OSIsoft.AFSDK.dll",
    "pi_servers": [
        "Servidor_01",
        "Servidor_02"
    ]
}
```

Este arquivo contém configurações específicas da máquina do usuário e não deve ser versionado.

---

# Utilização dos Scripts

Os scripts disponíveis encontram-se na pasta:

```text
scripts/
```

A documentação detalhada de cada automação encontra-se em:

```text
docs/
```

Os arquivos de entrada devem ser armazenados na pasta:

```text
templates/
```

A forma de execução, dependências, entradas e saídas de cada automação estão documentadas individualmente em seus respectivos arquivos de documentação.

---

# Scripts Disponíveis

| Script | Documentação |
|----------|----------|
| buscar_tags.py | docs/buscar_tags.md |
| gerar_config.py | docs/gerar_config.md |
| validar_ambiente.py | docs/validar_ambiente.md |

Novos scripts devem possuir documentação própria dentro da pasta `docs`.

---

# Desenvolvimento

Ao criar novas automações:

1. Utilizar as configurações existentes em `config/config.json`
2. Reutilizar funções compartilhadas da pasta `lib`
3. Evitar caminhos fixos no código
4. Não armazenar credenciais
5. Documentar cada automação em `docs`
6. Manter o README focado apenas em informações gerais do projeto
7. Seguir os padrões definidos para estrutura e organização do repositório

---

# Segurança

Nunca versionar ou armazenar:

- Usuários
- Senhas
- Tokens
- Chaves de acesso
- Informações sensíveis do ambiente

O arquivo:

```text
config/config.json
```

é ignorado pelo Git e deve permanecer apenas na máquina do usuário.

Também não devem ser incluídos no repositório:

- Nomes reais de servidores utilizados em ambientes produtivos
- Nomes reais de ativos
- Tags de ambientes produtivos
- Informações operacionais sensíveis
- Arquivos contendo credenciais ou dados de acesso

---

# Documentação

A documentação detalhada das automações encontra-se na pasta:

```text
docs/
```

Cada documento deve conter, quando aplicável:

- Objetivo
- Arquivos de entrada
- Arquivos de saída
- Dependências
- Forma de execução
- Limitações
- Observações relevantes
- Histórico de alterações

---

# Objetivo do Repositório

Este repositório tem como objetivo fornecer uma estrutura padronizada para automações relacionadas ao PI System, permitindo reaproveitamento de código, simplificação da manutenção e evolução contínua das ferramentas ao longo do tempo.