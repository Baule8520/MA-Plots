import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./total_act_power.csv")

x = pd.to_datetime(df["time"])

plt.plot(x, df["total_act_power"])

plt.xlabel('Referenzspannung [V]')
plt.ylabel('ADC-Spannung [V]')

plt.show()

#plt.savefig('results/arduino_55v_adc.svg', format='svg', dpi=1200)
#plt.clf()
