def mostrar_menu():
    """Exibe o menu principal de opções"""
    print("\nMENU PRINCIPAL:")
    print("1. Relatórios Semanais")
    print("2. Revisar Informações Enviadas")
    print("3. Configurações")
    print("4. Logout")
    print("5. Sair do Programa")

def relatorio_semanal(dados):
    """Exibe o relatório semanal com base nas informações inseridas"""
    print("\nRelatório Semanal:")
    print(f"Consumo de Água: {dados['consumo_agua']} litros")
    print(f"Consumo de Energia: {dados['consumo_energia']} kWh")
    print(f"Uso de Transporte: {dados['uso_transporte']} %")
    print(f"Resíduos Não Recicláveis: {dados['residuos_nao_reciclaveis']} %")

def revisar_informacoes(dados):
    """Permite o usuário revisar e atualizar as informações"""
    while True:
        print("\nRevisar Informações Enviadas:")
        print(f"1. Consumo de Água: {dados['consumo_agua']} litros")
        print(f"2. Consumo de Energia: {dados['consumo_energia']} kWh")
        print(f"3. Uso de Transporte: {dados['uso_transporte']} %")
        print(f"4. Resíduos Não Recicláveis: {dados['residuos_nao_reciclaveis']} %")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("\nEscolha a opção para editar (1-4) ou 5 para voltar: ")

        try:
            if opcao == '1':
                dados['consumo_agua'] = float(input("Digite o novo valor para o consumo de água (em litros): "))
            elif opcao == '2':
                dados['consumo_energia'] = float(input("Digite o novo valor para o consumo de energia (em kWh): "))
            elif opcao == '3':
                dados['uso_transporte'] = float(input("Digite o novo valor para o uso de transporte (%): "))
            elif opcao == '4':
                dados['residuos_nao_reciclaveis'] = float(input("Digite o novo valor para resíduos não recicláveis (%): "))
            elif opcao == '5':
                break
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Erro! Por favor, insira um valor numérico válido.")

def configuracoes():
    """Exibe as configurações do sistema (simuladas)"""
    print("\nConfigurações: Você pode alterar preferências do sistema.")
    print("Esta funcionalidade ainda não foi implementada.\n")

def logout():
    """Simula o logout do usuário"""
    print("\nVocê foi deslogado com sucesso!")

def main():
    """Função principal que controla o fluxo do programa"""
    dados = {
        'consumo_agua': 0.0,
        'consumo_energia': 0.0,
        'uso_transporte': 0.0,
        'residuos_nao_reciclaveis': 0.0
    }

    while True:
        mostrar_menu()
        
        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == '1':
            relatorio_semanal(dados)
        elif opcao == '2':
            revisar_informacoes(dados)
        elif opcao == '3':
            configuracoes()
        elif opcao == '4':
            logout()
            break
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
