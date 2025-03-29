from BancoDados_UsuarioSenha import database_usuarios, salvar_dados
import re
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11) if (soma % 11) > 1 else 0
    
    # Cálculo do segundo dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11) if (soma % 11) > 1 else 0
    
    return cpf[-2:] == f"{digito1}{digito2}"

def main():
    limpar_tela()
    print("╔" + "═" * 38 + "╗")
    print("║" + "🌟  REGISTRO DE USUÁRIO  🌟".center(38) + "║")
    print("╚" + "═" * 38 + "╝")
    
    try:
        # Seção de cadastro
        print("\n\033[1mDados Pessoais\033[0m".center(40))
        print("─" * 40)
        
        # Validação do username
        while True:
            username = input("│ ► Nome de Usuário: ").strip()
            if username in database_usuarios:
                print("│ ⚠️  \033[31mUsuário já existe! Tente outro.\033[0m")
                print("├" + "─" * 38)
                continue
            if len(username) < 3:
                print("│ ⚠️  \033[31mNome deve ter pelo menos 3 caracteres!\033[0m")
                print("├" + "─" * 38)
                continue
            break

        # Validação do email
        while True:
            email = input("\n│ ► E-mail: ").strip()
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email):
                print("│ ⚠️  \033[31mFormato de e-mail inválido! Ex: user@exemplo.com\033[0m")
                print("├" + "─" * 38)
                continue
            break

        # Validação do CPF
        while True:
            cpf = input("\n│ ► CPF (apenas números): ").strip()
            if not validar_cpf(cpf):
                print("│ ⚠️  \033[31mCPF inválido! Digite 11 números válidos.\033[0m")
                print("├" + "─" * 38)
                continue
            break

        # Validação da senha
        while True:
            senha = input("\n│ ► Senha (mínimo 6 caracteres): ").strip()
            if len(senha) < 6:
                print("│ ⚠️  \033[31mSenha muito curta! Use mais caracteres.\033[0m")
                print("├" + "─" * 38)
                continue
            break

        # Confirmação final
        limpar_tela()
        print("╔" + "═" * 38 + "╗")
        print("║" + "🔍  CONFIRA SEUS DADOS  🔍".center(38) + "║")
        print("╟" + "─" * 38 + "╢")
        print(f"│ ► Usuário: \033[34m{username}\033[0m")
        print(f"│ ► E-mail: \033[34m{email}\033[0m")
        print(f"│ ► CPF: \033[34m{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[0m")
        print("╚" + "═" * 38 + "╝")
        
        confirmacao = input("\n│ ❓ Confirmar cadastro? (S/N): ").upper()
        if confirmacao != 'S':
            print("\n\033[31m✖  Cadastro cancelado!\033[0m")
            return False

        # Salva no banco de dados
        database_usuarios[username] = {
            "nome": username,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "email": email,
            "senha": senha
        }
        salvar_dados()
        
        print("\n\033[32m╔══════════════════════════════════════╗")
        print("║ ✅  CADASTRO REALIZADO COM SUCESSO!  ║")
        print("╚══════════════════════════════════════╝\033[0m")
        return True

    except KeyboardInterrupt:
        print("\n\033[33m⚠️  Operação interrompida pelo usuário!\033[0m")
        return False

if __name__ == "__main__":
    main()