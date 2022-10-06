# To print a pattern
n=3 # No. of rows

for i in range(n):

    print(" " * (n-i-1),end="") # This one for spaces and end="" will not print new line
    print("*" * (2*i+1),end="") # For printing star
    print(" " * (n-i-1)) # For spaces again