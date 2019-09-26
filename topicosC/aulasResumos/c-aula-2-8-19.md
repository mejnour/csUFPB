# Aula 2/8/19

## Macro e Pré-processamento

### Function-like Macros

- Arquivo `c-aula-2-8-19.c`
- Macros que usam argumentos
- Parênteses da macro devem ser colados como em FUNCTION()
- Pré-processar usando -z

#### O Assert

- É uma macro
- Usar Assert é mais eficiente. Se usado em modo debug, gera código debug. Quando não roda em modo debug, não gera nada, sendo uma função eficiente nos dois modos.
- Compilar com o otimizador ligado para chamada de funções vazias.
- Programadores experientes preferem o Assert a um teste com um If

### Macro Pitfalls

- Problemas de precedência: sempre colocar parênteses ao redor do corpo de function-like macros.

### Macro Examples

- Quando se quer escrever macros com mais de uma linha, se quebra linha usando `\`
- Ainda sobre macros de mais de uma linha, tomar cuidado com a colocação de `;`, uma vez que o processamento pode ver duas `;` dependendo do usuário.
- Quando se quer passar uma string como argumento dentro de  uma macro, usa-se  `#` ao invés de aspas.

~~~c
#ifdef _DEBUG
    #define GL_CHECK(stmt) do { \
        stmt; \
        CheckOpenGLError(#stmt, __FILE__,  __LINE__); \
        } while (0)
#else 
    #define GL_CHECK(stmt) stmt
#endif
~~~

### O qualificador de tipo `const`

- É usado para que o valor de um variável não seja alterado ao longo do código.
- Acontece que o `const` transforma uma variável em modo "somente leitura". O C só garante que essa variável só não pode ser alterada pelo próprio programa.
- O `const` funciona como um `define`, substituindo uma variável  pelo seu valor ao longo do código. Isso aumenta a eficiência do código. A diferença entre const e define é que o `define` sempre substitui e o `const` nem sempre.
- No código abaixo, a atribuição de um const int pra um int é possível por se tratar de cópia e, portanto, somente leitura.

~~~c
const int ci = 20
int i = ci
return i + ci
~~~

- Ponteiro pra const depende da forma como é declarado.
- Abaixo, o const age sobre o objeto apontado. O ponteiro pode ser modificado. Estranhamente, a declaração abaixo só age sobre o próprio ponteiro. Fazer uma chamada  direto à variável (que não é const),  pode alterar o conteúdo dessa variável.

~~~C
const int *pci
~~~

- Abaixo, o const age sobre o ponteiro (o endereço). O objeto pode ser modificado.

~~~C
int const *pci
~~~

Um ponteiro const pode apontar pra quem é  const e pra quem não é const. Um ponteiro não-const pode apontar somente pra quem também é não-const.