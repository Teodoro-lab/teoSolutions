#include <stdio.h>

void prinTimes( char chr, int times );
void printDigits( int beginRange, int range, char first, char second, char third );
void print1_99( void );

int main(){
	char romanNum[] = "IVXLCDM";
	
//	printDigits(1, 9, romanNum[4],romanNum[5], romanNum[6]);
//	print1_99();
//	printf("%c", romanNum[4]);
	
	print1_99();// decenas&units
	printf("\n");
	
	for (int i = 1; i <= 9; i++){
		printDigits(i, i, romanNum[4],romanNum[5], romanNum[6]); //decenas&units
		printf("\n");
		for (int j = 1; j <= 9; j++){
			printDigits(i, i, romanNum[4],romanNum[5], romanNum[6]); // centenas
			print1_99(); // decenas&units
			printf("\n");
		}
	}
	
	
	
	return 0;
}

void prinTimes( char chr , int times){
	for (int i = 0; i < times; i++){
		printf("%c", chr);
	}
}

void printDigits( int beginRange, int range, char first, char second, char third ){
	//Counter
	int i;
	
	for (i = beginRange; i <= range; i++){
		if (i >= 1 && i <= 3){
			prinTimes(first, i);
		} else if (i == 4){
			printf("%c%c", first, second);
			
		} else if (i == 5){
			printf("%c", second);
			
		} else if(i >= 6 && i < 9){
			printf("%c", second);
			prinTimes(first, i - 5);
		} else if(i == 9){
			printf("%c%c", first, third);
		}
	}
}

void print1_99( void ){
	char romanNum[] = "IVXLCDM";
	for (int j = 1; j <= 9; j++){
			printDigits(j, j,romanNum[0], romanNum[1], romanNum[2]); // unidades
			printf("\n");
		}
	
	for (int i = 1; i <= 9; i++){
		printDigits(i, i, romanNum[2],romanNum[3], romanNum[4]); //decimas
		printf("\n");
		for (int j = 1; j <= 9; j++){
			printDigits(i, i, romanNum[2],romanNum[3], romanNum[4]); // decimas
			printDigits(j, j,romanNum[0], romanNum[1], romanNum[2]); // unidades
			printf("\n");
		}
	}
}
