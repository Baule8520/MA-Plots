import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Hall_Sensoren.xlsx')

x_1 = df.iloc[1:56, 0]
print(x_1)

y_1 = df.iloc[1:56, 1]

plt.plot(x_1, y_1, marker='x')
plt.plot([0.691,4.291], [-18,18], linestyle='--', color='black')

plt.xlim([0, 5])
plt.ylim([-20, 20])
plt.xlabel('Ausgangsspannung [V]')
plt.ylabel('Ampere [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_20A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[1:56, 1]

y_1 = df.iloc[1:56, 5]

plt.plot(x_1, y_1, marker='x')
plt.plot([-18,18], [0,0], linestyle='--', color='black')

plt.ylim([-5, 5])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_20A_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[1:56, 1]

y_1 = df.iloc[1:56, 6]

plt.plot(x_1, y_1, marker='x')
plt.plot([-18, 18], [0,0], linestyle='--', color='black')

plt.ylim([-1, 1])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_20A_A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[28:42, 1]
print(x_1)
y_1 = df.iloc[28:42, 16]
print(y_1)

plt.plot(x_1, y_1, marker='x')
plt.plot([0,4], [0,0], linestyle='--', color='black')

plt.ylim([-8, 8])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_20A_prozent_4A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[28:42, 1]

y_1 = df.iloc[28:42, 6]
y_1 = y_1 * 1000

plt.plot(x_1, y_1, marker='x')
plt.plot([0, 4], [0,0], linestyle='--', color='black')

plt.ylim([-300, 300])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_20A_mA_4A.svg', format='svg', dpi=1200)
