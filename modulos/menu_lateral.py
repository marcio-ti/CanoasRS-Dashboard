from dash import html, dcc
import dash_bootstrap_components as dbc



menu_educacao = html.Div(children=[
    dcc.Dropdown(
        id='dp_area',
        placeholder='Selecione um item',
        options=['LOCALIZAÇÃO ESCOLAS', 'IDEB']
    )
])