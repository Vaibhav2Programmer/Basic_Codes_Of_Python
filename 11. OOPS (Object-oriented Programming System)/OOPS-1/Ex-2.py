class Phone:
    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

''' In first 2 function we are passing arguments such as color and cost which we will like to have
and last two function will show us the color and cost we gave '''

''' Now we will create an object to pass the values to the arguments'''

p = Phone()
p.set_color("Black")
p.set_cost(16000)

print(p.show_color())
a = p.show_cost()
print(a)