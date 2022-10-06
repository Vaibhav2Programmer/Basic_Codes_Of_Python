import matplotlib.pyplot as plt
import numpy as np
import pdp as pdp # Python debugging

data = [[15,25,45,20],
        [40,22,29,35],
        [55,5,37,42]]

X = np.arange(4)
# pdp.set_trace() # Brakpoint
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.bar(X + 0.00, data[0], color='b',width=0.25)
ax.bar(X + 0.25, data[1], color = 'g', width=0.25)
ax.bar(X + 0.50, data[2], color = 'r', width=0.25)
# ax.show()