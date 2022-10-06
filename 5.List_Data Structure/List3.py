lst = [1,2,3,4,5]
abc = lst # multiple references as abc will also point to lst and any change made with abc will result in change of lst
            # we can see it as another name for lst
abc.append(6)
print(lst)

#splitting the string list

s = "one,two,three,four,five"
# slst =s.split(',')  # using split function to split through the string list
slst =s.split('o')
print(slst)

s="ghoor kyu rahe ho"
slst=s.split('o') # since we have passed no input it will split according to the spaces in between them
print(slst)

num=[10,20,30,40,50,60]
print(num[:]) # it will print the whole list
print(num[::2]) # syntax - [start:end:step-size]
print(num[1::2]) # Here starting index is given 1 and step size is 2 where as end is not given show it will go through the whole list

# We can also add two list using + sign
print(lst + num)

# To count the frequency of the numbers in the list/sequence we use count() function
dup=[1,2,2,2,1,1,3,3]
# Frequency of 1 -
print(dup.count(1))

'''Without List Comphrehension'''
squares = []
for i in range(10):
    squares.append(i**2) # ** - to the power
print(squares)

'''With List Comphrehension'''
squares1=[i**3 for i in range(10)] # with the help of list comphrehension we can write above code in single line
print(squares1)

lst1 = [i**2 for i in lst]
print(lst1)

coord=[(i,2*i) for i in range(10)]
print(coord)