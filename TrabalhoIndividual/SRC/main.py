import processador as pc
import geradorListaInvertida as gli
import indexador
import buscador

# Início da execução do módulo 'processando consultas'
pc.start_exec()
read, queries, expected = pc.read_config("PC.CFG")
# Lendo arquivo com consultas
xml_root = pc.get_xml_root(read)
# Escrevendo arquivos com consultas e resultados esperados, respectivamente
pc.get_queries_file(queries, xml_root)
pc.get_expected_file(expected, xml_root)
# Fim da execução do módulo
pc.finish_exec()


# Início da execução do módulo 'gerador lista invertida'
gli.start_exec()
read_files, write_file = gli.read_config_file("GLI.CFG")
# Gerando arquivo da lista invertida
gli.get_tokens_file(read_files, write_file)
# Fim da execução do módulo
gli.finish_exec()


# Início da execução do módulo 'indexador'
indexador.start_exec()
# Escolha do usuário entre usar o tf normalizado ou não
normalized = input("tf normalized [ y / n ]? ")
if normalized.lower() == "y":
    type_tf = "tfn"
else:
    type_tf = "tf"
tokens, model = indexador.read_config_file("INDEX.CFG")
# Gerando modelo através da matriz termo documento que foi construída com a lista invertida
indexador.save_model(model, tokens, type_tf)
# Fim da execução do módulo
indexador.finish_exec()


# Início da execução do módulo 'buscador'
buscador.start_exec()
model_file, queries_file, results_file = buscador.read_config_file("BUSCA.CFG")
# Lê o modelo na memória
model = buscador.get_model(model_file)
# Lê as consultas na memória
queries = buscador.get_queries(queries_file)
# Usa as consultas e o modelo para gerar o ranking de documentos que mais se aproximam das consultas
ranking = buscador.get_ranking(model, queries)
# Gera o arquivo de resultados com o arquivo de ranking gerado
buscador.get_results(results_file, ranking)
# Fim da execução do módulo
buscador.finish_exec()
