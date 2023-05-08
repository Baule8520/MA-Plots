import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Arduino_55V.xlsx')
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
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_55v_adc.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 9]
y_2 = df.iloc[2:23, 13]

x = [0,55]
y_oben = [0.09765636, 0.09765636]
y_unten = [-0.09765636, -0.09765636]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,55], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-1,1)
plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [%]')
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_55v_genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 1]
y_2 = df.iloc[2:23, 5]
y_1 = y_1*1000
y_2 = y_2*1000

x = [0,55]
y_oben = [53.711, 53.711]
y_unten = [-53.711, -53.711]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot([0,55], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-350,350)
plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [mV]')
plt.legend(['1-fach Messung', '10-fach Messung', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_55v_genauigkeit_mv.svg', format='svg', dpi=1200)