#include <stdio.h>
#define LEN 5

int main(){
	
	for(int i = LEN; i > 0; i--){
		for(int j = 0; j < i; j++){
			printf("%d", i);
		}
		printf("\n");
	}
	return 0;
}
