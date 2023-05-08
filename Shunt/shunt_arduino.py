import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Arduino_Shunt.xlsx')

x_1 = df.iloc[2:13, 0]
x_2 = df.iloc[2:13, 9]
print(x_1)

y_1 = df.iloc[2:13, 3]
y_2 = df.iloc[2:13, 12]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,4], [0,4], linestyle='--', color='black')

plt.xlabel('Referenzstrom [A]')
plt.ylabel('gemessener Strom [A]')
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

plt.savefig('results/arduino.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:13, 7]
y_2 = df.iloc[2:13, 16]

x = [0,4]
y_oben = [1.22075, 1.22075]
y_unten = [-1.22075, -1.22075]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,4], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-6,6)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

plt.savefig('results/arduino_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:13, 5]
y_2 = df.iloc[2:13, 14]
y_1 = y_1*1000
y_2 = y_2*1000

x = [0,4]
y_oben = [48.83, 48.83]
y_unten = [-48.83, -48.83]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,4], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-250,250)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

plt.savefig('results/arduino_ma.svg', format='svg', dpi=1200)
plt.clf()