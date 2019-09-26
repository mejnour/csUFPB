# Tópicos em C  - 9/8/19

### Reducing the Cost of Function Calls

- www.godbolt.org
- `gcc -Wall -Werror -pedantic -O2 -std=c99 -E <arq.c> > <arq.i>`
  `gcc -Wall -Werror -pedantic -O2 -std=c99 -fno-asynchronous -unwind-tables -S <arq.i>`
- O que porra é isso acima?
- Procurar por Compiler Explorer
- IR ATRAS DOS METODOS MAIS COMUNS DE OTIMIZACAO DO COMPILADOR
- Otimizações só acontecem quando o otimizador está ligado (não tem efeito colateral direto, acredito).
- Funções muito caras não valem a pena fazer o assembly escrever inline.
- Funções inline funcionam melhor quando as funções são pequenas e precisam ser chamadas muitas vezes.
- Para pedir pro compilador fazer determinada função inline, passa-se o especificador `inline` à funcão desejada.
- Funções `inline` são executadas mais rápidas por reduzirem o custo de chamada da função.
- Se o especificador `inline` for declarado e a flag de otimização `-O2` não for passada ao compilador, a otimização não vai ocorrer.
- O especificador `inline` sozinho não é garantia de que aquela função será traduzida inline no assembly. Funciona como uma espécie de pedido que o compilador pode ou não acatar.
- Funções recursivas não podem ser executadas com o especificador `inline`.
- Funções `inline` só funcionam na própria unidade de traducão.

### Splitting the Code

- Cada arquivo gera uma unidade de tradução.
- Entender o que é Unidade de Tradução.
  - Solução dos anos 70, limitada pela baixa capacidade da época. Usada até hoje.
- Se declarar uma função `inline` num arquivo `.h` de cabeçalho, essa função pode ser chamada através de `#include` por várias outras unidades de tradução como funções `inline`.
- Usar OBJDUMP ou MM pra saber se existe chamada à função. Caso haja, a funções não foi traduzida como `inline`.

### Inline Function in Multiple Files

- No caso de se querer que uma função `inline` declarada num arquivo de cabeçalho `.h`, seja chamada através de seu endereço (faça uma _call_), ou seja, **outline**, pode-se redeclarar a mesma função com um `extern`. 
- O código abaixo chama uma função inline declarada num header. Ela cria uma instância outline dessa função.

```C
extern inline void InsertionSort();
```

### Inline/Const vs Macros

- Usar macros deixa o código minimamente mais rápido que usar variáveis.