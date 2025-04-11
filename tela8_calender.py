import os
import datetime
from db_manager import conectar_db

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_calendario_manual(ano, mes, dias_registrados):
    # Calcula o primeiro dia do mês e o número de dias no mês
    primeiro_dia = datetime.date(ano, mes, 1).weekday()  # 0 = Segunda-feira, 6 = Domingo
    dias_no_mes = (datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)).day if mes < 12 else 31

    # Cabeçalho do calendário
    print("\n" + f"{datetime.date(ano, mes, 1):%B %Y}".upper())
    print("Se  Te  Qa  Qi  Sx  Sb  Dm")

    # Preenche os dias do calendário
    dia = 1
    linha = ["00 "] * primeiro_dia  # Espaços vazios antes do primeiro dia
    while dia <= dias_no_mes:
        while len(linha) < 7 and dia <= dias_no_mes:
            if dia in dias_registrados:
                linha.append(f"\033[92m{dia:02}\033[0m ")  # Verde para dias com registro
            else:
                linha.append(f"\033[91m{dia:02}\033[0m ")  # Vermelho para dias sem registro
            dia += 1
        while len(linha) < 7:  # Preenche o restante da semana com "00"
            linha.append("00 ")
        print("".join(linha))
        linha = []

def exibir_calendario(id_usuario):
    while True:
        limpar_tela()  # Limpa a tela antes de solicitar o mês e ano
        # Solicita o mês e o ano ao usuário
        print("\nDigite o mês e o ano que deseja visualizar (ou deixe em branco para o mês atual):")
        try:
            mes = input("► Mês (1-12): ").strip()
            ano = input("► Ano (ex: 2025): ").strip()

            if not mes:
                mes = datetime.datetime.now().month
            else:
                mes = int(mes)

            if not ano:
                ano = datetime.datetime.now().year
            else:
                ano = int(ano)

            if mes < 1 or mes > 12:
                print("Mês inválido! Insira um valor entre 1 e 12.")
                continue

            # Conecta ao banco de dados e busca registros
            conexao = conectar_db()
            if conexao is None:
                print("Erro ao conectar ao banco de dados.")
                return

            try:
                cursor = conexao.cursor(dictionary=True)
                query = """SELECT data_hora, periodo FROM gastos_usuarios WHERE id_usuario = %s"""
                cursor.execute(query, (id_usuario,))
                registros = cursor.fetchall()

                # Processa os registros para identificar os dias registrados
                dias_registrados = set()
                for registro in registros:
                    data_hora = registro['data_hora']
                    periodo = registro['periodo']

                    if periodo == "diário" and data_hora.month == mes and data_hora.year == ano:
                        dias_registrados.add(data_hora.day)
                    elif periodo == "mensal" and data_hora.year == ano:
                        dias_registrados.update(range(1, (datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)).day + 1))
                    elif periodo == "anual" and data_hora.year == ano:
                        dias_registrados.update(range(1, (datetime.date(ano, mes + 1, 1) - datetime.timedelta(days=1)).day + 1))

                limpar_tela()  # Limpa a tela antes de exibir o calendário

                # Verifica se há registros no mês
                if not dias_registrados:
                    print("\nNenhum registro encontrado para este mês e ano. Exibindo o calendário todo em vermelho.")
                    dias_registrados = set()  # Nenhum dia registrado

                # Gera o calendário manualmente
                gerar_calendario_manual(ano, mes, dias_registrados)

                # Exibe a tabela de registros
                if dias_registrados:
                    print("\nTabela de Registros:")
                    print("─" * 40)
                    print(f"{'Dia':<10}{'Período':<10}{'Descrição':<20}")
                    print("─" * 40)
                    for registro in registros:
                        data_hora = registro['data_hora']
                        periodo = registro['periodo']
                        descricao = f"Registro de {periodo}"
                        if periodo == "diário" and data_hora.month == mes and data_hora.year == ano:
                            print(f"{data_hora.day:<10}{periodo:<10}{descricao:<20}")
                        elif periodo == "mensal" and data_hora.year == ano:
                            print(f"{'Todo mês':<10}{periodo:<10}{descricao:<20}")
                        elif periodo == "anual" and data_hora.year == ano:
                            print(f"{'Todo ano':<10}{periodo:<10}{descricao:<20}")

            except Exception as err:
                print(f"Erro ao buscar registros: {err}")
            finally:
                cursor.close()
                conexao.close()

            # Pergunta se o usuário deseja visualizar outro mês
            opcao = input("\nDeseja visualizar outro mês? (s/n): ").strip().lower()
            if opcao != 's':
                break

        except ValueError:
            print("Entrada inválida! Tente novamente.")

if __name__ == "__main__":
    # Substitua pelo ID do usuário logado
    exibir_calendario(id_usuario=1)