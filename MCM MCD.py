def MCD(a, b):
    primo = 2
    arr = []
    while a % primo == 0 and b % primo == 0:
        while a % primo == 0:
            a //= primo
            arr.append(primo)
        else: primo += 1
        while b % primo == primo:
            b //= primo
            arr.append()
        else: primo += 1

def MCM(a, b):
    primo1 = 2
    primo2= 2
    mcm = 1
    while a != 0:
        if a % primo1 == 0:
            a //= primo1
            mcm *= primo1
        else: primo1 += 1
    while b != 0:
        if b % primo2 == 0:
            b //= primo2
            mcm *= primo2
        else: primo2 += 1
    return mcm

MCM(248, 336)
