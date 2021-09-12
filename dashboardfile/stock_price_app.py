import plotly.express as px
import pandas as pd

from plotly.graph_objs import layout
from dash import dcc, Output, Input
from dash import html

from django_plotly_dash import DjangoDash

from sample.models import StockPrice, Stocks

# ['033780', '035420', '005930']
stock = Stocks.objects.filter(stock_code = '005930')
stock_prices = StockPrice.objects.values('close_price', 'date', 'stocks_id').filter(stocks_id__in = stock).order_by('date')

# def get_each_stock_price(stock_id):
#     data = []
#     for price in stock_prices:
#         if price['stocks_id'] == stock_id:
#             data.append(price['close_price'])
#     return data


df = pd.DataFrame()
df['Date'] = [s['date'] for s in stock_prices]
df[stock[0].stock_name] = [s['close_price'] for s in stock_prices]

fig = px.line(df, x = 'Date', y = df.columns[1:2])
fig.update_layout(template = layout.Template())

app = DjangoDash('StockPriceSample')
app.layout = html.Div(children = [
    dcc.Graph(figure = fig),
])
# TODO : React 로 stock_code 변경 해서 가져 오는 것도 해보자