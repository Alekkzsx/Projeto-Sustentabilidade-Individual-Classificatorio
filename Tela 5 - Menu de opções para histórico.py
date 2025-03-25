def mostrar_menu():
    print("\n" + "="*28)
    print("=== MENU DE CATEGORIAS ===".center(28))
    print("="*28)
    print("1. Água".ljust(26) + " ")
    print("2. Energia".ljust(26) + " ")
    print("3. Transporte".ljust(26) + " ")
    print("4. Reciclável".ljust(26) + " ")
    print("5. Sair".ljust(26) + " ")
    print("="*28)

def menu_agua():
    print("\n" + "-"*30)
    print(" SUBCATEGORIAS DE ÁGUA ".center(30, '-'))
    print("-"*30)
    print("1. Consumo residencial".ljust(28) + " ")
    print("2. Consumo comercial".ljust(28) + " ")
    print("3. Dicas de economia".ljust(28) + " ")
    print("4. Voltar ao menu principal".ljust(28) + " ")
    opcao = input("\nEscolha uma opção: ").strip()
    # Lógica permanece a mesma

def menu_energia():
    print("\n" + "-"*32)
    print(" SUBCATEGORIAS DE ENERGIA ".center(32, '-'))
    print("-"*32)
    print("1. Energia elétrica".ljust(30) + " ")
    print("2. Energia solar".ljust(30) + " ")
    print("3. Energia eólica".ljust(30) + " ")
    print("4. Dicas de economia".ljust(30) + " ")
    print("5. Voltar ao menu principal".ljust(30) + " ")
    opcao = input("\nEscolha uma opção: ").strip()
    # Lógica permanece a mesma

def menu_transporte():
    print("\n" + "-"*34)
    print(" SUBCATEGORIAS DE TRANSPORTE ".center(34, '-'))
    print("-"*34)
    print("1. Transporte público".ljust(32) + " ")
    print("2. Transporte individual".ljust(32) + " ")
    print("3. Transporte sustentável".ljust(32) + " ")
    print("4. Voltar ao menu principal".ljust(32) + " ")
    opcao = input("\nEscolha uma opção: ").strip()
    # Lógica permanece a mesma

def menu_reciclavel():
    print("\n" + "-"*34)
    print(" SUBCATEGORIAS DE RECICLÁVEL ".center(34, '-'))
    print("-"*34)
    print("1. Plástico".ljust(32) + " ")
    print("2. Papel".ljust(32) + " ")
    print("3. Vidro".ljust(32) + " ")
    print("4. Metal".ljust(32) + " ")
    print("5. Orgânicos".ljust(32) + " ")
    print("6. Voltar ao menu principal".ljust(32) + " ")
    opcao = input("\nEscolha uma opção: ").strip()
    # Lógica permanece a mesma

def main():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma categoria (1-5): ").strip()
        
        if opcao == "1":
            menu_agua()
        elif opcao == "2":
            menu_energia()
        elif opcao == "3":
            menu_transporte()
        elif opcao == "4":
            menu_reciclavel()
        elif opcao == "5":
            print("\n" + "="*28)
            print(" Saindo do programa... ".center(28))
            print("="*28 + "\n")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()
