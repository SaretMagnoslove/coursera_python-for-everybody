fname = input('enter file name: ')
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word is not lst:
			lst.append(word)
lst.sort()
print(lst)
