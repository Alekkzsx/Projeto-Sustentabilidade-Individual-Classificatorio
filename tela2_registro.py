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
    print("="*40)
    print("\t\tFAÇA O SEU REGISTRO!")
    print("="*40)
    
    try:
        # Validação do username
        while True:
            username = input("Nome de Usuário: ").strip()
            if username in database_usuarios:
                print("❌ Usuário já existe! Tente outro nome.")
                continue
            if len(username) < 3:
                print("❌ Nome deve ter pelo menos 3 caracteres!")
                continue
            break

        # Validação do e-mail
        while True:
            email = input("E-mail: ").strip()
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$', email):
                print("❌ Formato de e-mail inválido!")
                continue
            break

        # Validação do CPF
        while True:
            cpf = input("CPF (apenas números): ").strip()
            if not validar_cpf(cpf):
                print("❌ CPF inválido! Digite novamente.")
                continue
            break

        # Validação da senha
        while True:
            senha = input("Senha (mínimo 6 caracteres): ").strip()
            if len(senha) < 6:
                print("❌ Senha muito curta!")
                continue
            break

        # Confirmação final
        limpar_tela()
        print("="*40)
        print("\tCONFIRME SEUS DADOS")
        print("="*40)
        print(f"Usuário: {username}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
        print("="*40)
        
        if input("Confirmar cadastro? (S/N): ").upper() != 'S':
            print("\n❌ Cadastro cancelado!")
            return False

        # Salva no banco de dados
        database_usuarios[username] = {
            "nome": username,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "email": email,
            "senha": senha
        }
        salvar_dados()
        
        print("\n✅ Cadastro realizado com sucesso!")
        return True

    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada pelo usuário!")
        return False

if __name__ == "__main__":
    main()