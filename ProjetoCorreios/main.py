import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from database.DBServices import DBservices

class SistemaCorreios:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Correios")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        self.treeview_custos = None
        # Configura o container para as telas
        self.container = ctk.CTkFrame(master=root, width=200, height=200)

        self.container.grid(row=0, column=0, sticky="e", pady=5)

        # Configura o grid do container
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Criar as telas
        self.tela_custos = ctk.CTkFrame(master=self.container)

        # Posiciona as telas no mesmo local
        self.tela_custos.grid(row=0, column=0, sticky="nsew")

        # Configura cada tela
        self.configurar_tela_custos()

        self.mostrar_tela(self.tela_custos)

    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_custos(self):
        # Configure column 0 of tela_custos to expand, allowing centering
        self.tela_custos.grid_columnconfigure(0, weight=1)
        self.tela_custos.grid_columnconfigure(1, weight=1) # Add weight to other columns if they contain centered content

        titulo = tk.Label(self.tela_custos, text="SIMULAÇÃO DE CUSTOS", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=0) # Center title as well

        form_frame = tk.Frame(self.tela_custos, padx=20)
        form_frame.grid(row=1, column=0, columnspan=2, pady=5) # Center form_frame

        # Campos comuns
        tk.Label(form_frame, text="Rota (distância):").grid(row=0, column=0, sticky="e", pady=5)
        self.rota_entry = tk.Entry(form_frame, width=15)
        self.rota_entry.grid(row=0, column=1, sticky="w", pady=5)
        # Função para exibir a seleção

        # Botão para mostrar a seleção
        mylist = ["Rodoviário", "Ferroviário", "Aéreo"]
        tk.Label(form_frame, text="Tipo de transporte").grid(row=1, column=0, sticky="e", pady=0)
        combobox_frame = ttk.Combobox(form_frame, values=mylist)
        combobox_frame.grid(row=1, column=1, sticky="w", pady=0)

        self.tipo_var = tk.StringVar(value="Carro")

        tk.Label(form_frame, text="Cubagem (L):").grid(row=3, column=0, sticky="e", pady=5)
        self.cubagem_entry = tk.Entry(form_frame, width=15)
        self.cubagem_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Label(form_frame, text="Peso (kg):").grid(row=4, column=0, sticky="e", pady=5)
        self.peso_entry = tk.Entry(form_frame, width=15)
        self.peso_entry.grid(row=4, column=1, sticky="w", pady=5)

        botoes_frame = tk.Frame(self.tela_custos)
        botoes_frame.grid(row=4, column=0, columnspan=2, pady=20) # Center botoes_frame
        tk.Button(botoes_frame, text="Cancelar", width=10,
                  command=None).grid(row=0, column=0, sticky="w", padx=5) # Adjusted row and column in botoes_frame

        tk.Button(botoes_frame, text="Salvar", width=10,
                  command=None).grid(row=0, column=1, sticky="e", padx=5) # Adjusted row and column in botoes_frame

        self.treeview_custos = ttk.Treeview(self.tela_custos, columns=("Rota", "Tipo de Transporte", "Cubagem", "Peso"), show='headings')
        self.treeview_custos.heading("Rota", text="Rota (distância)")
        self.treeview_custos.heading("Tipo de Transporte", text="Tipo de Transporte")
        self.treeview_custos.heading("Cubagem", text="Cubagem (L)")
        self.treeview_custos.heading("Peso", text="Peso (kg)")
        self.treeview_custos.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=20) # Centered and on row 5

if __name__ == "__main__":
    db = DBservices()
    db.criar_usuario("jose", 18)
    root = tk.Tk()
    sistema_correios = SistemaCorreios(root)
    root.mainloop()