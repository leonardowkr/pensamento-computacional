from models.ContaBancaria import ContaBancaria

usuario = ContaBancaria("Leonardo", 1000, 3500, [])
usuario.depositar(200)
usuario.transferir("ZeZé", 100)
usuario.exibir_historico(usuario)

