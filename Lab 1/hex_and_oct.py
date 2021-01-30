num = int(input('Enter a number: '))
h = o = ''
d = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
# for hexadecimal
t1=num
while(t1>0):
    temp = t1 % 16 
    if(temp > 9): temp = d.get(temp%10)
    h =str(temp) + h
    t1 = int(t1/16)

print('hex of',num,'is',h)
# for octal
t2 = num
while(t2>0):
    temp = t2 % 8
    o = str(temp) + o
    t2 = int(t2/10)

print('oct of',num,'is',o)