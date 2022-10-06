''' Set Operations '''

''' Union Operations '''

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 | set2) # it means union of set 1 and set 2

print(set1.union((set2))) # another way of union

''' Intersection Operations - Common between those two sets'''

print(set1 & set2)
print(set1.intersection(set2))

print(set1-set2) # Difference between two sets

''' Symmetric Difference - (union)-(intersection) '''
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

''' To check if a set is Subset or not we use - issubset function '''
set3={3,4,5}

print("Is set1 subset of set3:",set1.issubset(set3))
print("Is set3 subset of set1:",set3.issubset(set1))