fruits = ['Banana','Apple','Grapes','Melon']
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1

for a in fruits: # Here the plus point is we do not need to give reference to a variable here a will itself assign to the individual element
    print(a);    # and print itself