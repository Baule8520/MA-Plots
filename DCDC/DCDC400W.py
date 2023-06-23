import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/StepDown400W.xlsx')

x_1 = df.iloc[0:13, 5]
x_2 = df.iloc[14:29, 5]
x_3 = df.iloc[30:45, 5]
x_4 = df.iloc[46:61, 5]
print(x_1)
print(x_2)
print(x_3)
print(x_4)

y_1 = df.iloc[0:13, 7]
y_2 = df.iloc[14:29, 7]
y_3 = df.iloc[30:45, 7]
y_4 = df.iloc[46:61, 7]

plt.plot(x_1, y_1, marker='x')
plt.plot(x_2, y_2, marker='^')
plt.plot(x_3, y_3, marker='s')
plt.plot(x_4, y_4, marker='o')

# plt.xlim([0, 150])
# plt.ylim([91, 97])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')
plt.legend(['Ausgangsspannung 10 V', 'Ausgangsspannung 20 V','Ausgangsspannung 30 V', 'Ausgangsspannung 40 V'], loc='lower right')

#plt.show()

plt.savefig('results/DCDC_SD_400W.svg', format='svg', dpi=1200)