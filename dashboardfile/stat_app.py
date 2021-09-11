import plotly.express as px
import pandas as pd

from plotly.graph_objs import layout
from dash import dcc, Output, Input
from dash import html

from django_plotly_dash import DjangoDash

df = pd.DataFrame()

# fig = px.line(df, x = 'Date', y = df.columns[1:3])
# fig.update_layout(template = layout.Template())

# app = DjangoDash('StatSample')
# app.layout = html.Div(children = [
#     dcc.Graph(figure = fig),
# ])
