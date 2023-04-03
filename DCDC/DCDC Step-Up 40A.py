import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/DCDC Step-Up 40A.xlsx')
print (df)

x_1 = df.iloc[1:4, 10]
x_2 = df.iloc[5:8, 10]
x_3 = df.iloc[9:11, 10]
x_4 = df.iloc[12, 10]
print(x_4)

y_1 = df.iloc[1:4, 13]
y_2 = df.iloc[5:8, 13]
y_3 = df.iloc[9:11, 13]
y_4 = df.iloc[12, 13]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot(x_4, y_4, marker='o')

plt.xlim([20, 175])
plt.ylim([88, 95])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')
plt.legend(['Ausgangsspannung 15 V', 'Ausgangsspannung 20 V','Ausgangsspannung 25 V', 'Ausgangsspannung 30 V'], loc='upper right')

plt.show()