cadena = str(input("Ingrese un cadena de texto para encriptar: "))
while True:
    try:
        valor_deCambio = int(input("Ingrese un valor de cambio entre el 1 al 25: "))
        if valor_deCambio > 25 or valor_deCambio < 1:
            raise ValueError
    except ValueError:
        print ("Su valor es erroneo")
        continue
    break
encription = ""
move = 0
for char in cadena:
    if char.isdigit():
        encription += char
        continue
    elif char.isspace():
        encription += char
        continue
    else:
        if char.isupper():
            if ord(char) + valor_deCambio > ord("Z"):
                move = (ord("A")-1) + ((ord(char) + valor_deCambio) - ord("Z"))
            else: move = ord(char) + valor_deCambio
        else:
            if ord(char) + valor_deCambio > ord("z"):
                move = (ord("a")-1) + (ord(char) + valor_deCambio) - ord("z")
            else: move = ord(char) + valor_deCambio
    encription += chr(move)
print (encription)
##################################################################################
finish = True
while finish == True:
    finish = input("Si quiere que termine el prorama ingrese \"Stop\"")
    if finish == "Stop":
        break
    else: finish = True

