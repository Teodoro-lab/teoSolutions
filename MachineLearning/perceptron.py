import random

input1 = [.2, 4]
input2 = [.8, 2]
bias = .1

result = 1
expected = 2


while (result - expected) > 0.1 or (result - expected) < -.1:
    result = input1[1] * input1[0] +  input2[1] * input2[0] + bias
    print(result)
    input1[0] = random.uniform(.01, 1)
    input2[0] = 1 - input1[0]

print("El resultado aproximado fue de ",result)
