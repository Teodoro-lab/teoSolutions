#include <stdio.h>

void swap(int* A, int* B);
void printArr(int* arr);
void QuickSort(int* arr, int start, int end);
int order(int* arr, int start, int end);
int arrLen(int* arr);

void QuickSort(int* arr, int start, int end){
	/*Recibes the index of start and end in order to perform the swap of numbers*/
	if(end - start <= 1){
		return;
	}
	
	int croos_index = order(arr, start, end);
	
	/*Left*/
	QuickSort(arr, start, croos_index-1);
	/*Rigth*/
	QuickSort(arr, croos_index, end);
}

int main(){
	int arr[] = {3, 5, 1, 9, 4, NULL};
	printArr(arr);
	QuickSort(arr, 0, arrLen(arr)-1);
	printArr(arr);
	return 0;
}


int order(int* arr, int start, int end){
	/*return where the index croos themselves*/
	int pivot = arr[end]; 
   int i = start - 1; 
   for (int j = start; j <= end - 1; j++){
      if (arr[j] < pivot){
         i++; 
      	swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[end]);
    return i + 1;
}

void swap(int* A, int* B){
	char save = *B;
	*B = *A;
	*A = save;
}

void printArr(int* arr){
	for(int i = 0; arr[i]; i++){
		printf("%d - ", arr[i]);
	}
	printf("\n");
}

int arrLen(int* arr){
	int i;
	for(i = 0; arr[i]; i++){}
	return i;
}
