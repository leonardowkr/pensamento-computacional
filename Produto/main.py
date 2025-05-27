from models.Produto import Produto
from models.ProdutoEletronico import ProdutoEletronico
from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ConversorMoeda import ConversorMoeda

p2 = Produto("Produto Genérico", 100.0)
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
tipo_produto = input("Insira o tipo do produto (eletrônico ou alimentício): ") 

if(tipo_produto.lower() == "eletrônico"):
    p1 = ProdutoEletronico(produto, preco)
elif(tipo_produto.lower() == "alimentício"):
    p1 = ProdutoAlimenticio(produto, preco)

print(p1)
conversor = ConversorMoeda()
if conversor.converte_preco_para_usd(p1):
    print(f"Preço convertido para USD: {p1.getPreco()} {p1.getMoeda()}")
else:
    print("Conversão para USD não foi possível.")
print(p1)
