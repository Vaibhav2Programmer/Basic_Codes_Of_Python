
print('hello'.upper()) # it will convert into uppercase

print('AGAIN'.lower()) # it will convert into lowercase

print("Welcome to the House".split()) # if no argument is given it will split according to the whitespaces otherwise according to the
# argument given and will return it into the list form.

print(' '.join(['This','is','Awesome'])) # it will the join the strings and according to the argument in this example we provided the spaces
print('*'.join(['This','is','Awesome']))
print('1'.join(['This','is','Awesome']))

print("hello".find('li')) # find function will help us to find the characters in the string and will return the index at which they present
# if not prsent will return -1.

print("Mumbai Kings".replace('Kings','Indians')) # it will create a new string in which required result would be provided

s1 = "Chennai Giants"
s2 = s1.replace('Giants','Super Kings')
print(s1)
print(s2)

''' We know that strings are immutable thats why we created another to hold the result'''
print(id(s1))
print(id(s2))