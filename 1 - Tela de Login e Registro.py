import os
import json
import platform

# Configurações
ARQUIVO_USUARIOS = "usuario_cadastro.json"
LINHA = "=" * 40

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def mostrar_titulo(titulo):
    """Mostra o cabeçalho da tela"""
    print(LINHA)
    print(titulo.center(40))
    print("Sustentabilidade Individual".center(40))
    print(LINHA + "\n")

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON"""
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'w') as f:
            json.dump([], f)
        return []
    
    with open(ARQUIVO_USUARIOS, 'r') as f:
        return json.load(f)

def login():
    """Tela de login com verificação de erros"""
    limpar_tela()
    mostrar_titulo("Faça seu Login!")
    
    usuarios = carregar_usuarios()
    username = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    # Verifica se o usuário existe
    usuario_existente = next((u for u in usuarios if u["username"] == username), None)
    
    if not usuario_existente:
        print("\nErro: Usuário não cadastrado!")
        input("Pressione Enter para voltar...")
        return
    
    if usuario_existente["senha"] != senha:
        print("\nErro: Senha incorreta!")
        input("Pressione Enter para voltar...")
        return
    
    print("\nLogin realizado com sucesso!")
    input("Pressione Enter para continuar...")

def registro():
    """Tela de registro simplificada"""
    limpar_tela()
    mostrar_titulo("Faça seu Registro")
    
    usuarios = carregar_usuarios()
    
    novo_usuario = {
        "username": input("Nome de usuário: "),
        "email": input("Email: "),
        "cpf": input("CPF: "),
        "senha": input("Senha: ")
    }
    
    if input("\nConfirmar cadastro? (s/n): ").lower() == 's':
        usuarios.append(novo_usuario)
        with open(ARQUIVO_USUARIOS, 'w') as f:
            json.dump(usuarios, f, indent=4)
        
        print("\nCadastro realizado! Faça login.")
        input("Pressione Enter para continuar...")
        login()

def main():
    """Menu principal"""
    while True:
        limpar_tela()
        mostrar_titulo("Faça seu Login!")
        
        print("1. Login")
        print("2. Registro")
        print("3. Sair\n")
        
        opcao = input("Escolha: ")
        
        if opcao == '1':
            login()
        elif opcao == '2':
            registro()
        elif opcao == '3':
            print("\nAté logo!")
            break
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()