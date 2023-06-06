import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./data/total_act_power.csv")

x = pd.to_datetime(df["time"])

plt.plot(x, df["total_act_power"])

plt.ylabel('Haushaltsleistung [W]')

#plt.show()

plt.savefig('./results/haushaltsleistung.svg', format='svg', dpi=1200)
plt.clf()
