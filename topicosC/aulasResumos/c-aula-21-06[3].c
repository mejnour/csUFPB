#include <stdio.h>

int Sum(int begin, int end) {
  int i;
  int acc = 0;
  for (i = begin; i <= end; i++){
    acc += i;
  }

  return acc;
}

int main(void) {
  int a = 1;
  int b = 5;
  int sum = Sum(a, b);
  printf("Sum: %i\n", sum);

  return 0;
}
