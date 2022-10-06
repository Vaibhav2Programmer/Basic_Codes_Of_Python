t = () # empty tuple

t =  (1,2,3) # tuple with integeres
print(t)

t = (1,'infytq',[1,2.0,'TCS']) # tuple with mixed datatypes and an list
print(t)

t = (1,(2,3,4),[1,'infy',2,'tcs']) # nested tuple
print(t)

# When an single element is required to be named as an tuple

t = ('infytq') # an comma is always required to ensure it as an tuple
print(type(t)) # thats why it is showing an string

# to make it to an tuple class put an comma
t = ('infytq',)
print(type(t))

# Accessing tuples - nested

tup = (1,2,3,4)
print(tup[3])

tup1 = ('TCS',('Conducts','Infytq','Every','Year'))
print(tup1[0])
print(tup1[1])
print(tup1[1][0]) # Accessing the 0th index in 1st index as a whole
print(tup1[1][1]) # Accessing the 1st index in the index as a whole

'''Slicing of tuple'''

t = (1,2,3,4,5,6)
print(t[:-2]) # Here -2 means last second element and -1 as the last element as start is not given it will iterate through starting upto -2th element

'''A way to print an tuple/sequence in an reverse order'''

print(t[5:-7:-1])

'''A way to change the tuple with the help of an an list inside'''

t = (1,2,3,4,[5,6,7])
# we know that tuple is immutable but when we nested an list inside it we know that list is mutable and we can change it
t[4][2]='MSD'
print(t)

'''Concat Tuple'''
t = tup + tup1
print(t)

'''Delete an tuple'''
del t # - delete an entire tuple
# tuple does not support item deletion like an list

'''Count the frequency'''
t = (1,1,2,3,4,1,2,3,4,4)
print(t.count(1))

'''Sorting an tupple '''
t = (9,7,1,3,2)
sorted_tuple = sorted(t) # Here it will create a list bcoz we know tuple are immutable therefore we getan sorted tuple as an list
print(sorted_tuple)