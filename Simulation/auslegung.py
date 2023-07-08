import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/auslegungSimulation3.csv")

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

twin1 = ax.twinx()
twin2 = ax.twinx()

# Offset the right spine of twin2.  The ticks and label have already been
# placed on the right by twinx above.
twin2.spines.right.set_position(("axes", 1.2))

p1, = ax.plot(df["capacity"], df["costs"], "C0", label="Stromkosten")
p2, = twin1.plot(df["capacity"], df["ssr"]*100, "C1", label="Autarkiegrad")
p3, = twin2.plot(df["capacity"], df["scr"]*100, "C2", label="Eigenverbrauchsanteil")

ax.set(xlim=(0, 4), ylim=(635, 705), xlabel="Akkukapazität [kWh]", ylabel="Stromkosten [€]")
twin1.set(ylim=(19.5,28.5), ylabel="Autarkiegrad [%]")
twin2.set(ylim=(68,102), ylabel="Eigenverbrauchsanteil [%]")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())

ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())

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
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='brg', label='Data Points')

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
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='brg', label='Data Points')

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
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter3D(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["ssr"]*100, c=df["ssr"]*100, cmap='brg')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel("Eigenverbrauchsanteil [%]")

ax.set_xticks([400,500,600,700,800])
ax.set_yticks([100,200,300,400,500])

# Show the plot
plt.tight_layout()
# plt.show()

plt.savefig('results/auslegungSimulation5.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation6.csv")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter3D(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["scr"]*100, c=df["scr"]*100, cmap='brg')

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
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='brg', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([100,200,300,400,500,600,700,800,900,1000])
ax.set_yticks([100,200,300,400,500,600,700,800,900,1000])
#ax.set_zticks([0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,2,3])
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
#plt.show()

plt.savefig('results/auslegungSimulation1.svg', format='svg', dpi=1200)
plt.clf()

###########################################################################################

df = pd.read_csv("data/auslegungSimulation7.csv")

# Create the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
cax = ax.scatter(df["max_power_charging"]*1000, df["max_power_discharging"]*1000, df["capacity"], c=df["scr"]*100, cmap='brg', label='Data Points')

# Add a legend
cbar = fig.colorbar(cax)
cbar.set_label("Eigenverbrauchsanteil [%]")

# Add labels and title
ax.set_xticks([100,300,500,700,900,1100])
ax.set_yticks([100,300,500,700,900,1100])
#ax.set_zticks([0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,2,3])
ax.set_xlabel('Ladeleistung [W]')
ax.set_ylabel('Entladeleistung [W]')
ax.set_zlabel('Akkukapazität [kWh]')

# Show the plot
plt.tight_layout()
plt.show()

#plt.savefig('results/auslegungSimulation7.svg', format='svg', dpi=1200)
plt.clf()