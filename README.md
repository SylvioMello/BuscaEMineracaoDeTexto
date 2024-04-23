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