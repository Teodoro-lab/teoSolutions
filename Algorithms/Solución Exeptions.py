def readint(prompt, minimo, maximo):
    while True:
        try:
            prompt = int(input("Ingresa un número entero: "))
        except ValueError:
            print ("Error: entrada incorrecta")
            continue
        if prompt > maximo or prompt < minimo:
            try:
                raise IndexError
            except IndexError:
                print ("Error: el valor no está dentro del rango permitido (min..max)")
                continue
        break
    return prompt

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
print("El numero es:", v)


##################################################################
#######--------------PYTHON SOLUTION------------------#######################
##################################################################

def readint(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return value;

v = readint("Ingresa un número entre -10 a 10: ", -10, 10)

print("El numero es:", v)


##################################################################
#######----------MIO PERO MAS BONITO------------------#######################
##################################################################


def readint(prompt, minimo, maximo):
    while True:
        try:
            prompt = int(input("Ingresa un número entero: "))
        except ValueError:
            print ("Error: entrada incorrecta")
            continue
        try:
            if prompt > maximo or prompt < minimo:
                raise IndexError
        except IndexError:
            print ("Error: el valor no está dentro del rango permitido (min..max)")
            continue
        break
    return prompt

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)
print("El numero es:", v)

