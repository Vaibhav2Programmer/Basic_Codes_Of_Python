#Literal Collections have 4 literals namely list, dicitionary, tuple, set

fruits = ["Orange","Pineaapple","Guava","Guava"] #list - allows multiple values and we get order as we passed

numbers = (1,2,3,3,2) #tuple - also allows multiple values and the we get order as we passed

alphabets = {'a':'avacado','b':'ball','c':'cat'} #dictionary - contains key-value pair where key should be unique whereas value can have
# duplicate values and when value have dupliacte values dictionary overwites/assigns the new value to the key.

vowels = {'a','e','i','o','u'} # set - does not allow duplicate values. when we print set we always get values in random order not the sequence
# we have given to the set and when duplicate values are exist it prints it a single time.

print(fruits);print(numbers);print(alphabets);print(vowels)

vowels1 = {'a','e','i','o','o'} # set with duplicate values
print(vowels1)

alphabets1 = {'a':'avacado','b':'ball','c':'cat','a':'avacado'} #dictionary
print(alphabets1) # we get avacado as key is unique value

alphabets1 = {'a':'avacado','b':'ball','c':'cat','a':'evergreen'}
print(alphabets1)  # printed the latest assigned value