from random import randint

print("A continuación escriba <+> o <-> para indicar el rango del numero a adivinar")
range = [1,100]

numberNotFound = True
while numberNotFound:
        if range[0] == range[1]:
                print("Your number is", range[0])
                break
                
        guess = randint(range[0], range[1])
        response = input(f"Your number is...{guess}?").strip()
        if response == "+":
                range[0] = guess + 1
                print("Ahora el rango de busqueda es ", range)
        elif response == "-":
                range[1] = guess - 1
                print("Ahora el rango de busqueda es ", range)
        else:
                print("Your number is", guess)
                break
        



