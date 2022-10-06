# Array() - creates an array from an list or tuple

import numpy as np


a = np.array([1,2,3,4]) # Here list is Given output as an array
print(a)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

''' arrange() - creates an array of evenly spaced values and to do that we need to import matplotlib '''
import matplotlib.pyplot as plt
b = np.arange(1,10) # Here we can also give step size to the function as wellas the datatype
print(b)

c = np.arange(1,10,2)
print(c)

d = np.arange(5,dtype='complex') # Here it will return the array in the complex datatype
print(d)

