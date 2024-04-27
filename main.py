import dash_bootstrap_components as dbc
import dash_leaflet as dl
from dash import Dash, html

app = Dash()

app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Card(
            id='card-map',
            children=[
            dl.Map(
                dl.TileLayer(),
                id='mapa',
                center=[-29.9160182, -51.1795255],
                zoom=13,
                style={'height': '600px'})
        ])

    ]
)

# ! SERVIDOR
if __name__ == "__main__":
    app.run(
        debug=True,
        port="8050",
        dev_tools_ui=True,
        dev_tools_hot_reload=True,
        threaded=True,
    )
    # app.run(
    #    host="0.0.0.0",
    #    port="8080",
    #    threaded=True,
    # )
