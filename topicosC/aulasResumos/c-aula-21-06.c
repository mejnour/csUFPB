#include <stdio.h>

float Average(int *w, int n) {
  int i;
  int avg;
  for (i = 0; i < n; i++) {
    avg += w[i];
  }
}

int main(void) {
  int x[5] = {2, 2, 3, 4, 5};
  int num = 5;
  float avg = Average(x, num);
  printf("Average: %f\n", avg);
  return 0;
}
