#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int g = 100;

static int func(int a) {
	char *s = "abc";
	char *t = strdup(s);
	int x = 3;
	static int y = 300;
	void *z = malloc(10);
	printf("param a is at %p\n", &a);
	printf("char *s is at %p which points to %p\n", &s, s);
	printf("char *t is at %p which points to %p\n", &t, t);
	printf("local var x is at %p\n", &x);
	printf("static var y is at %p\n", &y);
	printf("void *z is at %p which points to %p\n", &z, z);
	return 0;
}

int main(int argc, char *argv[]) {
	printf("global var g is at %p\n", &g);
	func(4);
	printf("function func is at %p\n", &func);
}