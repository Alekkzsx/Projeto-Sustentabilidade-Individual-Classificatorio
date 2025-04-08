from db_manager import inserir_usuario
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
    print("╔" + "═" * 40 + "╗")
    print("║" + "🌟  REGISTRO DE USUÁRIO  🌟".center(38) + "║")
    print("╚" + "═" * 40 + "╝")
    
    try:
        # Seção de cadastro
        print("\033[1mDados Pessoais\033[0m".center(50))
        print("─" * 42)
        
        # Validação do username
        while True:
            username = input("│ ► Nome de Usuário: ").strip()
            # Aqui podemos opcionalmente consultar no banco se já existe
            # Para simplificar, vamos validar apenas a quantidade de caracteres.
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
            # Formata o CPF para o padrão 000.000.000-00
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
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
        
        print("╔" + "═" * 38 + "╗")
        print("║" + "🔍  CONFIRA SEUS DADOS  🔍".center(36) + "║")
        print("╟" + "─" * 38 + "╢")
        print("║" + f"  Usuário: \033[34m{username}\033[0m".center(47) + "║")
        print("║" + f"  E-mail: \033[34m{email}\033[0m".center(47) + "║")
        print("║" + f"  CPF: \033[34m{cpf_formatado}\033[0m".center(47) + "║")
        print("╚" + "═" * 38 + "╝")
        
        confirmacao = input("\n│ ❓ Confirmar cadastro? (S/N): ").upper()
        if confirmacao != 'S':
            print("\n\033[31m✖  Cadastro cancelado!\033[0m")
            return False

        # Insere os dados do usuário no banco de dados.
        # Note que, por simplicidade, estamos utilizando o mesmo valor para username e nome.
        sucesso = inserir_usuario(username, username, cpf_formatado, email, senha)
        
        if sucesso:
            print("\n\033[32m╔══════════════════════════════════════╗")
            print("║ ✅  CADASTRO REALIZADO COM SUCESSO!  ║")
            print("╚══════════════════════════════════════╝\033[0m")
            return True
        else:
            print("\n\033[31m✖  Ocorreu um erro ao cadastrar o usuário!\033[0m")
            return False

    except KeyboardInterrupt:
        print("\n\033[33m⚠️  Operação interrompida pelo usuário!\033[0m")
        return False

if __name__ == "__main__":
    main()
