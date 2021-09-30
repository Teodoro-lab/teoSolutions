#include <stdio.h>
#define LEN 10

int main(){
	
	//Imprime la punta
	printf("*\n");
							
	for(int i = 0; i < LEN - 2; i++){	
	
		//Imprime el cuerpo
		printf("*");
		for (int j = 0; j < i; j++){
			printf(" ");			
		}
		printf("*\n");
	}
	
	//Imprime la base
	for(int i = 0; i < LEN ; i++){
		printf("*");
	}
	
	return 0;
}
