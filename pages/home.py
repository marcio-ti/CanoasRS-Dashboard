import dash
from dash import register_page, html

register_page(
    __name__, path="/", title="Home", name="Home"
)

layout = html.Div()