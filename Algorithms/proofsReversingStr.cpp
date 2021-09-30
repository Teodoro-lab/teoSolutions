#include <stdio.h>

int main(){
	char str[] = "Holi Amigues";
	int len = sizeof(str) - 1;
	printf("%d", len);
	printf("%p", *str[0]);
	return 0;
}
