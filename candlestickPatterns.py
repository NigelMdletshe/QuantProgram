import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv("BTCUSD_1h.csv")
df= df.iloc[::-1]
df['date']=pd.to_datetime(df['date'])
df['20wma']=df['close'].rolling(window=140).mean()

fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['open'],high=df['high'],
                low=df['low'],close=df['close'])])

fig.add_trace(
    go.Scatter(
        x=df['date'],
        y=df['close'],
        line=dict(color='blue'),
        name = "20-week MA" 
        )
)


fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
fig.update_layout(yaxis_title ="Bitcoin Price (USD)", xaxis_title ="Date")
fig.update_yaxes(type="log")
fig.show()

#there is a dug, the graph is not printing in chrome 