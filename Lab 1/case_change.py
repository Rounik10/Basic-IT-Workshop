c = input('Enter a character: ')
if c>='a' and c<='z': print('Upper Case will be',chr(ord(c) - 32))
else: print('Lower Case will be: ',chr(ord(c) + 32))