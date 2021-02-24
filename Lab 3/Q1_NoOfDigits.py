num = int(input("Enter the number: "))
temp = num
count = 0
while(temp>0):
    temp//=10
    count+=1
print('Number of digts in',num,'is',count)