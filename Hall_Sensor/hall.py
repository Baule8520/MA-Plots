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
plt.ylabel('Strom [A]')
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

x_1 = df.iloc[1:56, 8]
print(x_1)

y_1 = df.iloc[1:56, 9]

plt.plot(x_1, y_1, marker='x')
plt.plot([1.304,3.68], [-18,18], linestyle='--', color='black')

plt.xlim([1, 4])
plt.ylim([-20, 20])
plt.xlabel('Ausgangsspannung [V]')
plt.ylabel('Strom [A]')
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

x_1 = df.iloc[1:48, 16]
print(x_1)

y_1 = df.iloc[1:48, 17]

plt.plot(x_1, y_1, marker='x')
plt.plot([1.567,3.415], [-4.99,5], linestyle='--', color='black')

plt.ylim([-5.5, 5.5])
plt.xlabel('Ausgangsspannung [V]')
plt.ylabel('Ampere [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_5A.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

x_1 = df.iloc[1:48, 17]

y_1 = df.iloc[1:48, 21]

plt.plot(x_1, y_1, marker='x')
plt.plot([-5,5], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_5A_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[1:48, 22]

plt.plot(x_1, y_1, marker='x')
plt.plot([-5, 5], [0,0], linestyle='--', color='black')

plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/hall_5A_A.svg', format='svg', dpi=1200)
plt.clf()