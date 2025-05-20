from models.Caminhao import Caminhao
from models.Carro import Carro
from models.Moto import Moto


fh_540 = Caminhao("IXJ8873", "FH-540", "Volvo", 2020, "Branca", 500000)
agile = Carro("IUJ-9290", "Agile", "Chevrolet", 2013, "Branco", 35000)
xj6 = Moto("ICM-9920", "XJ6", "Yamaha", 2025, "Preta", 50000)
print(fh_540)
print(agile)
print(xj6)