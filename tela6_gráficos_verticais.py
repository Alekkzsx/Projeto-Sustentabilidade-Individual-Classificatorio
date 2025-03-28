import os
import json
from datetime import datetime, timedelta

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

def exibir_grafico(categoria, periodo, dados):
    """
    Exibe o gráfico vertical para a categoria e período escolhidos.
    """
    limpar_tela()
    print("\n" + "═" * 50)
    print(f" GRÁFICO DE {categoria.upper()} ({periodo.upper()}) ".center(50, '─'))
    print("═" * 50)

    # Dicionário para acumular os valores por período
    acumulados = {}

    # Determinar os períodos a serem exibidos
    hoje = datetime.now()
    if periodo == "diário":
        periodos = [(hoje - timedelta(days=i)).strftime("%d/%m/%Y") for i in range(6, -1, -1)]  # Últimos 7 dias
    elif periodo == "mensal":
        periodos = [(hoje - timedelta(days=30 * i)).strftime("%m/%Y") for i in range(11, -1, -1)]  # Últimos 12 meses
    elif periodo == "anual":
        periodos = [(hoje.year - i) for i in range(4, -1, -1)]  # Últimos 5 anos
    else:
        print("\n⚠ Período inválido!")
        return

    # Acumular os valores para os períodos
    for registro in dados:
        if periodo == "diário":
            chave = registro["data_hora"].split(" ")[0]  # Apenas a data (ex: "28/03/2025")
        elif periodo == "mensal":
            chave = registro["data_hora"].split("/")[1] + "/" + registro["data_hora"].split("/")[2].split(" ")[0]  # Mês/Ano (ex: "03/2025")
        elif periodo == "anual":
            chave = int(registro["data_hora"].split("/")[2].split(" ")[0])  # Apenas o ano (ex: "2025")
        else:
            continue

        if chave in periodos:
            if chave not in acumulados:
                acumulados[chave] = registro[categoria]["valor"]
            else:
                acumulados[chave] += registro[categoria]["valor"]

    # Preencher períodos sem dados com valor 0
    valores = [acumulados.get(p, 0) for p in periodos]

    # Normalizar os valores para o gráfico
    max_valor = max(valores) if valores else 1
    escala = max(10, max_valor // 10)  # Define a escala mínima de 10

    # Exibir o gráfico
    print(f"\n{'Período':<15}{'Valor':<10}")
    print("-" * 50)

    for i in range(10, 0, -1):  # De cima para baixo
        linha = ''
        for valor in valores:
            if valor >= (i * escala / 10):
                linha += ' *** '
            else:
                linha += '     '
        print(f'{int(i * escala / 10):>4} |{linha}')
    print('     ' + '-' * (len(valores) * 5))
    print('      ' + '  '.join([str(p)[:5] for p in periodos]))  # Exibe os períodos no eixo horizontal

    input("\nPressione Enter para voltar...")

def menu_graficos(usuario_logado):
    """
    Menu principal para exibição de gráficos.
    """
    while True:
        limpar_tela()
        print("\n" + "═" * 50)
        print(f" GRÁFICOS DE CONSUMO - USUÁRIO: {usuario_logado.upper()} ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Diário':<38}")
        print(f"{'2. Mensal':<38}")
        print(f"{'3. Anual':<38}")
        print(f"{'4. Voltar':<38}")
        print(f"{'5. Sair':<38}")
        print("═" * 50)

        opcao_periodo = input("Escolha o período desejado (1-5): ").strip()

        if opcao_periodo == "4":
            print("\nVoltando ao menu anterior...")
            break
        elif opcao_periodo == "5":
            print("\nSaindo do programa...")
            exit()

        periodo = None
        if opcao_periodo == "1":
            periodo = "diário"
        elif opcao_periodo == "2":
            periodo = "mensal"
        elif opcao_periodo == "3":
            periodo = "anual"
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        limpar_tela()
        print("\n" + "═" * 50)
        print(f" CATEGORIAS DISPONÍVEIS ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Água':<38}")
        print(f"{'2. Energia':<38}")
        print(f"{'3. Resíduos':<38}")
        print(f"{'4. Transporte':<38}")
        print(f"{'5. Voltar':<38}")
        print("═" * 50)

        opcao_categoria = input("Escolha a categoria desejada (1-5): ").strip()

        if opcao_categoria == "5":
            continue

        categoria = None
        if opcao_categoria == "1":
            categoria = "agua"
        elif opcao_categoria == "2":
            categoria = "energia"
        elif opcao_categoria == "3":
            categoria = "residuos"
        elif opcao_categoria == "4":
            categoria = "transportes"
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        # Carregar os dados do usuário
        dados = carregar_dados_usuario(usuario_logado)
        if not dados:
            print("\nNenhum dado encontrado para o usuário.")
            input("Pressione Enter para voltar...")
            continue

        # Exibir o gráfico para a categoria e período escolhidos
        exibir_grafico(categoria, periodo, dados)

if __name__ == "__main__":
    usuario_logado = input("Digite o nome do usuário logado: ").strip()
    menu_graficos(usuario_logado)