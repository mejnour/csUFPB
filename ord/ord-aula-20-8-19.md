# ORD - 20/8/19

## Ordenação por Contagem

Algoritmo de Ordenação por Contagem - CountingSort.

- Existe um vetor A a ser ordenado
- Cria-se um vetor C que conta a quantidade de ocorrencias de cada elemento de A
- Ordeno o vetor C
- Mecânica de ordenação escrota. !!!PESQUISAR!!!

### Quantidade de Operações

Algoritmo:

```
for i <- 0 to k
	C[i] <- 0;

for j <- 1 to len(A)
	C[A[j]] <- C[A[j]] + 1;

for i <- 2 to k
	C[i] <- C[i] C[i - 1];

for j <- len(A) downto 1
	B[C[A[j]]] <- A[j];
	C[A[j]] <- C[A[j]] - 1;
```

Temos:

1. k + 3
2. 4 (k++)
3. n + 2
4. 8n
6. k + 1
7. 8(k - 1)
9. n + 2
10. 5n
11. 8n
