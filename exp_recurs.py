def exp_rec(num, potencia):
    if potencia == 1:
        return num*potencia
    return num*exp_rec(num, potencia - 1)

def exp_for(num, potencia):
    result = 1
    for i in range(potencia):
        result *= num
    return result

print(exp_rec(4,-2))
print(exp_for(4,-2))
