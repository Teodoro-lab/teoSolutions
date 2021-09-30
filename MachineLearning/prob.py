import numpy as np

def ecdf(n):
	x = np.sort(n, ascending=False)
	length = len(n)
	y = 1/np.arange(1, length+1)
	return x, y

def bernoully(n, p):
	count = 0
	for i in range(p):
		trial = np.random.rand()
		if trial <= n:
			count += 1
	return count

distribution = []
for i in range(100_000):
	distribution.append(bernoully(.5, 100))

from matplotlib import pyplot as plt
# print(help(plt.hist))

x, y = ecdf(distribution)
plt.plot(x, y, marker='.', linestyle='none')
plt.show()
# plt.hist(distribution, bins= int(np.sqrt(1_000_000)))
# plt.show()

