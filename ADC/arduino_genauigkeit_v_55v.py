import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/55V.xlsx')

y_1 = df.iloc[2:23, 1]
y_2 = df.iloc[2:23, 5]
y_1 = y_1*1000
y_2 = y_2*1000

x_1 = df.iloc[2:23, 0]
x_2 = df.iloc[2:23, 4]

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
plt.legend(['1-fach gesampelt','10-fach gesampelt', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/arduino_genauigkeit_v_55v.svg', format='svg', dpi=1200)