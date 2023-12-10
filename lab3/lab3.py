import numpy as np
import math
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

n = 100 #кількість варіант вибірки
#data = np.random.randint(100, 400, n)
data = pd.read_csv('my_data.csv')[' C'].values     #import from csv file
data_sorted = sorted(data)
x_max = data_sorted[n -1]
x_min = data_sorted[0]
R = x_max - x_min
m = math.ceil(1 + 3.3221 * math.log10(n))
k = round(R/(1 + 3.3221 * math.log10(n)), 2)
x_start = round(x_min - k/2, 2)

col_names = ["#", "Range", "Middle", "Quantity", "Frequency", "Accumulated Quantity", "Accumulated frequency"]
table_array = []
Accumulated_Quantity = 0

for i in range(1, m + 1):
    Range = '%.2f - %.2f' % (x_start + k * (i - 1), x_start + k * i)
    Middle = '%.2f' % (x_start + k * (i - 1) + k/2)
    Quantity = 0
    for d in range(0, n):
        if data_sorted[d] > x_start + k * (i - 1) and data_sorted[d] <= x_start + k * i:
            Quantity += 1
    Frequency = '%.2f' % (Quantity/n)
    if i == 1:
        Accumulated_Quantity = Quantity
    else:
        Accumulated_Quantity += Quantity
    Accumulated_frequency = '%.2f' % (Accumulated_Quantity/n)
    table_array.append([i, Range, Middle, Quantity, Frequency, Accumulated_Quantity, Accumulated_frequency])

#print(tabulate(table_array, headers=col_names, tablefmt="fancy_grid"))                                     # таблиця
#print(data)
'''
print('R = %.2f' % (x_max - x_min))
print('m = %.2f' % (m)) 
print('k = %.2f' % (k)) 
'''
column = 3

poligon_x = []
poligon_y = []
for i in table_array:
    poligon_x.append(float(i[column-1]))
column = 5
for i in table_array:
    poligon_y.append(float(i[column-1]))
'''plt.title('Poligon')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.plot(poligon_x, poligon_y)
plt.show()'''

histogram_y = ['%.1f' % x for x in data_sorted]
histogram_x =[]
'''plt.xlabel('n')
plt.ylabel('x')
plt.title('Histogram')
plt.hist(histogram_y)
plt.show()'''

histogram_y = []
column = 4
max_quantity = 0
for i in table_array:
    histogram_y.append(float(i[column-1]))


cumulative_y = []
column = 7
for i in table_array:
    cumulative_y.append(float(i[column-1]))
'''plt.xlabel('x')
plt.ylabel('y')
plt.title('Cumulative')
plt.plot(poligon_x, cumulative_y)
plt.show()'''

selective_average = 0
for i in range(0, m):
    selective_average += poligon_x[i] * histogram_y[i]
selective_average = selective_average/n
#print('selective_average = %.2f' % (selective_average))

dispersion = 0
for i in range(0, m):
    dispersion += ((poligon_x[i] - selective_average)**2) * histogram_y[i]
dispersion = (dispersion/n)
#print('dispersion = %.2f' % (dispersion))
'''
coefficient_of_variation = (math.sqrt(dispersion)/selective_average) * n
print('coefficient_of_variation = %f' % (coefficient_of_variation))

asymmetry = 0
for i in range(0, m):
    asymmetry += ((poligon_x[i] - selective_average)**3) * histogram_y[i]
asymmetry = (asymmetry/((math.sqrt(dispersion)**3) * n))
print('asymmetry = %f' % (asymmetry))

excess = 0
for i in range(0, m):
    excess += ((poligon_x[i] - selective_average)**4) * histogram_y[i]
excess = (excess/((math.sqrt(dispersion)**4) * n)) -3
print('excess = %f' % (excess))
'''
a = selective_average
print('a = %.2f' % a)
print('σ² = %.2f' % dispersion)

S = 0 
for i in range(len(poligon_x)):  
    S += poligon_x[i]

table = [float('%.2f' % x) for x in poligon_x]
table.append(float('%.2f' % S))

buff_array = [float('%.2f' % x**2) for x in poligon_x]
S = 0 
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.2f' % S))
table = np.vstack((table, buff_array))

buff_array = [float('%.2f' % x**3) for x in poligon_x]
S = 0 
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.2f' % S))
table = np.vstack((table, buff_array))

buff_array = [float('%.2f' % x**4) for x in poligon_x]
S = 0 
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.2f' % S))
table = np.vstack((table, buff_array))

S = 0 
buff_array = [float('%.2f' % x) for x in poligon_y]
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.2f' % S))
table = np.vstack((table, buff_array))

buff_array = []
for i in range(len(poligon_x)):
    buff_array.append(float('%.3f' % (poligon_x[i] * poligon_y[i])))
S = 0 
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.3f' % S))
table = np.vstack((table, buff_array))

buff_array = []
for i in range(len(poligon_x)):
    buff_array.append(float('%.3f' % ((poligon_x[i]**2) * poligon_y[i])))
S = 0 
for i in range(len(buff_array)):  
    S += buff_array[i]
buff_array.append(float('%.3f' % S))
table = np.vstack((table, buff_array))
#print(table)


M1 = [table[3][len(poligon_x)], table[2][len(poligon_x)], table[1][len(poligon_x)]]
M1 = np.vstack((M1, [table[2][len(poligon_x)], table[1][len(poligon_x)], table[0][len(poligon_x)]]))
M1 = np.vstack((M1, [table[1][len(poligon_x)], table[0][len(poligon_x)], float(len(poligon_x))]))

v1 = [table[6][len(poligon_x)], table[5][len(poligon_x)], table[4][len(poligon_x)]]

ans = np.linalg.solve(M1, v1)

print('-----------------------------------')
print('a = %.4f' % ans[0])
print('b = %.4f' % ans[1])
print('c = %.4f' % ans[2])