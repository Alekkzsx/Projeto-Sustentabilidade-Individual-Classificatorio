from BancoDados_UsuarioSenha import database_usuarios

print("="*70)
print("\tBem Vindo ao Sistema de Sustentabilidade Individual - Faça Seu Login")
print("="*70)

# Verificação do usuário primeiro
while True:
    NomeDeUsuario = input("\t\tNome de Usuário: ")
    
    # Verifica imediatamente se o usuário existe
    if NomeDeUsuario in database_usuarios:
        break  # Sai do loop se usuário for válido
    else:
        print("\n\t❌ Usuário não cadastrado! Tente novamente.\n")
        print("-"*48)

# Agora verifica a senha
tentativas = 3
while tentativas > 0:
    SenhaDoUsuario = input("\t\tSenha: ")
    
    if database_usuarios[NomeDeUsuario]["senha"] == SenhaDoUsuario:
        print("\n\t✅ Login bem-sucedido!")
        break
    else:
        tentativas -= 1
        print(f"\n\t❌ Senha incorreta! Tentativas restantes: {tentativas}")
        print("-"*48)

if tentativas == 0:
    print("\n\t🚫 Acesso bloqueado! Tente novamente mais tarde.")