import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FormatStrFormatter

df = pd.read_excel('data/ADS1115.xlsx')

x_1 = df.iloc[2:23, 0]
print(x_1)

y_1 = df.iloc[2:23, 1]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,5], linestyle='--', color='black')

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/ads1115_adc.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 3]

x = [0,5]
y_oben = [0.00152588, 0.00152588]
y_unten = [-0.00152588, -0.00152588]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim([-1, 1])
plt.xlabel('Referenzspannung [V]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/ads1115_genauigkeit_prozent.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

y_1 = df.iloc[2:23, 4]
y_1 = y_1 * 1000

x = [0,5]
y_oben = [0.076294, 0.076294]
y_unten = [-0.076294, -0.076294]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim([-20, 20])
plt.xlabel('Referenzspannung [V]')
plt.ylabel('Abweichung [mV]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')

#plt.show()

plt.savefig('results/ads1115_genauigkeit_mv.svg', format='svg', dpi=1200)
plt.clf()

############################################################################################################

decimal_places = 1

plt.subplot(2, 1, 1)
y_1 = df.iloc[2:23, 1]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,5], linestyle='--', color='black')

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')
plt.gca().xaxis.set_major_formatter(FormatStrFormatter(f'%.{decimal_places}f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter(f'%.{decimal_places}f'))


plt.subplot(2, 1, 2)
y_1 = df.iloc[2:23, 3]

x = [0,5]
y_oben = [0.00152588, 0.00152588]
y_unten = [-0.00152588, -0.00152588]

plt.plot(x_1, y_1, marker='x')
plt.plot([0,5], [0,0], linestyle='--', color='black')
plt.fill_between(x, y_oben, color='green', alpha=.5)
plt.fill_between(x, y_unten, color='green', alpha=.5)

plt.ylim([-1, 1])
plt.xlabel('Referenzspannung [V]')
plt.ylabel('Abweichung [%]')
plt.legend(['Messwert', "Idealwert"], loc='lower right')
plt.gca().xaxis.set_major_formatter(FormatStrFormatter(f'%.{decimal_places}f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter(f'%.{decimal_places}f'))

plt.tight_layout()
plt.savefig('results/ads1115_MA.svg', format='svg', dpi=1200)
plt.clf()