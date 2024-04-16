import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from aplicacao import aplicacao
import plotly.express as px
px.set_mapbox_access_token(open('pk.eyJ1IjoibWFyY2lvZWNuMjIiLCJhIjoiY2x2MmtzbTJnMGhpOTJqcGxzM2RrZHE5ZiJ9.V73G6bQtMUOxQlHU02oXJg').read())


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],)

app.layout = html.Div([
    aplicacao()
])

# ! SERVIDOR
if __name__ == "__main__":
    app.run(
        debug=True,
        port="8050",
        dev_tools_ui=True,
        dev_tools_hot_reload=True,
        threaded=True,
    )
    #app.run(
    #    host="0.0.0.0",
    #    port="8080",
    #    threaded=True,
    #)