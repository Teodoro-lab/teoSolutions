sudoku = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
#case2--------#sudoku = "195743862431865927876192543387459216612387495549216738763524189928671354254938671"
#case3--------#sudoku = input("Ingrese sus respuestas al sudoku: ")

arr = [sudoku[:9], sudoku[9:18], sudoku[18:27], sudoku[27:36], sudoku[36:45], sudoku[45: 54], sudoku[54:63], sudoku[63:72], sudoku[72:81]]

def filas(arr):
    cheker = [1,2,3,4,5,6,7,8,9]
    auxiliar = []
    for fila in arr:
        auxiliar = []
        for num in range(9):
            auxiliar.append(int(fila[num]))
        if sorted(auxiliar) == cheker:
            continue
        else:
            return("No")

def columnas(arr):
    cheker = [1,2,3,4,5,6,7,8,9]
    auxiliar = []
    for num in range(9):
        auxiliar = []
        for columnas in arr:
            auxiliar.append(int(columnas[num]))
        if sorted(auxiliar) == cheker:
            continue
        else:
            return("No")

def cuadrados(arr):
    cheker = [1,2,3,4,5,6,7,8,9]
    for num in range(3):
        sumador = -3
        a = -3
        b = -2
        c = -1
        a += 3
        b += 3
        c += 3
        for i in range(3):
            sumador += 3
            if sorted(map(int, list(sudoku[9 * a + sumador: 9 * a + sumador + 3 ] + sudoku[9 * b + sumador: 9 * b + sumador + 3] + sudoku[9 * c + sumador: 9 * c + sumador + 3]))) == cheker:
                continue
            else:
                return ("No")

if cuadrados(arr) != "No" and filas(arr) != "No" and columnas(arr) != "No":
    print ("YES")
else: print("NO")



