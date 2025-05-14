from models.ContaBancaria import ContaBancaria


Banco = []
while True:
    op = input(f'Selecione a operação desejada: \n[1] Criar conta \n[2] Consultar saldo \n[3] Sacar \n[4] Depositar \n[5] Transferir\n[6] Exibir histórico de transações\n[7] Excluir conta \n[0] Sair\n')
    if op == '1':
        titular = input("Insira o nome do titular: ")
        saldo = 0
        limite = 100
        existe = False
        for cliente in Banco:
            if cliente.titular == titular:
                print('Titular já possui conta')
                existe = True
        if not existe:
                Banco.append(ContaBancaria(titular, saldo, limite, []))
                print("Conta criada com sucesso.\n")

    if op == '2':
        titular = input("Insira o nome do titular que deseja consultar: ")
        encontrou = False
        for cliente in Banco:
            if cliente.titular == titular:
                print(f'O saldo de {cliente.titular} é de: R$ {cliente.saldo}')
                encontrou = True                
        if not encontrou:
            print('Cliente não encontrado')

    if op == '3':
        titular = input("Insira o nome do titular que deseja sacar: ")
        encontrou = False
        for cliente in Banco:
            if cliente.titular == titular:
                valor = float(input("Insira o valor que deseja sacar"))
                cliente.sacar(valor)
                encontrou = True
        if not encontrou:
            print('Cliente não encontrado')

    if op == '4':
        titular = input("Insira o nome do titular que deseja depositar: ")
        encontrou = False
        for cliente in Banco:
            if cliente.titular == titular:
                encontrou = True
                valor = float(input("Insira o valor que deseja depositar"))
                if cliente.depositar(valor):
                    print('Depósito realizado com sucesso')
                    #Banco.append(ContaBancaria(self.saldo, ))
        if not encontrou:
            print('Cliente não encontrado')

    if op == '5':
        titular_entregador = input("Insira o nome do titular que irá realizar a transferência: ")
        titular_recebedor = input("Insira o nome do titular que irá receber a transferência: ")
        encontrou_entregador = False
        for cliente in Banco:
            if cliente.titular == titular_entregador:
                encontrou_entregador = True
                valor = float(input("Insira o valor que deseja transferir"))
                if cliente.sacar(valor):
                    encontrou_recebedor = False
                    for cliente in Banco:
                        if(cliente.titular == titular_recebedor):
                            encontrou_recebedor = True
                            if(cliente.depositar(valor)):
                                print('Transferência realizada com sucesso')
                            else:
                                print('Erro. [Depósito]')
                    if not encontrou_recebedor:
                        print('Cliente não encontrado 1')
                else:
                    print('Erro. [Saque]')
        if not encontrou_entregador:
            print('Cliente não encontrado 2')

    if op == '6':
        titular = input('Insira o titular para exibir o histórico')
        for cliente in Banco:
            if(cliente.titular == titular):
                cliente.exibir_historico()
    if op == '7':
        titular = input('Insira o titular que deseja excluir a conta')
        for cliente in Banco:
            if(cliente.titular == titular):
                if titular.saldo < 0:
                    while confirmacao != 'ok' and confirmacao != 'OK':
                        confirmacao = input(f'É necessário realizar depósito de R$ {titular.saldo}[OK]')
                if titular.saldo > 0:
                    while confirmacao != 'ok' and confirmacao != 'OK':
                        None