word1 = (input("Ingresa la palabra a comprobar: ")).upper()
word2 = (input("Ingresa la palabra a comprobar: ")).upper()
wordaux1 = ""
wordaux2 = ""
for letter, letter2 in zip(word1,word2):
    if letter.isspace == True:
        continue
    else:
        wordaux1 += letter
    if letter2.isspace == True:
        continue
    else:
        wordaux2 += letter2
        
if sorted(wordaux1) == sorted(wordaux2):
    print("Anagramas")
else:
    print("No son Anagramas")
