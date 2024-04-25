import logging
import numpy as np
import pandas as pd
from tqdm import tqdm
from datetime import datetime
from utils import get_idf,get_tfn

# Configuramos o arquivo que será o log do módulo
logging.basicConfig(filename='../RESULT/INDEX.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
logging.info("Initializing log...")

def begin_execution():
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module Of Indexer started.")

def gerar_matriz_termos_documentos(tokens_file):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started generating the term document matrix.")
    start_time = datetime.now()
    numero_de_tokens = 0
    caminho = "../RESULT/" + tokens_file
    lista_invertida = pd.read_csv(caminho, sep=';', converters={"Appearance": pd.eval})
    matriz = pd.DataFrame(lista_invertida["Token"])
    matriz.set_index(["Token"], inplace=True)
    shape = (matriz.shape[0], 1)
    for token, documentos in lista_invertida.itertuples(index=False):
        numero_de_tokens += 1
        for documento in documentos:
            if str(documento) in matriz.columns:
                matriz.at[token, str(documento)] += 1
            else:
                zeros = pd.DataFrame(np.zeros(shape), index=lista_invertida["Token"], columns=[str(documento)])
                matriz = pd.concat([matriz, zeros], axis=1)
                matriz.at[token, str(documento)] = 1
    time_taken = datetime.now() - start_time
    logging.info(f"Finished generating the term document matrix. Time taken: {time_taken}.")
    logging.info(f"Matrix has {len(matriz.index)} tokens and {len(matriz.columns)} documents.")
    return matriz

def carregar_modelo(matriz, tipo_tf="tf"):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    msg = "Started generating the model with tf"
    if tipo_tf == "tf":
        msg += "."
    else:
        msg += " normalized."
    msg += " The time which the model will be constructed will depend upon the iterations per second, at 5it/s it takes around 20min to build the model"
    logging.info(msg)
    start_time = datetime.now()
    pesos = matriz.copy()
    for token in tqdm(pesos.index):
        idf = get_idf(token, pesos)
        for documento in pesos.columns:
            tf = get_tfn(token, documento, matriz) if tipo_tf == "tfn" else get_tfn(token, documento, matriz) 
            wij = tf * idf
            pesos.loc[token, str(documento)] = wij
    time_taken = datetime.now() - start_time
    logging.info(f"Finished generating the model. Time taken: {time_taken}.")
    return pesos

def salvar_matriz(save_path, tokens_file):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    matriz = gerar_matriz_termos_documentos(tokens_file)
    matriz.to_csv(save_path, sep=";")
    logging.info("Term document matrix saved.")
    return matriz

def salvar_modelo(caminho, tokens_file, tipo_tf):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    matriz = salvar_matriz("../RESULT/MATRIZ.csv", tokens_file)
    model = carregar_modelo(matriz, tipo_tf)
    model.to_csv(caminho, sep=";")
    logging.info("Model saved.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module indexer finished execution.")