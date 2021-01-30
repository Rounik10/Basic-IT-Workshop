print('For an equatin: a*x^2 + b*x + c = 0')

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = b*b - 4*a*c
x1 = (-b + (d**0.5))/(2*a)
x2 = (-b - (d**0.5))/(2*a)
print('First Root is:',x1,'\nSecond Root is:',x2,2)