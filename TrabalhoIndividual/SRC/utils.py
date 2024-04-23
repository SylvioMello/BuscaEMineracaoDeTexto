import os
import sys
import logging

def read_config(config_file):
    """"Based on the module, reads the configuration file and returns the necessary paths"""
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