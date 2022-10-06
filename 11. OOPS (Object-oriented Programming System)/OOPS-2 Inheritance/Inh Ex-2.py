''' Overriding init Method/ Constructor Method '''

class Vehicle:

    def __init__(self,mileage, cost):
       # self.name = name
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
       # print("Name of Vehicle:",self.name)
        print("Mileage of Vehicle:",self.mileage)
        print("Cost of Vehicle:",self.cost)

class Car(Vehicle):

    def __init__(self,mileage, cost, tyres, hp):
        super().__init__(mileage,cost)
# This above method will help us to initialize the attributes of the parent class
        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("Creta")
        print("tyres:",self.tyres)
        print("HP:",self.hp)

c1 = Car(20, '20 Lakhs', 4, 700) # Here we have to pass 4 arguments as 2 arguments of parent class and 2 of child class
c1.show_details()
c1.show_car_details()