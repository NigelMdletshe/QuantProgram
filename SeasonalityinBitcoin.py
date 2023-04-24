import pandas as pd
import plotly.graph_objects as go


def trp(l,n):
    return l[:n] + [None]*(n-len(l))

df = pd.read_csv("BCHAIN-MKPRU.csv")[["Date","Value"]]
df["Date"] = pd.to_datetime(df["Date"])
df.sort_values(by="Date",inplace = True)
df.set_index("Date",inplace=True)
df = df.resample("1M").last()

df = df.pct_change()
df["Value"]*=100

z_vals = [list(df["Value"])[i: i+12] for i in range(0,len(df),12)]

z_vals = [trp(x,12) for x in z_vals]


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Sep','Oct','Nov','Dec']
years = [str(x) for x in range(2009,2022)]

fig = go.Figure(data=go.Heatmap(
    z = z_vals,
    x = months,
    y= years,
    zmax=100,
    zmin=-20,
    zsmooth="best"
))

fig.show()
#heat wave graph not shown, there is an error, check adblock and firewall