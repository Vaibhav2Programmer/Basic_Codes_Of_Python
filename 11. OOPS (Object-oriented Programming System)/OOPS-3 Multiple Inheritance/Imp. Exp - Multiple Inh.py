''' Deadly Diamond/ Diamond Interface '''

class A:

    def explore(self):
        print("Class A ka Explore Function Hu")

class B(A):
    pass
    '''def explore(self):
        print("Class B ka Explore Function Hu")'''

class C(A):
    pass
    '''def explore(self):
        print("Class C ka Explore Function Hu")'''

class D(B,C):
   # pass
   def explore(self):
       print("Class D ka Explore Function Hu")


d_obj = D()
# Here we have not written explore function of D to see from which class does explore functiom gets derived.
# But if same function is itself present in the D class then the function gets derived from Class D itself.
d_obj.explore()