class Veiculos:
    """
    Classe com as principais funcionalidades do sistema de veiculos, como placas, veiculos, etc.
    """
    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, valor_fipe: float) -> None:
        """Construtor da classe Veiculo"""
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos =  f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos
    
    def getPlaca(self) -> str:
        """Retorna a placa do veiculo"""
        return self.__placa
    
    def setPlaca(self, placa) -> str:
        if(placa[:3].isalpha() and placa[3:4].isnumeric() and placa[5:].isnumeric()):
            self.__placa = placa
            print(f'Placa altearada para: {self.__placa}')
        else: 
            print('Placa inválida')
            
    def setValorFipe(self, valor):
        """
            Método que altera o valor da Fipe do veículo

            Argumento: valor (float): novo valor da Fipe
            Saída: True se ok
        """
        self.__valor_fipe = valor
        return True
    
    def calcular_consumo():
        print("metodo somente disponível para subclasses")

    def __eq__(self, placa_dois):
        if(self.__placa == placa_dois.getPlaca()):
            
            return True
        else: 
           
            return False