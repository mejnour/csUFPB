## GDB Usage Example

Determinado código `<c-aula-21-06.c>` foi dado. O valor retornado, apesar do código estar correto, não é o esperado. Toda a aula até então tenta debugar o código pra se conseguir o resultado correto.

  - não se programa com comportamentos indefinidos
  - `r + enter` pra rerun the program
  - whatchpoint pára o loop quando certa variável atinge determinado valor ou outra condição de parada
  - o uso de steps no gdb permite verificar tudo passo-a-passo
  - o problema é o tipo das variáveis durante uma divisão feita [int -> float]
  - usar o gdb, às vezes, é melhor que debugar usando printf
  - o gbd permite testar o código sem recompilar o programa, além do printf poder inserir erros por si só
  - gdb não permite acompanhar o código fonte durante a seção de debug
  - front-end pro GDB:
    - `ctrl + x + a` divide a tela do gdb entre código e debugger
    - cgdb: front baseado em curses
    - eclipse: pode usar o gdb como debugger
    - ddd: data display debugger

DDD:
  - interface gráfica antiga
  - precursor dos bons debuggers
  - bugado e antigo
  - disponível GNU

C Data Types:
  - ponteiro são variáveis como outra qualquer, só que no lugar de valores, guarda um endereço de memória
  - organização de memória Little Endian/Big Endian

Examinando Tipos:
  - print é o comando mais comum pra avaliar tipos no GDB
  - o gdb permite formatar a saída. `/x` pra saida hexadecimal e /t pra binário
    - ex.: `print /x x` // printa a variável x de acordo com /x, em hexadecimal

Scriptando GDB:
  - O GDB aceita scripts
  - scripts devem ter a extensão `*.gdb`
  - colocar uma flag `--command=<script.gdb>` na execução do gdb
  - colocar a flag `--batch` pra executar tudo em lotes
