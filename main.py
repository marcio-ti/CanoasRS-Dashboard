from dash import Dash, page_container

from modulos.menu_lateral import *

app = Dash(external_stylesheets=[dbc.themes.SLATE], use_pages=True)

# ! APP - LAYOUT
app.layout = html.Div(
    children=[
        # ? MENU PRINCIPAL
        dbc.Nav(
            id="nav",
            class_name="d-flex aligns-items-center justify-content-center text-center mx-auto p-2",
            style={"background-color": "#040D12"},
            children=[
                # / PÁGINA -> HOME
                dbc.NavItem(
                    children=[dbc.NavLink("Home", href="/", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Educação", href="/educacao", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Saúde", href="/saude", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Trânsito", href="/transito", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Finanças", href="/financas", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Economia", href="/economia", class_name="text-light")]
                ),
                dbc.NavItem(
                    children=[dbc.NavLink("Eleições", href="/eleicoes", class_name="text-light")]
                ),
            ]),
        # =============================================================================================== #
        # ? LAYOUT
        html.Div(children=[page_container], className="mt-4")

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
    # app.run(
    #    host="0.0.0.0",
    #    port="8080",
    #    threaded=True,
    # )
