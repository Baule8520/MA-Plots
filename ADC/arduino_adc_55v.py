import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/12_04_23.xlsx')
print (df)

x_1 = df.iloc[2:23, 0]
x_2 = df.iloc[2:23, 4]
print(x_1)

y_1 = df.iloc[2:23, 2]
y_2 = df.iloc[2:23, 6]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,55], [0,55], linestyle='--', color='black')

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['1-fach gesampelt', '10-fach gesampelt', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_adc_55v.svg', format='svg', dpi=1200)