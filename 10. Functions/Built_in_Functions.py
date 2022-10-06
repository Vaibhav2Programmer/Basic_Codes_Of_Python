# Built in Functions in the python

'''Absolute functions will return absolute value of an variable'''
num = -100
print(abs(num))

''' all function checks if given data structure(list,tuple etc.) is iterable or not and none,false,zero value shouldn't be present in the sequence
 otherwise it will return (false) as an output. Empty lists,set are always true.'''

lst = [1,2,3,4]
print(all(lst))

t = (1,2,4,8,0)
print(all(t))

''' To know all the functions of an list we use - dir() function '''
num = [1,2,3,4]
print(dir(num))
print(num,id(num))

''' divmod() function will give quotient and remainder as an tuple '''
print(divmod(20,3))

''' enumerate function - here enumerate means listing it will return index with its value
enumerate(number,start=0) here it will start from indexing 0 if we give 5 then index starts from 5'''

numbers = [100,200,300,400,500]
for index,elements in enumerate(numbers):
    print("index {0} contains value {1}".format(index,elements))

''' filter function will help us to filter out the elements '''

def positive_num(num):
    '''We will use this function to get +ve numbers'''
    if num > 0:
        return num

new_lst = range(-15,16)
print(list(new_lst)) # creating a list with the help of list() typecasting and range
# print(new_lst)
result = list(filter(positive_num,new_lst))
print(result)

''' isinstance functions - returns true or false tells if it is prsent or not '''

t = (1,2,5,65)
print(isinstance(t,tuple))

''' Map functions works similarly as filter functions these functions help us to avoid for loop '''

# To create a list with squared numbers-first method

numbers = [1,2,3,4,5,6]
numbers1 = [7,8,9,10]
squared = []
for i in numbers:
    squared.append(i**2)
print(squared)

# 2nd Second with the help of list comphrehension
squared1 = [i**2 for i in numbers]
print(squared1)

# With the use of map function -  map(function,iterable)

def double(num):
    '''Squares of the input'''
    return num**2;

squares = list(map(double,numbers))
print(squares)

''' reduce function '''

# without reduce function - product of an list

product = 1
for i in numbers:
    product *= i
print(product)

''' With reduce function '''
from functools import reduce
def multiply(x,y):
    return x*y

product1 = reduce(multiply,numbers) # It does rolling computation
print(product1)