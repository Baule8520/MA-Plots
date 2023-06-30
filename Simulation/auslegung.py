import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/auslegungSimulation3.csv")

fig, ax1 = plt.subplots()

# Create the 2D scatter plot
ax1.plot(df["capacity"], df["ssr"]*100, color="orange")

ax2 = ax1.twinx()

plt.plot(df["capacity"], df["scr"]*100, color="tab:blue")

ax1.set_xlabel('Akkukapazität [kWh]')
ax1.set_ylabel('Autarkiegrad [%]')
ax1.set_ylim([19.5,35.5])
ax2.set_ylim([65,105])
ax2.set_ylabel('Eigenverbrauchsanteil [%]')

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

df = pd.read_csv("data/auslegungSimulation4.csv")

# Create the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([400,500,600,700,800])
ax.set_yticks([400,500,600,700,800])
ax.set_zticks([0.75, 1, 1.25, 1.5])
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation4.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation5.csv")

# Create the 3D scatter plot
cax = plt.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, c=df["ssr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([400,500,600,700,800])
ax.set_yticks([100,200,300,400,500])
plt.xlabel('Ladeleistung [W]')
plt.ylabel('Entladeleistung [W]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation5.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation6.csv")

# Create the 3D scatter plot
cax = plt.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, c=df["ssr"]*100, cmap='viridis', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([500,600,700,800])
ax.set_yticks([200,300,400,500])
plt.xlabel('Ladeleistung [W]')
plt.ylabel('Entladeleistung [W]')

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation6.svg', format='svg', dpi=1200)
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