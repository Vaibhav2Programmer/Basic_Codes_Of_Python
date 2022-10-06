""" Integers,float and comples fall under python numbers defined as int, float and complex classes.
 To know that a variable/value belongs to which class we use type() function.
 we know that in python everything is treated as an object, therefore datatypes are actually classes and variables are instance(object) of these classes
 and to check if an variable belongs to that class we use isinstance() function."""

a=10.0
print(a,"has a type of",type(a))
print(isinstance(a,float))

b=1+3j
print(isinstance(b,complex),"b is a complex number")