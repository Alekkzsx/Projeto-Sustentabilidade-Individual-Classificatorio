def grafico_consumo_agua():
    periodos = {
        'Dias': ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5"],
        'Semanas': ["Semana 1", "Semana 2", "Semana 3", "Semana 4"],
        'Mensal': ["Janeiro", "Fevereiro", "Março", "Abril"]
    }

    consumos = {
        'Agua': [],
        'Energia': [],
        'Residuos': [],
        'Transporte': []
    }

    unidades = {
        'Agua': 'Litros',
        'Energia': 'KWh',
        'Residuos': '%',
        'Transporte': '%'
    }

    while True:
        tipo_consumo = input("Escolha o tipo de consumo (Agua, Energia, Residuos, Transporte): ").capitalize()
        periodo_tempo = input("Escolha o periodo de tempo (Dias, Semanas, Mensal): ").capitalize()

        if tipo_consumo in consumos and periodo_tempo in periodos:
            print(f"\nInsira os valores de consumo para {tipo_consumo} - {periodo_tempo}:")

            for periodo in periodos[periodo_tempo]:
                valor = int(input(f"Valor para {periodo} ({unidades[tipo_consumo]}): "))
                consumos[tipo_consumo].append(valor)

            print(f"\nGráfico sobre o consumo de {tipo_consumo} - {periodo_tempo}:\n")
            print(f"{'Periodo':<15}{'Valor (' + unidades[tipo_consumo] + ')':<15}")
            print("-" * 30)

            for periodo, valor in zip(periodos[periodo_tempo], consumos[tipo_consumo]):
                print(f"{periodo:<15}{valor:<15}")
                print(f"{'':<15}{'*' * (valor // 10)}")
            break
        else:
            print("Entrada inválida. Por favor, tente novamente.")

grafico_consumo_agua()
