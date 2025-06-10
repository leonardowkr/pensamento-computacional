# Modelo usado como teste
class LinhaTransporte:
    def __init__(self, rota: str, distancia: float, peso_cubagem: float) -> None: 
        """
        Classe construtora do simulador de custo
        """
        self.__rota = rota
        self.__distancia = distancia
        self.__peso_cubagem = peso_cubagem
    

    def getRota(self):
        return self.__rota
    
    def getDistancia(self):
        return self.__distancia

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