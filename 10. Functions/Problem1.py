# Progem to find the hcf/gcd of the 2 numbers

def hcf(a,b): # we will pass two numbers
    """This Function gives the hcf of the 2 numbers"""

    smaller = b if a > b else a
    hcf = 1

    for i in range(1,smaller+1):
        if(a % i == 0) and (b % i == 0):
            hcf = i
    return hcf

num1 = 20
num2 = 25

print("HCF of {0} and {1} numbers is {2}".format(num1,num2,hcf(num1,num2)))

