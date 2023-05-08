import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Arduino&ESP.xlsx')
print (df)

x_1 = df.iloc[2:23, 5]
x_2 = df.iloc[2:23, 10]
x_3 = df.iloc[2:23, 15]
print(x_1)

y_1 = df.iloc[2:23, 7]
y_2 = df.iloc[2:23, 12]
y_3 = df.iloc[2:23, 17]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot([0,3.3], [0,3.3], linestyle='--', color='black')

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['1-fach Messung', '5-fach Messung','10-fach Messung', "Idealwert"], loc='lower right')

# plt.show()

plt.savefig('results/esp32_adc.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 8]
y_2 = df.iloc[2:23, 13]
y_3 = df.iloc[2:23, 18]

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
plt.legend(['1-fach Messung', '5-fach Messung','10-fach Messung', "Idealwert"], loc='upper left')

#plt.show()

plt.savefig('results/esp32_genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 6]
y_2 = df.iloc[2:23, 11]
y_3 = df.iloc[2:23, 16]
y_1 = y_1*1000
y_2 = y_2*1000
y_3 = y_3*1000

x = [0,3.3]
y_oben = [0.806, 0.806]
y_unten = [-0.806, -0.806]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot([0,3.3], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.xlabel('Spannung [V]')
plt.ylabel('Abweichung [mV]')
plt.legend(['1-fach Messung', '5-fach Messung','10-fach Messung', "Idealwert"], loc='upper left')

#plt.show()

plt.savefig('results/esp32_genauigkeit_mv.svg', format='svg', dpi=1200)