import time
import math

# Función para evaluar qué número o números son primos en un rango
def isPrime(a, num):
    primos = []
    for x in range(a, num + 1):
        for i in range (2, int(math.sqrt(x + 1))):
            if i == num and i > 2:
                primos.append(num)
            elif num % i == 0:
                break
            elif  i == num - 1:
                primos.append(num)
    return primos #Devuelve una lista de números primos encontrados en el rango dado


# Función que evalua si la respuesta pide que se detenga el programa
def stop (a):
    return True if a == "Stop" else False


# Función qué pide al usuario la información para el programa 
def askNums():
    askAgain = True
    while askAgain:
        askAgain = False
        response = input("Escriba el rango de números de la siguiente manera \"num1 , num2\": ")
        if stop(response):
            break
        if response == "rev":
            askAgain = True
    return response


# Comienza interfaz de usuario
print("""
\t\t\tisPrime Cheker\n
El programa consta de los siguientes comandos.\n

rev = le permite escribir de nuevo un número
Stop = le permite terminar el programa en cualquier momento

\n\nSeleccione un range de números para evaluar si existe algún número primo o un número primo(presione enter)
""")


# Detiene el programa si se da la orden, y transforma los valores para ser evaluados por la función isPrime
a = askNums()
print(a)
if a == "Stop":
    pass
else:
    a = a.split()
    print(a)
    for index, i in enumerate(a):
        if i == ",":
            del a[index]
        elif i.isspace():
            del a[index]
        elif i.isalpha():
            del a[index]
        else:
            print(a)
            print(isPrime(int(a[0]),int(a[2])))

print((int(a[0]),int(a[1])))
print("finish program")
print(isPrime(0, 10))









#Useless functions...at this moment...


#def evaluate(a):
#    while True:
#        try:
#            if stop(a):
#                break
#            else:
#                return (int(a))
#        except:
##            a = input(("No escribió un número. Intente de nuevo en 5 segundos o escriba Stop: "))
 #           if stop(a):
 ####               break
    #        else:
    #            for i in range(3):
    #                time.sleep(1)
    #                print("...")
    #            continue
    


#for i in range(a, b):
 #   if isPrime(i):
  #     print(i, end=" ")
