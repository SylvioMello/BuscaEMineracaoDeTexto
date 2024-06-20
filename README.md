# BuscaEMineracaoDeTexto
Repositório da Aula de BMT (Busca e Mineração de Texto) - 2024.1 - UFRJ

# Trabalho Individual - Implementação de Um Sistema de Recuperação Em Memória Segundo o Modelo Vetorial

## Execução

Existem duas opções para executar o sistema de recuperação, a primeira delas é utilizar o anaconda, se ele estiver instalado em seu computador, basta criar um novo environment e, a partir dele, executar o arquivo main.py

```shell
conda create --name <environment_name>
```

Outro ponto importante é estar no diretório SRC, se não estiver a partir dele, o script pode não encontrar os arquivos de configuração e logs necessários.

```shell
cd TrabalhoIndividual/SRC
```

```shell
python3 main.py
```

Outra alternativa é, usando um python recente (3.12+), instalar os pacotes a partir do arquivo requirements.txt na raiz do projeto

```shell
pip install -r requirements.txt
```
```shell
python3 main.py
```

## AVALIAÇÃO DE UM MODELO DE RECUPERAÇÃO DA INFORMAÇÃO - Trabalho 2

Neste segundo trabalho, é solicitado que o modelo seja avaliado utilizando diferentes métricas. Antes de abordarmos essas métricas, algumas mudanças importantes foram feitas no funcionamento do mecanismo. Ambas as mudanças ocorrem dentro do arquivo de configuração de dois módulos.

A primeira mudança está no arquivo de configuração do módulo "Gerar Lista Invertida" [`GLI.CFG`](TrabalhoIndividual/BasesTrabalhoIndividual/GLI.CFG). Na primeira linha, será indicada a utilização ou não de um stemmer. As opções para essa linha são "STEMMER" ou "NOSTEMMER".

A segunda mudança ocorre no arquivo de configuração do módulo "Buscador" [`BUSCA.CFG`](TrabalhoIndividual/BasesTrabalhoIndividual/BUSCA.CFG). Aqui, será indicado se o texto das consultas passará por um stemmer ou não. Isso será feito adicionando "-stemmer" ao nome do arquivo de resultados, caso afirmativo, ou "-nostemmer", caso negativo.