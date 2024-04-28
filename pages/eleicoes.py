import dash
from dash import register_page, html

register_page(
    __name__, path="/eleicoes", title="Eleições", name="Eleições"
)

layout = html.Div()