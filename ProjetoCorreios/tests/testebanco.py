import folium

# Coordenadas aproximadas reais
coordenadas = {
    "São Paulo": [-23.5505, -46.6333],
    "Campinas": [-22.9099, -47.0626],
    "Ribeirão Preto": [-21.1775, -47.8103]
}

rotas = [
    {"origem": "São Paulo", "destino": "Campinas", "via": "Rodovia dos Bandeirantes", "distancia": 95, "pedagio": True},
    {"origem": "Campinas", "destino": "Ribeirão Preto", "via": "Rodovia Anhanguera", "distancia": 220, "pedagio": True}
]

mapa = folium.Map(location=coordenadas["São Paulo"], zoom_start=7)

# Marcadores
for cidade, coord in coordenadas.items():
    folium.Marker(coord, popup=cidade).add_to(mapa)

# Traçar rotas
for trecho in rotas:
    origem = coordenadas[trecho["origem"]]
    destino = coordenadas[trecho["destino"]]
    texto = f"{trecho['via']} - {trecho['distancia']} km {'(Pedágio)' if trecho['pedagio'] else ''}"
    
    folium.PolyLine([origem, destino], color="blue", weight=4.5, popup=texto).add_to(mapa)

# Salva o mapa
mapa.save("rotograma_real_manual.html")
print("Rotograma gerado com sucesso!")
