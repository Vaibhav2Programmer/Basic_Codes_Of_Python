#empty dictionary

emp = {}
a = dict() # we can create an empty dictionary using an dict function

dic1 = {1:'abc',2:'xyz'}
print(dic1)

dic1 = {'name':'dictionary','Surname':['Key',42]}
print(dic1)
print(dic1['Surname']) # Accessing keys

'''We can create a dictionary with list of tuples'''
dic2 = dict([(1,'abc'),(2,'xyz')])
print(dic2)

'''Another way of accessing key is get function - bcoz even if key is not there it will not give key error '''
print(dic1.get('name'))

''' Update a Key '''
dic1['name'] = 'Vaibhav'
print(dic1)

''' Adding a Key '''
dic1['address'] = 'khurai' # it will add this address key at the end
print(dic1)

''' Removing a Key - we use pop '''
dic1.pop('name') # if we print this it will return the key value
print(dic1)

''' Removing an arbitrary key - we use popitem function'''
dic3 = {1:'abc',2:'xyz',3:78}
print(dic3.popitem())
print(dic3)

''' we can also use del to delete a particular key '''
del dic3[2]
print(dic3)

''' To remove all items from a dictionary or to delete it we use 2 functions - 1. clear() and del'''
dic3.clear()
print(dic3) # When we cleared all items from an dictionary it still gave us an empty dic3 dictionary

del dic2
print(dic2) # Here it completely deleted dic2 dictionary therefore it gives an error - this is the main difference between clear() and del method