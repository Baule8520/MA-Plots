import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/ADS1115_Shunt.xlsx')
df2 = pd.read_excel('data/0.0075Ohm_Shunt.xlsx')
df3 = pd.read_excel('data/0.0025Ohm_Shunt.xlsx')

x_1 = df.iloc[2:26, 0]
y_1 = df.iloc[2:26, 4]

x_2 = df2.iloc[2:43, 0]
y_2 = df2.iloc[2:43, 4]

x_3 = df3.iloc[2:43, 0]
y_3 = df3.iloc[2:43, 4]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')

plt.plot([0,15], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['0,05 Ohm', '0,0075 Ohm', "0,0025 Ohm"], loc='lower right')
plt.ylim([-75, 15])

plt.savefig('results/genauigkeit_shunt_ma.svg', format='svg', dpi=1200)
plt.clf()