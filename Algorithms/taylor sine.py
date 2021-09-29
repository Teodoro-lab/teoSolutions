# Represent the Taylor expansion series of sin(x)
# Sin(x)= x - (x**3)/3! + (x**5)/5! + (x**7)/7! ...
import math as m

def factorials(n):
    solution = n
    n = n
    for i in range(n - 1, 1, -1):
        solution *= i
    return solution


def factorials_2(n):
    if n == 1:
        return 1
    return n * factorials_2(n - 1)


def calc_sin(angle, iter):  #This work
    sinx = angle - (angle ** 3)/factorials_2(3)
    increment = 5
    for i in range(iter - 1):
        sinx += (angle ** increment)/factorials_2(increment)
        increment += 2
    return sinx

a = m.pi/2
print(calc_sin(a,60))
print(m.sin(a))
print(factorials_2(5))

