# Dynamic Memory Allocation

## Malloc

- O malloc é ineficiente
- No lugar de malloc, que é caro, usa-se Memory Arena
- Em uma Memory Arena, uma região da memória é constantemente escrita e reescrita.

## Automatic Variables

- Variáveis locais e argumentos de funções são alocados automaticamente
- Sem o `static`, a variável é alocada
- Passagem de parâmetro em C, é tudo por cópia.
- Alocações automáticas são feitas na pilha de processos.
- A pilha de processos é feita no final da memória, de baixo pra cima, afim de não conflitar com outros elementos da memória virtual.
- No caso de uma função recursiva que se chama muitas vezes, a pilha aumenta, uma vez que o endereço de retorno também ocupa espaço na memória virtual.
- Uma vez que toda função recursiva demanda condição de parada, o stack vai crescendo de maneira que em uma memória virtual grande, as chamadas demandam tanta alocação de memória, que a memória física é consumida antes da memória virtual.
- Um computador só deixa o usuário utilizar a memória que foi pré alocada. Uma stack tem uma região memória pré-alocada, que cresce/diminui conforme o processo acontece. Se a stack aumenta numa taxa que o sistema operacional não consegue acompanhar a pré-alocação, ocorre stack-overflow. Não é a pilha que encosta na heap.
- Software Limit vs Hardware Limit. O usuário consegue pedir memória da stack via Software Limit. Somente um Super User consegue alterar o Hardware Limit. Um software limit é limitado pelo começo do hardware limit.
- GNU C tem a função `alloca()`, que aloca dinamicamente direto na pilha.
- Funções inline não são chamadas por call. O código é substituido.

## C99 Variable Length Array (VLA)

- VLA vs `alloca()`: o alloca só volta quando o return do assembly é chamado. O VLA volta quando o escopo retorna.
  
## Parameter Passing

- A "passagem por referência" em C, quando se passa o endereço de uma variável, na verdde é por cópia, uma vez que se copia o endereço passado para o escopo da função.

## Pointer to Pointer

- .

~~~
void insertAfter(Struct Node * nc, int Value) {
    struct Node* new_n = ...malloc...;
    new_n -> Value = Value;
    new_n -> next = nc -> next;
    nc -> next = new_n;
}

void insertAfter(Struct Node ** n, int Value) {
    if(!*nc) {
        *nc = ...malloc...;
        *nc -> Value = Value;
        *nc -> next = n -> Null;
    }
    else {
        pass
    }
}

insertAfter(&node, ...)
~~~

## Trivia

- Gargalo de VonNeumann
- Numa Memory

## Looking at the Assembly

- Uma variável é definida quando o compilador reserva espaço pra ela. Uma declaração não aloca espaço pelo compilador. Variáveis estáticas são sempre definidas.

## Assembly

- Linguagem de Montagem. Baixo nível. Alta correspondência (geralmente 1-1) com linguagem de máquina (binário).
- Montador: transforma assembly em linguagem de máquina.
- Compilador: transforma uma linguagem de alto nível em assembly.
- GCC: principalmente um compilador. GCC compila, AS monta e LD linka.
- 