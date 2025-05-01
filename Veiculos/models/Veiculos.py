class Veiculos: 
    def __init__(self, modelo, marca, placa,ano, cor, velocidade, latitude, longitude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude 
        self.longitude = longitude
    
    def acelerar (self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.Alterar_latitude()
        print("O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")
    
    def frear(self):
        if(self.velocidade >= 10):
            self.velocidade -= 10
        else:
            self.velocidade = 0
    def mostrar_infos(self):
        print(f"\nO veículos {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h")
        print(f"Lat: {self.latitude}, Long: {self.longitude}")

    def alterar_placa(self, placa):
        self.placa = placa

    def Alterar_modelo(self, modelo):
        self.modelo = modelo
    
    def Alterar_marca(self, marca):
        self.marca = marca
    
    def Alterar_ano(self, ano):
        self.ano = ano

    def Alterar_cor(self, cor):
        self.cor = cor
    
    def Alterar_latitude(self, latitude):
        self.latitude = latitude

    def Alterar_longitude(self, longitude):
        self.longitude = longitude
    



    def Obter_placa(self, placa):
        return self.placa 

    def Obter_modelo(self, modelo):
        return self.modelo
    
    def Obter_marca(self, marca):
        return self.marca 
    
    def Obter_ano(self, ano):
        return self.ano

    def Obter_cor(self, cor):
        return self.cor
    
    def Obter_latitude(self, latitude):
        return self.latitude

    def Obter_longitude(self, longitude):
        return self.longitude 
    

