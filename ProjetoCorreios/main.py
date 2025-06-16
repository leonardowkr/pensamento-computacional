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

        # Configura o container para as telas
        self.container = ctk.CTkFrame(root)
        self.container.grid(row=0, column=0, sticky="nsew", pady=5)
        style = ttk.Style()
        style.theme_use("default")
        
        
        
        style.configure("Treeview", 
                font=('Helvetica', 10),
                rowheight=28,
                foreground="#000000",
                background="#f0f0f0",
                fieldbackground="#")
        
        self.rotas = [
            ("Rota 1", "Rodoviário", "10", "100", "1000"),
            ("Rota 2", "Ferroviário", "20", "200", "1000"),
            ("Rota 3", "Aéreo", "30", "300", "1000")
        ]

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Criar as telas
        self.tela_custos = ctk.CTkFrame(master=self.container)

        # Posiciona as telas no mesmo local
        self.tela_custos.grid(row=0, column=0, sticky="nsew")

        self.configurar_tela_custos()
        self.mostrar_tela(self.tela_custos)
        # Estilo personalizado

    def salvar_linha_transporte(self):
        origem = self.rota_destino_entry.get()
        destino = self.rota_origem_entry.get()
        tipo_transporte = self.tipo_transporte_combobox.get()
        peso = self.peso_entry.get()
        db = DBservices()
        db.criar_linha_transporte(origem="SP", destino="MG", distancia=100,
                                  peso=10, tarifa_km=5 ,tipo_transporte="Rodviario")

        print(origem, destino, tipo_transporte, peso)

    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_custos(self):
        self.tela_custos.grid_columnconfigure(0, weight=1)
        self.tela_custos.grid_columnconfigure(1, weight=1)

        titulo = ctk.CTkLabel(self.tela_custos, text="SIMULAÇÃO DE CUSTOS", font=ctk.CTkFont(size=20, weight="bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        form_frame = ctk.CTkFrame(self.tela_custos)
        form_frame.grid(row=1, column=0, columnspan=2, pady=5)

        # Campo Rota
        ctk.CTkLabel(form_frame, text="Rota (Origem):").grid(row=0, column=0, sticky="e", pady=5, padx=5)
        self.rota_origem_entry = ctk.CTkEntry(form_frame, width=200)
        self.rota_origem_entry.grid(row=0, column=1, sticky="w", pady=5, padx=5)

        ctk.CTkLabel(form_frame, text="Rota (Destino):").grid(row=1, column=0, sticky="e", pady=5, padx=5)
        self.rota_destino_entry = ctk.CTkEntry(form_frame, width=200)
        self.rota_destino_entry.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        # Campo Tipo de Transporte
        ctk.CTkLabel(form_frame, text="Tipo de transporte:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
        self.tipo_transporte_combobox = ctk.CTkComboBox(form_frame, values=["Rodoviário", "Ferroviário", "Aéreo", "Hidroviário"])
        self.tipo_transporte_combobox.grid(row=2, column=1, sticky="w", pady=5, padx=5)

        # Campo Cubagem
        ctk.CTkLabel(form_frame, text="Cubagem (L):").grid(row=3, column=0, sticky="e", pady=5, padx=5)
        self.cubagem_entry = ctk.CTkEntry(form_frame, width=200)
        self.cubagem_entry.grid(row=3, column=1, sticky="w", pady=5, padx=5)

        # Campo Peso
        ctk.CTkLabel(form_frame, text="Peso (kg):").grid(row=4, column=0, sticky="e", pady=5, padx=5)
        self.peso_entry = ctk.CTkEntry(form_frame, width=200)
        self.peso_entry.grid(row=4, column=1, sticky="w", pady=5, padx=5)

        
        # Botões
        botoes_frame = ctk.CTkFrame(self.tela_custos)
        botoes_frame.grid(row=2, column=0, columnspan=2, pady=20)

        ctk.CTkButton(botoes_frame, text="Cancelar", width=100, command=None).grid(row=0, column=0, padx=10)
        ctk.CTkButton(botoes_frame, text="Salvar", width=100, command=self.salvar_linha_transporte()).grid(row=0, column=1, padx=10)

        # Treeview (mantida com ttk pois customtkinter não possui um widget equivalente)
        self.treeview_custos = ttk.Treeview(self.tela_custos, columns=("Rota", "Tipo de Transporte", "Cubagem", "Peso", "Preco"), show='headings')
        self.treeview_custos.heading("Rota", text="Rota (distância)")
        self.treeview_custos.heading("Tipo de Transporte", text="Tipo de Transporte")
        self.treeview_custos.heading("Cubagem", text="Cubagem (L)")
        self.treeview_custos.heading("Peso", text="Peso (kg)")
        self.treeview_custos.heading("Preco", text="Valor (R$)")

        self.treeview_custos.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20, pady=20)

        # Inserir dados iniciais
        for itens in self.rotas:
            self.treeview_custos.insert("", "end", values=itens)


if __name__ == "__main__":
    ctk.set_appearance_mode("system")  # ou "dark", "light"
    ctk.set_default_color_theme("blue")  # ou "dark-blue", "green", etc.

    root = ctk.CTk()
    sistema_correios = SistemaCorreios(root)
    root.mainloop()
