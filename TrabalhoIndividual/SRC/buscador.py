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

def get_model(model_file):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Loading model.")
    model = pd.read_csv(model_file, sep=";")
    model.set_index(["Token"], inplace=True)
    logging.info("Model loaded.")
    return model

def get_queries(queries_file):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Loading queries.")
    queries = pd.read_csv(queries_file, sep=";")
    queries.set_index(["QueryNumber"], inplace=True)
    for number, text in queries.itertuples():
        processed_text = gli.preproccess_text(text)
        queries.at[number, "QueryText"] = processed_text
    logging.info("Queries loaded.")
    return queries

def insert_queries(model, queries):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Inserting queries in model.")
    start_time = datetime.now()
    shape = (model.shape[0], 1)
    for qnumber, qtext in queries.itertuples():
        zeros = pd.DataFrame(np.zeros(shape), index=model.index, columns=[f"Q{qnumber}"])
        model = pd.concat([model, zeros], axis=1)
        for word in qtext:
            if not word in model.index:
                zeros = pd.DataFrame(np.zeros((1, len(model.columns))), index=[word], columns=model.columns)
                model = pd.concat([model, zeros], axis=0)
                shape = (model.shape[0], 1)
            model.at[word, f"Q{qnumber}"] += 1
    time_taken = datetime.now() - start_time
    logging.info(f"Queries inserted in model. Time taken: {time_taken}")
    return model

def get_ranking(model, queries):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Started getting rankings of each query by each document.")
    start_time = datetime.now()
    model = insert_queries(model, queries)
    ranking = pd.DataFrame()
    shape = (model.shape[1] - 99, 1)
    for query in queries.index:
        q = f"Q{query}"
        zeros = pd.DataFrame(np.zeros(shape), index=model.columns[:-99], columns=[q])
        ranking = pd.concat([ranking, zeros], axis=1)
        for document in model.columns[:-99]:
            result = sim_cos(q, document, model)
            ranking.loc[document, q] = result
    time_taken = datetime.now() - start_time
    logging.info(f"Rankings created. Time taken: {time_taken}")
    return ranking

def get_results(file, ranking):
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Generating the results file. CSV format file with 'QueryNumber; [position in ranking, doc_number, value of sim_cos]'.")
    with open(file, 'w') as results:
        results.write("QueryNumber;DocInfos\n")
        for query in ranking.columns:
            query_number = query.replace('Q', '')
            sorted_ranking = ranking[query].sort_values(ascending=False)
            position_ranking = 1
            for doc_number, cos in sorted_ranking.items():
                if cos == 0:
                    break
                doc_infos = [position_ranking, doc_number, cos]
                position_ranking += 1
                results.write(f"{query_number};{doc_infos}\n")
    logging.info("Results file created.")

def finish_execution():
    logging.basicConfig(filename='../RESULT/BUSCA.log', filemode='a',format='%(asctime)s - %(message)s', level=logging.INFO, force=True)
    logging.info("Module searcher finished execution.")