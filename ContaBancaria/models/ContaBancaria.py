class ContaBancaria: 
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor):
            self.saldo += valor
            self.historico += f"Depósito de {valor}\n"
    def sacar():
        None
    def transferir():
        None
    def exibir_historico(historico):
        print(historico)
    def exibir_saldo(): 
        None