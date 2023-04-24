import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date",inplace = True)
print(df)