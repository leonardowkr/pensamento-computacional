from tkinter import *
import tkinter as tk


class SistemaCorreios:
    def __init__(self, root):
            self.root = root
            self.root.title("Sistema Correios")
            self.root.geometry("1000x800")
            self.root.resizable(True, True)

            # Configura o container para as telas
            self.container = tk.Frame(root)
            self.container.pack(fill="both", expand=True)
            
            # Configura o grid do container
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)
            
            # Criar as telas
            self.tela_custos = tk.Frame(self.container)

            # Posiciona as telas no mesmo local
            self.tela_custos.grid(row=0, column=0, sticky="nsew")
            # for tela in (self.configurar_tela_custos):
            #     tela.grid(row=0, column=0, sticky="nsew")
            
            # Configura cada tela
            self.configurar_tela_custos()
 
            self.mostrar_tela(self.tela_custos)
    
    def mostrar_tela(self, tela):
        tela.tkraise()

    

    def configurar_tela_custos(self):
            titulo = tk.Label(self.tela_custos, text="SIMULAÇÃO DE CUSTOS", font=("Arial", 16, "bold"))
            titulo.pack(pady=20)

            form_frame = tk.Frame(self.tela_custos, padx=20)
            form_frame.pack(fill="both")
            
            # Campos comuns
            tk.Label(form_frame, text="Rota:").grid(row=0, column=0, sticky="e", pady=5)
            self.cpf_entry = tk.Entry(form_frame, width=15)
            self.cpf_entry.grid(row=0, column=1, sticky="w", pady=5)
            # Função para exibir a seleção
            

            # Botão para mostrar a seleção
            mylist = ["Rodoviário","Ferroviário","Aéreo"]
            combobox_frame = tk.Combobox(root, values= mylist)
            combobox_frame.grid(row=0, column=2, sticky="w", pady=5)
            tk.Label(form_frame, text="PLACA:").grid(row=1, column=0, sticky="e", pady=5)
            self.marca_entry = tk.Entry(form_frame, width=20)
            self.marca_entry.grid(row=1, column=1, sticky="w", pady=5)

            self.tipo_var = tk.StringVar(value="Carro")

            tipo_frame = tk.Frame(form_frame)
            tipo_frame.grid(row=3, column=2, sticky="w", pady=5)

            tk.Radiobutton(tipo_frame, text = "Carro", variable= self.tipo_var, value = "Carro").grid(row=2, column=0, sticky="e", pady=5)
            tk.Radiobutton(tipo_frame, text = "Moto", variable= self.tipo_var, value = "Moto").grid(row=3, column=0, sticky="e", pady=5)
            tk.Radiobutton(tipo_frame, text = "Caminhao", variable= self.tipo_var, value = "Caminhao").grid(row=4, column=0, sticky="e", pady=5, padx=5)

            botoes_frame = tk.Frame(self.tela_custos )
            botoes_frame.pack(pady=20)
            tk.Button(botoes_frame, text="Cancelar", width=10,
                    command=lambda: self.mostrar_tela(self.tela_principal)).grid(row=5, column=0, sticky="e", pady=5)
            
            # tk.Button(botoes_frame, text="Salvar", width=10,
            #         command=self.salvar_proprietario).grid(row=5, column=2, sticky="e", pady=5)

    
if __name__ == "__main__":
    root = tk.Tk()
    sistema_correios = SistemaCorreios(root)
    root.mainloop()
