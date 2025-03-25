from BancoDados_UsuarioSenha import database_usuarios

print("=" * 70)
print("\tBem Vindo ao Sistema de Sustentabilidade Individual")
print("\t\t\tFaça Seu Login")
print("=" * 70)

# Verificação do usuário
UserTentativas = 3
usuario_correto = None

while UserTentativas > 0:
    usuario = input("\t\tDigite seu Nome de Usuário: ")
    
    if usuario in database_usuarios:
        usuario_correto = usuario
        break  # Sai do loop se usuário for válido
    else:
        UserTentativas -= 1
        print("\n\t❌ Usuário não cadastrado! Tente novamente.")
        print(f"\tTentativas restantes: {UserTentativas}")
        print("-" * 70)

# Bloqueia se exceder tentativas de usuário
if UserTentativas == 0:
    print("\n\t🚫 Acesso bloqueado por excesso de tentativas! Tente novamente mais tarde.")
else:
    # Verificação da senha
    tentativas_senha = 3
    while tentativas_senha > 0:
        senha = input("\t\t\tSenha: ")
        
        if senha == database_usuarios[usuario_correto]["senha"]:
            print("\n\t\t✅ Login bem-sucedido!")
            break
        else:
            tentativas_senha -= 1
            print(f"\n\t❌ Senha incorreta! Tentativas restantes: {tentativas_senha}")
            print("-" * 70)

    # Bloqueia se exceder tentativas de senha
    if tentativas_senha == 0:
        print("\n\t🚫 Acesso bloqueado por senha incorreta! Tente novamente mais tarde.")