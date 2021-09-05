set = ['a', ['b', 'c']]
aux = []
leng = len(set)
subsets = []
count = {}

def subset(index:int):
	global set, leng, subsets, count
	if index == leng:
		print(aux)
		subsets.append(aux)
		try:
			count[len(aux)] += 1
		except:
			count[len(aux)] = 1
	else:
		aux.append(set[index])
		subset(index + 1)
		aux.pop()
		subset(index + 1)
		
subset(0)
print(len(subsets))
print(count)
# print(len([i for i in subsets if len(i) == 3]))
b = {1, 2, 3} 
a = {'a','b'}
# print((a.union(b)).difference(a))

from itertools import product
print(len(list(product(a, a.union(b)))))