# Identity Operators - is & is not operators check whether values or variables located on the same part of the memory.These
# Operators check with respective to the address given by the memory.

x1=10;x2=10
print('x1 address =',id(x1))
print('x2 address =',id(10))
print(x1 is x2) # is operator is true if both operands are identical or refer to a same object

str1='Hello';str2='hello'
print(str1 is not str2) # is not - is true when both operands are not identical

# Membership Operators - in becomes true if value/variable is found in sequence
# not in - true if variable not found in the sequence

st='Goodevening'
l=[1,'python',9.0]
dic={1:1.1,2:2.0}
print('o' in st)
print('python' in l)
print(1 in dic)
print(1.1 in dic)