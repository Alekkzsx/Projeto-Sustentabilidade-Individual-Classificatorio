#Tela Login

import tkinter as tk
from tkinter import messagebox

def criar_tela_login():
    # Configuração da janela principal
    janela = tk.Tk()
    janela.title("Sistema de Login")
    janela.configure(bg="#f0f0f0")
    
    # Centralizar elementos
    frame = tk.Frame(janela, bg="#f0f0f0")
    frame.pack(padx=20, pady=20)

    # Componentes da interface
    tk.Label(frame, text="Nome de Usuário", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    entrada_usuario = tk.Entry(frame, width=25)
    entrada_usuario.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Senha", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    entrada_senha = tk.Entry(frame, width=25, show="*")
    entrada_senha.grid(row=1, column=1, pady=5)

    # Link 'Esqueceu a senha'
    def esqueceu_senha():
        messagebox.showinfo("Recuperação", "Entre em contato com o suporte")
        
    link_senha = tk.Label(frame, text="Esqueceu sua senha? Clique Aqui", fg="blue", cursor="hand2", bg="#f0f0f0")
    link_senha.grid(row=2, columnspan=2, pady=5)
    link_senha.bind("<Button-1>", lambda e: esqueceu_senha())

    # Botões
    def cadastrar():
        messagebox.showinfo("Cadastro", "Redirecionando para cadastro...")
        
    tk.Button(frame, text="FAÇA SEU CADASTRO", command=cadastrar, bg="#4CAF50", fg="white").grid(row=3, column=0, pady=10, padx=5)

    def acessar():
        if entrada_usuario.get() and entrada_senha.get():
            messagebox.showinfo("Sucesso", "Login realizado!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")
    
    tk.Button(frame, text="ACESSAR", command=acessar, bg="#2196F3", fg="white").grid(row=3, column=1, pady=10, padx=5)

    janela.mainloop()

if __name__ == "__main__":
    criar_tela_login()
