import dash
from dash import dbc

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True