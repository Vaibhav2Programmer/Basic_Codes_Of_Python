# Tuple is not mutable,i.e. elements cannot be changed/replaced with another elements as we did in the lists.
# Tuple once created cannnot be modified.

tup = (1,2,3,5,'python',1+7j)
print(tup)

# tup[3]=4 - tuple does not support item assignment

print(tup[4:6]) ; print(tup[3:]) #multiple statements in a single line
# Here index 6 is exclusive as in any range we write