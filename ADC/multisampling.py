import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/11_04_23.xlsx')
print (df)

x_1 = df.iloc[2:23, 4]
x_2 = df.iloc[2:23, 8]
x_3 = df.iloc[2:23, 12]
print(x_1)

y_1 = df.iloc[2:23, 6]
y_2 = df.iloc[2:23, 10]
y_3 = df.iloc[2:23, 14]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot([0,3.3], [0,3.3], linestyle='--', color='black')

#plt.xlim([0, 3.3])
#plt.ylim([0, 3.3])
plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['1-fach gesampelt', '5-fach gesampelt','10-fach gesampelt', "Idealwert"], loc='lower right')

plt.show()