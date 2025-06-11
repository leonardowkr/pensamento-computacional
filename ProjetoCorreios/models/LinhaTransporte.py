# Modelo usado como teste
class LinhaTransporte:
    def __init__(self, distancia: float, peso_cubagem: float, origem: str, destino: str) -> None: 
        """
        Classe construtora do simulador de custo
        """
        self.__origem = origem
        self.__destino = destino
        self.__distancia = distancia
        self.__peso_cubagem = peso_cubagem
    
    
    def getDistancia(self):
        return self.__distancia
    
    def getOrigem(self):
        return self.__origem
    
    def getDestino(self):
        return self.__destino

    def getPesoCubagem(self):
        return self.__peso_cubagem

    def __str__(self) -> str:
        """
        
        """
        info = f"Rota: {self.getRota()}"
        info += f"Distância: {self.getDistancia()} Km"
        info += f"Peso/Cubagem: {self.getPesoCubagem()}"


    def calcular_custo(self):
        pass