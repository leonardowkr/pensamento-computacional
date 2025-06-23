from .LinhaTransporte import LinhaTransporte

class Rodoviario(LinhaTransporte):
    def __init__(self, origem: str, destino: str, distancia: float, peso: float) -> None:
        """
        Construtor da classe Rodoviario que herda da classe LinhaTransporte
        """
        super().__init__(origem, destino, distancia, peso)
        self.__tarifa_por_km = 1.5
        self.__tipo_transporte = "Rodoviário"

    def getTarifa(self) -> float:
        return self.__tarifa_por_km
    
    def getTipoTransporte(self) -> str:
        return self.__tipo_transporte
    
    def __str__(self):
        info = super().__str__()
        info += f"Tarifa: {self.getTarifa()} \n"
        info += f"Tipo de Transporte: {self.getTipoTransporte()} \n"
        return info

    def calcular_custo(self) -> float:
        calculo = self.getDistancia() * self.__tarifa_por_km  
        return round(calculo, 2)
