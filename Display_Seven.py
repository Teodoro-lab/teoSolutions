################################################################################
##########################-----MY SOLUTION--------############################
################################################################################

prueba1 = 123
prueba2 = 12345

fila1 = ["#", "###", "###", "# #", "###", "###", "###", "###", "###", "###"]
fila2 = ["#", "  #", "  #", "# #", "#  ", "#  ", "  #", "# #", "# #", "# #"]
fila3 = ["#", "###", "###", "###", "###", "###", "  #", "###", "###", "# #"]
fila4 = ["#", "#  ", "  #", "  #", "  #", "# #", "  #", "# #", "  #", "# #"]
fila5 = ["#", "###", "###", "  #", "###", "###", "  #", "###", "###", "###"]

arr = [fila1, fila2, fila3, fila4, fila5]
for filas in arr:
    str_generator = "" 
    for i in str(prueba2):
        str_generator += filas[int(i) - 1] + " "
    print(str_generator)

