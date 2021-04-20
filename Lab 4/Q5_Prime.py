num = int(input('Enter the number: '))
prime = True
for i in range(2,int(num**0.5)+1):
    if(num%i==0): 
        prime = False
        break
print(num,'is Prime') if prime else print(num,'is Not Prime')