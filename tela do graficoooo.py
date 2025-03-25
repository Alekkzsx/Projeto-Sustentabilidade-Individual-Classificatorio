def grafico_consumo_agua():
    dias = ["Dia 1", "Dia 2", "Dia 3", "Dia 4", "Dia 5"]
    consumo = [150, 300, 75, 125, 200]

    print("\nGráfico sobre o consumo de água:\n")
    print(f"{'Dias':<10}{'Litros':<10}")
    print("-" * 20)

    for dia, litro in zip(dias, consumo):
        print(f"{dia:<10}{litro:<10}")
        print(f"{'':<10}{'*' * (litro // 10)}")

grafico_consumo_agua()