import re
handle = open('test.txt')
total = 0
for line in handle:
    numbers = re.findall('[0-9]+', line)
    if numbers is None:
        continue
    else:
        for number in numbers:
            total += int(number)
print(total)