string = """_______________________________________________
LIS.Nuevo.Ingreso mailing list
LIS.Nuevo.Ingreso@fmat.uady.mx
https://intranet.matematicas.uady.mx/mailman/listinfo/lis.nuevo.ingreso
"""
arr = ""
for caracter in(string):
    arr += ((bin(ord(caracter))).lstrip("0b"))
contador = 0
for caracter in(string): 
    contador += ((bin(ord(caracter))).lstrip("0b")).count("1")
    
print(len(arr))
bytes = len(string)*8
print(bytes)
print(contador)

