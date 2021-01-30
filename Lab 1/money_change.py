amount = int(input('Enter the amount: '))
ten = five = two = one = 0

ten = int(amount/10)
amount = amount%10

five = int(amount/5)
amount = amount%5

two = int(amount/2)
amount = amount%2

one = amount

print(one,'One rupee coins\n', two,'two rupee coins\n', five,'five rupee coins\n', ten,'ten rupee coins')