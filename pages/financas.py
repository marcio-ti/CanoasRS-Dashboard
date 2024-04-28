import dash
from dash import register_page, html

register_page(
    __name__, path="/financas", title="Finanças Públicas", name="Finanças Públicas"
)

layout = html.Div()