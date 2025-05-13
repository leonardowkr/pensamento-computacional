import time 
class ContaBancaria: 
    '''
        Classe que implementa méotodos para manipular uma conta bancaria,add()
        Atributo: titular (str), saldo(float), limite(float), e históricos (lista de dicionários)

        OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2 - transferir
    '''
    

    def __init__(self, titular, saldo, limite, historico):
        '''
            Construtor da classe ContaBancaria
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor, remetente=None):
        '''
        Objetivo: Método que realiza do depósito na conta bancária.
        Entradas: valor (float) e remetente (str).
        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        '''
        op = 1
        # detecta se é uma transferência
        if remetente != None:
            op = 2
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": op,
                                   "remetente": remetente, 
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            return True
        else:
            print(f" O valor {valor} é inválido!")
            return False

    def sacar(self, valor, destinatario = None):
        op = 0
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo += valor
            self.historico.append({"operacao": 0,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data e tempo": time.time()})
            #print("Saque realizado!")
            return True
        else: 
            a = input(f"Deseja utilizar o limite? (R${self.limite}) [s para sim]")
            if a == 's':
                if(self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado!")
                    return True
                
    def transferir(self, destinatario, valor):
        self.sacar(valor, destinatario)
        self.historico.append({"operacao": 2,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data e tempo": time.localtime()})
        destinatario.depositar(valor)
        self.sacar(valor, destinatario.titular)

    def exibir_historico(self):
        dt = time.localtime()
        for transacao in self.historico:        
            print(f"\nOp: {transacao["operacao"]}, Remetente: {transacao["remetente"]}, Destinatário {transacao["destinatario"]}, Saldo: {transacao["saldo"]}, Data e Tempo {dt.tm_year}/{dt.tm_mon}/{dt.tm_mday} {dt.tm_hour}:{dt.tm_min}:{dt.tm_sec}")

    def exibir_saldo(): 
        None
    