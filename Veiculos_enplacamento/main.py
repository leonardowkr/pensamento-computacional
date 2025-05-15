from models.Veiculos import Veiculos

gol = Veiculos("Gol Copa", "Volkswagen", "INJ-1820", 2006, "Amarelo", 0,
-29.668241, -51.111896)

gol.mostrar_infos()
gol.acelerar()
gol.mostrar_infos()
gol.frear()
gol.alterar_placa("IND1A10")
gol.mostrar_infos()
