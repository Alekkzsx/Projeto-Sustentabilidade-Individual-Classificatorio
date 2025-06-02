# tela1_login.py
from db_manager import conectar_db
import tela2_registro
import os
# --- Importar a lógica da Cifra de Hill ---
from hill_cipher_logic import decrypt as hill_decrypt
# --- Fim da importação ---

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def buscar_usuario_por_username(username):
    """Busca um usuário no banco de dados pelo username."""
    conexao = conectar_db()
    if conexao is None:
        return None

    try:
        cursor = conexao.cursor(dictionary=True) # Retorna como dicionário
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        return cursor.fetchone() # Retorna o dicionário do usuário ou None
    except Exception as err:
        print("Erro ao buscar usuário:", err)
        return None
    finally:
        if conexao and conexao.is_connected(): # Verifica se a conexão existe e está aberta
             if 'cursor' in locals() and cursor: # Verifica se o cursor foi criado
                 cursor.close()
             conexao.close()
             
def redefinir_senha():
    """Permite ao usuário redefinir sua senha após validação de username e CPF."""
    limpar_tela()
    print("\n" + "=" * 70)
    print("🔑 Redefinição de Senha 🔑".center(70))
    print("=" * 70)

    username = input("Digite seu nome de usuário: ").strip()
    cpf_formatado = input("Digite seu CPF (apenas números): ").strip().replace('.', '').replace('-', '').replace('/', '')
    cpf = f"{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}"

    # Busca o usuário no banco de dados pelo username e CPF
    conexao = conectar_db()
    if conexao is None:
        print("\n⚠ Erro ao conectar ao banco de dados. Tente novamente mais tarde.")
        return

    try:
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE username = %s AND cpf = %s"
        cursor.execute(query, (username, cpf))
        usuario = cursor.fetchone()

        if usuario:
            print("\n✅ Usuário validado com sucesso!")
            
            while True:
                nova_senha = input("Digite sua nova senha (mínimo 6 caracteres): ").strip()
                if len(nova_senha) < 6:
                    print("\n⚠ A senha deve ter pelo menos 6 caracteres. Tente novamente.")
                    continue
                
                confirmar_senha = input("Confirme sua nova senha: ").strip()
                if nova_senha != confirmar_senha:
                    print("\n⚠ As senhas não coincidem. Tente novamente.")
                else:
                    break

            # Criptografa a nova senha usando a lógica da cifra de Hill
            from hill_cipher_logic import encrypt as hill_encrypt

            try:
                print("\n🔒 Criptografando senha...")
                senha_criptografada = hill_encrypt(nova_senha)
                print("🔑 Senha processada com sucesso.")
            except Exception as e:
                print(f"\n⚠ Erro ao criptografar a senha: {e}")
                return

            # Atualiza a senha no banco de dados
            update_query = "UPDATE usuarios SET senha = %s WHERE id = %s"
            cursor.execute(update_query, (senha_criptografada, usuario["id"]))
            conexao.commit()

            print("\n✅ Senha redefinida com sucesso!")
        else:
            print("\n❌ Nome de usuário ou CPF inválido. Tente novamente.")
            input("Pressione ENTER...")
    except Exception as err:
        print("\n⚠ Erro ao redefinir senha:", err)
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if conexao and conexao.is_connected():
            conexao.close()

def executar_fluxo_login():
    # Exibe a tela inicial com as opções de Login ou Novo Cadastro
    limpar_tela()
    print("\n" + "=" * 70)
    print("\t🌿 Bem Vindo ao Sistema de Sustentabilidade Individual 🌿")
    print("=" * 70)
    print("\t\t\t[1]  Fazer Login ")
    print("\t\t\t[2]  Novo Cadastro ")
    print("\t\t\t[3]  Esqueci Minha Senha ")
    print("=" * 70)

    # Seleção da opção
    while True:

        opcao = input("Escolha uma opção (1/2/3): ").strip()

        if opcao == '1':
            limpar_tela()
            break
        elif opcao == '2':
            limpar_tela()
            # Chama a função main de registro e verifica se foi bem-sucedido
            registro_ok = tela2_registro.main()
            limpar_tela()
            # Se o registro foi cancelado ou falhou, volta ao menu inicial
            if not registro_ok:
                 print("\nVoltando ao menu principal...")
                 return executar_fluxo_login() # Reinicia o fluxo de login/registro
            # Se o registro foi OK, continua para a tela de login
            return executar_fluxo_login() # Sai do loop de opção e vai para a autenticação
        elif opcao == '3':
            redefinir_senha()
            return executar_fluxo_login()
        else:
            print("\n⚠ Opção inválida!")
            return executar_fluxo_login()
            limpar_tela()
            # Não limpa a tela aqui para o usuário ver a mensagem
            # limpar_tela() # Removido

    # Processo de autenticação do usuário
    UserTentativas = 3
    usuario_correto = None # Armazenará o dicionário do usuário encontrado

    while UserTentativas > 0:
        print("=" * 70)
        print("🔒 Autenticação de Usuário 🔒".center(70))
        print("=" * 70)
        username = input("Digite o nome de usuário: ").strip()

        usuario = buscar_usuario_por_username(username) # Busca o usuário no DB
        if usuario:
            usuario_correto = usuario # Guarda os dados do usuário encontrado
            break # Usuário encontrado, sai do loop de username
        else:
            UserTentativas -= 1
            limpar_tela()
            print("\n" + "=" * 70)
            print("❌ Usuário não cadastrado!".center(70))
            print(f"Tentativas restantes: {UserTentativas}".center(70))
            if UserTentativas == 0: # Verifica aqui se as tentativas acabaram
                 limpar_tela()
                 print("\n" + "=" * 70)
                 print("🚫 Acesso bloqueado!".center(70))
                 print("Usuário não encontrado após múltiplas tentativas.".center(70))
                 print("=" * 70 + "\n")
                 return None # Termina a função se esgotou tentativas do username

    # Se chegou aqui, o usuário foi encontrado (usuario_correto não é None)
    # Autenticação de senha
    tentativas_senha = 3
    # Pega a senha cifrada do banco de dados a partir do dicionário 'usuario_correto'
    senha_cifrada_do_db = usuario_correto["senha"] # Certifique-se que a chave do dicionário é "senha"

    while tentativas_senha > 0:
        print("=" * 70)
        print("🔑 Autenticação de Senha 🔑".center(70))
        print("=" * 70)
        senha_digitada = input("Digite sua Senha: ").strip() # Senha que o usuário digita agora

        # --- Descriptografar a senha do DB e Comparar ---
        try:
            print("\n🔄 Verificando credenciais...") # Mensagem opcional

            # Descriptografar com Hill Cipher
            senha_decifrada_do_db = hill_decrypt(senha_cifrada_do_db)
            print("✅ Credenciais processadas.") # Mensagem opcional

            # Comparar a senha decifrada do DB com a senha digitada AGORA
            if senha_digitada == senha_decifrada_do_db:
                limpar_tela()
                print("\n" + "=" * 70)
                print("✅ Login bem-sucedido!")
                print(f"Bem-vindo, {usuario_correto['username']}!".center(70)) # Exibe o nome de usuário
                print("=" * 70 + "\n")
                return usuario_correto["username"] # Login OK, retorna o username
            else:
                # Senha incorreta
                tentativas_senha -= 1
                limpar_tela()
                print("\n" + "=" * 70)
                print("❌ Senha incorreta!".center(70))
                print(f"Tentativas restantes: {tentativas_senha}".center(70))

        except Exception as e:
            # Outro erro (ex: descriptografia falhou, talvez caractere inválido ou erro na lógica Hill)
            limpar_tela()
            print("\n" + "=" * 70)
            print(f"⚠️ Erro CRÍTICO ao verificar senha: {e}".center(70))
            print("Contacte o administrador.".center(70))
            tentativas_senha -= 1 # Penaliza a tentativa
            print(f"Tentativas restantes: {tentativas_senha}".center(70))
        # --- Fim da Verificação ---

    # Se esgotou as tentativas de senha
    if tentativas_senha == 0:
        limpar_tela()
        print("\n" + "=" * 70)
        print("🚫 Acesso bloqueado!".center(70))
        print("Senha incorreta múltiplas vezes".center(70))
        print("=" * 70 + "\n")
        return None # Termina a função

if __name__ == "__main__":
    resultado_login = executar_fluxo_login()
    if resultado_login:
        print(f"Usuário '{resultado_login}' logado com sucesso.")
        # Aqui você chamaria a próxima parte do seu sistema
    else:
        print("Falha no login ou usuário cancelou.")