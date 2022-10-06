import numpy as np
import matplotlib.pyplot as plt

''' To create a bar graph with ratio in it '''
w = 0.4
x = ['CSE','IT','EC','EE','MECH','CIVIL','CHEM']
boys = [100,80,85,120,150,160,130]
girls = [60,35,45,50,20,45,55]

plt.bar(x,boys, w, label="boys")
plt.bar(x, girls, w, bottom=boys,label="girls")

plt.xlabel("Courses") # Here, x is will be displayed on x label
plt.ylabel("Students")
plt.title("No. of Boys and Girls in Department")
plt.legend() # It will tell which color represents boy or girls
plt.show() # It will show the bar graph
