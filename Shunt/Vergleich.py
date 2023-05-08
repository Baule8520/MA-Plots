import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/ADS1115_Shunt.xlsx')
df2 = pd.read_excel('data/Arduino_Shunt.xlsx')

x_1 = df.iloc[2:26, 0]
y_1 = df.iloc[2:26, 6]

x_1_1 = df2.iloc[2:13, 0]
y_1_2 = df2.iloc[2:13, 7]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_1_1, y_1_2, marker='^')
plt.plot([0,4], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['ADS1115', 'Arduino', "Idealwert"], loc='lower right')

plt.savefig('results/genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:26, 4]
y_1_2 = df2.iloc[2:13, 5]
y_1_2 = y_1_2 * 1000

plt.plot(x_1, y_1, marker='x')
plt.plot(x_1_1, y_1_2, marker='^')
plt.plot([0,4], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['ADS1115', 'Arduino', "Idealwert"], loc='lower right')

plt.savefig('results/genauigkeit_ma.svg', format='svg', dpi=1200)
plt.clf()