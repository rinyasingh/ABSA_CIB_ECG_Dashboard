# # dash
# dash ==1.20.0
# dash-bootstrap-components==0.12.2

# #random data
# names == 0.3.0

# #data processing
# numpy==1.19.5
# pandas==1.1.5

# #plotting
# plotly==4.14.3

# #read and writing excel files
# openpyxl == 3.0.7
# xlrd== 1.2.0
## LIBRARIES: html, dcc
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import numpy as np 
import plotly.express as px

df = pd.read_csv('avocado-updated-2020.csv')

app = Dash()
geo_dropdown = dcc.Dropdown(options=df['geography'].unique(), value = 'New York')

# Div component to hold three Dash component children 
app.layout = html.Div(children = [
    html.H1(children='Avocado Prices Dashboard'), 
    geo_dropdown, dcc.Graph(id='price-graph'), 
    dcc.Graph (
        id = 'example-graph',
        figure = {
            'data': [
                {'x':[1,2,3], 'y': [4,1,2], 'type':   'bar', 'name': 'Delhi'},
                {'x':[1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': 'Jhb' },
            ]
        }
    )])
# decorator
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id = geo_dropdown, component_property='value')
)
def update_graph (selected_geography):
    filtered_avocado = df[df['geography']== selected_geography]
    line_fig = px.line(filtered_avocado,
        x = 'date', y = 'average_price',
        color = 'type',
        title = f'Avocado Prices in {selected_geography}')
    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)