# tela2_registro.py
from db_manager import criar_usuario  # Importa a função correta
import re
import os
# --- Importar a lógica da Cifra de Hill e Base64 ---
from hill_cipher_logic import encrypt as hill_encrypt
import base64
# --- Fim da importação ---

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

        # Validação da senha (obter a senha em texto plano)
        while True:
            # Renomeado para 'senha_plana' para clareza interna, mas pode manter 'senha'
            senha_plana = input("\n│ ► Senha (mínimo 6 caracteres): ").strip()
            if len(senha_plana) < 6:
                print("│ ⚠️  \033[31mSenha muito curta! Use mais caracteres.\033[0m")
                print("├" + "─" * 38)
                continue
            break

        # Confirmação final
        limpar_tela()
        print("╔" + "═" * 38 + "╗")
        print("║" + "🔍  CONFIRA SEUS DADOS  🔍".center(36) + "║")
        print("╟" + "─" * 38 + "╢")
        print("║" + f"  Usuário: \033[34m{username}\033[0m".center(47) + "║")
        print("║" + f"  E-mail: \033[34m{email}\033[0m".center(47) + "║")
        print("║" + f"  CPF: \033[34m{cpf_formatado}\033[0m".center(47) + "║")
        # Não mostre a senha na confirmação!
        print("╚" + "═" * 38 + "╝")

        confirmacao = input("\n│ ❓ Confirmar cadastro? (S/N): ").upper()
        if confirmacao != 'S':
            print("\n\033[31m✖  Cadastro cancelado!\033[0m")
            return False

        # --- Criptografar a senha com Hill Cipher antes de salvar ---
        try:
            print("\n🔒 Criptografando senha...") # Mensagem opcional
            senha_cifrada_raw = hill_encrypt(senha_plana)
            # Codificar em Base64 para armazenamento seguro no DB
            # Usa 'latin-1' para garantir que todos os bytes 0-255 sejam preservados
            senha_cifrada_b64 = base64.b64encode(senha_cifrada_raw.encode('latin-1')).decode('utf-8')
            print("🔑 Senha processada.") # Mensagem opcional
        except Exception as e:
            print(f"\n\033[31m✖ Erro CRÍTICO ao criptografar a senha: {e}\033[0m")
            print("\033[31m✖ Cadastro não pode ser concluído.\033[0m")
            # Poderia ser um caractere inválido ou erro na lógica Hill
            return False
        # --- Fim da Criptografia ---

        # Insere os dados do usuário no banco de dados.
        # AGORA envia a senha criptografada em Base64
        # **IMPORTANTE**: Certifique-se que o campo 'senha' no seu DB (tabela 'usuarios')
        # pode armazenar uma string longa (VARCHAR(100+), TEXT, etc).
        sucesso = criar_usuario(username, username, cpf_formatado, email, senha_cifrada_b64)

        if sucesso:
            limpar_tela()
            print("\n\033[32m╔══════════════════════════════════════╗")
            print("║ ✅  CADASTRO REALIZADO COM SUCESSO!  ║")
            print("╚══════════════════════════════════════╝\033[0m")
            input(print("Pressione ENTER para seguir..."))
            return True
        else:
            limpar_tela()
            print("\n\033[31m✖  Ocorreu um erro ao cadastrar o usuário!\033[0m")
            print("\033[31m✖  Seu Email, CPF ou Username já podem estar cadastrados! \033[0m")
            print("\033[31m✖  Tente novamente com outros dados.\033[0m")
            input(print("Pressione ENTER para seguir..."))
            return False

    except KeyboardInterrupt:
        print("\n\033[33m⚠️  Operação interrompida pelo usuário!\033[0m")
        return False

if __name__ == "__main__":
    main()