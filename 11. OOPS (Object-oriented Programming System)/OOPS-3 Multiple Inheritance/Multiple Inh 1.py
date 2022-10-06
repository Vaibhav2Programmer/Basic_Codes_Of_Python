''' Multiple inheritance lets child class have more than one properties of the parent classes and more than one parent class '''

class Parent1:
    def assign_string_one(self,str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1

class Parent2:

    def assign_str_two(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2

class Child(Parent1,Parent2): # Here it is inheriting 2 parent classes - multiple inheritance

    def assign_string_three(self,str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3

first_child = Child()

first_child.assign_string_one("String1 of Parent1")
first_child.assign_str_two("String2 of Parent2")
first_child.assign_string_three("String3 of Parent3")

print(first_child.show_string_one())
print(first_child.show_string_two())
print(first_child.show_string_three())
