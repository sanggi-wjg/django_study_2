import plotly.express as px
import pandas as pd

from plotly.graph_objs import layout
from dash import dcc, Output, Input
from dash import html

from django_plotly_dash import DjangoDash

from sample.models import StockPrice, Stocks

dataframe = pd.DataFrame()

for code in ['033780', '035420', '005930']:
    stock = Stocks.objects.filter(stock_code = code)
    stock_prices = StockPrice.objects.values('close_price', 'date', 'stocks_id').filter(stocks_id__in = stock).order_by('date')

    df = pd.DataFrame()
    # df['Date'] = [s['date'] for s in stock_prices]
    df[stock[0].stock_name] = [s['close_price'] for s in stock_prices]
    dataframe = pd.concat([dataframe, df])

print(dataframe.tail(n = 10))

fig = px.line(dataframe, y = dataframe.columns)
fig.update_layout(template = layout.Template())

app = DjangoDash('StockPriceScatterSample')
app.layout = html.Div(children = [
    dcc.Graph(figure = fig),
])
