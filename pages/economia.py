import dash
from dash import register_page, html

register_page(
    __name__, path="/economia", title="Economia", name="Economia"
)

layout = html.Div()