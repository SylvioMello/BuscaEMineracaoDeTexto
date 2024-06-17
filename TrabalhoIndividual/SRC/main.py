import buscador
import indexador
import processador as pc
from utils import read_config
import geradorListaInvertida as gli

# PROCESSADOR DE CONSULTAS
pc.begin_execution()
read, queries, expected = read_config("PC.CFG")
xml_root = pc.gerar_raiz_xml(read)
pc.gerar_arquivo_consultas(queries, xml_root)
pc.gerar_arquivo_esperado(expected, xml_root)
pc.finish_execution()

# GERADOR LISTA INVERTIDA
gli.begin_execution()
read_files, write_file, stemmer = read_config("GLI.CFG")
gli.gerar_arquivo_tokens(read_files, write_file, stemmer)
gli.finish_execution()

# INDEXADOR
indexador.begin_execution()
normalized = input("tf normalized [ y / n ]? ")
if normalized.lower() == "y":
    type_tf = "tfn"
else:
    type_tf = "tf"
tokens, model = read_config("INDEX.CFG")
indexador.salvar_modelo(model, tokens, type_tf)
indexador.finish_execution()

# BUSCADOR
buscador.begin_execution()
model_file, queries_file, results_file, stemmer = read_config("BUSCA.CFG")
model = buscador.carregar_modelo(model_file)
queries = buscador.carregar_queries(queries_file, stemmer)
ranking = buscador.criar_ranking(model, queries)
buscador.gerar_resultados(results_file, ranking)
buscador.finish_execution()