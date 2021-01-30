year = int(input('Enter the year: '))
leap = False
if year%4==0:
    if year % 100 == 0:
        if year % 400 == 0: leap = True
    else: leap = True
if leap : print(year,'is leap year.')
else: print(year,'is not a leap year.')