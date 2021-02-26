#"PascalTriangle = [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]"
                  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

                # (1,3) (3,6) (6, 10) (10, 15)
                   
# el algortimo inicia almacenando 1 en el array

# genera un for para el cual necesitaremos evaluar la longitud N del array
# y hacer N-1 iteraciones que generarán otro numero a partir de los dos evaluados
# en cada iteración

rows = int(input("Ingrese el numero de filas que desea que tenga la torre: "))
botton = 1
top = 3
incremento = 2 
PascalTriangle = [1, 1, 1]

print([1])
for i in range(rows - 1):
    incremento += 1
    
    # se generan los elementos de la fila
    PascalTriangle.append(1)    # se añade el numero 1 el extremo izquierdo
    for index in range(botton, top - 1): 
        PascalTriangle.append(PascalTriangle[index] + PascalTriangle[index + 1])
    PascalTriangle.append(1)    # se añade el numero 1 el extremo derecho
    
    # se imprime la fila anterior pues es de la que se sacaron los nuevos valores
    print(PascalTriangle[botton:top])
    
    # se empieza donde se terminó y se hace el incremento del top
    botton = top
    top += incremento


"""
sumatoria = 0
nums = []
for i in range(10):
    num = int(input(f"Ingrese uno de sus números {i + 1}:"))
    nums.append(num)
    sumatoria += num
print(sumatoria)
print(nums)
"""

"""
array_1 = []
array_2 = []
array_3 = []
exe = True
while exe:
    a,b = int(input("Ingrese el valor del primer arreglo: ")), int(input("Ingrese el valor del segundo arreglo: "))
    array_1.append(a)
    array_2.append(b)
    array_3.append(a+b)
    if int(input("Ingrese su numero:")) == 0:
        exe = False
print(array_1, array_2, array_3)
"""

"""
array_1 = []
array_2 = []
array_3 = []
exe = True
while exe:
    a,b = int(input("Ingrese el valor del primer arreglo: ")), int(input("Ingrese el valor del segundo arreglo: "))
    array_1.append(a)
    array_2.append(b)
    array_3.append(a*b)
    if int(input("Ingrese su numero:")) == 0:
        exe = False
print(array_1, array_2, array_3)
"""
"""
array_1 = []
array_2 = []
array_3 = []
exe = True
for i in range(int(input("Ingrese la longitud de los arreglos: "))):
    a,b = int(input("Ingrese el valor del primer arreglo: ")), int(input("Ingrese el valor del segundo arreglo: "))
    array_1.append(a)
    array_2.append(b)
    array_3.append(a*b)
productoEscalar = sum(array_3)
if productoEscalar == 0:
    print("Los vectores son ortogonales")
print(array_1, array_2, array_3)
print(productoEscalar)
"""
"""
for i in range(int(input("Ingrese la longitud de los arreglos: "))):
    a,b = int(input(f"Ingrese el valor {i} del primer arreglo: ")), int(input(f"Ingrese el valor {i} del segundo arreglo: "))
    array_1.append(a)
    array_2.append(b)
    
if array_1 == array_2:
    print("Los arreglos no son iguales")   
else:
    print("Los arreglos no son iguales")   

"""



def sort(arr, form=True):
    def asc(i):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    def des(i):
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    for i in arr:
        for i in range(len(arr) - 1):
            if form:
                asc(i)
            else:
                des(i)
            
arr = [1, 6, 3, 8, 2, 0, 5, 8, 4, 9, 11, 12]
response = input("Escriba 1 para ordernar ascendentemente o cualquier tecla para descendente: ")
if response == "1":
    sort(arr)
else:
    sort(arr, False)

print(arr)




#for i in range(6):
 #   arr.append(int(input(f"Ingrese el {i + 1} de su arreglo")))

"""
def reverser(arr):
    length = len(arr)
    for from_init in range(length//2):
        from_last = length-1-from_init
        arr[from_init] = arr[from_init] + arr[from_last]
        arr[from_last] = arr[from_init] - arr[from_last]
        arr[from_init] = arr[from_init] - arr[from_last]
    return arr
"""
def reverser(arr):
    length = len(arr)
    for from_init in range(length//2):
        from_last = length-1-from_init
        arr[from_init], arr[from_last] = arr[from_last], arr[from_init]
    return arr

def divider(num=1):
    result = []
    global arr
    for i in range(num):
        if i == 0:
            result += reverser(arr[:len(arr)//num if len(arr)%2==0 else len(arr)//num+1])
        else:
            result += reverser(arr[len(arr)//num:len(arr)-1])
    return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19, 20, 21]
arr = [1, 2, 3, 4, 5, 6]
"""
print("len:arr = ",len(arr))
arr_1 = reverser(arr[:len(arr)//2 if len(arr)%2==0 else len(arr)//2+1])
arr_2 = reverser(arr[len(arr)//2:len(arr)-1])
arr = arr_1 + arr_2
print(arr)
print("len:arr = ",len(arr))
arr = reverser(arr)
print(arr)
"""
print(reverser(arr))
