def mostrar_menu():
    """Exibe o menu principal para escolha de históricos"""
    print("\n" + "═" * 40)
    print(f"{' MENU DE HISTÓRICOS ':=^40}")
    print("═" * 40)
    print(f"{'1. Histórico de Água':<38} ")
    print(f"{'2. Histórico de Energia':<38} ")
    print(f"{'3. Histórico de Transporte':<38} ")
    print(f"{'4. Histórico de Resíduos':<38} ") 
    print(f"{'5. Todas as Categorias':<38} ")  # Nova opção
    print(f"{'6. Sair do Sistema':<38} ")      # Opção de saída ajustada
    print("═" * 40)

def exibir_historico(tipo):
    """Exibe mensagem de implementação para os históricos"""
    print("\n" + "═" * 40)
    print(f" HISTÓRICO DE {tipo.upper()} ".center(40, '─'))
    print("\n  🔨 Esta funcionalidade está em desenvolvimento!")
    print("  📅 Previsão de implementação: versão 2.0\n")
    print("═" * 40)
    input("Pressione Enter para voltar...")

def exibir_todas_categorias():
    """Exibe mensagem unificada para todas as categorias"""
    print("\n" + "═" * 40)
    print(" VISUALIZAÇÃO INTEGRADA ".center(40, '─'))
    print("\n  🌐 Carregando dados combinados...")
    print("  ⚙️  Processando todas as categorias")
    print("\n  🔧 Funcionalidade em desenvolvimento")
    print("  🚀 Lançamento previsto: versão 3.0\n")
    print("═" * 40)
    input("Pressione Enter para continuar...")

def main():
    """Função principal com nova opção integrada"""
    while True:
        mostrar_menu()
        opcao = input("\nEscolha o histórico desejado (1-6): ").strip()  # Ajustado para 6 opções
        
        if opcao == "1":
            exibir_historico('Água')
        elif opcao == "2":
            exibir_historico('Energia')
        elif opcao == "3":
            exibir_historico('Transporte')
        elif opcao == "4":
            exibir_historico('Resíduos')
        elif opcao == "5":  # Nova opção
            exibir_todas_categorias()
        elif opcao == "6":
            print("\n" + "═" * 40)
            print(f"{' OBRIGADO POR USAR O SISTEMA! ':=^40}")
            print("═" * 40 + "\n")
            break
        else:
            print("\n⚠ Opção inválida! Use valores de 1 a 6.")  # Mensagem atualizada
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()