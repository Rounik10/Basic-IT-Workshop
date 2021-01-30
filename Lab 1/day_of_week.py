n = int(input('Enter the day number: '))
d = {1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
print('Day number',n,'is',d.get(n))