import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Arduino&ESP.xlsx')
df2 = pd.read_excel('data/ADS1115.xlsx')

y_1 = df.iloc[2:23, 1]
y_2 = df.iloc[2:23, 6]
y_3 = df2.iloc[2:23, 4]
y_1 = y_1*1000
y_2 = y_2*1000
y_3 = y_3*1000

x_1 = list(range(len(y_1)))

plt.plot(x_1, y_1, marker='x')
plt.plot(x_1, y_2, marker='^')
plt.plot(x_1, y_3, marker='s')
plt.plot([0,20], [0,0], linestyle='--', color='black')

plt.xticks(x_1)
plt.xlabel('Messpunkt')
plt.ylabel('Abweichung [mV]')
plt.legend(['Arduino', 'ESP32', 'ADS1115', "Idealwert"], loc='upper left')

#plt.show()

plt.savefig('results/genauigkeit_mv.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 3]
y_2 = df.iloc[2:23, 8]
y_3 = df2.iloc[2:23, 3]
print(y_1)

plt.plot(x_1, y_1, marker='x')
plt.plot(x_1, y_2, marker='^')
plt.plot(x_1, y_3, marker='s')
plt.plot([0,20], [0,0], linestyle='--', color='black')

plt.xticks(x_1)
plt.xlabel('Messpunkt')
plt.ylabel('Abweichung [%]')
plt.legend(['Arduino', 'ESP32', 'ADS1115', "Idealwert"], loc='upper left')

#plt.show()

plt.savefig('results/genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()
