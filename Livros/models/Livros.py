class Livros:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self, pagina_atual):
        self.pagina_atual = pagina_atual +  1
        
    
    def voltar_pagina(self, pagina_atual):
        self.pagina_atual = pagina_atual -  1
    
    def exibir_informacoes(GoT):
        print(f"O livro {GoT.titulo} do autor {GoT.autor}, lançado no ano de {GoT.ano_publicacao} tem {GoT.numero_paginas} páginas. Você está na página {GoT.pagina_atual}\n")

    
