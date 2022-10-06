# in - a membewrship operator checks if a element is in a sequence or not
lst = ['one','two','three','four']
if 'two' in lst:
    print('Chinki')
if 'Six' not in lst:
    print('Minki')

# reverse - reverses the whole list

lst.reverse()
print(lst)

# Sorting

numbers = [3,7,8,9,10,5]
sorted_list = sorted(numbers)
print("List after sorting:",sorted_list) # List with sorted numbers

print("original List:",numbers)

# To print a list in reverse sorted order

print("Sorted list in reverse order:",sorted(numbers,reverse=True))
print("original:",numbers)

# To sort the original list
lst=[7,9,8,4]
lst.sort() # sort function helps us to sort the orginal list itself
print(lst)

# sort does not work with list consist of different datatypes
# as sorting works on the foundation of comparing internally and elements from datatypes like int and string are not comparable