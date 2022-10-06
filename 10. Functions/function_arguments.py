# Function arguments - consists of 3 types - 1. Default 2. Keyword 3. Arbitrary arguments

''' Default argument - where we make an argument default one, if user provides arguments then it gets printed (user one), otherwise
default argument gets printed so that there is no 1 missing parameter error.'''

def default(name,msg = "Love Charger"):
    ''' It is a default argument & we are trying to make last argument as default one '''
    print("Hello {0},{1}".format(name,msg))

default("Ankur","AFK") # Here we passed both the parameters so default one not gets printed
default("KG") # Calling of an function with one parameter, so here default parameter gets printed

''' Keyword arguments - are used when variable length of arguments is given to the function.
It is like dictionary, works on the basis of passing the key and getting corresponding value.'''

def keyword(**kwargs): # It is defined as **kwargs - keyword arguments

    print("Hello {0},{1}".format(kwargs['name'],kwargs['msg']))

''' Here we are passing name and msg as the keys to the function to get the corresponding values. '''

keyword(name='Ankur',msg='Love Charger') # Here we are passing values to the keys name and msg

''' Arbitrary arguments - any no. of arguments can be passed to the function '''

def arbitrary(*parameters):
    ''' We can write any other function name other then arbitrary also'''

    print(parameters)

    for input in parameters:
        print("Hello,{0}".format(input))

arbitrary('GFG','TB','KG') # Calling of an function and passing 3 Parameters