import matplotlib.pyplot as plt
import pandas as pd

df_4 = pd.read_csv('data/vergleich/4151-104-up-cp.txt', sep=' - ', header=None, names=["Pot", "A0", "U", "R"])
df_4['Pot'] = df_4['Pot'].str.replace('Pot: ', '', regex=True)
df_4['A0'] = df_4['A0'].str.replace('A0: ', '', regex=True)
df_4['U'] = df_4['U'].str.replace('U: ', '', regex=True)
df_4['R'] = df_4['R'].str.replace('R: ', '', regex=True)
df_4 = df_4.astype(float)

df_3 = pd.read_csv('data/vergleich/4151-103-up-cp.txt', sep=' - ', header=None, names=["Pot", "A0", "U", "R"])
df_3['Pot'] = df_3['Pot'].str.replace('Pot: ', '', regex=True)
df_3['A0'] = df_3['A0'].str.replace('A0: ', '', regex=True)
df_3['U'] = df_3['U'].str.replace('U: ', '', regex=True)
df_3['R'] = df_3['R'].str.replace('R: ', '', regex=True)
df_3 = df_3.astype(float)

df_2 = pd.read_csv('data/vergleich/4151-104-up-nm.txt', sep=' - ', header=None, names=["Pot", "A0", "U", "R"])
df_2['Pot'] = df_2['Pot'].str.replace('Pot: ', '', regex=True)
df_2['A0'] = df_2['A0'].str.replace('A0: ', '', regex=True)
df_2['U'] = df_2['U'].str.replace('U: ', '', regex=True)
df_2['R'] = df_2['R'].str.replace('R: ', '', regex=True)
df_2 = df_2.astype(float)

df_1 = pd.read_csv('data/vergleich/4151-103-up-nm.txt', sep=' - ', header=None, names=["Pot", "A0", "U", "R"])
df_1['Pot'] = df_1['Pot'].str.replace('Pot: ', '', regex=True)
df_1['A0'] = df_1['A0'].str.replace('A0: ', '', regex=True)
df_1['U'] = df_1['U'].str.replace('U: ', '', regex=True)
df_1['R'] = df_1['R'].str.replace('R: ', '', regex=True)
df_1 = df_1.astype(float)

x_1 = df_1.iloc[:, 0]
y_1 = df_1.iloc[:, 3]

x_2 = df_2.iloc[:, 0]
y_2 = df_2.iloc[:, 3]

x_3 = df_3.iloc[:, 0]
y_3 = df_3.iloc[:, 3]

x_4 = df_4.iloc[:, 0]
y_4 = df_4.iloc[:, 3]

plt.subplot(2, 2, 1)
plt.ylabel('Widerstand [$\Omega$]')
plt.plot(x_4, y_4, marker='o')
plt.xlabel('Potentiometer Stellung [0 - 2]')
plt.xticks([0, 1, 2])
plt.yticks([0, 200, 400, 600, 800, 1000, 1200])
plt.title("100 k$\Omega$ Poti normal")
plt.annotate('Minimum: 135 $\Omega$', xy=(0, 134.64), xytext=(0.5, 1000),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.subplot(2, 2, 2)
plt.plot(x_2, y_2, marker='o')
plt.xlabel('Potentiometer Stellung [253 - 255]')
plt.xticks([253, 254, 255])
plt.yticks([0, 200, 400, 600, 800, 1000, 1200])
plt.annotate('Minimum: 479 $\Omega$', xy=(255, 479.06), xytext=(253.5, 200),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.title("100 k$\Omega$ Poti umgekehrt")


plt.subplot(2, 2, 3)
plt.xlabel('Potentiometer Stellung [0 - 2]')
plt.ylabel('Widerstand [$\Omega$]')
plt.plot(x_3, y_3, marker='o')
plt.xticks([0, 1, 2])
plt.yticks([0, 50, 100, 150, 200, 250, 300])
plt.title("10 k$\Omega$ Poti normal")
plt.annotate('Minimum: 113 $\Omega$', xy=(0, 113.11), xytext=(0.5, 250),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.subplot(2, 2, 4)
plt.xlabel('Potentiometer Stellung [253 - 255]')
plt.plot(x_1, y_1, marker='o')
plt.xticks([253, 254, 255])
plt.yticks([0, 50, 100, 150, 200, 250, 300])
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.title("10 k$\Omega$ Poti umgekehrt")
plt.annotate('Minimum: 178 $\Omega$', xy=(255, 178.13), xytext=(253.5, 50),
            arrowprops=dict(facecolor='black', shrink=0.05))

#plt.show()

plt.tight_layout()

plt.savefig('results/Vergleich.svg', format='svg', dpi=1200)