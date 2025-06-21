# Modelo usado como teste
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class LinhaTransporte:
    def __init__(self, origem: str, destino: str, distancia: str, peso = float) -> None: 
        """
        Método construtor da classe linha de transporte
        """
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        self.__peso = peso
    
    
    def getDistancia(self):
        return self.__distancia
    
    def getOrigem(self):
        return self.__origem
    
    def getDestino(self):
        return self.__destino

    def getPeso(self):
        return self.__peso

    def __str__(self) -> str:
        """
        
        """
        info = f"Distância: {self.getDistancia()} Km \n"
        info += f"Origem: {self.getOrigem()} \n"
        info += f"Destino: {self.getDestino()} \n"
        info += f"Peso: {self.getPeso()} Kg"
        return info


    def calcular_custo(self):
        pass