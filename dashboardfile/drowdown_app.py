import plotly.express as px
import pandas as pd

from plotly.graph_objs import layout
from dash import dcc, Output, Input
from dash import html

from django_plotly_dash import DjangoDash

datasets = {
    'Date'   : ['2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', '2021-09-05', '2021-09-06'],
    'SamSung': [45000, 51000, 42000, 50000, 61500, 53000],
    'Naver'  : [120500, 132000, 155000, 140000, 141500, 123000],
    'SinHan' : [30000, 35000, 33000, 32000, 38000, 40000],
}
df = pd.DataFrame(datasets)

# fig = px.line(df, x = 'Date', y = df.columns[1:4])
# fig.update_layout(template = layout.Template())

app = DjangoDash('Dropdown')
app.layout = html.Div(children = [
    dcc.Dropdown(id = 'stock_name',
                 options = [{ 'label': x, 'value': x } for x in df.columns[1:4]],
                 value = df.columns[1],
                 clearable = False,
                 ),
    dcc.Graph(id = "time-series-chart"),
])


@app.callback(
    Output("time-series-chart", 'figure'),
    [Input("stock_name", "value")]
)
def create_figure(stock_name):
    fig = px.line(df, x = 'Date', y = stock_name)
    return fig
