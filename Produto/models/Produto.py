class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco

    def getMoeda(self):
        return self.__moeda
    
    def setMoeda(self, moeda):
        self.__moeda = moeda

    def __str__(self):
        info = f"Produto: {self.getNome()}\n"
        info += f"Preço: {self.getPreco()}\n"
        info += f"Moeda: {self.getMoeda()}\n"
        return info