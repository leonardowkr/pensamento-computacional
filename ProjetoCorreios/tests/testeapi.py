import folium

# Coordenadas reais das cidades
coordenadas = {
    "São Paulo": [-23.5505, -46.6333],
    "Campinas": [-22.9099, -47.0626],
    "Ribeirão Preto": [-21.1775, -47.8103],
    "Belo Horizonte": [-19.9167, -43.9345]
}

# Dados do rotograma conforme o tutorial
rotas = [
    {"origem": "São Paulo", "destino": "Campinas", "rodovia": "Rod. dos Bandeirantes", "distancia": 95, "pedagio": True},
    {"origem": "Campinas", "destino": "Ribeirão Preto", "rodovia": "Rod. Anhanguera", "distancia": 220, "pedagio": True},
    {"origem": "Ribeirão Preto", "destino": "Belo Horizonte", "rodovia": "Rod. BR-381", "distancia": 570, "pedagio": True}
]

# Cria o mapa
mapa = folium.Map(location=coordenadas["São Paulo"], zoom_start=6)

# Adiciona marcadores
for cidade, coord in coordenadas.items():
    folium.Marker(coord, popup=cidade).add_to(mapa)

# Desenha rotas entre as cidades
for trecho in rotas:
    ori = coordenadas[trecho["origem"]]
    dst = coordenadas[trecho["destino"]]
    popup = f"{trecho['rodovia']} – {trecho['distancia']} km"
    if trecho["pedagio"]:
        popup += " (Pedágio)"
    folium.PolyLine([ori, dst], color="blue", weight=4, popup=popup).add_to(mapa)

# Salva o rotograma
mapa.save("rotograma_real_manual.html")
print("Rotograma gerado: rotograma_real_manual.html")
