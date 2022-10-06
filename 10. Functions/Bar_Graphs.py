import numpy as np # It helps us to create an array
import matplotlib.pyplot as plt

# First of all, creating an dataset

data = {'C':20,'C++':25,'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5)) # In figsize function first we have width,then we have length

''' Creating the bar plot - Here courses will come on x-axis and values will come on y-axis '''

plt.bar(courses,values,color='red',width=0.3)
plt.xlabel("Courses Offered") # This is the label which will appear on x-axis
plt.ylabel("No. of Students Enrolled") # This is the albel which will appear on y-axis
plt.title("Programming Courses Taken By Students")
plt.show()