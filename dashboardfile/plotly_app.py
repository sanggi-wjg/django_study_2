import plotly.express as px
import pandas as pd

from plotly.graph_objs import layout
from dash import dcc, Output, Input
from dash import html

from django_plotly_dash import DjangoDash

# Example 1
df = pd.DataFrame({
    "Fruit" : ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City"  : ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
fig = px.bar(df, x = "Fruit", y = "Amount", color = "City", barmode = "group")

app = DjangoDash('DashboardSample', external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div(children = [
    html.H3(children = 'Dashboard 1'),
    html.Div(children = 'Dash: A web application framework for Python.'),
    dcc.Graph(id = 'example-graph', figure = fig)
])

# Example 2
datasets = {
    'Date'   : ['2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', '2021-09-05', '2021-09-06'],
    'SamSung': [45000, 51000, 42000, 50000, 61500, 53000],
    'Naver'  : [120500, 132000, 155000, 140000, 141500, 123000],
    'SinHan' : [30000, 35000, 33000, 32000, 38000, 40000],
}
dataframe = pd.DataFrame(datasets)
# dataframe['Date'] = ['2021-09-01', '2021-09-02', '2021-09-03', '2021-09-04', '2021-09-05', '2021-09-06']
# dataframe['SamSung'] = [45000, 51000, 42000, 50000, 61500, 53000]
# dataframe['Naver'] = [120500, 132000, 155000, 140000, 141500, 123000]
# dataframe['SinHan'] = [30000, 35000, 33000, 32000, 38000, 40000]

fig = px.line(dataframe, x = 'Date', y = dataframe.columns[1:4])
fig.update_layout(template = layout.Template())

app = DjangoDash('StockExample')
app.layout = html.Div(children = [
    html.H3(children = 'Dashboard 2'),
    dcc.Graph(figure = fig),
    html.Button('Download Excel', id = 'btn_download_xlsx'),
    dcc.Download(id = 'download-dataframe-xlsx')
])


@app.callback(
    Output('download-dataframe-xlsx', 'data'),
    Input("btn_download_xlsx", "n_clicks"),
    prevent_initial_call = True,
)
def callback_btn_download_xlsx(n_clicks):
    return dcc.send_data_frame(dataframe.to_excel, "sample.xlsx")

# Example 3
# df = px.data.gapminder().query("country in ('Korea, Rep.', 'China', 'Japan')")
# print(df)
