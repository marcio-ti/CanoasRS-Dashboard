import dash
from dash import register_page, html

register_page(
    __name__, path="/saude", title="Saúde", name="Saúde"
)

layout = html.Div()