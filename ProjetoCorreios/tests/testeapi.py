from geopy.geocoders import Nominatim
from geopy.distance import geodesic


geolocator = Nominatim(user_agent="geoapiExcercise")

lat1, long1 = geolocator.geocode("RS").latitude, geolocator.geocode("RS").longitude
lat2, long2 = geolocator.geocode("SP").latitude, geolocator.geocode("SP").longitude

distancia = geodesic((lat1, long1), 
                     (lat2, long2)).kilometers

print(distancia)
