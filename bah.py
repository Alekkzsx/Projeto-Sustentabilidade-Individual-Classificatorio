import tkinter as tk
from tkinter import messagebox

def acessar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    # Aqui você pode adicionar lógica para verificar os dados de login
    messagebox.showinfo("Acesso", f"Usuário: {usuario}\nSenha: {senha}")

def cadastrar():
    messagebox.showinfo("Cadastro", "Aqui você pode adicionar a lógica de cadastro.")

def recuperar_senha():
    messagebox.showinfo("Recuperar Senha", "Aqui você pode adicionar a lógica para recuperação de senha.")

# Cria a janela principal
root = tk.Tk()
root.title("Tela de Login")

# Cria os elementos da interface
label_usuario = tk.Label(root, text="Nome de Usuário")
label_usuario.pack(pady=10)

entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)

label_senha = tk.Label(root, text="Senha")
label_senha.pack(pady=10)

entry_senha = tk.Entry(root, show="*", width=30)
entry_senha.pack(pady=5)

# Texto para "Esqueceu sua senha?"
label_recuperar = tk.Label(root, text="Esqueceu sua senha? Clique Aqui", fg="blue", cursor="hand2")
label_recuperar.pack(pady=10)
label_recuperar.bind("<Button-1>", lambda e: recuperar_senha())

# Botões de "Faça seu cadastro" e "Acessar"
button_cadastro = tk.Button(root, text="FAÇA SEU CADASTRO", command=cadastrar, bg="white")
button_cadastro.pack(side=tk.LEFT, padx=10, pady=20)

button_acessar = tk.Button(root, text="ACESSAR", command=acessar, bg="green", fg="white")
button_acessar.pack(side=tk.RIGHT, padx=10, pady=20)

# Inicia o loop da interface
root.mainloop()