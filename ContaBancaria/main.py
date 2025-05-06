from models.ContaBancaria import ContaBancaria

usuario = ContaBancaria("Leonardo", 1000, 3500, "Teste")
usuario.depositar(200)
usuario.exibir_historico()
