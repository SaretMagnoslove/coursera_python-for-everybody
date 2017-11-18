score = input("Enter Score: ")
try:
    s = float(score)
except:
    grade = 'not a number'
if s >= 0 and s <= 1:
    if s >= 0.9:
        grade = 'A'
    elif s >= 0.8:
        grade = 'B'
    elif s >= 0.7:
        grade = 'C'
    elif s >= 0.6:
        grade = 'D'
    elif s < 0.6:
        grade = 'F'
else:
    print('pls enter a number between 0-1')
    quit()
print(grade)
