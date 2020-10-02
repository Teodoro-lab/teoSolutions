def misplit(strng):
    cad = ""
    arr = []
    strng = strng + " "
    for i in strng:
        if i != " ":
            cad += i
        else:
            arr.append(cad)
            cad = ""
    while " " in arr or "" in arr:
        if " " in arr:
            del(arr[arr.index(" ")])    
        if "" in arr:
            del(arr[arr.index("")])
        else:
            break
    return arr

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))



