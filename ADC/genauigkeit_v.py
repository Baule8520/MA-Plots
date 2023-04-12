import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Genauigkeit_V.xlsx')

y_1 = df.iloc[2:23, 1]
y_2 = df.iloc[2:23, 5]
y_3 = df.iloc[2:23, 9]
y_4 = df.iloc[2:23, 13]
y_1 = y_1*1000
y_2 = y_2*1000
y_3 = y_3*1000
y_4 = y_4*1000

x_1 = list(range(len(y_1)))

plt.plot(x_1, y_1, marker='x')
plt.plot(x_1, y_2, marker='^')
plt.plot(x_1, y_3, marker='s')
plt.plot(x_1, y_4, marker='o')
plt.plot([0,20], [0,0], linestyle='--', color='black')

plt.xticks(x_1)
plt.xlabel('Messpunkt')
plt.ylabel('Abweichung [mV]')
plt.legend(['Arduino 1-fach gesampelt', 'ESP32 1-fach gesampelt','ESP32 5-fach gesampelt', 'ESP32 10-fach gesampelt', "Idealwert"], loc='lower left')

#plt.show()

plt.savefig('results/genauigkeit_v.svg', format='svg', dpi=1200)