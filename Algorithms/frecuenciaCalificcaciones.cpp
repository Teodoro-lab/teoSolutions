#include <stdio.h>
#define NUM_ALUMNOS 40
#define RANGO 10

int main(){
	
	int calificaciones[NUM_ALUMNOS] = { 1, 2, 6, 4, 8, 5, 9, 7, 8, 10, 1, 6, 3, 8, 6, 10, 3, 8, 2, 7, 6, 5, 7, 6, 8, 6, 7, 5, 6, 6, 5, 6, 7, 5, 6, 4, 8, 6, 8, 10 };
	int frecuencia[RANGO] = {0};
	
	
//	Aumenta en 1 el valor de la frecuencia de acuerdo a la calificacion
	for (int i = 0; i < NUM_ALUMNOS; i++){
		++frecuencia[calificaciones[i] - 1]; 
//		printf("La calificacion es %d y la suma ahora es %d\n", calificaciones[i], frecuencia[calificaciones[i] - 1]);
	}
	
//	imprime las frecuencias
	printf("%s%16s\n", "Rango", "Frecuencia");
	for (int j = 0; j < RANGO; j++){
		printf("%5d%15d\n", j + 1, frecuencia[j]);
	}
	
	return 0;
}
