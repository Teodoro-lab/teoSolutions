#include <stdio.h>

void countSort(int* arr, int lng);
int len(int* arr);
void printArr(int* arr);
void swap(int* A, int* B);

int main(){	
	int arr[] = {5, 3, 6, 2, 1, 1, 22, 100, 63, NULL};
	int lng = len(arr);
	countSort(arr, lng);
	printArr(arr);
	return 0;
}

int len(int* arr){
	int i;
	for(i = 0; arr[i]; i++){}
	return i;
}

void printArr(int* arr){
	for(int i = 0; arr[i]; i++){
		printf("%d - ", arr[i]);
	}
}

void swap(int* A, int* B){
	char guardar = *B;
	*B = *A;
	*A = guardar;
}

void countSort(int* arr, int lng){
	int last_index = lng - 1;
	for(int i = 0; i < lng; i++){
		for(int j = 0; j < last_index ; j++){
			if(arr[j] > arr[last_index]){
				swap(&arr[j], &arr[last_index]);
			}
		}
		last_index--;
	}
}
