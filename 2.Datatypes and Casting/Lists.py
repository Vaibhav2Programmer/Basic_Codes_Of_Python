# List is an ordered sequence of items. All items in a list can be of different datatypes and we can also extract a item/multiple
# items using slicing and index starts from 0 to n-1.

list1 = [5,'apple',10,15,20,'elephant',25.0] # have all kind sof datatypes

print(list1[5])
print(list1[0:]) # Slicing - extracting values from index 0 upto last index.
print(list1[1],list1[5])

list1[1]=30 # replacing/altering index 1 value 'apple' to 30
list1[5]=40 # replacing/altering index 5 value 'elephant' to 40

print(list1)


