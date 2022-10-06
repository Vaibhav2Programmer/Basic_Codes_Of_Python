# Program to find the sum of n natural numbers

n = int(input("Enter a number upto which u want sum:"))
sum=0;i=1

''' for i in range(1,n+1):
    sum+=i '''

# Using while loop

while i <= n:
    sum+=i
    i+=1

print("Sum of {} natural numbers is {}".format(n,sum))