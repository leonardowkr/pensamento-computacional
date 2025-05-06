from models.Livros import Livros

GoT = Livros("Game of Thrones", "George R. R. Martin", 1996, 231, 1)
GoT.avancar_pagina(GoT.pagina_atual)
GoT.exibir_informacoes()
GoT.avancar_pagina(GoT.pagina_atual)
GoT.exibir_informacoes()