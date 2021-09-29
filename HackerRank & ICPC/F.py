puntos = input()

countLeft = 0
countRight = 0

gamesLeft = 0
gamesRight = 0

sacador = "L"
 
for letra in puntos:
    if letra == "S":
        pass
    elif letra == "R":
        if sacador == "L":
            sacador = "R"
        else:
            sacador = "L"
    else:
        if sacador == "L":
            if gamesLeft == 2:
                print(f"{gamesLeft} (winner) - {gamesRight}")
            else:   
                print(f"{gamesLeft} ({countLeft}*) - {gamesRight} ({countRight})")
        else:
            if gamesRight == 2:
                print(f"{gamesLeft} - {gamesRight} (winner)")
            else:
                print(f"{gamesLeft} ({countLeft}) - {gamesRight} ({countRight}*)")
    if letra == "Q":
        pass
    else:
        if sacador == "L":
            countLeft += 1
        else:
            countRight += 1
        
    # Derecha
    
    if countRight == 10:
        gamesRight +=1
        
        countLeft = 0
        countRight = 0
    else:
        if countRight - countLeft >= 2 and countRight >= 5:
            gamesRight +=1
            
            countLeft = 0
            countRight = 0
        else: pass

    # Izquierda
    
    if countLeft == 10:
        gamesLeft +=1
        
        countLeft = 0
        countRight = 0
        
    else:
        if countLeft - countRight >= 2 and countLeft >= 5:
            gamesLeft +=1
            
            countLeft = 0
            countRight = 0
        else: pass
        





