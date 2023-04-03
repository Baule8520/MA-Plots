import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/DCDC Step-Down 20A.xlsx')
print (df)

x_1 = df.iloc[1:4, 9]
x_2 = df.iloc[5:8, 9]
x_3 = df.iloc[9:12, 9]
x_4 = df.iloc[13:16, 9]
print(x_4)

y_1 = df.iloc[1:4, 11]
y_2 = df.iloc[5:8, 11]
y_3 = df.iloc[9:12, 11]
y_4 = df.iloc[13:16, 11]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot(x_4, y_4, marker='o')

plt.xlim([0, 175])
plt.ylim([91, 97])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')
plt.legend(['Ausgangsspannung 10 V', 'Ausgangsspannung 12 V','Ausgangsspannung 15 V', 'Ausgangsspannung 20 V'], loc='upper right')

plt.show()