import os # Importing operating system
print(os.getcwd()) # will give us current directory location

# os.chdir - new directory location

f = open("file",'w') # Here w stands for write function
f.close()

''' It is necessary to close the function because file goes from python file to RAM - Volatile memory so it is necessary to close it as once you 
close it it will move from RAM to storage of your Pc, otherwise the file will get deleted once we close the pc as RAM is Volatile memory.'''

''' One good to close the file is using exception handling - try, catch, Finally '''

try:
    f = open('file','w') # Do whatever you want
finally:
    f.close()

# Write to a file
# 1. Open the file and then use write function
f = open("Goals",'w')
f.write("I Will be the best coder and i am going to prove it \n")
f.write("I Choose Health, Happiness, Peace of mind, Success and I Believe in my subconscious mind to provide to me, to bring into the reality")
f.close()

# How to read a file
f = open('Goals','r')
print(f.read())

f = open('Goals','r')
print(f.read(2)) # It will return the first two characters as we passes the 2 in the read function

print(f.tell()) # It tells where is the cursor present now.

print(f.read(6)) # It will return the 6 characters from the place the cursor is present now

f.seek(0) # Brings cursor to the initial Position in the file
print(f.tell())

for line in f:
    print(line)  # Will return both the lines

f = open("Goals","r")
print(f.readline()) # It will return the first line in the code and then again it will return another line

f.seek(0)
print(f.readlines()) # It will return everything in a file as a list

''' To get the every file in the current directory we are working on we use operating system and function of getcwd '''
print(os.listdir(os.getcwd()))




