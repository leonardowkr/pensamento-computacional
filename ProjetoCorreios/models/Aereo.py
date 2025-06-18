from .LinhaTransporte import LinhaTransporte

class Aereo(LinhaTransporte):
    """
    Construtor da linha de transporte ferroviária
    """
    def __init__(self, origem: str, destino: str, distancia: float, peso: float) -> None:
        super().__init__(origem, destino, distancia, peso)
        self.__tarifa_por_km = 2
        self.__tipo_transporte = "Aéreo"
    
    def getTarifa(self) -> float:
        return self.__tarifa_por_km
    
    def getTipoTransporte(self) -> str:
        return self.__tipo_transporte

    def __str__(self) -> str:
        info = super().__str__()
        info += f"Tarifa: R${self.getTarifa()} \n"
        info += f"Tipo de Transporte: {self.getTipoTransporte()} \n"
        return info

    def calcular_custo(self) -> float:
        """
        Método que cálcula o custo do transporte 
        ferroviário com base no peso, na tarfifa da agencia e na distância
        """
        calculo = self.__tarifa_por_km * self.getDistancia()
        return calculo
