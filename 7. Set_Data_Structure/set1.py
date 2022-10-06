# Set consist of an unordered collection of items
# It does not allow Duplicates every element is unique
# But it is mutable

'''Set does not support indexing as it is unordered'''

s = {1,2,3}
print(s)
print(type(s))

'''Set does not allow duplicate elements'''
s = {1,2,3,3,2}
print(s)

'''Empty Set'''
s = set()
print(s)

'''Set From a List'''
s = set([1,2,1,4,7,7,3,4])
print(s)

'''add element and multiple elements'''
s.add(5) # add takes only one argument/element to add multiple we use update
print(s)

s.update([6,8,7])
print(s)

'''adding list and set - but these will add as an individual elements not as the list or set as we pass as the argument.'''
s.update([9,10],{11,12})
print(s)

'''remove an element and discard'''
(s.remove(10))
(s.discard(11))
print(s)

# Discard and remove does the same thing that it removes the element but if we use remove and that element is not prsent
# in the set it will throw an error where as in case of discard it does not throw an error

'''Using pop function - it will remove an random element'''
s.pop() # 1 is removed
print(s)
s.pop()
print(s) # 2 is removed

'''clear function - will clear all the items from the set and set will be an empty set'''
s.clear()
print(s)