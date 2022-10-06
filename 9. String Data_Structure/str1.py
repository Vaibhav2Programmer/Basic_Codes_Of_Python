# string is sequence of characters, it supports indexing but it is immutable/cannot be changed.

st = "hello_Adele"
print(st[:])
print(st[-1::-1]) # To reverse the order

''' delete a string '''
del st
# print(st)

s1="hello "
s2="again"

''' Concatenation of strings '''
print(s1 + s2)

# print a string n number of times
print(s1 * 4)

count=0

for i in s1 + s2:
    if i == 'a':
        count+=1
print("No. of times a prsent:",count)