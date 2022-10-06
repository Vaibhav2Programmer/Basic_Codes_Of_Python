#Implicit Conversion - it happens automatically from a lower datatype ex. int to higher datatype ex. float
#It does not requires user involvement.

num_int = 125
num_flo = 1.25
print(num_int+num_flo,type(num_int+num_flo))

#2. If a string(higher datatype) added to a lower datatype it will generate error as this kind of operand is not supported.

# Explicit Conversion - In this Conversion user changes from one datatype to the required datatype.
# Thats why it is also called as typecasting as user changes the datatype

num_int = 456
num_str = '987'

print(type(num_int),type(num_str))

# Now converting the string datatype to int

num_str=int(num_str) # Here only type is changed from string to int not the variable

ans = num_str+num_int
print(type(num_str))
print(ans,type(ans))