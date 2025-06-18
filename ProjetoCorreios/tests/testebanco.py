import customtkinter as ctk
import tkinter.ttk as ttk

# Configurações iniciais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1000x600")
app.title("Sistema Correios")

# Topo com logo e campo de busca
top_frame = ctk.CTkFrame(app, corner_radius=0)
top_frame.pack(fill="x", pady=(10, 0), padx=10)

logo = ctk.CTkLabel(top_frame, text="📬 Sistema Correios", font=("Arial", 16, "bold"))
logo.pack(side="left", padx=10)

search_entry = ctk.CTkEntry(top_frame, placeholder_text="Pesquisar", width=200)
search_entry.pack(side="right", padx=10)

# Título e formulário
title = ctk.CTkLabel(app, text="SIMULAÇÃO DE CUSTOS", font=("Arial", 20, "bold"))
title.pack(pady=10)

form_frame = ctk.CTkFrame(app)
form_frame.pack(pady=10)

campos = [
    ("Origem:", "origem"),
    ("Destino:", "destino"),
    ("Cubagem (L):", "cubagem"),
    ("Peso (Kg):", "peso")
]
entries = {}

for idx, (label, key) in enumerate(campos):
    l = ctk.CTkLabel(form_frame, text=label)
    l.grid(row=idx, column=0, padx=10, pady=5, sticky="e")
    e = ctk.CTkEntry(form_frame, width=200)
    e.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
    entries[key] = e

# Tipo de transporte
tipo_label = ctk.CTkLabel(form_frame, text="Tipo de transporte:")
tipo_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
tipo_menu = ctk.CTkOptionMenu(form_frame, values=["Rodoviário", "Ferroviário", "Aéreo", "Hidroviário"])
tipo_menu.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Botões
btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=10)

cancel_btn = ctk.CTkButton(btn_frame, text="Cancelar", fg_color="#c0392b", hover_color="#a93226")
cancel_btn.pack(side="left", padx=10)

save_btn = ctk.CTkButton(btn_frame, text="Salvar", fg_color="#2980b9", hover_color="#2471a3")
save_btn.pack(side="left", padx=10)

# Tabela
tree_frame = ctk.CTkFrame(app)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

cols = ["Origem", "Destino", "Distancia (Km)", "Peso (kg)", "Tipo de Transporte", "Custo"]
tree = ttk.Treeview(tree_frame, columns=cols, show="headings")

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=120)

tree.pack(fill="both", expand=True)

# Dados mock
for i in range(6):
    tree.insert("", "end", values=["Teste", "Teste", 100.0, 3.0, "Rodoviário", 300.0])

app.mainloop()
