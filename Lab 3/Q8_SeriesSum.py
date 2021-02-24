x = int(input('Enter the value of x: '))
n = int(input('Enter the number of terms: '))
s = 0
for i in range(n):
    term = x**(i+1)
    if(i%2==0): s-=term
    else: s+=term
print('Sum of series is:',s)