def factorials(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

count = 1
e = 1
a = 1
while True:
    e += 1 / factorials(count)
    if a == e:
        break
    else:
        a = e
    count += 1
    print(e)
    
