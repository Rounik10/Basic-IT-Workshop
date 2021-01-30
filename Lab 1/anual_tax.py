sal = int(input('Enter the anual salary'))
if sal < 150000: per = 'No Tax'
elif sal >150000 and sal <=300000: per = 10
elif sal >300000 and sal <=500000: per = 20
else: per = 30
if per == 'No Tax': print(per)
else: print('Tax on Rs',sal,'/- will be',per,'%, that is Rs',per*sal/100)