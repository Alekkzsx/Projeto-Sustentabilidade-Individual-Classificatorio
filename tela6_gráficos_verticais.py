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

    # Limite máximo para os valores de consumo
    limite_valor = 10000

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
                    while True:
                        valor = int(input(f"Valor para {periodo} ({unidades[tipo_consumo]}): "))
                        if valor <= limite_valor:
                            consumos[tipo_consumo].append(valor)
                            break
                        else:
                            print(f"Valor excede o limite de {limite_valor}. Por favor, insira um valor menor ou igual a {limite_valor}.")

                # Exibe o gráfico de consumo no terminal
                print(f"\nGráfico sobre o consumo de {tipo_consumo} - {periodo_tempo}:\n")
                print(f"{'Periodo':<15}{'Valor (' + unidades[tipo_consumo] + ')':<15}")
                print("-" * 30)

                # Exibe os valores de consumo e um gráfico de barras simples
                max_valor = max(consumos[tipo_consumo])
                escala = max_valor // 10

                for i in range(escala, 0, -1):
                    linha = ''
                    for valor in consumos[tipo_consumo]:
                        if valor // 10 >= i:
                            linha += '  *  '
                        else:
                            linha += '     '
                    print(f'{i*10:>4} |{linha}')
                print('     ' + '-' * (len(consumos[tipo_consumo]) * 5))
                print('      ' + '  '.join([f'{p[:3]}' for p in periodos[periodo_tempo]]))
                break
            else:
                print("Entrada inválida. Por favor, tente novamente.")
        except ValueError:
            print("\nValor inválido. Por favor, insira um valor numérico.\n")

# Chama a função para iniciar o programa
grafico_consumo_agua()
