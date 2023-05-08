import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/Hall_Sensoren.xlsx')

x_1 = df.iloc[1:56, 8]
print(x_1)

y_1 = df.iloc[1:56, 9]

plt.plot(x_1, y_1, marker='x')
plt.plot([1.304,3.68], [-18,18], linestyle='--', color='black')

plt.xlim([1, 4])
plt.ylim([-20, 20])
plt.xlabel('Ausgangsspannung [V]')
plt.ylabel('Ampere [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_30A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[1:56, 9]

y_1 = df.iloc[1:56, 13]

plt.plot(x_1, y_1, marker='x')
plt.plot([-18,18], [0,0], linestyle='--', color='black')

plt.ylim([-5, 5])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_30A_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[1:56, 9]

y_1 = df.iloc[1:56, 14]

plt.plot(x_1, y_1, marker='x')
plt.plot([-18, 18], [0,0], linestyle='--', color='black')

plt.ylim([-1, 1])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_30A_A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[28:42, 9]
print(x_1)
y_1 = df.iloc[28:42, 17]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,4], [0,0], linestyle='--', color='black')

plt.ylim([-6, 6])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_30A_prozent_4A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[28:42, 9]

y_1 = df.iloc[28:42, 14]
y_1 = y_1 * 1000

plt.plot(x_1, y_1, marker='x')
plt.plot([0, 4], [0,0], linestyle='--', color='black')

plt.ylim([-250, 250])
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_30A_A_4A.svg', format='svg', dpi=1200)
