import tkinter as tk

def mostrar_opcao():
    rotulo.config(text = f"Escolheu: {opcao.get()}")
    texto = f"Você escolheu: "
    texto += "Dinheiro" if dinheiro.get() else ""
    texto += ", Tempo" if tempo.get() else ""
    texto += ", Vida Social" if vidasocial.get() else ""
    
    
    if dinheiro.get() == True:
        tempo.set(False)
    
    if tempo.get() == True:
        vidasocial.set(False)
    
    if vidasocial.get() == True:
        dinheiro.set(False)
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")

dinheiro = tk.StringVar(value = False)
tempo = tk.StringVar(value = False)
vidasocial = tk.StringVar(value = False)

tk.Radiobutton(janela, text = "Dinheiro", variable= dinheiro, value = True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text = "Tempo", variable= tempo, value = True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text = "Vida Social", variable= vidasocial, value = True, command=mostrar_opcao).pack()

rotulo = tk.Label(janela, text = "Escolheu A")
rotulo.pack(pady = 10)

janela.mainloop()