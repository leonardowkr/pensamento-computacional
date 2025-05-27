from models.Produto import Produto

class ConversorMoeda(Produto):
    def __init__(self):
        self.__USD_BRL = 5.0
        self.__EUR_BRL = 6.0
        self.__EUR_USD = 1.22

    def converte_preco_para_usd(self, produto: Produto) -> bool:
        if produto.getMoeda() == "BRL":
            produto.setPreco(produto.getPreco() / self.__USD_BRL)
            produto.setMoeda("USD")
            return True
        elif produto.getMoeda() == "EUR":
            produto.setPreco(produto.getPreco() / self.__EUR_USD)
            produto.setMoeda("USD")
            return True
        elif produto.getMoeda() == "USD":
            return False

    def converte_preco_para_eur(self, produto: Produto) -> bool:
        if produto.getMoeda() == "BRL":
            produto.setPreco(produto.getPreco() / self.__EUR_USD)
            produto.setMoeda("EUR")
            return True
        elif produto.getMoeda() == "USD":
            produto.setPreco(produto.getPreco() / self.__EUR_BRL)
            produto.setMoeda("EUR")
        elif produto.getMoeda() == "EUR":
            return False

    def converte_preco_para_brl(self, produto: Produto) -> bool:
        if produto.getMoeda() == "USD":
            produto.setPreco(produto.getPreco() * self.__USD_BRL)
            produto.setMoeda("BRL")
            return True
        elif produto.getMoeda() == "EUR":
            produto.setPreco(produto.getPreco() * self.__EUR_BRL)
            produto.setMoeda("BRL")
            return True
        elif produto.getMoeda() == "BRL":
                return False