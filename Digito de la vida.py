digit_life = input("Dinos tu fecha de cumpleaños(AAAAMMDD: Todo junto) y recibe tu \"Dígito de la Vida\":" )
suma = 0
while len(digit_life) != 1:
    for num in digit_life:
        suma += int(num)
    digit_life = str(suma)
    suma = 0
print(digit_life)
