# Modules -  Module is a file containing python files and definitions.
# We already many no. of modules built in python which we can use using import function.

import math
print(math.pi) # Printing pi value using math module

import datetime
print(datetime.datetime.now()) # It gives date as well as the year and current time

''' we can also import function and give them another reference so it will be easy for to write everytime we call them '''

import math as m
print(m.pi) # Here we referenced matrh as m so everytime we use math function insted of writing math we will write it as m

''' We can also import only a certain section from a module '''

from datetime import datetime
print(datetime.now())

''' To import everything from the module'''
# from math import *

''' To know every attributes of module we use dir '''
print(dir(math))
