import os
import datetime
import calendar
from db_manager import conectar_db

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_calendario_terminal(ano, mes, dias_registrados):
    # Cria o calendário do mês
    cal = calendar.Calendar(firstweekday=0)  # Começa na segunda-feira
    dias_mes = cal.monthdayscalendar(ano, mes)

    # Cabeçalho do calendário
    print(f"\n{calendar.month_name[mes].upper()} {ano}")
    print("Seg  Ter  Qua  Qui  Sex  Sáb  Dom")

    # Preenche os dias do mês
    for semana in dias_mes:
        linha = ""
        for dia in semana:
            if dia == 0:  # Dias fora do mês
                linha += "     "
            elif dia in dias_registrados:
                linha += f"\033[92m{dia:2}\033[0m   "  # Verde para dias registrados
            else:
                linha += f"\033[91m{dia:2}\033[0m   "  # Vermelho para dias não registrados
        print(linha)

def exibir_grafico_registros(registros):
    print("\nGRÁFICO DE REGISTROS:")
    print("-" * 50)
    for registro in registros:
        data_hora = registro['data_hora']
        periodo = registro['periodo']
        agua = registro.get('gasto_agua', 'N/A')
        energia = registro.get('gasto_energia', 'N/A')
        residuos = registro.get('gasto_residuos', 'N/A')
        transportes = registro.get('transportes', 'N/A')  # Lista de transportes concatenada

        print(f"Data: {data_hora.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  - Período: {periodo}")
        print(f"  - Gasto de Água: {agua}")
        print(f"  - Gasto de Energia: {energia}")
        print(f"  - Gasto de Resíduos: {residuos}")
        print(f"  - Transportes: {transportes}")
        print("-" * 50)

def exibir_calendario(id_usuario):
    while True:
        limpar_tela()

        # Conecta ao banco de dados e busca registros
        conexao = conectar_db()
        if conexao is None:
            print("Erro ao conectar ao banco de dados.")
            return

        try:
            cursor = conexao.cursor(dictionary=True)
            query = """SELECT DISTINCT data_hora, periodo FROM gastos_usuarios WHERE id_usuario = %s"""
            cursor.execute(query, (id_usuario,))
            registros = cursor.fetchall()

            if not registros:
                print("Nenhum registro encontrado.")
                return

            # Exibe o índice com as datas disponíveis
            print("ÍNDICE DE DATAS COM REGISTROS:")
            for i, registro in enumerate(registros):
                print(f"[{i}] {registro['data_hora'].strftime('%Y-%m-%d %H:%M:%S')} - Período: {registro['periodo']}")

            # Solicita ao usuário selecionar uma data pelo índice
            indice = input("\nSelecione o índice da data que deseja visualizar: ").strip()
            if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(registros):
                print("Índice inválido. Tente novamente.")
                continue

            registro_selecionado = registros[int(indice)]
            data_hora = registro_selecionado['data_hora']
            periodo = registro_selecionado['periodo']

            # Define o ano e o mês com base na data selecionada
            ano = data_hora.year
            mes = data_hora.month

            # Identifica os dias registrados com base no período
            dias_registrados = set()
            if periodo == "diário":
                dias_registrados.add(data_hora.day)
            elif periodo == "mensal":
                dias_registrados.update(range(1, calendar.monthrange(ano, mes)[1] + 1))
            elif periodo == "anual":
                for m in range(1, 13):
                    dias_registrados.update(range(1, calendar.monthrange(ano, m)[1] + 1))

            limpar_tela()

            # Gera o calendário no terminal
            gerar_calendario_terminal(ano, mes, dias_registrados)

            # Busca registros detalhados para o gráfico
            query_detalhada = """
                SELECT 
                    g.data_hora, g.periodo, g.gasto_agua, g.gasto_energia, g.gasto_residuos,
                    GROUP_CONCAT(t.tipo_transporte SEPARATOR ', ') AS transportes
                FROM gastos_usuarios g
                LEFT JOIN transportes_usuario t
                ON g.id_usuario = t.id_usuario AND DATE(g.data_hora) = DATE(t.data_hora)
                WHERE g.id_usuario = %s AND YEAR(g.data_hora) = %s AND MONTH(g.data_hora) = %s
                GROUP BY g.data_hora, g.periodo, g.gasto_agua, g.gasto_energia, g.gasto_residuos
            """
            cursor.execute(query_detalhada, (id_usuario, ano, mes))
            registros_detalhados = cursor.fetchall()

            # Exibe o gráfico de registros
            exibir_grafico_registros(registros_detalhados)

        except Exception as err:
            print(f"Erro ao buscar registros: {err}")
        finally:
            cursor.close()
            conexao.close()

        # Pergunta se o usuário deseja visualizar outra data
        opcao = input("\nDeseja visualizar outra data? (s/n): ").strip().lower()
        if opcao != 's':
            break

if __name__ == "__main__":
    # Substitua pelo ID do usuário logado
    exibir_calendario(id_usuario=1)