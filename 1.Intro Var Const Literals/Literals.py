# Literals - is a raw data or value which is assigned to a variable or a constant is called as a Literal.

a = 0b1010 #binary literal
b = 14527 #decimal
c = 0o7563 #Octal
d = 0xAB1125 # hexadecimal

# Float Lietrals

float_1 = 1.23659
float_2 = 1.235e3

print(a,b,c,d, float_1, float_2)
# we can write like this to print multiple values in a single line

### String Literals

string_l1 = "This is python programming"
v = "f"  # example of a character literal

multiline_str = '''This is a example of multi line string'''

print(string_l1,v)
print(multiline_str)

## Boolean Literals

# Boolean has only 2 kind of Values - True and False
# where, True = 1 and False  = 0

x = (1==True) # Here first we are checking if 1==True which is true, therefore, x = True as True is assigned to the x
y = (1==False) # similarly, here we check if 1==False as False = 0, therefore y = False
a = True + 9
b = False + 12

print("x Value is:", x)
print("y Value is:", y)
print("a Value is:", a)
print("b Value is:", b)

# Another Condition
x = (1==True)
y =(0==False) # Here sice 0 == False condition is right, therefore y is assigned to True
print("x is:",x , "y is:" ,y)
print(x)
