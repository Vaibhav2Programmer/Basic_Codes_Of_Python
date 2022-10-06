'''Frozen sets'''

set1 = frozenset([1,2,3,4]) # this is a frozenset now
set2 = frozenset([4,4,5,6]) # this is how we can make a frozenset
print(set2)

'''Does not support indexing'''

print(set1 | set2) # Union
print(set1 & set2) # Intersection

print(set1 ^ set2) # Symmetric Difference