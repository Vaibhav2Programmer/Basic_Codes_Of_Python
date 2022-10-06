class Employee:

    def __init__(self,name,age=10,salary='2 Lakhs',profession='SDE_1'):
        self.name = name
        self.age = age
        self.salary = salary
        self.profession = profession

    def employeeDetails(self):
        print('Name of Employee: ',self.name)
        print('Age: ', self.age)
        print('Salary: ', self.salary)
        print('Profession: ', self.profession)

e1 = Employee('Akshat')
e1.employeeDetails()