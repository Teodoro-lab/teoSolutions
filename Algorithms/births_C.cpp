#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct key_value{
	char name[12];
	int gain_lost;
};

key_value * key(char* string, int money){
	struct key_value* aux = (key_value*)(malloc(sizeof(key_value)));
	strcpy((*aux).name, string);
	(*aux).gain_lost = money;
	return aux;
}

int look_index(char* name, struct key_value* arr[], int len){
	for(int i = 0; i < len; i++){
		if (strcmp((*arr[i]).name, name)){
			return i;
		}
	}
}

int main(){
	int n_givers;
	printf("Ingrese numero de personas ");
	scanf("%d", &n_givers);
	char name[13];
	struct key_value* arr[n_givers];
	
	for(int i  = 0; i < n_givers; i++){
		fflush(stdin);
		printf("dame los nombres ");
		gets(name);
		arr[i] = key(name, 0);
	}
	
	int index, money, n_people, spend;
	for (int i = 0; i < n_givers; i++){
		
		printf("Ingrese el nombre de la persona");
		fflush(stdin);
		gets(name);
		
		index = look_index(name, arr, n_givers);
		
		printf("Ingrese su dinero gastado ");
		scanf("%d", &money); 
		
		printf("Ingrese el n de personas que recibio regalo");
		scanf("%d", &n_people);
		
		spend = (money / n_people) * n_people;
		int win_per_person = money / n_people;
		(*arr[index]).gain_lost -= spend;
		char person_name[13];
		
		for(int j = 0; j < n_people; j++){
			printf("Ingrese el nombre de la persona %d", j);
			fflush(stdin);
			gets(person_name);
			(*arr[look_index(person_name, arr, n_givers)]).gain_lost += win_per_person;
			
		}
	}
	
	for(int i = 0; i < n_givers; i++){
		printf("%s  %d",(*arr[i]).name,(*arr[i]).gain_lost);
	}
	
	return 0;
}

