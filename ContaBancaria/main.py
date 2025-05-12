from models.ContaBancaria import ContaBancaria


Banco = []
while True:
    op = input("Selecione a operação desejada: ")
    if op == '1':
        titular = input("Insira o nome do titular: ")
        saldo = 0
        limite = 100
        Banco.append(ContaBancaria(titular, saldo, limite, []))
        print("Conta criada com sucesso.\n")
    if op == '2':
        titular = input("Insira o nome do titular que deseja consultar: ")
        for cliente in Banco:
            if cliente.titular == titular:
                print(f'O saldo de {cliente.titular} é de: R$ {cliente.saldo}')
            else: 
                print('Cliente não encontrado')
    if op == '3':
        titular = input("Insira o nome do titular que deseja sacar: ")
        for cliente in Banco:
            if cliente.titular == titular:
                valor = float(input("Insira o valor que deseja sacar"))
                cliente.sacar(valor)
            else: 
                print('Cliente não encontrado')

    if op == '4':
        titular = input("Insira o nome do titular que deseja depositar: ")
        for cliente in Banco:
            if cliente.titular == titular:
                valor = float(input("Insira o valor que deseja depositar"))
                cliente.depositar(valor)
                if(cliente.depositar(valor)):
                    print('Depósito realizado com sucesso')
                    


    if op == '5':
        titular = input("Insira o nome do titular que deseja transferir: ")
        titular_saque = input("Insira o nome do titular da conta a transferir")
        for cliente in Banco:
            if cliente.titular == titular_saque:
                valor = float(input("Insira o valor que deseja transferir"))
                if(cliente.sacar(valor)):
                    for cliente in Banco:
                        if(cliente.titular == titular):
                            if(cliente.depositar):
                                print('Saque realizado com sucesso')
                        else:
                            print('Erro. [Depósito]')
                else:
                    print('Erro. [Saque]')
            else: 
                print('Cliente não encontrado')
"""""
novo_cliente = input("\nDigite o nome do titular: ")
novo_cliente = {"titular": titular, "saldo": 0, "limite": 200}
Banco.append(titular)

print(f"A conta de {Banco['titular']['titular']} foi criada")
titular = input("Digite o titular da conta que deseja ver o saldo:")

pedro = ContaBancaria("Pedro", 100, 50, [])
guilherme = ContaBancaria("Guilherme", 1000, 500, [])
guilherme.transferir(pedro, 500)
guilherme.exibir_historico()

"""
