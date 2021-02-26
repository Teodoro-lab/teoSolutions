coeficientes = int(input("Ingrese el numero de coeficientes: "))
pascal = []

for i in range(coeficientes + 1):
    coef = 1
    for j in range(i + 1):
        pascal.append(coef)
        coef *= (i-j)/(j+1)

[print(int(i)) for i in pascal]
