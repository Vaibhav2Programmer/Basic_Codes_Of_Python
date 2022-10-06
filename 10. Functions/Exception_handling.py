# To know every exception in python in the python we use dir function

# print(dir(__builtins__))

''' We need to import sys to use try and except in the program 
to know about the error we use sys.exc_info() '''
''' When there is no error except will not run'''

# import sys
#lst = ['a',0,2]
#for input in lst:
#    try:
#        print("This input is ",input)
#        r = 1/int(input)
#    except:
#        print("This Input {} Causes".format(input),sys.exc_info()[0],"error")
#print("The Reciprocal of",input,"is",r)

''' We can also have different except handling for different errors '''

import sys
lst1 = ['a',1,'b']
for input in lst1:
    try:
        print("This input is ",input)
        ans = 1 + input
    except(ValueError):
        print("This Input a Gives Value Error")
    except(ZeroDivisionError):
        print("This Input 0 Gives Zero Divison Error")
    except:
        print("For Any other error")
print("The Reciprocal is",ans)


''' To get an  error by ourself we use - raise ex. raise keyboardinterrupt, raise Memoryerror'''

''' finally - gets executed no matter what happens even if program throws error or crashes'''

try:
    f=open("Finally",'w')
    f.write("finally executes no matter what")

finally:
    f = open("Finally", 'r')
    print(f.readline())
    f.close()