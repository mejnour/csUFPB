# Ordenação e Recuperação - 25/06/19

## Grafos
- Conceitos básicos
- Vértices: entidades
- Arestas: relações entre vértices
- Tamanho: n(vértices) + n(arestas)
- Dois vértices são adjacentes quando tocados pela mesma aresta
- Quando duas extremidades de uma aresta tocam o mesmo vértice, diz-se loop
- O complementar de um grafo G, é um outro grafo G2, onde todos as ligações são invertidas

### Representação
- Lista de Adjacências
- Matriz de Adjacências

### Algoritmos de Busca em Grafos
- Busca em Extensão/Largura
- Busca em Profundidade

### Exercício
1. Implementar algoritmos de busca em grafos
- Implementar matriz e lista de adjacências
- Implementar leitor de grafos em arquivos
- Implementar Busca em Largura
- Implementar Busca em Profundidade

```mermaid
classDiagram
  Class01 <|-- AveryLongClass : Cool
  Class03 *-- Class04
  Class05 o-- Class06
  Class07 .. Class08
  Class09 --> C2 : Where am i?
  Class09 --* C3
  Class09 --|> Class07
  Class07 : equals()
  Class07 : Object[] elementData
  Class01 : size()
  Class01 : int chimp
  Class01 : int gorilla
  Class08 <--> C2: Cool label
```

