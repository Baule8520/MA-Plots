import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Genauigkeit_Prozent.xlsx')

y_1 = df.iloc[2:23, 5]
y_2 = df.iloc[2:23, 9]
y_3 = df.iloc[2:23, 13]

x_1 = df.iloc[2:23, 4]
x_2 = df.iloc[2:23, 8]
x_3 = df.iloc[2:23, 12]

x = [0,3.3]
y_oben = [0.0260606, 0.0260606]
y_unten = [-0.0260606, -0.0260606]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot([0,3.3], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [%]')
plt.legend(['1-fach gesampelt','5-fach gesampelt', '10-fach gesampelt', "Idealwert"], loc='lower left')

#plt.show()

plt.savefig('results/esp32_genauigkeit_prozent.svg', format='svg', dpi=1200)