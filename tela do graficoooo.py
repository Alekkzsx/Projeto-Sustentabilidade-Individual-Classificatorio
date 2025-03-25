def grafico_consumo_agua():
    # Dicionário com os períodos de tempo
    periodos = {
        'Dias': ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"],
        'Semanas': ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        'Mensal': ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    }

    # Dicionário para armazenar os consumos
    consumos = {
        'Agua': [],
        'Energia': [],
        'Residuos': [],
        'Transporte': []
    }

    # Dicionário com as unidades de medida para cada tipo de consumo
    unidades = {
        'Agua': 'Litros',
        'Energia': 'KWh',
        'Residuos': '%',
        'Transporte': '%'
    }

    # Loop principal para solicitar entradas do usuário
    while True:
        try:
            # Solicita o tipo de consumo e o período de tempo
            tipo_consumo = input("Escolha o tipo de consumo (Agua, Energia, Residuos, Transporte): ").capitalize()
            periodo_tempo = input("Escolha o periodo de tempo (Dias, Semanas, Mensal): ").capitalize()

            # Verifica se as entradas são válidas
            if tipo_consumo in consumos and periodo_tempo in periodos:
                print(f"\nInsira os valores de consumo para {tipo_consumo} - {periodo_tempo}:")

                # Solicita os valores de consumo para cada período
                for periodo in periodos[periodo_tempo]:
                    valor = int(input(f"Valor para {periodo} ({unidades[tipo_consumo]}): "))
                    consumos[tipo_consumo].append(valor)

                # Exibe o gráfico de consumo no terminal
                print(f"\nGráfico sobre o consumo de {tipo_consumo} - {periodo_tempo}:\n")
                print(f"{'Periodo':<15}{'Valor (' + unidades[tipo_consumo] + ')':<15}")
                print("-" * 30)

                # Exibe os valores de consumo e um gráfico de barras simples
                for periodo, valor in zip(periodos[periodo_tempo], consumos[tipo_consumo]):
                    print(f"{periodo:<15}{valor:<15}")
                    print(f"{'':<15}{'*' * (valor // 10)}")
                break
            else:
                print("Entrada inválida. Por favor, tente novamente.")
        except ValueError:
            print("\nValor inválido. Por favor, insira um valor numérico.\n")

# Chama a função para iniciar o programa
grafico_consumo_agua()
