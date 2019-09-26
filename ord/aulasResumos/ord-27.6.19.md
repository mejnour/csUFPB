# ORD 27/06/2019

O arquivo provido no SIGAA continha os nodos de um grafo em formato triangular ou piramidal. Como assim é uma matriz (e uma matriz é quadrada)?

A seguinte tabela foi escrita no quadro sobre o arquivo `dij10.txt`.

|      |  1   |  2   |  3   |  4   |
| ---: | :--: | :--: | :--: | :--: |
|    1 |  0   |  7   |  2   |  4   |
|    2 |  7   |  0   |  5   |  1   |
|    3 |  2   |  5   |  0   |  6   |
|    4 |  4   |  1   |  6   |  0   |

## O Problema do Caminho Mínimo

Dado um grafo como input, determine o menor caminho entre dois vértices.

- Caminho: sequência de vértices
- Peso do Caminho: o somatório dos pesos de suas arestas constituintes.

### Algoritmos

- Relaxação (Relaxamento?)

  O algoritmo de Relaxação de vértices funciona "perguntando" a cada novo vértice se existe caminho melhor do que o que já se segue. Em caso afirmativo, adota-se o novo caminho. Do contrário, não.

- Dijkstra

  1. Primeiro vértice recebe 0
  2. Demais vértices recebem $\infty$
  3. O algoritmo de Dijkstra visita todos os vértices do vetor `d` relaxando arestas e atualizando qual o melhor caminho.
  4. Usando o vator $\pi$ e uma pilha, é  possível descrever o caminho através de backtracking.

  Efeitos colaterais:

  - Falou rápido demais

  Para o Algoritmo de Dijkstra seja eficiente, é necessário:

  - Fila de Prioridade Mínima (minHEAPIFY?)
  - Build
  - RELAX = Decrease 