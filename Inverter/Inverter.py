import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data/WR 100W.xlsx')

x_1 = df.iloc[2:25, 3]
print(x_1)

y_1 = df.iloc[2:25, 5]
print(y_1)

plt.scatter(x_1, y_1, marker='x')

z = np.polyfit(x_1, y_1, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x_1, p(x_1))

plt.xlim([0, 110])
# plt.ylim([78, 85])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')

#plt.show()

plt.tight_layout()
plt.savefig('results/WR_100W.svg', format='svg', dpi=1200)
plt.clf()

#########################################################################

df = pd.read_excel('data/WR 300W.xlsx')

x_2 = df.iloc[1:30, 3]
print(x_2)

y_2 = df.iloc[1:30, 5]
print(y_2)

plt.scatter(x_2, y_2, marker='x')

z = np.polyfit(x_2, y_2, 3)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x_2, p(x_2))

plt.xlim([0, 285])
# plt.ylim([84.5, 92.5])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')

#plt.show()

plt.tight_layout()
plt.savefig('results/WR_300W.svg', format='svg', dpi=1200)
plt.clf()

#####################################################################

plt.subplot(2, 1, 1)

plt.scatter(x_2, y_2, marker='x')

z = np.polyfit(x_2, y_2, 3)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x_2, p(x_2))

plt.title("300W Wechselrichter")
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')


plt.subplot(2, 1, 2)

plt.scatter(x_1, y_1, marker='x')

z = np.polyfit(x_1, y_1, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x_1, p(x_1))

plt.title("100W Wechselrichter")
plt.xlim([-2, 110])
plt.xlabel('Ausgangsleistung [W]')
plt.ylabel('Wirkungsgrad [%]')

plt.tight_layout()
plt.savefig('results/InverterVergleich.svg', format='svg', dpi=1200)
plt.clf()