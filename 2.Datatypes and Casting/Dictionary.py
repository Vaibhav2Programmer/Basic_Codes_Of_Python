# Dictionary is an ordered collection of key-Value Pairs, also changeables but does not allow duplicate values instead overwrites existing values.
# Used for huge amount of data and to retrieve data.
# Always, key is Passed to access the value and it is not other way around.
# key and Value can be of any data-types

dic = {1:'a',2:'b'}
print(dic)
print(dic[2])

# print(dic['a']) - generates error as there is no key named 'a'

dic[1]='c'# Always Pass the key to retrieve the value
print(dic)
# Now the value of key 1 has been updated to 'c' from 'a'
# Therefore it is mutable

thisdic = {"Brand":"Ford","Model":"Mustang","Year":2022, 'Year':1964}
print(thisdic['Brand'])
print(thisdic) # Here interpretor overwrites the value of year.