import dash
from dash import register_page, html

register_page(
    __name__, path="/transito", title="Trânsito", name="Trânsito"
)

layout = html.Div()