import os
from datetime import datetime, timedelta
from db_manager import buscar_gastos_usuario, buscar_transportes_usuario

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados_usuario(id_usuario, periodo):
    """
    Carrega os dados do usuário do banco de dados e filtra com base no período selecionado.
    """
    dados_gastos = buscar_gastos_usuario(id_usuario)
    dados_transportes = buscar_transportes_usuario(id_usuario)
    if not dados_gastos and not dados_transportes:
        print("Nenhum dado encontrado para o usuário.")
        return None

    # Determinar o intervalo de tempo com base no período
    hoje = datetime.now()
    if periodo == "dias":
        inicio = hoje - timedelta(days=7)
    elif periodo == "semanas":
        inicio = hoje - timedelta(weeks=4)
    elif periodo == "mensal":
        inicio = hoje - timedelta(days=365)
    else:
        inicio = None  # Sem filtro de período

    # Filtrar os dados de gastos e transportes
    if inicio:
        dados_gastos = [registro for registro in dados_gastos if registro["data_hora"] >= inicio]
        dados_transportes = [registro for registro in dados_transportes if registro["data_hora"] >= inicio]

    return {"gastos": dados_gastos, "transportes": dados_transportes}
    """
    Retorna os períodos disponíveis no banco de dados com base no tipo de período escolhido.
    Filtra os dados para considerar apenas os registros dentro do intervalo de tempo especificado.
    """
    periodos = []
    hoje = datetime.now()

    if periodo == "dias":
        # Filtrar os últimos 7 dias
        inicio = hoje - timedelta(days=7)
        dados_filtrados = [registro for registro in dados if registro["data_hora"] >= inicio]
        periodos = sorted(set(registro["data_hora"].strftime("%d/%m/%Y") for registro in dados_filtrados))

    elif periodo == "semanas":
        # Filtrar as últimas 4 semanas
        inicio = hoje - timedelta(weeks=4)
        dados_filtrados = [registro for registro in dados if registro["data_hora"] >= inicio]
        semanas = {}
        for registro in dados_filtrados:
            data = registro["data_hora"]
            semana_inicio = (data - timedelta(days=data.weekday())).strftime("%d/%m/%Y")
            semana_fim = (data + timedelta(days=6 - data.weekday())).strftime("%d/%m/%Y")
            chave = f"{semana_inicio} - {semana_fim}"
            semanas[chave] = True
        periodos = sorted(semanas.keys())

    elif periodo == "mensal":
        # Filtrar os últimos 12 meses
        inicio = hoje - timedelta(days=365)
        dados_filtrados = [registro for registro in dados if registro["data_hora"] >= inicio]
        periodos = sorted(set(
            registro["data_hora"].strftime("%m/%Y")
            for registro in dados_filtrados
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

    # Carregar os dados do usuário com base no período
    dados = carregar_dados_usuario(id_usuario, periodo)
    if not dados:
        print("\nNenhum dado encontrado para o usuário.")
        input("\nPressione Enter para voltar...")
        return

    # Caso a categoria seja "transportes", exibir uma tabela textual
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

    # Acumular os valores para os períodos
    acumulados = {}
    for registro in dados["gastos"]:
        data_hora = registro["data_hora"]
        chave = None  # Inicializa a variável chave

        if periodo == "dias":
            chave = data_hora.strftime("%d/%m/%Y")  # Apenas a data
        elif periodo == "semanas":
            # Agrupamento por semanas
            semana_inicio = (data_hora - timedelta(days=data_hora.weekday())).strftime("%d/%m/%Y")
            semana_fim = (data_hora + timedelta(days=6 - data_hora.weekday())).strftime("%d/%m/%Y")
            chave = f"{semana_inicio} - {semana_fim}"
        elif periodo == "mensal":
            chave = data_hora.strftime("%m/%Y")  # Mês/Ano

        if chave is None:
            continue  # Ignora registros que não se encaixam em nenhum período

        if chave not in acumulados:
            acumulados[chave] = registro.get(f"gasto_{categoria}", 0)
        else:
            acumulados[chave] += registro.get(f"gasto_{categoria}", 0)

    # Ordenar os períodos
    periodos = sorted(acumulados.keys())

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

def menu_principal(usuario_logado, id_usuario):
    """
    Menu principal para exibição de gráficos.
    """
    while True:
        limpar_tela()
        print("\n" + "═" * 50)
        print(f" GRÁFICOS DE CONSUMO - {usuario_logado} ".center(50, '─'))
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
    menu_principal(usuario_logado, id_usuario)  # Substitua pelo ID do usuário logado