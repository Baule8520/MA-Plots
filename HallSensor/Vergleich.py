import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Hall_Sensoren.xlsx')

x_1 = df.iloc[1:48, 17]
y_1 = df.iloc[1:48, 22]

x_2 = df.iloc[1:56, 1]
y_2 = df.iloc[1:56, 6]

x_3 = df.iloc[1:56, 9]
y_3 = df.iloc[1:56, 14]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot([-18, 18], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [A]')
plt.legend(['5 A Hall Sensor', "20 A Hall Sensor", "30 A Hall Sensor"], loc='lower right')

#plt.show()

plt.savefig('results/hall_vergleich_ma.svg', format='svg', dpi=1200)
plt.clf()