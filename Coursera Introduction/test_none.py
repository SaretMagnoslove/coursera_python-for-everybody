smallest = None
for ii in [4, 5, 6, 7, 8, 8, 10]:
    if smallest is None:
        smallest = ii
    if ii < smallest:
        smallest = ii
print('the smallest number is',smallest)
