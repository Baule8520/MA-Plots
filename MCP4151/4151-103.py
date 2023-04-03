import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/pot_u/4151-103-up-nm.txt', sep=' - ', header=None, names=["Pot", "A0", "U"])
df['Pot'] = df['Pot'].str.replace('Pot: ', '', regex=True)
df['A0'] = df['A0'].str.replace('A0: ', '', regex=True)
df['U'] = df['U'].str.replace('U: ', '', regex=True)
df = df.astype(float)
#print(df)

x_1 = df.iloc[:, 0]
#print(x_1)

y_1 = df.iloc[:, 2]
#print(y_1)

plt.figure()
plt.plot(x_1, y_1)

plt.xlabel('Potentiometer Stellung')
plt.ylabel('Spannung [V]')

plt.show()