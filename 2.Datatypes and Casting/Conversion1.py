# We can convert using functions like int(),float(), str() etc.
# conversion to float from int will truncate the value

a=int(10.6)
b=int(-10.6)
d=float(2)
print(a,b,d)

# To convert into a string it should be compatible with the types
c=float('2.5')
print(c)

# We can convert list,set etc into each other.

e=list({1,'python','eggless',7.9}) # conversion of set into a list
print(e)

# But to convert in an dictionary each element should be a pair

