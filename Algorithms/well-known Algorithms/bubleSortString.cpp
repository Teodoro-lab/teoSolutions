#include <stdio.h>
#define len 10

void swap(char* A, char* B);
void print_String(char* arr);
void bubble_Sort_String(char* string);

int main(){
	char string[len + 1]	= "aebcffgidf";
	puts(string);
	bubble_Sort_String(string);
	puts(string);
	return 0;
}

void swap(char* A, char* B){
	char guardar = *B;
	*B = *A;
	*A = guardar;
}

void print_String(char* arr){
	for(int i = 0; i < len; i++){
	 	printf("%c", arr[i]);
	 }
	 printf("\n");
}

void bubble_Sort_String(char* string){
	for(int i = 0; i < len; i++){
		for(int j = 0; j < len - 1; j++){
			if (string[j] > string[i]){
				swap(&string[i], &string[j]);
			}
		}
	}
}
