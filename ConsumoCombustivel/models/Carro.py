from .Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe):
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        eficienciaMedia = 12
        self.eficienciaMedia = eficienciaMedia

    def calcular_consumo(self, distancia):
        consumo = distancia / self.eficienciaMedia
        self.consumo = consumo
        return consumo
    
    def __str__(self):
        infos = super().__str__()
        infos += f"Eficiência média: {self.eficienciaMedia} km/h"
        return infos