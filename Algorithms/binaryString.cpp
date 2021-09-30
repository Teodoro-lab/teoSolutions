#include <stdio.h>

char[] bin( int dec );

int main(){
	int decimal = 5;
	printS(bin(decimal))
	return 0;
}

char[] bin( int dec ){
	char[] binString;
	int counter, mod;
	
	counter = 0;
	while (dec > 0){
		mod = dec % 2;
		binsString[counter] = "1" ? 1 : binsString[counter] = "0";
		dec = (dec-mod)/2;
		counter++;
	}
	
	return binString;
}

void printS( int arr[], int len ){
	for (int i = 0; i < len; i++){
		printf("%d}\n", arr[i]);
	}
}
