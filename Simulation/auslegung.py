import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/auslegungSimulation3.csv")

# Create the 2D scatter plot
cax = plt.scatter(df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = plt.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
plt.xticks([100,200,300,400,500])
plt.yticks([1,2,3,4,5,6,7,8,9,10])
plt.xlabel('Entladeleistung [W]')
plt.ylabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation3.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation2.csv")

# Create the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([400,500,600,700])
ax.set_yticks([100,200,300,400])
ax.set_zticks([0.9,1,1.1,1.2])
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation2.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation1.csv")

# Create the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([100,200,300,400,500,600,700])
ax.set_yticks([100,200,300,400,500,600,700,800,900,1000])
ax.set_zticks([0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,2,3])
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation1.svg', format='svg', dpi=1200)
plt.clf()