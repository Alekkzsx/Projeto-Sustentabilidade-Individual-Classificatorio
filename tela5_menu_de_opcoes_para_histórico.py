import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados_usuario(usuario):
    """
    Carrega os dados do usuário do arquivo JSON.
    """
    arquivo_json = "gastos_usuarios.json"
    if not os.path.exists(arquivo_json):
        print("Nenhum dado encontrado para o usuário.")
        return None

    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    
    return dados.get(usuario, [])

def exibir_tabela(categoria, dados):
    """
    Exibe os da1dos do usuário em formato de tabela para a categoria escolhida.
    """
    limpar_tela()
    print("\n" + "═" * 50)
    print(f" HISTÓRICO DE {categoria.upper()} ".center(50, '─'))
    print("═" * 50)
    print(f"{'Categoria':<15}{'Data e Hora':<20}{'Classificação':<15}")
    print("─" * 50)

    encontrou_dados = False
    for registro in dados:
        if categoria == "água":
            print(f"{'Água':<15}{registro['data_hora']:<20}{registro['agua']['classificacao']:<25}")
            encontrou_dados = True
        elif categoria == "energia":
            print(f"{'Energia':<15}{registro['data_hora']:<20}{registro['energia']['classificacao']:<25}")
            encontrou_dados = True
        elif categoria == "resíduos":
            print(f"{'Resíduos':<15}{registro['data_hora']:<20}{registro['residuos']['classificacao']:<25}")
            encontrou_dados = True
        elif categoria == "transporte":
            for transporte in registro["transportes"]:
                print(f"{'Transporte':<15}{registro['data_hora']:<20}{transporte['classificacao']:<25}")
                encontrou_dados = True

    if not encontrou_dados:
        print(f"\nNenhum dado encontrado para a categoria {categoria.capitalize()}.")

    print("═" * 50)
    input("\nPressione Enter para voltar ao menu...")

def exibir_todas_categorias(dados):
    """
    Exibe os dados de todas as categorias em formato de tabela.
    """
    limpar_tela()
    print("\n" + "═" * 70)
    print(" HISTÓRICO DE TODAS AS CATEGORIAS ".center(70, '─'))
    print("═" * 70)
    print(f"{'Categoria':<15}{'Data e Hora':<20}{'Classificação':<15}")
    print("─" * 70)

    encontrou_dados = False
    for registro in dados:
        # Água
        print(f"{'Água':<15}{registro['data_hora']:<20}{registro['agua']['classificacao']:<25}")
        encontrou_dados = True
        # Energia
        print(f"{'Energia':<15}{registro['data_hora']:<20}{registro['energia']['classificacao']:<25}")
        encontrou_dados = True
        # Resíduos
        print(f"{'Resíduos':<15}{registro['data_hora']:<20}{registro['residuos']['classificacao']:<25}")
        encontrou_dados = True
        # Transportes
        for transporte in registro["transportes"]:
            print(f"{'Transporte':<15}{registro['data_hora']:<20}{transporte['classificacao']:<25}")
            encontrou_dados = True

    if not encontrou_dados:
        print("\nNenhum dado encontrado para o usuário.")

    print("═" * 70)
    input("\nPressione Enter para voltar ao menu...")

def mostrar_menu(usuario_logado):
    """
    Exibe o menu principal para escolha de históricos.
    """
    while True:
        limpar_tela()
        print("\n" + "═" * 50)
        print(f" HISTÓRICO DO USUÁRIO: {usuario_logado.upper()} ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Histórico de Água':<38}")
        print(f"{'2. Histórico de Energia':<38}")
        print(f"{'3. Histórico de Transporte':<38}")
        print(f"{'4. Histórico de Resíduos':<38}")
        print(f"{'5. Todas as Categorias':<38}")
        print(f"{'6. Sair':<38}")
        print("═" * 50)

        opcao = input("Escolha o histórico desejado (1-6): ").strip()

        dados = carregar_dados_usuario(usuario_logado)
        if not dados:
            print("\nNenhum dado encontrado para o usuário.")
            input("Pressione Enter para voltar...")
            return

        if opcao == "1":
            exibir_tabela("água", dados)
        elif opcao == "2":
            exibir_tabela("energia", dados)
        elif opcao == "3":
            exibir_tabela("transporte", dados)
        elif opcao == "4":
            exibir_tabela("resíduos", dados)
        elif opcao == "5":
            exibir_todas_categorias(dados)
        elif opcao == "6":
            print("\nSaindo do histórico...")
            break
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    mostrar_menu(usuario_logado)