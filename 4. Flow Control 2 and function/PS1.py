# 1. Program to print a table of a given number using a for loop

num=int(input('Enter a number to print the table:'))
print('Table of {} is:'.format(num))

for i in range(1,11): # Here i will iterate from 1 to 10 , 11 will be exclusive
    print('{} * {} ='.format(num,i),num*i)

# Another ways to use the print function

''' 1. Using string concatenation

    print(str(num) + "X" + str(i) + "=" + str(num*i))
Converting variables into a string for concatenation property using typecasting

    2. Using f string
    
    print(f "{num} X {i} = {num*i}")
    
    Just write f before the quotes and variables in curly braces.
'''