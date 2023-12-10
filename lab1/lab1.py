import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = np.random.normal(loc = 0.5, scale = 0.15, size = 100)
#data = pd.read_csv('my_data.csv')['A'].values     #import from csv file
data_sorted = sorted(data)
data_final = [x * 4 for x in data_sorted]

np.savetxt ("my_data.csv", np.column_stack((data, data_sorted, data_final)), delimiter=",", header="A, B, C")

plt.hist(data_sorted, 50, density=True, facecolor='g', alpha=0.75)
plt.axis([-3, 3, 0, 3])
plt.show()
print(data_final)
print('Розмах вибірки = %.2f' % (data_final[99] - data_final[0]))

sns.histplot(data, color="red", label="100% Equities", kde=True, stat="density", linewidth=0)

plt.show() 