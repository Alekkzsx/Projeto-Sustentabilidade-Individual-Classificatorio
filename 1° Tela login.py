# Tela Login com Placeholders Centralizados (Senha Corrigida)
import tkinter as tk
from tkinter import ttk, messagebox

def criar_tela_login():
    janela = tk.Tk()
    janela.title("Sistema de Login")
    janela.configure(bg="white")
    janela.geometry("400x400")

    # Variável para armazenar a senha real
    senha_real = tk.StringVar()

    # Estilo para campos de entrada
    estilo = ttk.Style()
    estilo.configure("Placeholder.TEntry", foreground="#808080", justify="center")

    # Frame principal centralizado
    frame_principal = tk.Frame(janela, bg="white")
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")

    # Função para gerenciar placeholders
    def config_placeholder(entry, texto, is_password=False):
        entry.insert(0, texto)
        entry.config(style="Placeholder.TEntry")
        if is_password:
            entry.config(show="")
        entry.bind("<FocusIn>", lambda e: remover_placeholder(entry, texto, is_password))
        entry.bind("<FocusOut>", lambda e: restaurar_placeholder(entry, texto, is_password))

    def remover_placeholder(entry, texto, is_password):
        if entry.get() == texto:
            entry.delete(0, tk.END)
            entry.config(style="TEntry", foreground="black", justify="left")
            if is_password:
                entry.config(show="*")

    def restaurar_placeholder(entry, texto, is_password):
        if not entry.get():
            entry.insert(0, texto)
            entry.config(style="Placeholder.TEntry", justify="center")
            if is_password:
                entry.config(show="")

    # Campo de Usuário
    entrada_usuario = ttk.Entry(frame_principal, width=30, font=("Arial", 10))
    entrada_usuario.pack(pady=15, ipady=8)
    config_placeholder(entrada_usuario, "Nome de Usuário")

    # Campo de Senha
    entrada_senha = ttk.Entry(
        frame_principal,
        width=30,
        font=("Arial", 10),
        textvariable=senha_real
    )
    entrada_senha.pack(pady=15, ipady=8)
    config_placeholder(entrada_senha, "Senha", is_password=True)

    # Link "Esqueceu a senha"
    def esqueceu_senha():
        messagebox.showinfo("Recuperação", "Entre em contato com o suporte")

    link_senha = tk.Label(
        frame_principal,
        text="Esqueceu sua senha? Clique Aqui",
        fg="blue",
        cursor="hand2",
        bg="white"
    )
    link_senha.pack(pady=10)
    link_senha.bind("<Button-1>", lambda e: esqueceu_senha())

    # Botões
    frame_botoes = tk.Frame(frame_principal, bg="white")
    frame_botoes.pack(pady=20)

    btn_cadastrar = tk.Button(
        frame_botoes,
        text="FAÇA SEU CADASTRO",
        command=lambda: messagebox.showinfo("Cadastro", "Redirecionando..."),
        bg="#4CAF50",
        fg="white",
        padx=20
    )
    btn_cadastrar.pack(side=tk.LEFT, padx=10)

    def validar_login():
        usuario = entrada_usuario.get()
        senha = senha_real.get()  # Usa a variável que armazena o valor real
        
        # Verifica se os valores não são placeholders
        usuario_valido = usuario not in ["", "Nome de Usuário"]
        senha_valida = senha not in ["", "Senha"]
        
        if usuario_valido and senha_valida:
            messagebox.showinfo("Sucesso", "Login realizado!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    btn_acessar = tk.Button(
        frame_botoes,
        text="ACESSAR",
        command=validar_login,
        bg="#2196F3",
        fg="white",
        padx=30
    )
    btn_acessar.pack(side=tk.LEFT, padx=10)

    janela.mainloop()

if __name__ == "__main__":
    criar_tela_login()