#include <stdio.h>

int fibonacci(int n) {
	if (n == 0) {
		return 0;
	}

	if (n == 1) {
		return 1;
	}

	return fibonacci(n - 2) + fibonacci(n - 1);
}


int main() {
   int start = 3;

   for (int i = 0; i < 30; i++) {
	fibonacci(i);
   } 
}
