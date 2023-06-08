import numpy as np
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()

r2 = 0.05
r3 = 0.0075
r4 = 0.001

i = np.linspace(0, 20, 20)
iQuadrat = np.square(i)

p2 = iQuadrat*r2
p3 = iQuadrat*r3
p4 = iQuadrat*r4

u2 = i*r2*1000
u3 = i*r3*1000
u4 = i*r4*1000

color = 'tab:red'
ax1.set_xlabel('Strom [A]')
ax1.set_ylabel('Verlustleistung [W]', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0,2)

ax1.plot(i, p2, marker='^', color=color)
ax1.plot(i, p3, marker='s', color=color)
ax1.plot(i, p4, marker='d', color=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Spannungsfall [mV]', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0,200)

ax2.plot(i, u2, marker='^', color=color)
ax2.plot(i, u3, marker='s', color=color)
ax2.plot(i, u4, marker='d', color=color)

plt.legend(['0.05 Ohm','0.0075 Ohm','0.001 Ohm'], loc='upper left')

plt.tight_layout()

#plt.show()

plt.savefig('results/shunt_loss.svg', format='svg', dpi=1200)
plt.clf()