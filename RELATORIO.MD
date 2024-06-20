# Relatório do Trabalho de Avaliação do MEcanismo de Busca

## Construção de gráficos e obtenção dos dados

Todo o processo de criação dos gráficos, bem como a organização dos dados que os formam, está documentado em um notebook do Jupyter localizado no diretório [SRC](TrabalhoIndividual/SRC), com o nome [`AvaliacaoModeloRI.ipynb`](TrabalhoIndividual/SRC/AvaliacaoModeloRI.ipynb). Nele, estão incluídas as gerações dos gráficos dos resultados do mecanismo de busca utilizando o stemmer. Para os gráficos do mecanismo sem o uso do stemmer, foi utilizado o mesmo notebook, alterando apenas o arquivo de entrada no início.

Os arquivos CSV usados para gerar os gráficos estão armazenados no diretório [`AVALIA`](TrabalhoIndividual/SRC), assim como os próprios gráficos. O README do mecanismo foi atualizado para refletir a alteração implementada, permitindo a escolha de utilizar ou não o stemmer. Mais detalhes sobre a criação das métricas de avaliação podem ser encontrados dentro do próprio notebook.

## 1. Gráfico de 11 pontos de precisão e recall

* Stemmer

![11pontos-stemmer](TrabalhoIndividual/AVALIA/11pontos-stemmer-1.png)

* NoStemmer

![11pontos-nostemmer](TrabalhoIndividual/AVALIA/11pontos-nostemmer-1.png)

## 2. $F_1$ score

* Stemmer

![f1-stemmer](TrabalhoIndividual/AVALIA/f1-stemmer-3.png)

* NoStemmer

![f1-nostemer](TrabalhoIndividual/AVALIA/f1-nostemmer-3.png)

## 3. Precision@5

* Stemmer

![precision@5-stemmer](TrabalhoIndividual/AVALIA/precision@5-stemmer-5.png)

* NoStemmer

![precision@5-nostemmer](TrabalhoIndividual/AVALIA/precision@5-nostemmer-5.png)

## 4. Precision@10

* Stemmer

![precision@10-stemmer](TrabalhoIndividual/AVALIA/precision@10-stemmer-7.png)

* NoStemmer

![precision@10-nostemmer](TrabalhoIndividual/AVALIA/precision@10-nostemmer-7.png)

## 5. Histograma Comparativo de R-Precision

![r-precision](TrabalhoIndividual/AVALIA/r-precision-comparativo-9.png)

## 6. MAP

* Stemmer

![map-stemmer](TrabalhoIndividual/AVALIA/map-stemmer-10.png)

* NoStemmer

![map-nostemmer](TrabalhoIndividual/AVALIA/map-nostemmer-10.png)

## 7. MRR

* Stemmer

![mrr-stemmer](TrabalhoIndividual/AVALIA/mrr-stemmer-12.png)

* NoStemmer

![mrr-nostemmer](TrabalhoIndividual/AVALIA/mrr-nostemmer-12.png)

## 8. Discounted Cumulative Gain

* Stemmer

![dcg-stemmer](TrabalhoIndividual/AVALIA/dcg-stemmer-14.png)

* NoStemmer

![dcg-nostemmer](TrabalhoIndividual/AVALIA/dcg-nostemmer-14.png)

## 9. Normalized Discounted Cumulative Gain

* Stemmer

![ndcg-stemmer](TrabalhoIndividual/AVALIA/ndcg-stemmer-16.png)

* NoStemmer

![ndcg-nostemmer](TrabalhoIndividual/AVALIA/ndcg-nostemmer-16.png)