a = float(input('Enter length of the first side: '))
b = float(input('Enter length of the second side: '))
c = float(input('Enter length of the third side: '))
s = a+b+c/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('Area is: {:0.2f}'.format(area))