import time

class ContaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo (float),  limite (float) e históricos (lista de dicionários)
    
    OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2, transferir
    '''
    
    def __init__(self, titular, saldo, limite, historico):
        '''
        Construtor da classe ContaBancária
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
        
    def depositar(self, valor, remetente = None):
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
        '''
        Objetivo: Método que realiza o saque na conta bancária.
        Entradas: valor (float) e destinarário (str).
        Return: True, se a operação foi realizada com sucesso. False, se a operação não foi realizada.
        '''
        op = 0
        # detecta se é uma transferência e muda a operacao para 2
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": op,
                                   "remetente": self.titular, 
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Saque realizado!")
            return True
        else: # sem grana em conta
            a = input(f"Deseja utilizar o Limite? (R${self.limite}) [s para sim]")
            if a == 's':
                if (self.saldo + self.limite) >= valor: 
                    self.saldo -= valor
                    print("Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
        return False
    
    
    def transferir(self, destinatario, valor):
        """
        Objetivo: método para transferir um valor entre duas contas.
        Entradas: valor (float) e obj ContaBancaria do destinatário.
        Saída: Se ok -> True, Se NOK -> False.
        """
        # se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # deposita na conta do destinatário
            destinatario.depositar(valor, self.titular)
        
        
        
    
    def exibirHistorico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:
            dt = time.localtime(transacao["dataetempo"])
            print("Op:", transacao["operacao"],
                  ". Remetente:",  transacao["remetente"], 
                  ". Destinatário: ", transacao["destinatario"],
                  ". Saldo: ", transacao["saldo"],
                  ". Valor: ", transacao["valor"],
                  ". Data e Tempo:", 
                  f"{dt.tm_hour}:{dt.tm_min}:{dt.tm_sec} {dt.tm_mday}/{dt.tm_mon}/{dt.tm_year}")
    
    # def exibirSaldo(self):