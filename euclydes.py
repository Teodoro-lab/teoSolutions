def  euclydes(a:int, b:int) -> 'MCD':
    if b == 0:
        return a
    return euclydes(b, a%b)


#def bezout(a:int,b:int):
 #   mcm = euclydes(a, b)

def expand10( n:str ):
    exp = len(n) -1
    if exp == 0:
        return f"({n} ^ {10 * exp})"
    return f"({n[0]} ^ {10 * exp})" + " + " + expand(n[1:], exp-1)
    
def expand( n:str, base:int ):
    exp = len(n) - 1
    if exp == 0:
        return f"({n} ^ {base * exp})"
    return f"({n[0]} ^ {base * exp})" + " + " + expand(n[1:], exp-1)


arr = [1, 2, 3, 4]
arr_id = id(arr)
arr2 = arr[0]
arr2_id = id(arr2)

##print(arr_id)
#print(arr2_id)


operators = "+-*"
string = []
counter = 0
index = 0
var = 4
for i in range(var):
    for j in range(var):
        for k in range(var):
            for number in arr:
                eval(f"{arr[index]}  {arr[index + 1]}")
                string.append(f"{operators[i]}   {operators[j]}   {operators[k]}")

[print(i) for i in string]
print("counter", counter)
