from models.Veiculo import Veiculo

class Proprietario(Veiculo):
    def __init__(self, cpf, placa):
        self.__cpf__ = cpf
        self.__placa__ = placa
        
    def criar_proprietario(self, veiculo: Veiculo, cpf):
        # Lógica para criar um novo proprietário
        self.__placa__ = veiculo.get_placa()
        self.__cpf__ = cpf
        
    def validar_proprietario(self):
        # Lógica para validar os dados do proprietário
        pass

    def adicionar_veiculo(self, placa):
        # Lógica para adicionar um veículo ao proprietário
        self.__placa = placa
        

    def remover_veiculo(self, placa):
        # Lógica para remover um veículo do proprietário
        self.__placa = None