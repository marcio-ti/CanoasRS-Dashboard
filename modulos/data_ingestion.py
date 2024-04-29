import pandas as pd
import folium
from folium.plugins import HeatMap






def escolas_markers(mapa):
    dados_escolas = pd.read_excel('dados/escolas.xlsx')

    for index, elemento in dados_escolas.iterrows():
        nome_escola = elemento['ESCOLA']
        lat = elemento['LAT']
        long = elemento['LONG']
        rede = elemento['REDE']

        if pd.notnull(lat) and pd.notnull(long):
            if rede == 'Municipal':
                escola_municipal = folium.CustomIcon(
                    icon_image='assets/icons/escola_municipal.png',
                    icon_size=(25, 25)
                )
                folium.Marker(
                    location=[lat, long], popup=nome_escola, icon=escola_municipal
                ).add_to(mapa)
            elif rede == 'Estadual':
                escola_estadual = folium.CustomIcon(
                    icon_image='assets/icons/escola_estadual.png',
                    icon_size=(25, 25)
                )
                folium.Marker(
                    location=[lat, long], popup=nome_escola, icon=escola_estadual
                ).add_to(mapa)

    return mapa



def escolas_heat(mapa):
    dados_escolas = pd.read_excel('dados/escolas.xlsx')

    dados = []
    for index, elemento in dados_escolas.iterrows():
        lat = elemento['LAT']
        long = elemento['LONG']
        valor = elemento['IDEB']

        if pd.notnull(lat) and pd.notnull(long) and pd.notnull(valor):
            dados.append([lat, long, valor])

    HeatMap(dados).add_to(mapa)

    return mapa
