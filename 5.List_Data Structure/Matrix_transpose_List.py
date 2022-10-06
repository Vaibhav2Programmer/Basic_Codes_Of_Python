# transpose of a matrix without list comphrehension

# matrix = [[1,2,3],[4,5,6],[7,8,9]] - declaring of matrix

matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
]

transposed = []

for i in range(3): # as we have only 3 columns and this for loop is for columns
    lst=[]
    for row in matrix: # this loop is for rows
        lst.append(row[i])
    transposed.append(lst)

print(transposed)

'''With List Comphrehension'''

transposed1 = [[row[i] for row in matrix]for i in range(3)]
print(transposed1)