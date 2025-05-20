from ..ConsumoCombustivel.models.Veiculos import Veiculos

class Frota(Veiculos):
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe):
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
    def listar_veiculos():
        pass
    def calc_consumo_total_frota():
        pass