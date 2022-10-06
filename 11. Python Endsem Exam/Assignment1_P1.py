# Python Program to arithmetic Operations

a = float(input("Enter a number:" ))
b = float(input("Enter a number:"))
c = str(input('Enter a Sign to do arithmetic Operation: '))
output  = 0
if c=='+':
    output = a+b
elif c=='-':
    output=a-b
elif c=='*':
    output=a*b
elif c=='/':
    if b==0:
        print('Cannot divide by zero')
    else:
        output=a/b

print(output)