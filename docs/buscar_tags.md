# buscar_tags.py

## Objetivo

Localizar e exportar para CSV todas as tags associadas aos equipamentos informados pelo usuário.

---

## Arquivos Utilizados

### Entrada

```text
templates/equipamentos.txt
```

### Saída

```text
resultado_tags.csv
```

---

## Formato do Arquivo de Entrada

Adicionar um equipamento por linha.

Exemplo:

```text
AREA_EQ0001
AREA_EQ0002
AREA_EQ0003
```

---

## Execução

Executar o script:

```bash
python scripts/buscar_tags.py
```

---

## Funcionamento

O script:

1. Carrega a configuração local.
2. Conecta ao servidor PI configurado.
3. Lê os equipamentos informados no arquivo de entrada.
4. Pesquisa as tags associadas a cada equipamento.
5. Exporta os resultados para um arquivo CSV.

---

## Estrutura da Saída

Exemplo:

```csv
Equipamento;Tag
AREA_EQ0001;AREA_EQ0001_TAG001
AREA_EQ0001;AREA_EQ0001_TAG002
AREA_EQ0002;AREA_EQ0002_TAG001
```

---

## Dependências

Antes da execução:

- Configuração inicial concluída.
- Arquivo `config/config.json` disponível.
- Acesso ao ambiente PI.
- AF SDK instalado.

---

## Limitações

- O script depende da conectividade com o ambiente PI.
- O retorno está limitado às permissões do usuário executando o script.
- Equipamentos sem tags associadas serão retornados com quantidade igual a zero durante a execução.

---

## Segurança

O script:

- Não armazena credenciais.
- Não modifica informações no ambiente PI.
- Realiza apenas consultas de leitura.

---

## Histórico

| Versão | Descrição |
|---------|---------|
| 1.0 | Implementação inicial de busca de tags por equipamento. |
`