def main():
    print("========================================")
    print("               FAÇA O SEU REGISTRO!               ")
    print("========================================")
    print("Nome de Usuário: ________________________")
    print("E-mail: ________________________")
    print("Seu CPF: ________________________")
    print("Sua Senha: ________________________")
    print("========================================")
    print("[1] SAIR")
    print("[2] REGISTRE-SE")
    print("========================================")

    while True:
        choice = input("Escolha uma opção: ")
        if choice == '1':
            print("Saindo...")
            break
        elif choice == '2':
            username = input("Nome de Usuário: ")
            email = input("E-mail: ")
            cpf = input("Seu CPF: ")
            password = input("Sua Senha: ")
            print("Registrando...")
            # Aqui você pode adicionar o código para registrar os dados
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()