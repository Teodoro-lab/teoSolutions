from os import strerror
letras = {}
try:
    arch = input("ingrese el nombre de su archivo: ")
    openArch = open(arch + ".txt", "rt", encoding = "utf-8")
    
    for i in openArch.read():
        helper = i
        if helper.isupper():
            helper = chr(ord(helper)+ 32)
        if helper in letras:
            letras[helper] = letras[helper] + 1
        else:
            letras[helper] = 1
            
    for keys in letras.keys():
        print(keys, "->", letras[keys] )
        
    openArch.close()
    
except IOError as e:
    print(strerror(e.errno))
        
