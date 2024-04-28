import folium
from folium import TileLayer, LayerControl
from dash import callback, Input, Output, State, register_page
from modulos.menu_lateral import *
from modulos.data_ingestion import escolas_markers, escolas_heat


register_page(
    __name__, path="/educacao", title="Educação", name="Educação"
)



# Gerando arquivo do Mapa
mapa_canoas = folium.Map(location=(-29.9127397, -51.1923038), zoom_start=13)

mapa_canoas.save("mapa.html")

# --------------------------------------------------------------------------------------------
layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            className="mt-3",
            children=[
                dbc.Col(
                    width=3,
                    id='menu_lateral',
                    children=[menu_educacao]
                ),
                dbc.Col(
                    width=9,
                    id='coluna_mapa',
                    children=[
                        html.Div(id="map")
                    ]),

            ]
        ),

    ]
)


@callback(
    Output("map", "children"),
    Input("dp_area", "value"),
    State("map", "id")
)
def educacao(area_selecionada, _):
    mapa_canoas = folium.Map(
        location=(-29.9127397, -51.1923038),
        zoom_start=13
        )


    if area_selecionada == 'LOCALIZAÇÃO ESCOLAS':
        mapa_canoas = escolas_markers(mapa_canoas)
        mapa_canoas.save("mapa.html")
        mapa_html = html.Iframe(srcDoc=open('mapa.html', 'r').read(),
                                style={
                                    'width': '100%',
                                    'height': '650px',
                                    'border-radius': '5px',
                                    'border': 'solid 1px grey'
                                })
        return mapa_html
    elif area_selecionada == 'IDEB':
        mapa_canoas = escolas_heat(mapa_canoas)
        mapa_canoas.save("mapa.html")
        mapa_html = html.Iframe(srcDoc=open('mapa.html', 'r').read(),
                                style={
                                    'width': '100%',
                                    'height': '650px',
                                    'border-radius': '5px',
                                    'border': 'solid 1px grey'
                                })
        return mapa_html
    elif area_selecionada is None:
        mapa_canoas.save("mapa.html")

        mapa_html = html.Iframe(srcDoc=open('mapa.html', 'r').read(),
                                style={
                                    'width': '100%',
                                    'height': '650px',
                                    'border-radius': '5px',
                                    'border': 'solid 1px grey'
                                })
        return mapa_html
