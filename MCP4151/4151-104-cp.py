import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df_1 = pd.read_csv('data/pot_u/4151-104-up-cp.txt', sep=' - ', header=None, names=["Pot", "A0", "U"])
df_1['Pot'] = df_1['Pot'].str.replace('Pot: ', '', regex=True)
df_1['A0'] = df_1['A0'].str.replace('A0: ', '', regex=True)
df_1['U'] = df_1['U'].str.replace('U: ', '', regex=True)
df_1 = df_1.astype(float)
#print(df_1)

df_2 = pd.read_csv('data/pot_r/4151-104-up-cp.txt', sep=' - ', header=None, names=["Pot", "A0", "U", "R"])
df_2['Pot'] = df_2['Pot'].str.replace('Pot: ', '', regex=True)
df_2['A0'] = df_2['A0'].str.replace('A0: ', '', regex=True)
df_2['U'] = df_2['U'].str.replace('U: ', '', regex=True)
df_2['R'] = df_2['R'].str.replace('R: ', '', regex=True)
df_2 = df_2.astype(float)
#print(df_2)

x_1 = df_1.iloc[:, 0]
#print(x_1)
y_1 = df_1.iloc[:, 2]
#print(y_1)

x_2 = df_2.iloc[:, 0]
y_2 = df_2.iloc[:, 3]

fig, ax1 = plt.subplots()

ax1.set_xlabel('Potentiometer Stellung [0 - 255]')
ax1.set_ylabel('Spannung [V]')
ax1.set_xlim(0, 255)
ax1.set_ylim(0, 5)
ax1.plot(x_1, y_1, color='black')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Widerstand [Ohm]', color=color)  # we already handled the x-label with ax1
ax2.set_ylim(0, 130000)
ax2.plot(x_2, y_2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.show()

plt.savefig('results/4151-104-cp.svg', format='svg', dpi=1200)