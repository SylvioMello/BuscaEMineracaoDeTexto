# Relatório do Trabalho de Avaliação do MEcanismo de Busca

## Construção de gráficos e obtenção dos dados

Todo o processo de criação dos gráficos, bem como a organização dos dados que os formam, está documentado em um notebook do Jupyter localizado no diretório [SRC](TrabalhoIndividual/SRC), com o nome [`AvaliacaoModeloRI.ipynb`](TrabalhoIndividual/SRC/AvaliacaoModeloRI.ipynb). Nele, estão incluídas as gerações dos gráficos dos resultados do mecanismo de busca utilizando o stemmer. Para os gráficos do mecanismo sem o uso do stemmer, foi utilizado o mesmo notebook, alterando apenas o arquivo de entrada no início.

Os arquivos CSV usados para gerar os gráficos estão armazenados no diretório [`AVALIA`](TrabalhoIndividual/SRC), assim como os próprios gráficos. O README do mecanismo foi atualizado para refletir a alteração implementada, permitindo a escolha de utilizar ou não o stemmer. Mais detalhes sobre a criação das métricas de avaliação podem ser encontrados dentro do próprio notebook.

## 1. Gráfico de 11 pontos de precisão e recall

* Stemmer

![11pontos-stemmer](AVALIA/11pontos-stemmer-1.png)

* NoStemmer

![11pontos-nostemmer](AVALIA/11pontos-nostemmer-2.png)

## 2. $F_1$ score

* Stemmer

![f1-stemmer](AVALIA/f1-stemmer-3.png)

* NoStemmer

![f1-nostemer](AVALIA/f1-nostemmer-4.png)

## 3. Precision@5

* Stemmer

![precision@5-stemmer](AVALIA/precision@5-stemmer-5.png)

* NoStemmer

![precision@5-nostemmer](AVALIA/precision@5-nostemmer-6.png)

## 4. Precision@10

* Stemmer

![precision@10-stemmer](AVALIA/precision@10-stemmer-7.png)

* NoStemmer

![precision@10-nostemmer](AVALIA/precision@10-nostemmer-8.png)

## 5. Histograma Comparativo de R-Precision

![r-precision](AVALIA/r-precision-comparativo-9.png)

## 6. MAP

* Stemmer

![map-stemmer](AVALIA/map-stemmer-10.png)

* NoStemmer

![map-nostemmer](AVALIA/map-nostemmer-11.png)

## 7. MRR

* Stemmer

![mrr-stemmer](AVALIA/mrr-stemmer-12.png)

* NoStemmer

![mrr-nostemmer](AVALIA/mrr-nostemmer-13.png)

## 8. Discounted Cumulative Gain

* Stemmer

![dcg-stemmer](AVALIA/dcg-stemmer-14.png)

* NoStemmer

![dcg-nostemmer](AVALIA/dcg-nostemmer-15.png)

## 9. Normalized Discounted Cumulative Gain

* Stemmer

![ndcg-stemmer](AVALIA/ndcg-stemmer-16.png)

* NoStemmer

![ndcg-nostemmer](AVALIA/ndcg-nostemmer-17.png)