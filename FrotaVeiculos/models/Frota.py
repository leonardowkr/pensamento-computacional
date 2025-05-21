class Frota():
    def __init__(self, veiculo):
        self.__frota = [veiculo]

    def adicionar_veiculos(self, veiculo):
        self.__frota.append(veiculo)
        
    def listar_veiculos(self):
        for veiculo in self.__frota:
            print(veiculo)

    def calc_consumo_total(self, distancia):
        consumo_total = 0
        for veiculo in self.__frota:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total