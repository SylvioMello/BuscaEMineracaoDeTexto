import nltk
import logging
import numpy as np
from datetime import datetime
from nltk.corpus import stopwords
from xml.etree import ElementTree as ET
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import wordpunct_tokenize

# Configuramos o arquivo que será o log do módulo e baixamos dependências do nltk
logging.basicConfig(filename='../RESULT/GLI.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
logging.info("Initializing log...")
logging.info("Downloading 'punkt' and 'stopwords' from nltk-data...")
nltk.download('punkt')
nltk.download('stopwords')
logging.info("Finished downloading 'punkt' and 'stopwords'.")

def begin_execution():
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module of Inverted List Generated started.")

def gerar_texto_recordnum(arquivo):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the dictionary record_num: {arquivo}")
    start_time = datetime.now()
    arquivo_xml = ET.parse(arquivo)
    raiz_xml = arquivo_xml.getroot()
    texto_recordnum = {}
    registros = 0
    for registro in raiz_xml:
        registros += 1
        text = ""
        for elemento in registro:
            if elemento.tag == "RECORDNUM":
                numero_registro = int(elemento.text)
            elif elemento.tag == "ABSTRACT" or elemento.tag == "EXTRACT":
                text = elemento.text.upper()
        texto_recordnum[numero_registro] = text
    time_taken = datetime.now() - start_time
    logging.info(f"Finished creating the dictionary record_num: {arquivo}. {registros} records in file. Time taken: {time_taken}s")
    return texto_recordnum

def preprocessar_texto(text, stemmer):
    tokens = wordpunct_tokenize(text)
    stop_en = stopwords.words("english")
    texto_filtrado = []
    for palavra in tokens:
        if palavra.lower() in stop_en:
            continue
        elif not palavra.isalpha():
            continue
        elif len(palavra) < 3:
            continue    
        # Inserção da palavra aplicando o stemmer ou não
        if stemmer:
            stemmer = PorterStemmer()
            word_stemmed = stemmer.stem(palavra)
            texto_filtrado.append(word_stemmed.upper())
        else:
            texto_filtrado.append(palavra.upper())
    return texto_filtrado

def frequencia_palavra(text, numero_registro, stemmer):
    texto_tokenizado = preprocessar_texto(text, stemmer)
    dicionario_frequencia = {}
    for palavra in texto_tokenizado:
        keys = list(dicionario_frequencia.keys())
        if palavra in keys:
            dicionario_frequencia[palavra].append(numero_registro)
        else:
            dicionario_frequencia[palavra] = [numero_registro]
    return dicionario_frequencia

def gerar_lista_invertida(arquivos_leitura, stemmer):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the inverted list.")
    times = np.array([])
    arquivos = 0
    lista_invertida = {}
    for arquivo in arquivos_leitura:
        start_time = datetime.now()
        arquivos += 1 
        registros_arquivos = gerar_texto_recordnum(arquivo)
        registros_arquivos_nums = list(registros_arquivos.keys())
        for numero_registro in registros_arquivos_nums:
            record_dict = frequencia_palavra(registros_arquivos[numero_registro], numero_registro, stemmer)
            used_tokens = list(record_dict.keys())
            for token in used_tokens:
                previous_records = lista_invertida.get(token, [])
                if previous_records == []:
                    lista_invertida[token] = record_dict[token]
                else:
                    lista_invertida[token] += record_dict[token]
        time_taken = datetime.now() - start_time
        times = np.append(times, [time_taken])
    mean = np.mean(times)
    logging.info(f"{arquivos} files procesed. Average time: {mean}s.")
    logging.info(f"Finished creating the inverted list.")
    return lista_invertida

def gerar_arquivo_tokens(arquivos_leitura, path, stemmer):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the inverted list file.")
    with open(path, 'w') as w_file:
        lista_invertida = gerar_lista_invertida(arquivos_leitura, stemmer)
        tokens = list(lista_invertida.keys())
        w_file.write("Token;Appearance\n")
        for token in tokens:
            w_file.write(f"{token};{lista_invertida[token]}\n")
    logging.info(f"Finished creating the inverted list file.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module generate_inverted_list finished execution.")