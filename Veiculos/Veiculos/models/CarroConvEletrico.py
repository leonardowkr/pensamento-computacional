from .CarrosCombustao import CarrosCombustao

class CarroConvEletrico(CarrosCombustao, CarroEletrico): 
    """
    Classes que implementa métodos específicos de um carro convertido em Elétrico
    """
    
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, combustivel, nPortas, nAssentos, nCilindrada, nCambio, nivel_combustivel, nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, combustivel, nPortas, nAssentos, nCilindrada, nCambio, nivel_combustivel)
        CarroEletrico.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, nPortas, nAssentos, nivel_bateria, tipo_bateria, autonomia)
    def __str__(self):
        info = super().__str__()
        info += f"Nível de bateria: {self.__nivel_bateria}"
        info += f"Tipo de bateria: {self.__tipo_bateria}"
        info += f"Autonomia: {self.__autonomia}"
        return super().__str__()
    
    def abastecer(self, percentual_adicionado: False) -> bool:
        """
        Método abastecer desativado
        Args:
            percentual_adicionado
        Return: 
            False, pois não pode abastecer
        """
        print("Carro convertido para elétrico! Não é mais possível abastecer!")
        return False