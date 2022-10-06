
''' We use copy function to copy from one dictionary to another '''
squares = {2:4,3:9,4:16,5:25}
copied_dic = squares.copy()
print(copied_dic)

''' We use fromkeys function to make key-value pair '''

subjects = {}.fromkeys(['Maths','English','History'],0)
print(subjects)

''' To get whole key-value pair of an dictionary we use items function '''
print(squares.items())

''' If we wan't only keys or values we use either keys() or values() '''
print(squares.keys())
print(squares.values())

''' To know all functions of dictionary we use dir'''

d={}
print(dir(d))

d = {'a':1,'b':2,'c':3,}
for pair in d.items():
    print(pair)

for value in d.values():
    print(value)

for key in d.keys():
    print(key)

d1 = d.copy()
d1['d'] = 6
d1['f'] = 9
print(d1)

''' Dictionary Comphrehension '''

ans = {k:v for k,v in d1.items() if v>2}
print(ans)

new_dic = {'c':3,'d':4,'f':5}

new_dic = {k+'og':v+1 for k,v in new_dic.items() if v > 3}
print(new_dic)