import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Genauigkeit_Prozent.xlsx')

y_1 = df.iloc[2:23, 1]

x_1 = df.iloc[2:23, 0]

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
plt.legend(['Arduino', "Idealwert"], loc='lower left')

#plt.show()

plt.savefig('results/arduino_genauigkeit_prozent.svg', format='svg', dpi=1200)