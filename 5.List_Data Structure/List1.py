lst = [1,'python',4.0,45,56] # List is a ordered collection of items(can be of different datatype) as well as it is mutable
print(len(lst))

sublist = [[1,2],[3,4]] # sublist
print(sublist)

lst_1 = ['one','two','three']
lst_1.append('four') # append will always add an element at the end
print(lst_1)

lst_1.insert(3,'five')  # Insert can add any element at any index position
print(lst_1)            # and from the example the four element shifts to new index position

lst_2 = ['one','two','three']
lst_2.remove('three') # remove can remove any element from the list
print(lst_2)

ls1 = ['one','two']
ls2 = ['three','four']
ls1.append(ls2) # append can also add a list to another list at the end
print(ls1)

ls1=['one','two']
ls1.extend(ls2) # extend will help to add another list at the end but as an elements.
print(ls1)

lst = ['one','two','three','four']
del lst[3] # del - will delete index 3 of lst
print(lst)

a=lst.pop(2) # Here pop will also remove index 2 - three from the list but it holds it and we are assigning it to a new variable which we
print(lst) # can use as compared to del it removes element completely


