import logging
import numpy as np
from datetime import datetime
from xml.etree import ElementTree as ET

# Configuramos o arquivo que será o log do módulo
logging.basicConfig(filename='../RESULT/PC.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
logging.info("Initializing log...")

def begin_execution():
    logging.basicConfig(filename='../RESULT/PC.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module of Query Processor Started.")

def gerar_raiz_xml(caminho):
    logging.basicConfig(filename='../RESULT/PC.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started parsing the xml file.")
    arquivo_xml = ET.parse(caminho)
    raiz_xml = arquivo_xml.getroot()
    logging.info("XML file parsed.")
    return raiz_xml

def gerar_arquivo_consultas(caminho, raiz_xml):
    logging.basicConfig(filename='../RESULT/PC.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Starting the generation of queries csv file.")
    with open(caminho, 'w') as consultas:
        consultas.write("QueryNumber;QueryText\n")
        consultas_lidas = 0
        times = np.array([])
        for consultas_xml in raiz_xml:
            start_time = datetime.now()
            consultas_lidas += 1
            consulta_numero = ""
            consulta_texto = ""
            for elemento in consultas_xml:
                if elemento.tag == "QueryNumber":
                    consulta_numero = int(elemento.text)
                elif elemento.tag == "QueryText":
                    consulta_texto = elemento.text.upper()
                    consulta_texto = consulta_texto.replace('\n  ', '')
                    consulta_texto = consulta_texto.replace(';', '')

            consultas.write(f"{consulta_numero};{consulta_texto}")
            time_taken = datetime.now() - start_time
            times = np.append(times, [time_taken])
    mean = np.mean(times) 
    logging.info(f"{consultas_lidas} queries processed.")
    logging.info(f"Mean time each queriy has taken to be processed in queries file: {mean}s")
    logging.info("Queries csv file generated.")

def gerar_arquivo_esperado(caminho, raiz_xml):
    logging.basicConfig(filename='../RESULT/PC.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Starting the generation of expected csv file.")
    with open(caminho, 'w') as esperado:
        esperado.write("QueryNumber;DocNumber;DocVotes\n")
        times = np.array([])
        for consultas in raiz_xml:
            start_time = datetime.now()
            consulta_numero = ""
            for elemento in consultas:
                if elemento.tag == "QueryNumber":
                    consulta_numero = int(elemento.text)
                elif elemento.tag == "Records":
                    for item in elemento:
                        documento_numero = int(item.text)
                        score = item.attrib['score'].replace('0', '')
                        documento_votos = len(score)
                        esperado.write(f"{consulta_numero};{documento_numero};{documento_votos}\n")
            time_taken = datetime.now() - start_time
            times = np.append(times, [time_taken])
    mean = np.mean(times)
    logging.info(f"Mean time each query has taken to be processed in expected file: {mean}s")
    logging.info("Expected csv file generated.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/PC.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module of Query Processor Finished.")