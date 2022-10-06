# 1. Program to find sum of all numbers

numbers = [9,6,7,5,4,3,2,1,8]
sum=i=0

for x in numbers:  # iterating/traversing over the list
    sum=sum+x
    print(numbers[i]) # printing each elements of numbers sequence list
    i+=1
print('Sum of all the numbers:',sum)

'''Range Function - range(start,stop,step_size)'''
'''By default step_size is 1'''

print(range(10))
print(list(range(0,10))) # Here 10 is exlusive that is stop is not included in

'''len function in range help us to iterate using indexing'''
alphabets = ['a','b','c','d','e']

for i in len(alphabets):
    print(alphabets[i])

print(alphabets)

''' for loop with else
break keyword can be used to stop a for loop or any other sequence. But else part will get ignored.'''

digits = [0,2,4,5,6]

for i in digits:
    print(i)
else:
    print('No more digits left')