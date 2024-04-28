import pandas as pd
import folium
from folium.plugins import HeatMap


def escolas_markers(mapa):
    dados_escolas = pd.read_csv('dados/dados_escolas.csv', sep=';')

    for index, elemento in dados_escolas.iterrows():
        # Obtenha o nome da escola (chave do dicionário)
        nome_escola = elemento['ESCOLA']

        # Obtenha a latitude e longitude
        lat = elemento['LAT']
        long = elemento['LONG']
        folium.Marker(
            location=[lat, long], popup=nome_escola
        ).add_to(mapa)

    return mapa


def escolas_heat(mapa):
    dados_escolas = pd.read_csv('dados/dados_escolas.csv', sep=';')

    dados = []
    for index, elemento in dados_escolas.iterrows():
        # Obtenha a latitude e longitude
        lat = elemento['LAT']
        long = elemento['LONG']
        valor = elemento['IDEB']

        dados.append([lat, long, valor])

    mapa = HeatMap(dados).add_to(mapa)

    return mapa
