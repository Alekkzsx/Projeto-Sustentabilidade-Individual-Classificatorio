def obter_gasto(categoria):
    while True:
        try:
            gasto = float(input(f"Digite o gasto com {categoria}: "))
            break
        except:
            print("Valor inválido! Digite um número válido.")
    return gasto

def classificar_sustentabilidade(total_gasto):
    if total_gasto <= 50:
        return "Meio ambiente agradece !!!"
    elif total_gasto <= 100:
        return "Sustentável"
    elif total_gasto <= 200:
        return "Baixo nível de sustentabilidade"
    else:
        return "Desperdício !!!"

print("*** TABELA DE HISTÓRICO COM DATA/HORA - DIVISÃO DE CATEGORIA - CLASSIFICAÇÃO ***")

agua = obter_gasto("Água")
energia = obter_gasto("Energia")
transporte = obter_gasto("Transporte")
reciclavel = obter_gasto("Reciclável")

total_gasto = agua + energia + transporte + reciclavel

classificacao = classificar_sustentabilidade(total_gasto)

print("\n*** RESULTADO ***")
print(f"Água: {agua}")
print(f"Energia: {energia}")
print(f"Transporte: {transporte}")
print(f"Reciclável: {reciclavel}")
print(f"Total gasto: {total_gasto}")
print(f"Classificação: {classificacao}")
