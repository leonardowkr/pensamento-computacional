from LinhaTransporte import LinhaTransporte

class Aereo(LinhaTransporte):
    """
    Construtor da linha de transporte ferroviária
    """
    def __init__(self, origem: str, destino: str,  tipo_transporte: str, distancia: float, peso_cubagem: float) -> None:
        super().__init__(origem, destino, tipo_transporte, distancia, peso_cubagem)
        self.__tarifa_agencia = 3.5
        self.__tipo_transporte = "Aéreo"
    
    def getTarifa(self) -> float:
        return self.__tarifa_agencia
    
    def getTipoTransporte(self) -> str:
        return self.__tipo_transporte

    def __str__(self) -> str:
        info = super().__str__()
        info += f"Tarifa: R${self.getTarifa()}"
        info += f"Tipo de Transporte: {self.getTipoTransporte()}"
        return info

    def calcular_custo(self) -> float:
        """
        Método que cálcula o custo do transporte 
        ferroviário com base no peso, na tarfifa da agencia e na distância
        """
        calculo = self.__peso_cubagem * self.__tarifa_agencia * self.__distancia
        return calculo
