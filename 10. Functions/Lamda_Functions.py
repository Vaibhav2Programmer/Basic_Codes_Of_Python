# Lambda function are also known as Anonymous functions
# We use lambda functions using lamda keyword

''' Normal Function with same use '''

def double(x):
    return x*2;
print(double(10))

''' Same use of program with the help of lambda where we dont have to use the function '''

double = lambda x: x*2 # Here, x is argument and x*2 is the expression and double is the lamda function name
print(double(12))

''' Lambda with the map() - In map function we used to pass the function name and the iterable sequence like tuple,list
but here we will use lambda function '''

lst = [2,4,6,8,10]
ans_lst = list(map(lambda x: x**2,lst))
print(ans_lst)

''' Lambda with filter() function - map and filter works on the same syntax but with filter we use when need to filter the elements
and with map function we perform different operations on the sequence,list'''

lst = [1,2,3,4,5,6]
ans = list(filter(lambda x: x % 2 != 0,lst))
print(ans)

''' Lambda function with the reduce '''
from functools import reduce
lst1 = [2,5,1,2,]

product = (reduce(lambda x,y:x**y,lst1)) # We dont need to make it an list since it does rolling computation and giving us an product
print(product)
