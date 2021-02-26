def bit_count (s):
    s = s.split()
    equip = 0
    a = int(s[0])
    b = int(s[1])
    x = int(s[2])
    for num in range(a, b + 1):
        counter = 0
        var = num
        while var != 1:
            binario = bin(var)
            var = binario.count("1")
            counter += 1
        if equip > x:
            continue
        elif counter == x:
            equip += 1
    return equip


print(bit_count("27 31 2"))
