name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    if line.startswith('From '):
        line = line.split()
        line = line[5].split(':')
        hour = line[0]
        count[hour] = count.get(hour,0)+1
lst = list()
lst = sorted([ (k,v) for k,v in count.items()])
print(lst)
        
            
