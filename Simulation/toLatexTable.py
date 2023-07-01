import pandas as pd

df = pd.read_csv("data/auslegungSimulation3.csv")

print(df)

df["ssr"] = df["ssr"] * 100
df["scr"] = df["scr"] * 100

df.round(2)

print(df)

df.to_excel("./data/latex.xlsx")