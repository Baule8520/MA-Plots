import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/11_04_23.xlsx')
print (df)

x_1 = df.iloc[2:23, 0]
print(x_1)

y_1 = df.iloc[2:23, 2]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,5], linestyle='--', color='black')

#plt.xlim([0, 3.3])
#plt.ylim([0, 3.3])
plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

plt.show()