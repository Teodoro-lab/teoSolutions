#include <stdio.h>

int main(){
	int w, x, y, z, n = 0;
	int i, j, k, l; // Iterators
	int table[16][5];
	
	//	Generates all the combinations and evaluates the function for each combination
	for(i = 0; i < 2; i++){
		for(j = 0; j < 2; j++){
			for(k = 0; k < 2; k++){
				for(l = 0; l < 2; l++, n++){
					w = table[n][0] = i;
					x = table[n][1] = j;
					y = table[n][2] = k;
					z = table[n][3] = l;
					table[n][4] = ( w && y && !z ) || ( !w && !x && y ) || ( x && !y && z ) || ( !w && y) || ( x && !z );
				}
			}
		}
	}
	
	int karnaughMap[4][4];
	int combination[4][2] = {{0,0},{0,1},{1,1},{1,0}};
	int beginIndex, lastIndex, switcher;
	
	//	Generates the karnaugh Map and stores it in a matrix 
	for(i = 0; i < 4; i++){
		w = combination[i][0];
		x = combination[i][1];
		for(j = 0; j < 4; j++){
			y = combination[j][0];
			z = combination[j][1];
			
			int variables[4] = {w, x, y, z};
			beginIndex = 0, lastIndex = 15, switcher = 8;
			
			// Implements a binary-search for looking the result of each combination into the 'table' array
			for(int variable:variables){
				if (variable){
					beginIndex += switcher;
				} else {
					lastIndex -= switcher;
				}
				switcher /= 2;
			}
			karnaughMap[i][j] = table[lastIndex][4];
		}	
	}
	
	printf("f(w,x,y,z) = wyz'+ w'x'y + xy'z + w'y + xz'\n");
	printf("Expression: ( w && y && !z ) || ( !w && !x && y ) || ( x && !y && z ) || ( !w && y) || ( x && !z )\n\n");
	
	printf("|w  x  y  z| = f(...)\n");
	for(auto value:table) 
		printf("[%d, %d, %d, %d] = [%d]\n", value[0], value[1], value[2], value[3], value[4]);
	
	printf("\nDisjunctive Form\n");
	for(int n = 0; n < 16; n++){
		if (table[n][4]){
			printf("(%s%s%s%s)%s", 
					table[n][0]? "w": "w'", 
					table[n][1]? "x": "x'", 
					table[n][2]? "y": "y'", 
					table[n][3]? "z": "z'", 
					n < 14? " + ":"\n");	
		}
	}
	
	printf("\nConjunctive Form\n");
	for(auto value:table){
		if (!value[4]){
			printf("(%s + %s + %s + %s)", 
					!value[0]? "w": "w'", 
					!value[1]? "x": "x'", 
					!value[2]? "y": "y'", 
					!value[3]? "z": "z'");	
		}
	}

	printf("\n\n%s\n\n%14s\n","Karnaugh Table", "00 01 11 10");
	for(i = 0; i < 4; i++)
		printf("%d%d|[%d, %d, %d, %d]\n", combination[i][0], combination[i][1], karnaughMap[i][0], karnaughMap[i][1], karnaughMap[i][2], karnaughMap[i][3]);
					
	return 0;
}
