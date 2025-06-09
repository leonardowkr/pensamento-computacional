# Modelo usado como teste

class LinhaTransporte:
    def __init__(self, rota: str,  tipo_transporte: str, distancia: float, peso_cubagem: float) -> None: 
        """
        Classe construtora do simulador de custo
        """
        self.__rota = rota
        self.__tipo_transporte = tipo_transporte
        self.__distancia = distancia
        self.__peso_cubagem = peso_cubagem
    
    def calcular_custo(self):
        pass