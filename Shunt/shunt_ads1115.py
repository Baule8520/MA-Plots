import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/ADS1115_Shunt.xlsx')

x_1 = df.iloc[2:26, 0]
print(x_1)

y_1 = df.iloc[2:26, 3]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,4], [0,4], linestyle='--', color='black')

plt.xlabel('Referenzstrom [A]')
plt.ylabel('gemessener Strom [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

plt.savefig('results/ads1115_005Ohm.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:26, 6]

x = [0,4]
y_oben = [0.0346791, 0.0346791]
y_unten = [-0.0346791, -0.0346791]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,4], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-2,2)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_005Ohm_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:26, 4]

x = [0,4]
y_oben = [1.387163636, 1.387163636]
y_unten = [-1.387163636, -1.387163636]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,4], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-100,100)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_005Ohm_ma.svg', format='svg', dpi=1200)
plt.clf()

##########################################################################################################

df = pd.read_excel('data/0.0075Ohm_Shunt.xlsx')

x_1 = df.iloc[2:43, 0]
print(x_1)

y_1 = df.iloc[2:43, 3]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,15], linestyle='--', color='black')

plt.xlabel('Referenzstrom [A]')
plt.ylabel('gemessener Strom [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00075Ohm.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:43, 6]

x = [0,15]
y_oben = [0.0346791, 0.0346791]
y_unten = [-0.0346791, -0.0346791]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-2,2)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00075Ohm_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:43, 4]

x = [0,15]
y_oben = [1.387163636, 1.387163636]
y_unten = [-1.387163636, -1.387163636]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-100,100)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00075Ohm_ma.svg', format='svg', dpi=1200)
plt.clf()

##########################################################################################################

df = pd.read_excel('data/0.0025Ohm_Shunt.xlsx')

x_1 = df.iloc[2:43, 0]
print(x_1)

y_1 = df.iloc[2:43, 3]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,15], linestyle='--', color='black')

plt.xlabel('Referenzstrom [A]')
plt.ylabel('gemessener Strom [A]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00025Ohm.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:43, 6]

x = [0,15]
y_oben = [0.0346791, 0.0346791]
y_unten = [-0.0346791, -0.0346791]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-2,2)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00025Ohm_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:43, 4]

x = [0,15]
y_oben = [1.387163636, 1.387163636]
y_unten = [-1.387163636, -1.387163636]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,15], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim(-100,100)
plt.xlabel('Strom [A]')
plt.ylabel('Abweichung [mA]')
plt.legend(['Messwert',"Idealwert"], loc='lower right')

plt.savefig('results/ads1115_00025Ohm_ma.svg', format='svg', dpi=1200)
plt.clf()