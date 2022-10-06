# We create a function using def

def Name_Output(name):  # This is the definition of function here our function name is Name_Output and we are passing an parameter as a name
    '''This function print the name which has been passed and hello'''
    print('Hello'+ str(name))

Name_Output(" Vaibhav") # Calling of a Function where we passes 'Vaibhav' string as an input to the function

''' To print the docstring of a function we use (function_name.__doc__) attribute '''
# print(Name_Output.__doc__)

def sum(a):
    ''' This Function will return the sum of the list/any value passed with function '''
    sum = 0
    for elements in a:
       sum = sum + elements
    return sum

ans = sum({2,4,6,8,10}) # Calling of an sum Function
print(ans)
