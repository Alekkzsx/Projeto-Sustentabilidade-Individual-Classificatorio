import datetime
import os
import json

GASTOS_JSON = "gastos_usuarios.json"

# Modelos de transportes reconhecidos
modelos_transportes_meio_ambiente = ["bicicleta", "a pé", "caminhada"]
modelos_transportes_alta = ["bicicleta elétrica", "patins elétrico", "veículo elétrico", "veículos elétricos"]
modelos_transportes_moderada = ["ônibus", "metrô", "trem", "veículo público", "veículos públicos"]
modelos_transportes_baixa = ["carro", "moto", "caminhão", "veículo movido a fósseis", "veículos movidos a fósseis"]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def classificar_consumo(agua, energia, residuos, transportes):
    # Classificação do consumo de água
    if agua < 100:
        agua_cat = "🟢 Meio Ambiente Agradece"
    elif agua < 150:
        agua_cat = "🟡 Alta Sustentabilidade"
    elif agua < 200:
        agua_cat = "🟠 Moderada Sustentabilidade"
    else:
        agua_cat = "🔴 Baixa Sustentabilidade"
    
    # Classificação do consumo de energia
    if energia < 2.5:
        energia_cat = "🟢 Meio Ambiente Agradece"
    elif energia < 5:
        energia_cat = "🟡 Alta Sustentabilidade"
    elif energia < 10:
        energia_cat = "🟠 Moderada Sustentabilidade"
    else:
        energia_cat = "🔴 Baixa Sustentabilidade"
    
    # Classificação da geração de resíduos
    if residuos < 20:
        residuos_cat = "🟢 Meio Ambiente Agradece"
    elif residuos < 50:
        residuos_cat = "🟡 Alta Sustentabilidade"
    elif residuos < 60:
        residuos_cat = "🟠 Moderada Sustentabilidade"
    else:
        residuos_cat = "🔴 Baixa Sustentabilidade"
    
    # Classificação do uso de transporte com base no melhor nível entre os transportes cadastrados
    transportes_cat = classificar_transportes(transportes)
    
    return agua_cat, energia_cat, residuos_cat, transportes_cat

def classificar_transportes(transportes):
    # Define ranking: maior valor significa melhor sustentabilidade
    ranking = {
        "🟢 Meio Ambiente Agradece": 4,
        "🟡 Alta Sustentabilidade": 3,
        "🟠 Moderada Sustentabilidade": 2,
        "🔴 Baixa Sustentabilidade": 1
    }
    if not transportes:
        return "Sem transporte registrado"
    melhor = "🔴 Baixa Sustentabilidade"
    for _, _, cat in transportes:
        if ranking.get(cat, 0) > ranking.get(melhor, 0):
            melhor = cat
    return melhor

def salvar_gastos(usuario, agua, energia, residuos, transportes, agua_cat, energia_cat, residuos_cat, transportes_cat):
    # Cria o arquivo JSON caso não exista
    if not os.path.exists(GASTOS_JSON):
        with open(GASTOS_JSON, 'w') as f:
            json.dump({}, f)
    
    with open(GASTOS_JSON, 'r') as f:
        dados = json.load(f)
    
    if usuario not in dados:
        dados[usuario] = []
    
    registro = {
        "data_hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "agua": agua,
        "agua_classificacao": agua_cat,
        "energia": energia,
        "energia_classificacao": energia_cat,
        "residuos": residuos,
        "residuos_classificacao": residuos_cat,
        "transportes": transportes,
        "transportes_classificacao": transportes_cat
    }
    dados[usuario].append(registro)
    
    with open(GASTOS_JSON, 'w') as f:
        json.dump(dados, f, indent=4)

def main(usuario_logado):
    while True:
        limpar_tela()
        print(f"\nBem-vindo(a), {usuario_logado}!")
        print("\n[1] Registrar novos dados")
        print("[2] Acessar Histórico")
        print("[3] Sair")
        
        choice = input("▶ Escolha uma opção: ")
        
        if choice == '1':
            limpar_tela()
            try:
                agua = float(input("\n► Consumo de água (litros/dia): "))
                energia = float(input("► Consumo de energia (kWh/dia): "))
                residuos = float(input("► Resíduos não recicláveis (%): "))
                
                # Cadastro de transportes com validação
                transportes = []
                while True:
                    transporte = input("\n► Informe o meio de transporte utilizado: ").lower().strip()
                    # Verifica se o transporte informado está entre os modelos reconhecidos
                    if transporte in modelos_transportes_meio_ambiente:
                        classificacao = "🟢 Meio Ambiente Agradece"
                    elif transporte in modelos_transportes_alta:
                        classificacao = "🟡 Alta Sustentabilidade"
                    elif transporte in modelos_transportes_moderada:
                        classificacao = "🟠 Moderada Sustentabilidade"
                    elif transporte in modelos_transportes_baixa:
                        classificacao = "🔴 Baixa Sustentabilidade"
                    else:
                        print("Meio de transporte não reconhecido pelo sistema. Tente novamente.")
                        continue
                    
                    try:
                        vezes = int(input(f"► Quantidade de vezes que utilizou {transporte}: ").strip())
                    except ValueError:
                        print("Entrada inválida para quantidade. Tente novamente.")
                        continue
                    
                    transportes.append((transporte, vezes, classificacao))
                    
                    opcao = input("Deseja adicionar outro meio de transporte? [1] Sim [2] Não: ").strip()
                    if opcao == '1':
                        continue
                    elif opcao == '2':
                        break
                    else:
                        print("Opção inválida. Encerrando cadastro de transportes.")
                        break
                
                # Classifica os consumos
                agua_cat, energia_cat, residuos_cat, transportes_cat = classificar_consumo(agua, energia, residuos, transportes)
                # Salva os dados junto com as classificações
                salvar_gastos(usuario_logado, agua, energia, residuos, transportes, agua_cat, energia_cat, residuos_cat, transportes_cat)
                
                limpar_tela()
                print("\nDADOS REGISTRADOS COM SUCESSO!")
                print(f"🌊 Água: {agua}L - {agua_cat}")
                print(f"💡 Energia: {energia}kWh - {energia_cat}")
                print(f"♻️ Resíduos: {residuos}% - {residuos_cat}")
                print(f"🚦 Transportes: {transportes_cat}")
                input("\nPressione Enter para continuar...")
            
            except ValueError:
                print("\nERRO: Entrada inválida! Tente novamente.")
                input("Pressione Enter para continuar...")
        
        elif choice == '2':
            limpar_tela()
            print("\nHISTÓRICO (EM DESENVOLVIMENTO)")
            input("\nPressione Enter para voltar...")
        
        elif choice == '3':
            limpar_tela()
            print("\nOBRIGADO POR UTILIZAR O SISTEMA!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main("Usuário")
