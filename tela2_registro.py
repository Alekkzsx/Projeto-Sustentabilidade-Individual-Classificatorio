from BancoDados_UsuarioSenha import database_usuarios
import re
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    if len(cpf) != 11:
        return False
    
    # Verifica dígitos repetidos
    if cpf == cpf[0] * 11:
        return False
    
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    return cpf[-2:] == f"{digito1}{digito2}"

def main():
    limpar_tela()
    print("="*40)
    print("\t\tFAÇA O SEU REGISTRO!")
    print("="*40)
    
    while True:
        # Validação do nome de usuário
        while True:
            username = input("Nome de Usuário: ").strip()
            if username in database_usuarios:
                print("❌ Este nome de usuário já está em uso!")
                continue
            if len(username) < 3:
                print("❌ O nome deve ter pelo menos 3 caracteres!")
                continue
            break
        
        # Validação do e-mail
        while True:
            email = input("E-mail: ").strip()
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                print("❌ E-mail inválido! Use o formato nome@provedor.com")
                continue
            break
        
        # Validação do CPF
        while True:
            cpf = input("CPF (somente números): ").strip()
            if not validar_cpf(cpf):
                print("❌ CPF inválido! Digite novamente.")
                continue
            break
        
        # Validação da senha
        while True:
            password = input("Senha (mínimo 6 caracteres): ").strip()
            if len(password) < 6:
                print("❌ Senha muito curta!")
                continue
            break
        
        # Confirmação dos dados
        limpar_tela()
        print("="*40)
        print("\tCONFIRME SEUS DADOS")
        print("="*40)
        print(f"Usuário: {username}")
        print(f"E-mail: {email}")
        print(f"CPF: {cpf}")
        print("="*40)
        
        confirmacao = input("Confirmar cadastro? (S/N): ").upper()
        if confirmacao == 'S':
            # Formata o CPF
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            
            # Adiciona ao banco de dados
            database_usuarios[username] = {
                "nome": username,
                "cpf": cpf_formatado,
                "email": email,
                "senha": password
            }
            
            limpar_tela()
            print("\n✅ Cadastro realizado com sucesso!")
            print("Retornando ao menu principal...")
            break
        else:
            limpar_tela()
            print("\n❌ Cadastro cancelado!")
            break

if __name__ == "__main__":
    main()