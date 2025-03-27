import datetime
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        print("\n╔" + "═" * 78 + "╗")
        print("║" + " BEM-VINDO AO SISTEMA DE SUSTENTABILIDADE ".center(78, '─') + "║")
        print("╠" + "═" * 78 + "╣")
        print("║" + "O QUE VOCÊ GOSTARIA DE FAZER HOJE?".center(78) + "║")
        print("╚" + "═" * 78 + "╝")

        print("\t\t\t    [1] Registrar novos dados")
        print("\t\t\t    [2] Acessar Histórico")
        print("\t\t\t    [3] Sair")
        print("─" * 79)

        choice = input("▶ Escolha uma opção (1/2/3): ")
        
        if choice == '1':
            limpar_tela()
            try:
                print("\n" + "═" * 78)
                print(" NOVO REGISTRO ".center(78, '─'))
                print("═" * 78)
                
                agua = float(input("\n► Consumo de água (litros): "))
                energia = float(input("► Consumo de energia (KWh): "))

                transporte_categorias = {
                    'transporte_eco': ["bicicleta", "a pé", "patinete"],
                    'transporte_sustentavel': ["ônibus", "metrô", "trem"],
                    'transporte_baixo': ["bicicleta elétrica", "patins elétrico"],
                    'transporte_poluente': ["carro", "moto", "caminhão"]
                }

                transportes = []
                print("\n" + "─" * 78)
                print(" CATEGORIAS DE TRANSPORTE ".center(78, '─'))
                print("\t🟢Meio Ambiente Agradece  🟡Sustentável  🟠Baixo  🔴Poluente")
                print("─" * 78)

                while True:
                    transporte = input("\n► Transporte utilizado (deixe em branco para sair): ").lower().strip()
                    if not transporte:
                        break

                    categoria = None
                    if transporte in transporte_categorias['transporte_eco']:
                        categoria = "🟢"
                    elif transporte in transporte_categorias['transporte_sustentavel']:
                        categoria = "🟡"
                    elif transporte in transporte_categorias['transporte_baixo']:
                        categoria = "🟠"
                    elif transporte in transporte_categorias['transporte_poluente']:
                        categoria = "🔴"
                    else:
                        print("► Categoria não reconhecida! Use transporte listado.")
                        continue

                    vezes = int(input(f"► Quantidade de viagens com {transporte}: "))
                    transportes.append((transporte, vezes, categoria))

                residuos = float(input("\n► Resíduos não recicláveis (%): "))
                limpar_tela()
                
                data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                print("\n╔" + "═" * 78 + "╗")
                print("║" + " DADOS REGISTRADOS ".center(78, '─') + "║")
                print(f"║ 📅 Data/hora: {data_hora}".ljust(79) + "║")
                print(f"║ 🌊 Água: {agua}L".ljust(79) + "║")
                print(f"║ 💡 Energia: {energia}KWh".ljust(79) + "║")
                print(f"║ 🚦 Transportes registrados: {len(transportes)}".ljust(79) + "║")
                print(f"║ ♻️ Resíduos: {residuos}%".ljust(79) + "║")
                print("╚" + "═" * 78 + "╝")
                input("\nPressione Enter para continuar...")

            except ValueError:
                limpar_tela()
                print("\n╔" + "═" * 78 + "╗")
                print("║" + " ERRO: VALOR INVÁLIDO! ".center(78, '!') + "║")
                print("╚" + "═" * 78 + "╝")
                input("Pressione Enter para tentar novamente...")
        
        elif choice == '2':
            limpar_tela()
            print("\n╔" + "═" * 78 + "╗")
            print("║" + " HISTÓRICO (EM DESENVOLVIMENTO) ".center(78, '~') + "║")
            print("╚" + "═" * 78 + "╝")
            input("\nPressione Enter para voltar...")
        
        elif choice == '3':
            limpar_tela()
            print("\n╔" + "═" * 78 + "╗")
            print("║" + " OBRIGADO POR UTILIZAR NOSSO SISTEMA! ".center(78) + "║")
            print("╚" + "═" * 78 + "╝")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()