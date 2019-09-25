# ORD - Algoritmos de Ordenação

## Counting Sort

Ideia básica:

- Determinar quantos elementos são menores que um <img src="/ord/sortingAlgos/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>;
- De acordo com essa quantidade, adicionar o elemento <img src="/ord/sortingAlgos/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> na posição quantidade + 1;
- É um algoritmo estável.

Manipulação do Algo:

- A[1 .. n] - arranjo desordenado;
- B[1 .. n] - arranjo ordenado;
- C[0 .. K] - arranjo auxiliar;
- K - valor máximo de A.

Algoritmo:

- Inicializa-se C no intervalo <img src="/ord/sortingAlgos/tex/31a48417b00785d49d162362e21106d0.svg?invert_in_darkmode&sanitize=true" align=middle width=39.79453994999999pt height=24.65753399999998pt/>, onde <img src="/ord/sortingAlgos/tex/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode&sanitize=true" align=middle width=15.13700594999999pt height=22.465723500000017pt/> é o valor máximo de A. Isto quer dizer que C terá <img src="/ord/sortingAlgos/tex/13ad028012a330194a33397c3b15ff72.svg?invert_in_darkmode&sanitize=true" align=middle width=43.44740069999999pt height=22.465723500000017pt/> posições:

  ```python
  for i in range(K + 1):
      C.append(0)
  ```

- Em cada posição A[i] de C, adicione <img src="/ord/sortingAlgos/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/>. Isto conta quantas ocorrências existem de cada elemento de A. Assim:

  ```python
  for i in range(len(A)):
      C[A[i]] += 1
  ```

- Some, cumulativamente, passo a passo, todos os elementos de C. Isto quer dizer que cada C[i] conterá o número de elementos iguais ou menores que aquela posição i. Assim:

  ```python
  for i in range(1, len(C)):
      C[i] += C[i - 1]
  ```

- Popule o arranjo B com as ocorrências de A na posição certa, C[A[i]], de B e decremente em <img src="/ord/sortingAlgos/tex/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=21.18721440000001pt/> a cada passo daquele valor C[A[i]]:

  ```python
  for i in range(len(A), -1, -1):
      B[C[A[i]]] = A[i]
      C[A[i]] -= 1
  ```

Complexidade:

- O primeiro laço é <img src="/ord/sortingAlgos/tex/ee3a2859dceb8b002ddf000a6279813a.svg?invert_in_darkmode&sanitize=true" align=middle width=40.91785829999999pt height=24.65753399999998pt/>.
- O segundo laço é <img src="/ord/sortingAlgos/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/>.
- Tempo total = <img src="/ord/sortingAlgos/tex/f71d1a30c10c85b50b7b6de970d1d9d5.svg?invert_in_darkmode&sanitize=true" align=middle width=70.87592489999999pt height=24.65753399999998pt/>. Embora a literatura use sempre o tempo maior, <img src="/ord/sortingAlgos/tex/1f08ccc9cd7309ba1e756c3d9345ad9f.svg?invert_in_darkmode&sanitize=true" align=middle width=35.64773519999999pt height=24.65753399999998pt/>, para descrever o Counting Sort, quando <img src="/ord/sortingAlgos/tex/d6328eaebbcd5c358f426dbea4bdbf70.svg?invert_in_darkmode&sanitize=true" align=middle width=15.13700594999999pt height=22.465723500000017pt/> é muito grande (quadrático, p.ex.), pode-se dizer que Counting Sort é um algoritmo *pseudo-linear*.

## Radix Sort

Ideia básica:

- Ordena pela posição dos algarismos em cada <img src="/ord/sortingAlgos/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> da entrada, ou seja, quebrando cada <img src="/ord/sortingAlgos/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> em colunas, ordena da direita para esquerda;
- É um algoritmo estável;

Manipulação:

- A[1 .. n] - arranjo desordenado;
- d - Número de dígitos do maior elemento do arranjo A. Quando iterado sobre, é o digito que está sendo trabalhado, sendo 1 o dígito menos significativo (mais a direita) e d o dígito mais significativo (o dígito mais a esquerda);

Algoritmo:

- Usa-se um tipo de ordenação para o arranjo A sobre um laço no intervalor <img src="/ord/sortingAlgos/tex/7dacc0c1b12adc4ee85a48883ccc8ef1.svg?invert_in_darkmode&sanitize=true" align=middle width=33.213503399999986pt height=24.65753399999998pt/>:

  ```python
  def RADIX_SORT(A, d):
      for i in range(1, d):
          COUNTING_SORT(A, i)
  ```

- Na prática é usado para ordernar registros chaveados por vários campos distintos.

Complexidade:

Se <img src="/ord/sortingAlgos/tex/3d2f4d6ce345404899df8a876198b240.svg?invert_in_darkmode&sanitize=true" align=middle width=46.734520799999984pt height=22.831056599999986pt/>, então Radix Sort tem tempo:
<p align="center"><img src="/ord/sortingAlgos/tex/aa6eb10cdc8fa0ae04706d373b080f9e.svg?invert_in_darkmode&sanitize=true" align=middle width=98.93927504999999pt height=16.438356pt/></p>

## Insertion Sort

Ideia básica:

Manipulação:

Algoritmo:

Complexidade:

## Selection Sort

Ideia básica:

Manipulação:

Algoritmo:

Complexidade:

## Merge Sort

Ideia básica:

Manipulação:

Algoritmo:

```python
def MERGE_SORT(A, l, r):
    if (l < r):
        q = floor((p + r) / 2)
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q + 1, r)
        MERGE(A, p, q, r)
```

Complexidade:

## Quick Sort

Ideia básica:

Manipulação:

Algoritmo:

```python
def QUICK_SORT(A, l, r):
    if (l < r):
        q = PARTITION(A, l, r)
        QUICK_SORT(A, l, q - 1)
        QUICK_SORT(A, q + 1, r)
```

Complexidade:

## Relações de Recorrência

### Divisão e Conquista

- Divide-se um problema em outros problemas menores para então combinar as respostas e conseguir a solução do problema original:
  - Divisão
  - Conquista
  - Combinação
- Resolve-se em geral recursivamente

Formato de Recorrência na divisão e conquista:
<p align="center"><img src="/ord/sortingAlgos/tex/bf9353c4e24d4af34259372032d1a341.svg?invert_in_darkmode&sanitize=true" align=middle width=165.78508649999998pt height=30.1801401pt/></p>
Em que:

- <img src="/ord/sortingAlgos/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> = número de subproblemas criados;
- <img src="/ord/sortingAlgos/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> = tamanho da entrada;
- <img src="/ord/sortingAlgos/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> = tamanho de cada problema em relação ao problema original;
- <img src="/ord/sortingAlgos/tex/3d425a215e8eeb2a056f553633aaae4a.svg?invert_in_darkmode&sanitize=true" align=middle width=32.46972299999999pt height=24.65753399999998pt/> = custo da solução de cada subproblema.

Exemplo de Divisão e Conquista:

- Busca Binária
- Merge Sort
- Quick Sort

#### Busca Binária

Na Busca Binária, as "entradas" são divididas pela metade a cada iteração. Uma lista de 8 itens vira uma de 4 itens, depois uma de 2 itens e, por fim, vira uma lista de 1 item que é a solução do problema. Assim, temos que:

- <img src="/ord/sortingAlgos/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> = 1 (subproblemas a cada iteração);
- <img src="/ord/sortingAlgos/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/> = <img src="/ord/sortingAlgos/tex/c5f8a19caa3a6028487eec738b02aeaa.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999996pt height=43.42856099999997pt/> (tamanho de cada subproblema);
- <img src="/ord/sortingAlgos/tex/3e2880c56369bb6f328d0504694b0a6f.svg?invert_in_darkmode&sanitize=true" align=middle width=61.501157849999984pt height=24.65753399999998pt/> (custo <img src="/ord/sortingAlgos/tex/3e18a4a28fdee1744e5e3f79d13b9ff6.svg?invert_in_darkmode&sanitize=true" align=middle width=7.11380504999999pt height=14.15524440000002pt/> constante).

Montando a relação de recorrência:
<p align="center"><img src="/ord/sortingAlgos/tex/753aa54e31746337459b848876bf38e0.svg?invert_in_darkmode&sanitize=true" align=middle width=217.8625548pt height=51.583387349999995pt/></p>

#### Merge Sort

No Merge Sort, as entradas são divididas ao meio em duas soluções. Cada solução desta, por sua vez, é dividida novamente pela metade. Assim, uma lista de 8 itens viram duas listas de 4 itens cada, depois viram quatro listas de 2 itens cada e, por fim, viram oito listas de 1 item cada. Temos daí que:

- <img src="/ord/sortingAlgos/tex/cf34371d316f136e859347be44d26b44.svg?invert_in_darkmode&sanitize=true" align=middle width=38.82599489999999pt height=21.18721440000001pt/> (subproblemas a cada iteração);
- <img src="/ord/sortingAlgos/tex/94166fc8cb17bbd567a69c48396e9398.svg?invert_in_darkmode&sanitize=true" align=middle width=39.16423499999999pt height=43.42856099999997pt/> (tamanho dos subproblemas);
- <img src="/ord/sortingAlgos/tex/5c4fe0ee7387172ce4b47c3a1a841673.svg?invert_in_darkmode&sanitize=true" align=middle width=64.25423069999998pt height=24.65753399999998pt/> (custo <img src="/ord/sortingAlgos/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, que varia conforme o tamanho da entrada <img src="/ord/sortingAlgos/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>).

Montando a relação de recorrência:
<p align="center"><img src="/ord/sortingAlgos/tex/f366f41aafa37682383c2dcb84726f2b.svg?invert_in_darkmode&sanitize=true" align=middle width=228.834837pt height=51.583387349999995pt/></p>
Esta relação só é válida caso <img src="/ord/sortingAlgos/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> seja potência de 2. Recorrência válida sempre:
<p align="center"><img src="/ord/sortingAlgos/tex/df131000357923a2cebdcf5087199de0.svg?invert_in_darkmode&sanitize=true" align=middle width=244.19183249999998pt height=49.315569599999996pt/></p>


#### Quick Sort

No QuickSort, um arranjo é dividido em duas partições. Uma contendo elementos com valor maior que um pivô, outra contendo elementos com valor menor que esse pivô.

Montando relação de recorrência para o melhor caso:
<p align="center"><img src="/ord/sortingAlgos/tex/df131000357923a2cebdcf5087199de0.svg?invert_in_darkmode&sanitize=true" align=middle width=244.19183249999998pt height=49.315569599999996pt/></p>
Montando relação de recorrência para o pior caso:
<p align="center"><img src="/ord/sortingAlgos/tex/8f6c932c1b78306775a35b237b00e08d.svg?invert_in_darkmode&sanitize=true" align=middle width=172.36486574999998pt height=49.315569599999996pt/></p>

[!equation](http://www.sciweavers.org/tex2img.php?eq=T%28n%29%20%3D%0A%5Cbegin%7Bcases%7D%20%0A%5Cdisplaystyle%7B%20%0AT%281%29%20%3D%201%20%5C%5C%20%0AT%20%28n%20-%201%29%20%2B%20c%20%5C%2C%20n%20%0A%7D%0A%5Cend%7Bcases%7D&bc=White&fc=Black&im=png&fs=18&ff=modern&edit=0)