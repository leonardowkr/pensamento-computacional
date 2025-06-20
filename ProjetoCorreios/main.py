import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from database.DBServices import DBservices
from models.LinhaTransporte import LinhaTransporte
from models.Aereo import Aereo
from models.Rodoviario import Rodoviario 
from models.Ferroviario import Ferroviario 
from models.Hidroviario import Hidroviario
import os
from PIL import Image, ImageTk

class SistemaCorreios:
    def __init__(self, root, modo="login"):
        self.modo = modo

        if modo == "login":
            self.root_login = root
            self.root_login.title("Login - LogiCost")
            self.root_login.geometry("900x500")
            self.root_login.resizable(False, False)
            self.root_login.iconbitmap("ProjetoCorreios/utils/favicon.ico")


            self.container_login = ctk.CTkFrame(master=self.root_login)
            self.container_login.pack(fill="both", expand=True)
            self.tela_login = ctk.CTkFrame(master=self.container_login)
            self.tela_login.grid(row=0, column=0, sticky="nsew")
            self.tela_login.grid_rowconfigure(0, weight=1)
            self.tela_login.grid_columnconfigure((0, 1), weight=1)
            

            self.configurar_tela_login()
            self.mostrar_tela(self.tela_login)
            

        elif modo == "custos":
            self.root = root
            self.root.title("Sistema Correios")
            self.root.geometry("1000x800")
            self.root.resizable(True, True)
            self.root.iconbitmap("ProjetoCorreios/utils/favicon.ico")

            self.container = ctk.CTkFrame(master=self.root)
            self.container.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
            self.container.grid_columnconfigure(0, weight=1)

            self.tela_custos = ctk.CTkFrame(master=self.container)
            self.tela_custos.grid(row=0, column=0, sticky="nsew")
            self.configurar_tela_custos()
            self.mostrar_tela(self.tela_custos)
        

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
                messagebox.showerror("Dados inválidos", "Os campos origem e destino devem ser um texto e peso deve ser um número")
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
    
    def configurar_tela_login(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        caminho_imagem = os.path.join(BASE_DIR, "assets", "image.png")
        self.imagem_fundo = ctk.CTkImage(Image.open(caminho_imagem), size=(450, 500))

        self.tela_login.grid_rowconfigure(0, weight=1)
        self.tela_login.grid_columnconfigure((0, 1), weight=1)

        # Frame esquerdo (login)
        login_frame = ctk.CTkFrame(self.tela_login, corner_radius=0, fg_color="black")
        login_frame.grid(row=0, column=0, sticky="nsew")
        login_frame.grid_rowconfigure(99, weight=1)  # empurra o rodapé

        ctk.CTkLabel(login_frame, text="Faça seu Login.", font=ctk.CTkFont(size=28, weight="bold"), text_color="white").pack(pady=(60, 20))

        ctk.CTkLabel(login_frame, text="Email", anchor="w", text_color="white").pack(padx=50, anchor="w")
        self.entry_email = ctk.CTkEntry(login_frame, width=350, height=40, placeholder_text="Digite seu e-mail", border_color="#FFCC00", border_width=2)
        self.entry_email.pack(padx=50, pady=(5, 20))

        ctk.CTkLabel(login_frame, text="Senha", anchor="w", text_color="white").pack(padx=50, anchor="w")
        self.entry_senha = ctk.CTkEntry(login_frame, width=350, height=40, show="*", placeholder_text="Digite sua senha", border_color="#FFCC00", border_width=2)
        self.entry_senha.pack(padx=50, pady=(5, 10))

        ctk.CTkLabel(login_frame, text="Esqueci minha senha", font=ctk.CTkFont(underline=True, size=12), text_color="white", cursor="hand2").pack(padx=50, anchor="w")

        self.botao_login = ctk.CTkButton(
            login_frame,
            text="Entrar",
            width=350,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#9F5FFF",
            hover_color="#7B3FE4",
            command=lambda: self.fazer_login()
        )
        self.botao_login.pack(pady=(30, 10))

        ctk.CTkButton(
            login_frame, 
            text="Ainda não tenho uma conta", 
            fg_color="black", 
            font=ctk.CTkFont(size=12, underline=True), 
            text_color="white",
            command=self.configurar_tela_cadastro
            ).pack()
        
        ctk.CTkLabel(login_frame, text="2025 | Desenvolvido por LogiCost", font=ctk.CTkFont(size=10), text_color="gray").pack(side="bottom", pady=10)

        # Frame direito (imagem)
        imagem_label = ctk.CTkLabel(self.tela_login, text="", image=self.imagem_fundo)
        imagem_label.grid(row=0, column=1, sticky="nsew")

    
    def fazer_login(self):
        self.configurar_tela_custos()

    def configurar_tela_cadastro(self):
        # Cria o frame da tela de cadastro
        self.tela_cadastro = ctk.CTkFrame(master=self.container_login)
        self.tela_cadastro.grid(row=0, column=0, sticky="nsew")

        self.tela_cadastro.grid_rowconfigure(0, weight=1)
        self.tela_cadastro.grid_columnconfigure(0, weight=1)

        # Left side (registration form) - similar to login's left side
        frame_left_cadastro = ctk.CTkFrame(self.tela_cadastro, width=450, height=550, corner_radius=0, fg_color="black")
        frame_left_cadastro.pack(side="left", fill="y")

        ctk.CTkLabel(frame_left_cadastro, text="Criar Conta", font=ctk.CTkFont(size=28, weight="bold"), text_color="white").pack(pady=(15, 20), padx=50, anchor="w")

        ctk.CTkLabel(frame_left_cadastro, text="Nome", text_color="white").pack(padx=50, anchor="w")
        self.cadastro_nome = ctk.CTkEntry(frame_left_cadastro, width=350, height=40, placeholder_text="Seu nome", border_color="#FFCC00", border_width=2)
        self.cadastro_nome.pack(padx=50, pady=(5, 10))

        ctk.CTkLabel(frame_left_cadastro, text="Email", text_color="white").pack(padx=50, anchor="w")
        self.cadastro_email = ctk.CTkEntry(frame_left_cadastro, width=350, height=40, placeholder_text="Seu e-mail", border_color="#FFCC00", border_width=2)
        self.cadastro_email.pack(padx=50, pady=(5, 10))

        ctk.CTkLabel(frame_left_cadastro, text="Senha", text_color="white").pack(padx=50, anchor="w")
        self.cadastro_senha = ctk.CTkEntry(frame_left_cadastro, width=350, height=40, show="*", placeholder_text="Crie uma senha", border_color="#FFCC00", border_width=2)
        self.cadastro_senha.pack(padx=50, pady=(5, 20))

        ctk.CTkButton(frame_left_cadastro, text="Cadastrar", width=350, height=45, fg_color="#6A0DAD", hover_color="#5a009e", command=None).pack(pady=(10, 10))

        # Voltar para tela de login - changed text and color to match login
        ctk.CTkButton(frame_left_cadastro, text="Já tenho uma conta", font=ctk.CTkFont(size=12, underline=True), text_color="white", fg_color="black", command=lambda: self.mostrar_tela(self.tela_login)
        ).pack(pady=(10, 10))

        # "Desenvolvido por" text at the bottom, similar to login
        ctk.CTkLabel(frame_left_cadastro, text="2025 | Desenvolvido por LogiCost", font=ctk.CTkFont(size=10), text_color="#A9A9A9").pack(pady=(20, 10), side="bottom")

        # Right side (background image) - similar to login's right side
        if self.imagem_fundo:
            ctk.CTkLabel(self.tela_cadastro, text="", image=self.imagem_fundo).pack(side="right", fill="both", expand=True)
        
    
    def salvar_usuario(self):
        print("Usuário criado!")

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

    root_login = ctk.CTk()
    sistema_correios = SistemaCorreios(root_login, modo="login")
    
    root_login.mainloop()
    