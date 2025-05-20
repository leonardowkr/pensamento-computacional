from models.Retangulo import Retangulo
from models.Triangulo import Triangulo

tri = Triangulo(20)
qua = Retangulo(10)

qua.calc_area()
tri.calc_area()
print(qua)
print(tri)