import tkinter as tk

def imprimirInfos():
        if rotulo['text'] == 'Olá Mundo!':
            rotulo.config(text = "Olá Turma!")
        else: 
            rotulo.config(text = "Olá Mundo!")
toggle = True
janela = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text = "Clique no botão abaixo", font = ("Arial", 16))
rotulo.pack(pady = 10)
botao = tk.Button (janela, text = "Clique Aqui", command = imprimirInfos)
botao.pack(pady = 10)
janela.mainloop()
 
