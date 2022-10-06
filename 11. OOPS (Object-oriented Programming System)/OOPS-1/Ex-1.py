# First we will create a class and make sure to write first letter of classname a Capital One.

class Phone:
    def Call(self):
        print("Call SomeBody")
    def Play(self):
        print("let's Play Some Games")

''' We need to pass self as first argument for the function as it is necessary otherwise it will not be possible to call it
using class method '''

p1 = Phone()
''' Here we created an object of Class Phone that is p1 which can call Phone class methods '''

p1.Call()
p1.Play()



