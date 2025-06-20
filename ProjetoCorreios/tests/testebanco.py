import customtkinter as ctk
from PIL import Image
import os

class TelaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro - Sistema Correios")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        # Frame principal
        self.container = ctk.CTkFrame(master=self.root)
        self.container.pack(fill="both", expand=True)

        # Frame direito (imagem)
        '''
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        imagem_path = os.path.join(BASE_DIR, "assets", "image.png")
        imagem = ctk.CTkImage(Image.open(imagem_path), size=(450, 500))
        imagem_label = ctk.CTkLabel(self.container, text="", image=imagem)
        imagem_label.place(x=450, y=0)
        '''

        # Frame esquerdo (formulário)
        frame_formulario = ctk.CTkFrame(self.container, width=450, height=500, corner_radius=0, fg_color="black")
        frame_formulario.place(x=0, y=0)

        # Título
        ctk.CTkLabel(frame_formulario, text="Criar Conta", font=ctk.CTkFont(size=28, weight="bold"), text_color="white").pack(pady=(40, 10))

        # Campo nome
        ctk.CTkLabel(frame_formulario, text="Nome completo", text_color="white").pack(padx=50, anchor="w")
        self.entry_nome = ctk.CTkEntry(frame_formulario, width=350, height=40, placeholder_text="Digite seu nome", border_color="#FFCC00", border_width=2)
        self.entry_nome.pack(padx=50, pady=(5, 10))

        # Campo e-mail
        ctk.CTkLabel(frame_formulario, text="Email", text_color="white").pack(padx=50, anchor="w")
        self.entry_email = ctk.CTkEntry(frame_formulario, width=350, height=40, placeholder_text="Digite seu e-mail", border_color="#FFCC00", border_width=2)
        self.entry_email.pack(padx=50, pady=(5, 10))

        # Campo senha
        ctk.CTkLabel(frame_formulario, text="Senha", text_color="white").pack(padx=50, anchor="w")
        self.entry_senha = ctk.CTkEntry(frame_formulario, width=350, height=40, show="*", placeholder_text="Crie uma senha", border_color="#FFCC00", border_width=2)
        self.entry_senha.pack(padx=50, pady=(5, 20))

        # Botão cadastrar
        ctk.CTkButton(
            frame_formulario,
            text="Cadastrar",
            width=350,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#27ae60",
            hover_color="#1e8449",
            command=None
        ).pack(pady=(10, 20))

        # Voltar
        voltar_login = ctk.CTkLabel(frame_formulario, text="Já tenho uma conta", font=ctk.CTkFont(size=12, underline=True), text_color="white", cursor="hand2")
        voltar_login.pack()
        voltar_login.bind("<Button-1>", lambda e: self.root.destroy())

        # Rodapé
        ctk.CTkLabel(frame_formulario, text="2025 | Desenvolvido por Kauê Graff", font=ctk.CTkFont(size=10), text_color="gray").pack(side="bottom", pady=10)

if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    app = TelaCadastro(root)
    root.mainloop()
