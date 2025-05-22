from models.Caminhao import Caminhao
from models.Carro import Carro
from models.Moto import Moto
from models.Veiculos import Veiculos
from FrotaVeiculos.models.Frota import Frota

fh_540 = Caminhao("IXJ8I73", "FH-540", "Volvo", 2020, "Branca", 500000)
agile = Carro("ICM9U20", "Agile", "Chevrolet", 2013, "Branco", 35000)
xj6 = Moto("ICM9U20", "XJ6", "Yamaha", 2025, "Preta", 50000)

frota = Frota(agile)
frota.adicionar_veiculos(fh_540)
frota.calc_consumo_total(200)
agile.calcular_consumo(120)
fh_540.calcular_consumo(50)
xj6.calcular_consumo(200)
frota.calc_consumo_total(200)
print(agile.setPlaca('IUG8K12'))
placas_duplicadas = []
if(agile.__eq__(xj6)):
    placas_duplicadas.append(agile.getPlaca())
    print('Placas iguais.')
else:
    print('Placas não-iguais.')