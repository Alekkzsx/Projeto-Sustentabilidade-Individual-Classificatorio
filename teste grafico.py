import matplotlib.pyplot as plt

def mostrar_grafico():
    # Dados de exemplo
    semanas = ['Sem. 1', 'Sem. 2', 'Sem. 3', 'Sem. 4']
    consumo_agua = [300, 700, 150, 400]

    # Criar o gráfico de barras
    plt.bar(semanas, consumo_agua, color='cyan')
    plt.xlabel('Semana')
    plt.ylabel('Litros')
    plt.title('Gráfico sobre o consumo de água')
    plt.show()

def menu():
    while True:
        print("="*80)
        print("                       BEM-VINDO")
        print("                     O QUE GOSTARIA DE VER?                ")
        print("="*80)
        print("[1] Dias")
        print("[2] Semanas")
        print("[3] Mensal")
        print("[4] Voltar")
        print("="*80)
        
        periodo = input("Escolha um período de tempo: ")
        if periodo == '2':
            print("\nVocê escolheu: Semanas\n")
            break
        elif periodo == '4':
            print("\nVoltando para a tela principal...\n")
            return
        else:
            print("\nOpção inválida. Tente novamente.\n")
    
    while True:
        print("="*80)
        print("                       CATEGORIA DE CONSUMO")
        print("="*80)
        print("[1] Água")
        print("[2] Energia")
        print("[3] Resíduos")
        print("[4] Transporte")
        print("[5] Voltar")
        print("="*80)
        
        categoria = input("Escolha uma categoria de consumo: ")
        if categoria == '1':
            print("\nVocê escolheu: Água\n")
            mostrar_grafico()
            break
        elif categoria == '5':
            print("\nVoltando para a tela principal...\n")
            return
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()