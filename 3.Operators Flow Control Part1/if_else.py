# To check if a number is positive or not
num = float(input('Enter a Number to be checked:')) # Having a input as well as explicit conversion

# num=float(num) # Converting from a str type to a int type

if num > 0:
    print(num,'is a positive no.')
else:
    print(num,'is a negative no.')

''' Nested If else statements '''

if num>=0:
    if num == 0:
        print('It is a Zero')
    else:
        print('Not a Zero')
else:
    print('Negative Number')