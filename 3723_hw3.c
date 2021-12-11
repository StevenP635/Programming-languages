#include <stdio.h>

int x = 300;
int y = 200;
int z = 100;

static void funcA(void) {
  x += 10;
  y += 20;
  z += 30;
  printf("funcA: x y z = %d %d %d\n", x, y, z);
}

static void funcB(int y) {
  int z = 400;
  y += 10;
  z += 20;
  funcA();
  printf("funcB: x y z = %d %d %d\n", x, y, z);
}

static void funcC(int x) {
  funcB(200);
  x += 50;
  printf("funcC: x y z = %d %d %d\n", x, y, z);
}

int main(int argc, char *argv[]) {
  funcC(100);
  printf("main:  x y z = %d %d %d\n", x, y, z);
  return 0;
}
