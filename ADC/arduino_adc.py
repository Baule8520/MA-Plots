import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Arduino&ESP.xlsx')
print (df)

x_1 = df.iloc[2:23, 0]
print(x_1)

y_1 = df.iloc[2:23, 2]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,5], linestyle='--', color='black')

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_adc.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 3]

x = [0,5]
y_oben = [0.09766, 0.09766]
y_unten = [-0.09766, -0.09766]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim([-1, 1])
plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 1]
y_1 = y_1 * 1000

x = [0,5]
y_oben = [4.883, 4.883]
y_unten = [-4.883, -4.883]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim([-20, 20])
plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [mV]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_genauigkeit_mv.svg', format='svg', dpi=1200)