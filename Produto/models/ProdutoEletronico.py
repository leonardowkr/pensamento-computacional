from models.Produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome: str, preco: float):
        super().__init__(nome, preco)
        self.__tipo = "eletrônico"
    
    def __str__(self):
        return super().__str__() + f"Tipo: {self.__tipo}"