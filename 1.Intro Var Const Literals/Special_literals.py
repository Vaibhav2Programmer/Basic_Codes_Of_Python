drink = "Coco-Cola" # string / string literals
food = None # we use special literal None as we dont want to assign a value

def menu(x):   # defining the menu function
    if x==drink:  # checking the condition
        print(drink)
    else:
        print(food)

menu(food) # now passing the value to the menu function as food
menu(drink) #