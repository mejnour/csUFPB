# ORD (Resumo) - Primeira Prova

- Heap:
  - Heap Binário
  - MaxHEAPIFY
  - BuilMaxHEAP
  - HeapSort
  - Fila de Prioridade Máxima
    - Implementado com MaxHEAPIFY
    - Funções:
      - HEAP-MAXIMUM(A)
        Retorna o elemento com maior valor
      - MAX-HEAP-INSERT(A, x)
        Insere um elemento
      - HEAP-EXTRACT-MAX(A)
        Remove um elemento
      - HEAP-INCREASE-KEY(A, i, x)
        Aumenta o valor da chave de `x` para o valor de `i` (Aumenta a prioridade)
- Grafos
  - Representação:
    - Lista de Adjacências
    - Matriz de Adjacências
  - Busca:
    - Extensão
    - Profundidade
- DIjkstra
  - Estratégia Gulosa
    Algoritmo faz escolha localmente ótima na esperança de encontrar um ótimo global. Quando o problema for NP-completo ou NP-difícil, estratégias gulosas podem obter uma solução aproximada em tempo polinomial.
  - Relaxação
    Inicia todos os vértices com $\infty$ e vai trocando as chaves pela combinação dos pesos conforme o melhor caminho (revisar Slide).
- Huffman
- Árvore B
- Tabelas Hash