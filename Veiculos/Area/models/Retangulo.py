class Retangulo: 
    def __init__(self, lado: float):
        self.lado = lado
        self.area = 0

    def calc_area(self):
        self.area = (self.lado*self.lado)
        
    def __str__(self):
        info = f"Area Retângulo {self.area}"
        return info