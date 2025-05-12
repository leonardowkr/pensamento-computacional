from models.ContaBancaria import ContaBancaria

guilherme = ContaBancaria("Guilherme", 1000, 500, [])
guilherme.depositar(50)
pedro = ContaBancaria("Pedro", 100, 50, [])

guilherme.transferir(pedro, 50)
guilherme.exibirHistorico()
pedro.exibirHistorico()