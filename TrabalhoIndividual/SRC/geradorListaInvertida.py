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

def get_recordnum_text(file):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the dictionary record_num: {file}")
    start_time = datetime.now()
    xml_file = ET.parse(file)
    xml_root = xml_file.getroot()
    recordnum_text = {}
    total_records = 0
    for record in xml_root:
        total_records += 1
        text = ""
        for element in record:
            if element.tag == "RECORDNUM":
                record_num = int(element.text)
            elif element.tag == "ABSTRACT" or element.tag == "EXTRACT":
                text = element.text.upper()
        recordnum_text[record_num] = text
    time_taken = datetime.now() - start_time
    logging.info(f"Finished creating the dictionary record_num: {file}. {total_records} records in file. Time taken: {time_taken}s")
    return recordnum_text

def preproccess_text(text):
    tokens = wordpunct_tokenize(text)
    stop_en = stopwords.words("english")
    filtered_text = []
    for word in tokens:
        if word.lower() in stop_en:
            continue
        elif not word.isalpha():
            continue
        elif len(word) < 3:
            continue    
        else:
            stemmer = PorterStemmer()
            word_stemmed = stemmer.stem(word)
            filtered_text.append(word_stemmed.upper())
    return filtered_text

def word_frequency(text, record_num):
    tokenized_text = preproccess_text(text)
    frequency_dict = {}
    for word in tokenized_text:
        keys = list(frequency_dict.keys())
        if word in keys:
            frequency_dict[word].append(record_num)
        else:
            frequency_dict[word] = [record_num]
    return frequency_dict

def get_inverted_list(read_files):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the inverted list.")
    times = np.array([])
    total_files = 0
    inverted_list = {}
    for file in read_files:
        start_time = datetime.now()
        total_files += 1 
        file_records = get_recordnum_text(file)
        file_record_nums = list(file_records.keys())
        for record_num in file_record_nums:
            record_dict = word_frequency(file_records[record_num], record_num)
            used_tokens = list(record_dict.keys())
            for token in used_tokens:
                previous_records = inverted_list.get(token, [])
                if previous_records == []:
                    inverted_list[token] = record_dict[token]
                else:
                    inverted_list[token] += record_dict[token]
        time_taken = datetime.now() - start_time
        times = np.append(times, [time_taken])
    mean = np.mean(times)
    logging.info(f"{total_files} files procesed. Average time: {mean}s.")
    logging.info(f"Finished creating the inverted list.")
    return inverted_list

def get_tokens_file(read_files, path):
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info(f"Started creating the inverted list file.")
    with open(path, 'w') as w_file:
        inverted_list = get_inverted_list(read_files)
        tokens = list(inverted_list.keys())
        w_file.write("Token;Appearance\n")
        for token in tokens:
            w_file.write(f"{token};{inverted_list[token]}\n")
    logging.info(f"Finished creating the inverted list file.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/GLI.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module generate_inverted_list finished execution.")