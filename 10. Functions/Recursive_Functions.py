#1. Finding the factorial of an number using recursive function

def factorial(n):
    ''' This function will return the factorial of an input number '''

    if n==1:
        return 1
    else:
        return n * factorial(n-1)

''' We can also write above function in a single line '''

# return 1 if n==1 else return(n*factorial(n-1))

# num=7
print("Factorial of {0} is {1}".format(10,factorial(10)))

#2. Finding the Fibonacci Series using recursive function

def fibonacci(n):
    if n == 0:
        return n
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

'''   if n==0:  Here we will start the range from zero to n thats why when n = 0 we print zero as first element
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2)) '''

n = int(input("Enter Number to print the Series:"))
if n < 0:
    print("enter Positive Number")
else:
    for i in range(n):
        print(fibonacci(i))