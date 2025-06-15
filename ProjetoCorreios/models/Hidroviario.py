from LinhaTransporte import LinhaTransporte

class Hidroviario(LinhaTransporte):
    def __init__(self, origem: str, destino: str, distancia: float, peso_cubagem: float) -> None:
        """
        Construtor da classe Hidroviario que herda da classe LinhaTransporte
        """
        super().__init__(origem, destino, distancia, peso_cubagem)
        self.__tarifa_por_km = 0.9
        self.__tipo_transporte = "Hidroviario"

    def getTarifa(self) -> float:
        return self.__tarifa_por_km
    
    def getTipoTransporte(self) -> str:
        return self.__tipo_transporte
    
    def setTarifa(self, nova_tarifa):
        self.__tarifa_por_km = nova_tarifa
        return self.__tarifa_por_km

    def __str__(self):
        info = super().__str__()
        info += f"Tarifa: {self.getTarifa()}"
        info += f"Tipo de Transporte: {self.getTipoTransporte()}"

    def calcular_custo(self) -> float:
        calculo = self.__distancia * self.__tarifa_por_km + self.__peso_cubagem * 2
        return calculo
