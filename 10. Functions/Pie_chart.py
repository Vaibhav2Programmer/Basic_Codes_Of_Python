from matplotlib import pyplot as plt


''' Creating a dataset '''
Cars = ['AUDI','FERRARI','BMW','MAHINDRA','MERCEDES',"THAR"]

Data = [20,24,17,40,35,0] # Here data must be of same length as labels

'''Creating a Plot'''
# fig = plt.figure(figsize=(14,9)) This line is not necessary it used to change the width and length of the bar graph/pie chart etc.
plt.pie(Data,labels=Cars)
plt.show()