def fib(n):
    p1= p2 = 1
    ret = 0
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            ret = p1 + p2
            p1, p2 = p2, ret
            yield ret

v = [x for x in fib(10)]
print (v)

z = list(fib(10))
print(z)


for i in range(10):
    if i in fib(10):
        print("Yes", i)


def potenciasDe2(n):
    potencia= 1
    for i in range(n):
        yield potencia
        potencia*= 2

for i in range(20):
    if i in potenciasDe2(4):
        print(i)



j = [[[0 for x in range(10)]for x in range(10)]for x in range(10)]
print(j)

#o = [0] * 10
#print(o)

f = [0 if x % 2 == 1 else 1 for x in range(10)]
print(f)
