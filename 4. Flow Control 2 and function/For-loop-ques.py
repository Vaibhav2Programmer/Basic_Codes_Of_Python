# 1. program to find the students marks from the dictionary

student_name=input("Enter student's name to find the marks:")
marks = {'TB':12,'Steph':30,'VK':17,'RS':45}

for i in marks:
    if student_name==i:
        print(marks[student_name])
        break
    else:
        print("Student with this name is not found")




