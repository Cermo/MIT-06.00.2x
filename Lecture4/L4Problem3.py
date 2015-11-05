#L = ['a', 'z', 'p']
L = ['apples', 'oranges', 'kiwis', 'pineapples']

def stdDev(X):
	lengths = []
	for x in X:
		lengths.append(len(x))
	mean = sum(lengths)/float(len(lengths))
	tot = 0.0
	for x in lengths:
		tot += (x - mean)**2
	return (tot/len(lengths))**0.5

print stdDev(L)
