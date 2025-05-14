class Veiculos:
    """
    Classe com as principais funcionalidades do sistema de veículos, como placa
    """
    def __init__ (self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:

    def __str__(self):
        """Retorna uma string com as informações do veículo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
    
    def 