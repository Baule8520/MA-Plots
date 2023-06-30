import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/auslegungSimulation2.csv")

df = df.drop(columns=["simulation", "total_demand", "total_generation", "costs"])
df = df.drop(df.columns[0], axis=1)

print(df)

# Create the parallel coordinates plot
plt.figure(figsize=(10, 6))
pd.plotting.parallel_coordinates(df, "capacity", colormap='rainbow')

# Add a legend
plt.legend(loc='lower right')

# Add labels
plt.xlabel('Variables')
plt.ylabel('kW bzw. %')

# Show the plot
plt.show()