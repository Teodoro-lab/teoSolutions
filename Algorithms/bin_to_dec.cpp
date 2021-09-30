#include <stdio.h>
#include <stdlib.h>

int len(char*array);
int decToBinary(char* binaryStr, int length);
int pow(int number, int pow);
int swap(char* arr);

int main(){
	char binaryString[256];
	int finDeEjecucion = false;
	do {
		printf("Ingrese el numero binario a convertir a decimal: ");
		fflush(stdin);
		gets(binaryString);	
		int length = len(binaryString);
		printf("%d\n", decToBinary(binaryString, length));
		printf("Presione 1 si desea terminar la ejecion: ");
		scanf("%d", finDeEjecucion);
		system("cls");
	} while(not(finDeEjecucion));
	return 0;
}




//------------------------------------------------------------ 1010111

//int decTobinary(char* binaryStr, int length, int power = 0){ 
//	if (length == -1)
//		return 0;
//	else if (binaryStr[length - 1] == '1')
//		return pow(2, power) + decTobinary(binaryStr, length - 1, power + 1);
//	else
//		return decTobinary(binaryStr, length - 1, power + 1);
//} 101011011  11

int decToBinary(char* binaryStr, int length){
	if (length == -1)
		return 0;
	else if (*binaryStr == '1')
		return pow(2, length - 1) + decToBinary(binaryStr + 1, length - 1);
	else
		return decToBinary(binaryStr + 1, length - 1);
}

//------------------------------------------------------------


//
//
//
//
//
//
//
//
//
////------------------------------------------------------------
//
//int decTobinary(char* binaryStr, int length, int index = 0){ 
//	if (index == length)
//		return 0;
//	else if (binaryStr[index] == '1')
//		return pow(2, ) + decTobinary(binaryStr, length, index + 1);
//	else
//		return decTobinary(binaryStr, length, index + 1);
//}
//
////------------------------------------------------------------
//
//
//
//
//int decTobinary(char* binaryStr, int length, int index = 0){ 
//	if (length == -1)
//		return 0;
//	else if (binaryStr[length - 1] == '1')
//		return pow(2, power) + decTobinary(binaryStr, length - 1, power + 1);
//	else
//		return decTobinary(binaryStr, length - 1, power + 1);
//}


int len(char*array){
	int counter = 0;
	for (int i = 0; array[i]; i++)
		counter++;
	return counter;
}

int pow(int number, int power){ 
	if (power < 1)
		return 1;
	return number *  pow(number, power - 1);
}

int swap(char* arr, int length){
	int begin = 0, last = length - 1;
	for(int i = 0; i < length/2; i++){ 
		arr[begin] += arr[last]; 
		arr[last] = arr[begin] - arr[last]; 
		arr[begin] = arr[begin] - arr[last];
	}
}
