from BancoDados_UsuarioSenha import database_usuarios
import tela2_registro
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def executar_fluxo_login():
    limpar_tela()
    print("=" * 70)
    print("\tBem Vindo ao Sistema de Sustentabilidade Individual")
    print("\t\tFaça Seu Login ou Registre-se")
    print("=" * 70)

    while True:
        opcao = input("\t\t\t[1] Fazer Login\n\t\t\t[2] Novo Cadastro\n\t\t\tEscolha uma opção: ")
        
        if opcao == '1':
            limpar_tela()
            break
        elif opcao == '2':
            limpar_tela()
            if tela2_registro.main():  # Se registro for bem-sucedido
                limpar_tela()
                print("\n" + "=" * 70)
                print("\t\t\tFaça Seu Login")
                print("=" * 70)
            else:  # Se registro for cancelado
                limpar_tela()
                continue
        else:
            print("Opção inválida!")
            limpar_tela()

    # Processo de login
    UserTentativas = 3
    usuario_correto = None

    while UserTentativas > 0:
        usuario = input("\t\tDigite seu Nome de Usuário: ")
        
        if usuario in database_usuarios:
            usuario_correto = usuario
            break
        else:
            UserTentativas -= 1
            limpar_tela()
            print("\n\t❌ Usuário não cadastrado! Tente novamente.")
            print(f"\tTentativas restantes: {UserTentativas}")
            print("-" * 70)

    if UserTentativas == 0:
        limpar_tela()
        print("\n\t🚫 Acesso bloqueado por excesso de tentativas! Tente novamente mais tarde.")
        return None

    # Verificação de senha
    tentativas_senha = 3
    while tentativas_senha > 0:
        senha = input("\t\t\tSenha: ")
        
        if senha == database_usuarios[usuario_correto]["senha"]:
            limpar_tela()
            print("\n\t\t✅ Login bem-sucedido!")
            return usuario_correto  # Retorna o usuário logado
        else:
            tentativas_senha -= 1
            limpar_tela()
            print(f"\n\t❌ Senha incorreta! Tentativas restantes: {tentativas_senha}")
            print("-" * 70)

    limpar_tela()
    print("\n\t🚫 Acesso bloqueado por senha incorreta! Tente novamente mais tarde.")
    return None

if __name__ == "__main__":
    executar_fluxo_login()