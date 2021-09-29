def encryption(s):
    encrip = ""
    s.replace (" ", "")
    tamaño = len(s)
    raiz = math.ceil(tamaño ** .5)
    if (raiz - 1) * (raiz) >= tamaño:
        mult_1 = raiz -1
        mult_2 = raiz
    else: 
        mult_1 = mult_2 = raiz
    espacios = (mult_1 * mult_2) - tamaño
    s = s + (espacios * " ")
    list (s)
    index = -1
    for i in range(mult_2):
        index += 1
        if index > 0:
            encrip += " "
        for i in range(mult_1):
            if s [index] != " ":
                encrip += s [index]
            index += mult_2
            if i == mult_1 - 1:
                index = index - ((i + 1) * mult_2)
    return encrip
