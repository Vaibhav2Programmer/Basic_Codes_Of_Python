# Program to print the multiplication table with while loop

num=int(input("Enter a number:"))
i=1

while i <= 10:
    print(str(num) + "*" + str(i) + "=" + str(num*i))
#
    i+=1