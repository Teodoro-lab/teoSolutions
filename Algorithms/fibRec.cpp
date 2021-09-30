#include <stdio.h>

int fib(int n);

int main(){
	for(int i = 0; i < 10; i++)
		printf("%d\n", fib(i));
	return 0;
}

int fib(int n){
	if (n == 0 || n == 1){
		return 1;
	}
	return fib(n - 1) + fib(n - 2);
}
