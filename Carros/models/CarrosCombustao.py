from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que representa um carro a combustão, herda de veículos
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float ,combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str) -> None:

        super().__init(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.nPortas = nPortas
        self.nAssentos = nAssentos
        self.nCilindradas = nCilindradas
        self.nCambio = nCambio
        