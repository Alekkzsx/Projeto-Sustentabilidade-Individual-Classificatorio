from BancoDados_UsuarioSenha import database_usuarios
import tela2_registro
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def executar_fluxo_login():
    # Exibe a tela inicial com as opções de Login ou Novo Cadastro
    limpar_tela()
    print("\n" + "=" * 70)
    print("\t🌿 Bem Vindo ao Sistema de Sustentabilidade Individual 🌿")
    print("=" * 70)
    print("\t\t\t[1]  Fazer Login ")
    print("\t\t\t[2]  Novo Cadastro ")
    print("=" * 70 + "\n")
    
    # Seleção da opção
    while True:
        opcao = input("Escolha uma opção (1/2): ").strip()
        
        if opcao == '1':
            limpar_tela()
            break
        elif opcao == '2':
            limpar_tela()
            tela2_registro.main()
            limpar_tela()
            # Redisplay da tela inicial após o cadastro
            print("\n" + "=" * 70)
            print("🌿 Faça Seu Login 🌿")
            print("=" * 70 + "\n")
        else:
            print("\n⚠ Opção inválida!")
            limpar_tela()
    
    # Processo de autenticação do usuário
    UserTentativas = 3
    usuario_correto = None

    while UserTentativas > 0:
        print("=" * 70)
        print("🔒 Autenticação de Usuário 🔒".center(70))
        print("=" * 70)
        usuario = input("Digite o nome de usuário: ").strip()
        
        if usuario in database_usuarios:
            usuario_correto = usuario
            break
        else:
            UserTentativas -= 1
            limpar_tela()
            print("\n" + "=" * 70)
            print("❌ Usuário não cadastrado!".center(70))
            print(f"Tentativas restantes: {UserTentativas}".center(70))

    if UserTentativas == 0:
        limpar_tela()
        print("\n" + "=" * 70)
        print("🚫 Acesso bloqueado!".center(70))
        print("Tente novamente mais tarde".center(70))
        print("=" * 70 + "\n")
        return None

    # Autenticação de senha
    tentativas_senha = 3

    while tentativas_senha > 0:
        print("=" * 70)
        print("🔑 Autenticação de Senha 🔑".center(70))
        print("=" * 70)
        senha = input("Digite sua Senha: ").strip()
        
        if senha == database_usuarios[usuario_correto]["senha"]:
            limpar_tela()
            print("\n" + "=" * 70)
            print("✅ Login bem-sucedido!")
            print("=" * 70 + "\n")
            return usuario_correto
        else:
            tentativas_senha -= 1
            limpar_tela()
            print("\n" + "=" * 70)
            print("❌ Senha incorreta!".center(70))
            print(f"Tentativas restantes: {tentativas_senha}".center(70))

    if tentativas_senha == 0:
        limpar_tela()
        print("\n" + "=" * 70)
        print("🚫 Acesso bloqueado!".center(70))
        print("Senha incorreta múltiplas vezes".center(70))
        print("=" * 70 + "\n")
        return None

if __name__ == "__main__":
    executar_fluxo_login()