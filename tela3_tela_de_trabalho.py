import datetime
import os
import json

GASTOS_JSON = "gastos_usuarios.json"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def classificar_consumo(agua, energia, residuos, transportes):
    if agua < 100:
        agua_cat = "🟢 Meio Ambiente Agradece"
    elif agua < 150:
        agua_cat = "🟡 Alta Sustentabilidade"
    elif agua < 200:
        agua_cat = "🟠 Moderada Sustentabilidade"
    else:
        agua_cat = "🔴 Baixa Sustentabilidade"
    
    if energia < 2.5:
        energia_cat = "🟢 Meio Ambiente Agradece"
    elif energia < 5:
        energia_cat = "🟡 Alta Sustentabilidade"
    elif energia < 10:
        energia_cat = "🟠 Moderada Sustentabilidade"
    else:
        energia_cat = "🔴 Baixa Sustentabilidade"
    
    if residuos < 20:
        residuos_cat = "🟢 Meio Ambiente Agradece"
    elif residuos < 50:
        residuos_cat = "🟡 Alta Sustentabilidade"
    elif residuos < 60:
        residuos_cat = "🟠 Moderada Sustentabilidade"
    else:
        residuos_cat = "🔴 Baixa Sustentabilidade"
    
    transportes_cat = "🔴 Baixa Sustentabilidade"
    for t, _, _ in transportes:
        if t in ["bicicleta", "a pé"]:
            transportes_cat = "🟢 Meio Ambiente Agradece"
        elif t in ["bicicleta elétrica", "patins elétrico"]:
            transportes_cat = "🟡 Alta Sustentabilidade"
        elif t in ["ônibus", "metrô", "trem"]:
            transportes_cat = "🟠 Moderada Sustentabilidade"
    
    return agua_cat, energia_cat, residuos_cat, transportes_cat

def salvar_gastos(usuario, agua, energia, residuos, transportes):
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
        "energia": energia,
        "residuos": residuos,
        "transportes": transportes
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
                
                transportes = []
                while True:
                    transporte = input("\n► Transporte utilizado (deixe em branco para sair): ").lower().strip()
                    if not transporte:
                        break
                    vezes = int(input(f"► Quantidade de viagens com {transporte}: "))
                    transportes.append((transporte, vezes))
                
                agua_cat, energia_cat, residuos_cat, transportes_cat = classificar_consumo(agua, energia, residuos, transportes)
                salvar_gastos(usuario_logado, agua, energia, residuos, transportes)
                
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
