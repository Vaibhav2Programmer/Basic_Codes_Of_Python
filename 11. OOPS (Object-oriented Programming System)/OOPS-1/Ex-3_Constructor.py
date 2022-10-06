# Creating a Class using a Constructor
# Constructor will help us to initalize objects many at a single time as compared to class we created in Ex-2
# where we created 4 functions to tell about color and cost we can do it in a single constructor only

class Employee:
    # This is how we create a constructor
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employeeDetails(self):
        print("Name Of Employee:", self.name)
        print("Age of Employee:", self.age)
        print("Salary of Employee:", self.salary)
        print("Gender of Employee:", self.gender)

# Object created emp of Employee class
emp = Employee("Vaibhav", 22, "25 Lakhs",'M')
emp.employeeDetails()
