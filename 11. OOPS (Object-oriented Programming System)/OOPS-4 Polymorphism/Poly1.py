''' Polymorphism - Different Forms '''

''' Class Level Polymorphism '''

class A:
    def p(self):
        return "Function p in Class A"

class B:
    def p(self):
        return "Function p in Class B"

a = A() # Object Of Class A
b = B() # Object Of Class B

for i in (a,b):
    print(i.p()) # Here, Function depends on the object this is polymorphism first a is used and then b.

# Here, First i will fetch the value of a and then b so it will go like -
# 1. When i = a, print(a.p())
# 2. when i = b, print(b.p())
print("\n")

x = a;
print(x.p())

x = b;
print(x.p())

