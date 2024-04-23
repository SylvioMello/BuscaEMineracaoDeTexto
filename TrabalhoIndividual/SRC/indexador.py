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

def get_term_document_matrix(tokens_file):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started generating the term document matrix.")
    start_time = datetime.now()
    number_tokens = 0
    path = "../RESULT/" + tokens_file
    inverted_list = pd.read_csv(path, sep=';', converters={"Appearance": pd.eval})
    matrix = pd.DataFrame(inverted_list["Token"])
    matrix.set_index(["Token"], inplace=True)
    shape = (matrix.shape[0], 1)
    for token, docs in inverted_list.itertuples(index=False):
        number_tokens += 1
        for doc in docs:
            if str(doc) in matrix.columns:
                matrix.at[token, str(doc)] += 1
            else:
                zeros = pd.DataFrame(np.zeros(shape), index=inverted_list["Token"], columns=[str(doc)])
                matrix = pd.concat([matrix, zeros], axis=1)
                matrix.at[token, str(doc)] = 1
    time_taken = datetime.now() - start_time
    logging.info(f"Finished generating the term document matrix. Time taken: {time_taken}.")
    logging.info(f"Matrix has {len(matrix.index)} tokens and {len(matrix.columns)} documents.")
    return matrix

def get_model(matrix, type_tf="tf"):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    msg = "Started generating the model with tf"
    if type_tf == "tf":
        msg += "."
    else:
        msg += " normalized."
    msg += " The time which the model will be constructed will depend upon the iterations per second, at 5it/s it takes around 20min to build the model"
    logging.info(msg)
    start_time = datetime.now()
    weights = matrix.copy()
    for token in tqdm(weights.index):
        idf = get_idf(token, weights)
        for document in weights.columns:
            tf = get_tfn(token, document, matrix) if type_tf == "tfn" else get_tfn(token, document, matrix) 
            wij = tf * idf
            weights.loc[token, str(document)] = wij
    time_taken = datetime.now() - start_time
    logging.info(f"Finished generating the model. Time taken: {time_taken}.")
    return weights

def save_matrix(save_path, tokens_file):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    matrix = get_term_document_matrix(tokens_file)
    matrix.to_csv(save_path, sep=";")
    logging.info("Term document matrix saved.")
    return matrix

def save_model(path, tokens_file, type_tf):
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    matrix = save_matrix("../RESULT/MATRIZ.csv", tokens_file)
    model = get_model(matrix, type_tf)
    model.to_csv(path, sep=";")
    logging.info("Model saved.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/INDEX.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module indexer finished execution.")