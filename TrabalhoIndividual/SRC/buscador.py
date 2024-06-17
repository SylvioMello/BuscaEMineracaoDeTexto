import logging
import numpy as np
import pandas as pd
from utils import sim_cos
from datetime import datetime
import geradorListaInvertida as gli

# Configuramos o arquivo que será o log do módulo
logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
logging.info("Initializing log...")

def begin_execution():
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module of Searceher started.")

def carregar_modelo(arquivo_modelo):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Loading model.")
    modelo = pd.read_csv(arquivo_modelo, sep=";")
    modelo.set_index(["Token"], inplace=True)
    logging.info("Model loaded.")
    return modelo

def carregar_queries(arquivo_consultas, stemmer):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Loading queries.")
    consultas = pd.read_csv(arquivo_consultas, sep=";")
    consultas.set_index(["QueryNumber"], inplace=True)
    for numero, texto in consultas.itertuples():
        texto_processado = gli.preprocessar_texto(texto, stemmer)
        consultas.at[numero, "QueryText"] = texto_processado
    logging.info("Queries loaded.")
    return consultas

def inserir_queries(modelo, consultas):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Inserting queries in model.")
    start_time = datetime.now()
    shape = (modelo.shape[0], 1)
    for qnumber, qtext in consultas.itertuples():
        zeros = pd.DataFrame(np.zeros(shape), index=modelo.index, columns=[f"Q{qnumber}"])
        modelo = pd.concat([modelo, zeros], axis=1)
        for palavra in qtext:
            if not palavra in modelo.index:
                zeros = pd.DataFrame(np.zeros((1, len(modelo.columns))), index=[palavra], columns=modelo.columns)
                modelo = pd.concat([modelo, zeros], axis=0)
                shape = (modelo.shape[0], 1)
            modelo.at[palavra, f"Q{qnumber}"] += 1
    time_taken = datetime.now() - start_time
    logging.info(f"Queries inserted in model. Time taken: {time_taken}")
    return modelo

def criar_ranking(modelo, consultas):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started getting rankings of each query by each document.")
    start_time = datetime.now()
    modelo = inserir_queries(modelo, consultas)
    ranking = pd.DataFrame()
    shape = (modelo.shape[1] - 99, 1)
    for consulta in consultas.index:
        q = f"Q{consulta}"
        zeros = pd.DataFrame(np.zeros(shape), index=modelo.columns[:-99], columns=[q])
        ranking = pd.concat([ranking, zeros], axis=1)
        for documento in modelo.columns[:-99]:
            result = sim_cos(q, documento, modelo)
            ranking.loc[documento, q] = result
    time_taken = datetime.now() - start_time
    logging.info(f"Rankings created. Time taken: {time_taken}")
    return ranking

def gerar_resultados(file, ranking):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Generating the results file. CSV format file with 'QueryNumber; [position in ranking, doc_number, value of sim_cos]'.")
    with open(file, 'w') as results:
        results.write("QueryNumber;DocInfos\n")
        for consulta in ranking.columns:
            numero_consulta = consulta.replace('Q', '')
            ranking_ordenado = ranking[consulta].sort_values(ascending=False)
            posicao = 1
            for documento, cos in ranking_ordenado.items():
                if cos == 0:
                    break
                doc_infos = [posicao, documento, cos]
                posicao += 1
                results.write(f"{numero_consulta};{doc_infos}\n")
    logging.info("Results file created.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module searcher finished execution.")