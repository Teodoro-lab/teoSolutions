N, K = int(input()), int(input())
boxes = []

boxes = list(map(int, list(input())))

A, B = int(input()), int(input())

def sub_lists (l): 
    base = []   
    lists = [base] 
    for i in range(len(l)): 
        orig = lists[:] 
        new = l[i] 
        for j in range(len(lists)): 
            lists[j] = lists[j] + [new] 
        lists = orig + lists  
    return lists
 
subBoxes = sub_lists(boxes)

counter = 0
for i in subBoxes:
    if len(i) > K:
        continue
    elif len(i) < K:
        continue
    else:
        sumatoria = sum(i)
        if sumatoria >= A and sumatoria <= B:
            counter += 1
print (counter)

