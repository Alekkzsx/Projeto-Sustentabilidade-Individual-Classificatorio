import datetime
import os
import json

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_dados_json(usuario, agua, energia, residuos, transportes, classificacoes):
    """
    Salva os dados do usuário em um arquivo JSON chamado 'gastos_usuarios.json'.
    Se o arquivo não existir, ele será criado.
    """
    arquivo_json = "gastos_usuarios.json"
    
    # Cria o arquivo JSON se não existir
    if not os.path.exists(arquivo_json):
        with open(arquivo_json, 'w') as f:
            json.dump({}, f)
    
    # Carrega os dados existentes do arquivo JSON
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    
    # Adiciona o usuário se não estiver no arquivo
    if usuario not in dados:
        dados[usuario] = []
    
    # Adiciona o novo registro com data/hora
    registro = {
        "data_hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "agua": {"valor": agua, "classificacao": classificacoes["agua"]},
        "energia": {"valor": energia, "classificacao": classificacoes["energia"]},
        "residuos": {"valor": residuos, "classificacao": classificacoes["residuos"]},
        "transportes": [
            {"meio": t[0], "viagens": t[1], "classificacao": t[2]} for t in transportes
        ]
    }
    dados[usuario].append(registro)
    
    # Salva os dados atualizados no arquivo JSON
    with open(arquivo_json, 'w') as f:
        json.dump(dados, f, indent=4)

def main(usuario_logado):
    while True:
        limpar_tela()
        # Exibe uma mensagem de boas-vindas com o nome do usuário
        print(f"\nBem-vindo(a), {usuario_logado}!")
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
            print("\n" + "═" * 78)
            print(" NOVO REGISTRO ".center(78, '─'))
            print("═" * 78)
            
            # Validação para o consumo de água
            while True:
                try:
                    agua = float(input("\n► Consumo de água (litros): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para o consumo de água.")

            # Validação para o consumo de energia
            while True:
                try:
                    energia = float(input("► Consumo de energia (KWh): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para o consumo de energia.")

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

            # Loop para registrar transportes
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

                # Validação para a quantidade de viagens
                while True:
                    try:
                        vezes = float(input(f"► Quantidade de viagens com {transporte}: "))
                        break
                    except ValueError:
                        print("ERRO: Por favor, insira um número válido para a quantidade de viagens.")

                transportes.append((transporte, vezes, categoria))

            # Validação para resíduos não recicláveis
            while True:
                try:
                    residuos = float(input("\n► Resíduos não recicláveis (%): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para os resíduos não recicláveis.")

            limpar_tela()

            # Classificação dos dados
            classificacoes = {
                "agua": "🟢 Meio Ambiente Agradece" if agua < 100 else "🟡 Alta Sustentabilidade" if agua < 150 else "🟠 Moderada Sustentabilidade" if agua < 200 else "🔴 Baixa Sustentabilidade",
                "energia": "🟢 Meio Ambiente Agradece" if energia < 2.5 else "🟡 Alta Sustentabilidade" if energia < 5 else "🟠 Moderada Sustentabilidade" if energia < 10 else "🔴 Baixa Sustentabilidade",
                "residuos": "🟢 Meio Ambiente Agradece" if residuos < 20 else "🟡 Alta Sustentabilidade" if residuos < 50 else "🟠 Moderada Sustentabilidade" if residuos < 60 else "🔴 Baixa Sustentabilidade"
            }

            # Salvar os dados no arquivo JSON
            salvar_dados_json(usuario_logado, agua, energia, residuos, transportes, classificacoes)
            
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
    main("Usuário")