# Inheritance - With inheritance one class can derive/inherit/use properties of another Class.
class Vehicle:

    def __init__(self,name, mileage, cost):
        self.name = name
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("Name of Vehicle:",self.name)
        print("Mileage of Vehicle:",self.mileage)
        print("Cost of Vehicle",self.cost)

v = Vehicle("KTM",10,"1 Lakhs")
v.show_details()

class Car(Vehicle):
# Here we have passed Vehicle class to Car class it means Vehicle is the Father Class and Car is the Child Class and Car can inherit
# the properties, method of its Parent Class (Vehicle) with its class object with its properties as well.

    def car_name(self):
        print("BMW")

c1 = Car("Jawa",15,"2 lakhs")
c1.show_details()
c1.car_name()






