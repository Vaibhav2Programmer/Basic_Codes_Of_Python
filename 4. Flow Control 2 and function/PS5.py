# Program to find the factorial  of a given number using for loop

num=int(input("Enter a Number: "))
fact=1

for i in range(1,num+1):
    fact *= i;
print("The Factorial of given {} is {}".format(num,fact))