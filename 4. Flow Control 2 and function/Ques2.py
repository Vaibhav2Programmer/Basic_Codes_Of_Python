#2. Program to check if a number is prime or not

num=int(input("Enter a Number:"))
'''i=1;count=0


while i <= num:
    if num%i==0:
        count+=1
    i+=1

if count > 2:
    print('It is Not a Prime Number')
else:
    print('It is a Prime Number')

if num==1:
    print('It is a Prime Number')

else:
    print('It May be a Negative Integer or a Floating Value and We Dont do that here') '''

# Method 2

if num>1:

    for i in range(2,num):
        if(num % i == 0):
            print(num,"is not a prime Number")

