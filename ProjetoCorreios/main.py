import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from database.DBServices import DBservices
from models.LinhaTransporte import LinhaTransporte
from models.Aereo import Aereo
from models.Rodoviario import Rodoviario 
from models.Ferroviario import Ferroviario 
from models.Hidroviario import Hidroviario
from PIL import Image, ImageTk

class SistemaCorreios:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Sistema Correios")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        self.treeview_custos = None
        self.root.iconbitmap("ProjetoCorreios/utils/favicon.ico")
        
        #icon = ImageTk.PhotoImage(file="ProjetoCorreios/utils/favicon.png")
        #self.root.wm_iconphoto(True, icon)
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
        origem = self.rota_destino_entry.get().title()
        destino = self.rota_origem_entry.get().title()
        tipo_transporte = self.tipo_transporte_combobox.get().title()
        peso = self.peso_entry.get()
        db = DBservices()

        if not origem or not destino or not peso:
            messagebox.showerror("Dados incompletos", "Favor preencher todos os campos!")
            return
        else:
            try:
                origem = str(origem)
                destino = str(destino)
                tipo_transporte = str(tipo_transporte)
                peso = float(peso)
            except ValueError:
                messagebox.showerror("Dados inválidos", "Os campos origem e destino devem ser do tipo float")
                return
        if tipo_transporte == "Rodoviário":
            linha_transporte = Rodoviario(origem, destino, distancia=100.0, peso=3)
            db.criar_linha_transporte(linha_transporte.getOrigem(), 
                                    linha_transporte.getDestino(),
                                    linha_transporte.getDistancia(),
                                    linha_transporte.getPeso(),
                                    linha_transporte.getTarifa(),
                                    linha_transporte.getTipoTransporte(),
                                    linha_transporte.calcular_custo()
                                )
        elif tipo_transporte == "Ferroviário":
            linha_transporte = Ferroviario(origem, destino, distancia=100, peso=3.4)
            db.criar_linha_transporte(linha_transporte.getOrigem(), 
                                    linha_transporte.getDestino(),
                                    linha_transporte.getDistancia(),
                                    linha_transporte.getPeso(),
                                    linha_transporte.getTarifa(),
                                    linha_transporte.getTipoTransporte(),
                                    linha_transporte.calcular_custo()
                                )

        elif tipo_transporte == "Hidroviário":
            linha_transporte = Hidroviario(origem, destino, distancia=100, peso=3.4)
            db.criar_linha_transporte(linha_transporte.getOrigem(), 
                                    linha_transporte.getDestino(),
                                    linha_transporte.getDistancia(),
                                    linha_transporte.getPeso(),
                                    linha_transporte.getTarifa(),
                                    linha_transporte.getTipoTransporte(),
                                    linha_transporte.calcular_custo()
                                )

        elif tipo_transporte == "Aéreo":
            linha_transporte = Aereo(origem, destino, distancia=100, peso=3.4)
            db.criar_linha_transporte(linha_transporte.getOrigem(), 
                                    linha_transporte.getDestino(),
                                    linha_transporte.getDistancia(),
                                    linha_transporte.getPeso(),
                                    linha_transporte.getTarifa(),
                                    linha_transporte.getTipoTransporte(),
                                    linha_transporte.calcular_custo()
                                )
        else:
            messagebox.showerror("Dados Inválidos", "O Tipo de transporete deve estar disponível na lista")
            return
        messagebox.showinfo("Banco de dados", "Dados salvos com sucesso")

        self.atualizar_treeview()

    def mostrar_tela(self, tela):
        tela.tkraise()

    def configurar_tela_custos(self):
        self.tela_custos.grid_columnconfigure(0, weight=1)
        self.tela_custos.grid_columnconfigure(1, weight=1)

        titulo = ctk.CTkLabel(self.tela_custos, text="SIMULAÇÃO DE CUSTOS", font=ctk.CTkFont(size=22, weight="bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)

        # Frame de formulário
        form_frame = ctk.CTkFrame(self.tela_custos, fg_color="transparent")
        form_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=40, sticky="ew")
        form_frame.grid_columnconfigure((0, 1), weight=1)

        def criar_linha(row, texto, entry_widget):
            ctk.CTkLabel(form_frame, text=texto).grid(row=row, column=0, sticky="e", pady=8, padx=10)
            entry_widget.grid(row=row, column=1, sticky="w", pady=8, padx=10)

        self.rota_origem_entry = ctk.CTkEntry(form_frame, width=250, placeholder_text="Ex: São Paulo")
        criar_linha(0, "Rota (Origem):", self.rota_origem_entry)

        self.rota_destino_entry = ctk.CTkEntry(form_frame, width=250, placeholder_text="Ex: Rio de Janeiro")
        criar_linha(1, "Rota (Destino):", self.rota_destino_entry)

        self.tipo_transporte_combobox = ctk.CTkComboBox(form_frame, values=["Rodoviário", "Ferroviário", "Aéreo", "Hidroviário"], width=250)
        self.tipo_transporte_combobox.grid(row=2, column=1, sticky="w", pady=8, padx=10)
        ctk.CTkLabel(form_frame, text="Tipo de transporte:").grid(row=2, column=0, sticky="e", pady=8, padx=10)
        self.tipo_transporte_combobox.configure(state="readonly")

        self.cubagem_entry = ctk.CTkEntry(form_frame, width=250, placeholder_text="Ex: 80.0")
        criar_linha(3, "Cubagem (L):", self.cubagem_entry)

        self.peso_entry = ctk.CTkEntry(form_frame, width=250, placeholder_text="Ex: 3.5")
        criar_linha(4, "Peso (kg):", self.peso_entry)

        # Botões
        botoes_frame = ctk.CTkFrame(self.tela_custos, fg_color="transparent")
        botoes_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ctk.CTkButton(botoes_frame, text="Cancelar", width=120, fg_color="#c0392b", hover_color="#922b21", command=None).grid(row=0, column=0, padx=20)
        ctk.CTkButton(botoes_frame, text="Salvar", width=120, fg_color="#2980b9", hover_color="#2471a3", command=self.salvar_linha_transporte).grid(row=0, column=1, padx=20)

        # Tabela de resultados
        treeview_frame = ctk.CTkFrame(self.tela_custos)
        treeview_frame.grid(row=3, column=0, columnspan=2, pady=20, padx=40, sticky="nsew")

        self.treeview_custos = ttk.Treeview(treeview_frame, columns=("Origem", "Destino", "Distância", "Peso", "Tarifa por Km", "Tipo de Transporte", "Custo"), show='headings')
        for col in ("Origem", "Destino", "Distância", "Peso", "Tarifa por Km", "Tipo de Transporte", "Custo"):
            self.treeview_custos.heading(col, text=col)
            self.treeview_custos.column(col, anchor="center", width=140)
        self.treeview_custos.pack(fill="both", expand=True)
        
        self.atualizar_treeview()

    def atualizar_treeview(self) -> None:
        # Método utilizado para atualizar a tabela toda vez que um novo cadastro é feito
        self.limpar_treeview()
        db = DBservices()
        linhas_transportes = []
        # Salva os valores que estão no banco em uma lista 
        for item in db.buscar_todas_linhas_transportes():
            linhas_transportes.append((item.origem, item.destino, item.distancia, item.peso, item.tarifa_km, item.tipo_transporte, item.custo ))
        # Inserir dados iniciais
        # Percorre a lista e adiciona os dados no treeview
        for itens in linhas_transportes:
            self.treeview_custos.insert("", "end", values=itens)
    
    def limpar_treeview(self) -> None:
        # Método para limpar a treeview antes de atualizar com a nova informação
        for item in self.treeview_custos.get_children():
         self.treeview_custos.delete(item)

if __name__ == "__main__":
    ctk.set_appearance_mode("system")  # ou "dark", "light"
    ctk.set_default_color_theme("blue")  # ou "dark-blue", "green", etc.

    root = ctk.CTk()
    sistema_correios = SistemaCorreios(root)
    
    root.mainloop()
    