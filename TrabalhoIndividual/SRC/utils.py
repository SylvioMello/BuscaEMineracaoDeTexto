import os
import sys
import logging
import numpy as np
from math import log10

def read_config(config_file):
    module = config_file.split('.')[0]
    logging.basicConfig(filename=f'../RESULT/{module}.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started reading the configuration file.")
    read_file = "../BasesTrabalhoIndividual/"
    read_files = []
    read_file_index = "../RESULT/"
    model_file = "../RESULT/"
    write_file = "../RESULT/"
    queries_file = "../RESULT/"
    expected_file = "../RESULT/"
    results_file = "../RESULT/"
    cfg_path = "../BasesTrabalhoIndividual/" + config_file

    if module == 'PC':
        with open(cfg_path, "r") as config_file:
            for line in config_file.readlines():
                instruction, filename = line.split("=")
                filename = filename.strip()
                if instruction == "LEIA":
                    read_file += filename
                elif instruction == "CONSULTAS":
                    queries_file += filename
                elif instruction == "ESPERADOS":
                    expected_file += filename
            logging.info("Finished reading the configuration file.")
            return (read_file, queries_file, expected_file)
    elif module == 'GLI':
        with open(cfg_path, "r") as config_file:
            for line in config_file.readlines():
                instruction, filename = line.split("=")
                filename = filename.strip()
                if instruction == "LEIA":
                    file_path = os.path.join("../BasesTrabalhoIndividual", filename)
                    read_files.append(file_path)
                elif instruction == "ESCREVA":
                    write_file += filename
            logging.info("Finished reading the configuration file.")
            return (read_files, write_file)
    elif module == 'INDEX':
        with open(cfg_path, "r") as config_file:
            for line in config_file.readlines():
                instruction, filename = line.split("=")
                filename = filename.strip()
                if instruction == "LEIA":
                    read_file_index += filename
                elif instruction == "ESCREVA":
                    write_file += filename
            logging.info("Finished reading the configuration file.")
            return (read_file_index, write_file)
    elif module == 'BUSCA':
        with open(cfg_path, "r") as config_file:
            for line in config_file.readlines():
                instruction, filename = line.split("=")
                filename = filename.strip()
                if instruction == "MODELO":
                    model_file += filename
                elif instruction == "CONSULTAS":
                    queries_file += filename
                elif instruction == "RESULTADOS":
                    results_file += filename
            logging.info("Finished reading the configuration file.")
            return model_file, queries_file, results_file
    else:
        print('This module is not implemented to be used, please use one of: PC, GLI, INDEX, BUSCA')
        sys.exit(1)

def get_vector(document, model):
    return model[str(document)].to_numpy()  

def get_vector_size(vector):
    return np.linalg.norm(vector)

def sim_cos(query, document, model):
    q = get_vector(query, model)
    d = get_vector(document, model)
    q_dot_d = np.dot(q, d)
    qxd = get_vector_size(q) * get_vector_size(d)
    return q_dot_d / qxd

def get_n(matrix):
    N = len(matrix.columns)
    return N

def get_nj(token, matrix):
    row = matrix.loc[token]
    return row.astype(bool).sum()

def get_tf(token, document, matrix):
    return int(matrix.loc[token, str(document)])

def get_tfn(token, document, matrix):
    tf = get_tf(token, document, matrix)
    biggest_tf = int(matrix.loc[:, str(document)].max())
    return tf / biggest_tf

def get_idf(token, matrix):
    return log10(get_n(matrix) / get_nj(token, matrix))