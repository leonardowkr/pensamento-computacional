from geopy.geocoders import Nominatim
from geopy.distance import geodesic


def calcular_distancia(origem: str, destino: str) -> float:
    geolocator = Nominatim(user_agent="geoapiExcercise")

    lat1, long1 = geolocator.geocode(origem).latitude, geolocator.geocode(destino).longitude
    lat2, long2 = geolocator.geocode(destino).latitude, geolocator.geocode(destino).longitude

    distancia = geodesic((lat1, long1), (lat2, long2)).kilometers
    return distancia
