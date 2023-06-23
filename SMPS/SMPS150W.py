import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/SMPS150W.xlsx')

x_1 = df.iloc[0:15, 5]
print(x_1)

y_1 = df.iloc[0:15, 7]

plt.plot(x_1, y_1, marker='x')

plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')

#plt.show()

plt.savefig('results/SMPS150W.svg', format='svg', dpi=1200)