import buscador
import indexador
import processador as pc
from utils import read_config
import geradorListaInvertida as gli

# PROCESSADOR DE CONSULTAS
pc.begin_execution()
read, queries, expected = read_config("PC.CFG")
xml_root = pc.get_xml_root(read)
pc.get_queries_file(queries, xml_root)
pc.get_expected_file(expected, xml_root)
pc.finish_execution()

# GERADOR LISTA INVERTIDA
gli.begin_execution()
read_files, write_file = read_config("GLI.CFG")
gli.get_tokens_file(read_files, write_file)
gli.finish_execution()

# INDEXADOR
indexador.begin_execution()
normalized = input("tf normalized [ y / n ]? ")
if normalized.lower() == "y":
    type_tf = "tfn"
else:
    type_tf = "tf"
tokens, model = read_config("INDEX.CFG")
indexador.save_model(model, tokens, type_tf)
indexador.finish_execution()

# BUSCADOR
buscador.begin_execution()
model_file, queries_file, results_file = read_config("BUSCA.CFG")
model = buscador.get_model(model_file)
queries = buscador.get_queries(queries_file)
ranking = buscador.get_ranking(model, queries)
buscador.get_results(results_file, ranking)
buscador.finish_execution()