# IntComp - 6/8/19

## Caixeiro Viajante

### O Problema

- Passar por N pontos e retornar ao ponto inicial.

### Aplicações

- Transporte
- Furação de Placas de Circuito Integrado
- Máquinas automáticas de Solda

### Histórico do Caixeiro VIajante

- Surgiu na década de 20 no meio acadêmico nos USA

### Quantidade de Permutações

- Para o Simétrico:

  $\displaystyle \frac{n!}{2n} = \frac{n - 1}{2}$

- Para o Assimétrico:
  $\displaystyle \frac{n!}{n} = (n - 1)!$

- Jack Edmonds
  - Propôs, na década de 60, que resolver problemas eficientemente seja resolver em tempo polinomial.
  - Desde então, desenvolvou-se toda a teoria da complexidade em torno disto.
- Programação Dinamica?

### resolvendo problemas NP-dificil

Podem ser resolvidos por famílias de algoritmos:

- Exatos
  - Programação Dinamica
    - Problemas Polinomiais
    - Problema dos Parênteses em Multiplicação de N matrizes (Cormen)
- Aproximados
  - Metaheuristica
    - Solução Unica
    - Solução Baseada em Populações

## Heuristica

- Heuristica é montar uma forma de resolver o problema de acordo com o que se acredita que pode resolvê-lo. A forma comparativa de testar se aquele "feeling" está de acordo é compará-lo a métodos exatos
- No problema do CV, quando existe um cruzamento entre os caminhos, esta solução não é ótima.
- Heuristica da melhor inserção