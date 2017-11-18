# Use the file name mbox-short.txt as the filename
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
    	pos = line.find('0')
    	num = float(line[pos:])
    	count += 1
    	total = total + num
average = total / count
print('Average spam confidence:', average)
