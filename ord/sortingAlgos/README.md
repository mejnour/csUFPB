# ORD - Algoritmos de Ordenação

## Counting Sort

Ideia básica:

- Determinar quantos elementos são menores que um $x$;
- De acordo com essa quantidade, adicionar o elemento $x$ na posição quantidade + 1;
- É um algoritmo estável.

Manipulação do Algo:

- A[1 .. n] - arranjo desordenado;
- B[1 .. n] - arranjo ordenado;
- C[0 .. K] - arranjo auxiliar;
- K - valor máximo de A.

Algoritmo:

- Inicializa-se C no intervalo $[0, K]$, onde $K$ é o valor máximo de A. Isto quer dizer que C terá $K + 1$ posições:

  ```python
  for i in range(K + 1):
      C.append(0)
  ```

- Em cada posição A[i] de C, adicione $1$. Isto conta quantas ocorrências existem de cada elemento de A. Assim:

  ```python
  for i in range(len(A)):
      C[A[i]] += 1
  ```

- Some, cumulativamente, passo a passo, todos os elementos de C. Isto quer dizer que cada C[i] conterá o número de elementos iguais ou menores que aquela posição i. Assim:

  ```python
  for i in range(1, len(C)):
      C[i] += C[i - 1]
  ```

- Popule o arranjo B com as ocorrências de A na posição certa, C[A[i]], de B e decremente em $1$ a cada passo daquele valor C[A[i]]:

  ```python
  for i in range(len(A), -1, -1):
      B[C[A[i]]] = A[i]
      C[A[i]] -= 1
  ```

Complexidade:

- O primeiro laço é $O(K)$.
- O segundo laço é $O(n)$.
- Tempo total = $O(n + K)$. Embora a literatura use sempre o tempo maior, $O(n)$, para descrever o Counting Sort, quando $K$ é muito grande (quadrático, p.ex.), pode-se dizer que Counting Sort é um algoritmo *pseudo-linear*.

## Radix Sort

Ideia básica:

- Ordena pela posição dos algarismos em cada $x$ da entrada, ou seja, quebrando cada $x$ em colunas, ordena da direita para esquerda;
- É um algoritmo estável;

Manipulação:

- A[1 .. n] - arranjo desordenado;
- d - Número de dígitos do maior elemento do arranjo A. Quando iterado sobre, é o digito que está sendo trabalhado, sendo 1 o dígito menos significativo (mais a direita) e d o dígito mais significativo (o dígito mais a esquerda);

Algoritmo:

- Usa-se um tipo de ordenação para o arranjo A sobre um laço no intervalor $[1, d]$:

  ```python
  def RADIX_SORT(A, d):
      for i in range(1, d):
          COUNTING_SORT(A, i)
  ```

- Na prática é usado para ordernar registros chaveados por vários campos distintos.

Complexidade:

Se $k \le n^{c}$, então Radix Sort tem tempo:
$$
O(n \, \log_{10}(n))
$$

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
$$
T(n) = aT \left( n \over b\right)+ f(n)
$$
Em que:

- $a$ = número de subproblemas criados;
- $n$ = tamanho da entrada;
- $b$ = tamanho de cada problema em relação ao problema original;
- $f(n)$ = custo da solução de cada subproblema.

Exemplo de Divisão e Conquista:

- Busca Binária
- Merge Sort
- Quick Sort

#### Busca Binária

Na Busca Binária, as "entradas" são divididas pela metade a cada iteração. Uma lista de 8 itens vira uma de 4 itens, depois uma de 2 itens e, por fim, vira uma lista de 1 item que é a solução do problema. Assim, temos que:

- $a$ = 1 (subproblemas a cada iteração);
- $b$ = $\displaystyle{1 \over 2}$ (tamanho de cada subproblema);
- $f(n) = c$ (custo $c$ constante).

Montando a relação de recorrência:
$$
T(n)=\begin{cases}    T(1) = 1 \\    T \left(\displaystyle \frac{n}{2}\right) + c \qquad n > 1\end{cases}
$$

#### Merge Sort

No Merge Sort, as entradas são divididas ao meio em duas soluções. Cada solução desta, por sua vez, é dividida novamente pela metade. Assim, uma lista de 8 itens viram duas listas de 4 itens cada, depois viram quatro listas de 2 itens cada e, por fim, viram oito listas de 1 item cada. Temos daí que:

- $a = 2$ (subproblemas a cada iteração);
- $b = \displaystyle{1 \over 2}$ (tamanho dos subproblemas);
- $f(n) = n$ (custo $n$, que varia conforme o tamanho da entrada $n$).

Montando a relação de recorrência:
$$
T(n) =\begin{cases}	T(1) = 1 \\	2T \left(\displaystyle{\frac{n}{2}}\right) + n \qquad n > 1\end{cases}
$$
Esta relação só é válida caso $n$ seja potência de 2. Recorrência válida sempre:
$$
T(n) =\begin{cases}	\displaystyle{	T(1) = 1 \\	T \left( \left \lceil \frac{n}{2} \right \rceil  \right) + T \left( \left \lfloor \frac{n}{2} \right \rfloor  \right) + c \, n	}\end{cases}
$$


#### Quick Sort

No QuickSort, um arranjo é dividido em duas partições. Uma contendo elementos com valor maior que um pivô, outra contendo elementos com valor menor que esse pivô.

Montando relação de recorrência para o melhor caso:
$$
T(n) =\begin{cases}	\displaystyle{	T(1) = 1 \\	T \left( \left \lceil \frac{n}{2} \right \rceil  \right) + T \left( \left \lfloor \frac{n}{2} \right \rfloor  \right) + c \, n	}\end{cases}
$$
Montando relação de recorrência para o pior caso:
$$
T(n) =\begin{cases}	\displaystyle{	T(1) = 1 \\	T (n - 1) + c \, n	}\end{cases}
$$
