import os
from datetime import datetime, timedelta
from db_manager import buscar_gastos_usuario, buscar_transportes_usuario

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados_usuario(id_usuario):
    """
    Carrega os dados do usuário do banco de dados.
    """
    dados_gastos = buscar_gastos_usuario(id_usuario)
    dados_transportes = buscar_transportes_usuario(id_usuario)
    if not dados_gastos and not dados_transportes:
        print("Nenhum dado encontrado para o usuário.")
        return None
    return {"gastos": dados_gastos, "transportes": dados_transportes}

def obter_periodos(dados, periodo):
    """
    Retorna os períodos disponíveis no banco de dados com base no tipo de período escolhido.
    """
    periodos = []

    if periodo == "dias":
        # Obter todas as datas únicas
        periodos = sorted(set(registro["data_hora"].strftime("%d/%m/%Y") for registro in dados))
    elif periodo == "semanas":
        # Obter semanas únicas
        semanas = {}
        for registro in dados:
            data = registro["data_hora"]
            semana_inicio = (data - timedelta(days=data.weekday())).strftime("%d/%m/%Y")
            semana_fim = (data + timedelta(days=6 - data.weekday())).strftime("%d/%m/%Y")
            chave = f"{semana_inicio} - {semana_fim}"
            semanas[chave] = True
        periodos = sorted(semanas.keys())
    elif periodo == "mensal":
        # Obter meses únicos
        periodos = sorted(set(
            registro["data_hora"].strftime("%m/%Y")
            for registro in dados
        ))

    return periodos

def exibir_grafico(id_usuario, categoria, periodo):
    """
    Exibe o gráfico vertical para a categoria e período escolhidos.
    Se a categoria for "transporte", exibe uma tabela textual.
    """
    limpar_tela()
    print("\n" + "═" * 90)
    print(f" RELATÓRIO DE {categoria.upper()} ({periodo.upper()}) ".center(90, '─'))
    print("═" * 90)

    # Carregar os dados do usuário
    dados = carregar_dados_usuario(id_usuario)
    if not dados:
        print("\nNenhum dado encontrado para o usuário.")
        input("\nPressione Enter para voltar...")
        return

    # Caso a categoria seja "transporte", exibir uma tabela textual
    if categoria == "transportes":
        print(f"\n{'Categoria':<15}{'Data':<20}{'Classificação':<30}{'Meio':<15}{'Viagens':<10}")
        print("-" * 90)

        for registro in dados["transportes"]:
            data = registro["data_hora"].strftime("%d/%m/%Y")
            meio = registro["tipo_transporte"]
            viagens = registro["quantidade"]
            classificacao = registro["classificacao_transporte"]
            print(f"{'Transporte':<15}{data:<20}{classificacao:<30}{meio:<15}{viagens:<10}")

        print("-" * 90)
        input("\nPressione Enter para voltar...")
        return

    # Caso contrário, exibir o gráfico vertical
    periodos = obter_periodos(dados["gastos"], periodo)

    # Acumular os valores para os períodos
    acumulados = {}
    for registro in dados["gastos"]:
        data_hora = registro["data_hora"]
        if periodo == "dias":
            chave = data_hora.strftime("%d/%m/%Y")  # Apenas a data
        elif periodo == "semanas":
            data = data_hora
            for p in periodos:
                inicio, fim = p.split(" - ")
                inicio = datetime.strptime(inicio, "%d/%m/%Y")
                fim = datetime.strptime(fim, "%d/%m/%Y")
                if inicio <= data <= fim:
                    chave = p
                    break
        elif periodo == "mensal":
            chave = data_hora.strftime("%m/%Y")  # Mês/Ano
        else:
            continue

        if chave not in acumulados:
            acumulados[chave] = registro.get(f"gasto_{categoria}", 0)
        else:
            acumulados[chave] += registro.get(f"gasto_{categoria}", 0)

    # Preencher períodos sem dados com valor 0
    valores = [acumulados.get(p, 0) for p in periodos]

    # Determinar o maior valor dinamicamente
    max_valor = max(valores) if valores else 1

    # Normalizar os valores para o gráfico
    escala = max_valor / 10  # Divide o maior valor em 10 níveis

    # Exibir o gráfico
    print(f"\n{'Período':<15}{'Valor':<10}")
    print("-" * 50)

    for i in range(10, 0, -1):  # De cima para baixo
        linha = ''
        for valor in valores:
            if valor >= (i * escala):
                linha += ' *** '
            else:
                linha += '     '
        print(f'{int(i * escala):>4} |{linha}')
    print('     ' + '-' * (len(valores) * 5))
    print('      ' + '  '.join([str(p)[:5] for p in periodos]))  # Exibe os períodos no eixo horizontal

    input("\nPressione Enter para voltar...")

def menu_principal(id_usuario):
    """
    Menu principal para exibição de gráficos.
    """
    while True:
        limpar_tela()
        print("\n" + "═" * 50)
        print(f" GRÁFICOS DE CONSUMO - USUÁRIO: {id_usuario} ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Últimos 7 Dias':<38}")
        print(f"{'2. Últimas 4 Semanas':<38}")
        print(f"{'3. Últimos 12 Meses':<38}")
        print(f"{'4. Sair':<38}")
        print("═" * 50)

        opcao_periodo = input("Escolha o período desejado (1-4): ").strip()

        if opcao_periodo == "4":
            print("\nSaindo do programa...")
            break

        periodo = None
        if opcao_periodo == "1":
            periodo = "dias"
        elif opcao_periodo == "2":
            periodo = "semanas"
        elif opcao_periodo == "3":
            periodo = "mensal"
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
            continue

        limpar_tela()
        print("\n" + "═" * 50)
        print(f" CATEGORIAS DISPONÍVEIS ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Consumo de Água':<38}")
        print(f"{'2. Consumo de Energia':<38}")
        print(f"{'3. Geração de Resíduos':<38}")
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

        # Exibir o gráfico para a categoria e período escolhidos
        exibir_grafico(id_usuario, categoria, periodo)

if __name__ == "__main__":
    menu_principal(id_usuario)  # Substitua pelo ID do usuário logado