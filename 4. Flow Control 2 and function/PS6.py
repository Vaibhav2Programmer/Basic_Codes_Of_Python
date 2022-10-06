# Program to print the table in reverse order

num=int(input("Enter a number: "))

var=0
L1=list()
for i in range (1,11):
        var=num*i
        L1.append(var)
L1.reverse()
print(L1)