from BancoDados_UsuarioSenha import database_usuarios
import tela2_registro
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# ============================================================
#                   TELA INICIAL
# ============================================================
print("\n" + "=" * 70)
print(f"{'\t\t\tTela Inicial\n\t\tSistema de Sustentabilidade Individual':^70}")
print("=" * 70)
print(f"{'\t\t\t[1] Fazer Login':^32}")
print(f"{'\t\t\t[2] Novo Cadastro':^34}")
print("=" * 70 + "\n")

# ============================================================
#                  SELEÇÃO DE OPÇÃO
# ============================================================
while True:
    opcao = input(f"{'Escolha uma opção (1/2): ':>28}").strip()
    
    if opcao == '1':
        limpar_tela()
        break
        
    elif opcao == '2':
        limpar_tela()
        tela2_registro.main()
        limpar_tela()
        
        # Redisplay após registro
        print("\n" + "=" * 70)
        print(f"{'Faça Seu Login':^70}")
        print("=" * 70 + "\n")
        
    else:
        print(f"\n{'⚠ Opção inválida!':^70}")
        limpar_tela()

# ============================================================
#                  AUTENTICAÇÃO DE USUÁRIO
# ============================================================
UserTentativas = 3
usuario_correto = None

while UserTentativas > 0:
    print("="*70)
    usuario = input(f"{'Digite o nome de usuário: ':>25}").strip()
    
    if usuario in database_usuarios:
        usuario_correto = usuario
        break
        
    else:
        UserTentativas -= 1
        limpar_tela()
        print("\n" + "=" * 70)
        print(f"{'❌ Usuário não cadastrado!':^70}")
        print(f"{f'Tentativas restantes: {UserTentativas}':^70}")
        print("=" * 70 + "\n")

if UserTentativas == 0:
    limpar_tela()
    print("\n" + "=" * 70)
    print(f"{'🚫 Acesso bloqueado!':^70}")
    print(f"{'Tente novamente mais tarde':^70}")
    print("=" * 70 + "\n")
    exit()

# ============================================================
#                  AUTENTICAÇÃO DE SENHA
# ============================================================
tentativas_senha = 3

while tentativas_senha > 0:
    senha = input("Digite sua Senha: ").strip()
    
    if senha == database_usuarios[usuario_correto]["senha"]:
        limpar_tela()
        print("\n" + "=" * 70)
        print(f"{'✅ Login bem-sucedido!':^70}")
        print("=" * 70 + "\n")
        break
        
    else:
        tentativas_senha -= 1
        limpar_tela()
        print("\n" + "=" * 70)
        print(f"{'❌ Senha incorreta!':^70}")
        print(f"{f'Tentativas restantes: {tentativas_senha}':^70}")
        print("=" * 70 + "\n")

if tentativas_senha == 0:
    limpar_tela()
    print("\n" + "=" * 70)
    print(f"{'🚫 Acesso bloqueado!':^70}")
    print(f"{'Senha incorreta múltiplas vezes':^70}")
    print("=" * 70 + "\n")