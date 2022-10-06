# strings is sequence of unicode characters. But are immutable cannot be altered using indexes but slicing property can be used.
import string

s = "A STRING"

print(s[0:8])

'''s[0]='B'
print(s)''' # string does not support item assignment/ immutable in python

print(type(s))
print(isinstance(s,str))

print("s[1:]=",s[2:])