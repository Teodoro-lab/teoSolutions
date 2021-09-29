word = input("Escriba la palabra para analizar: ")
new_word = ""
for chra in word:
    if chra.isspace() == True:
        continue
    else:
        new_word += chra
        
chain_rv = ""
for i in range(1, len(word) + 1):
    compi = word[-i] 
    if compi.isspace() == True:
        continue
    else:
        chain_rv += compi.upper()
if chain_rv == new_word.upper():
    print (word,"es un palíndromo")
else:    
    print (word,"no es un palíndromo")

    
    
