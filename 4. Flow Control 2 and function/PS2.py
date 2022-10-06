#2. Program to greet all the person names stored in a list which starts with S

l = ["Rahul","Harry","Soham","sachin"]

for name in l:
    if name.startswith('S'):
        print("Goodmorning {}".format(name))
