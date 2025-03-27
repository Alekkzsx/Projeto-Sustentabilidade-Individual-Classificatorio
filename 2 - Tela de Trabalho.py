import os
import json
from datetime import datetime

# Configurações globais
ARQUIVO_CONSUMO = "consumido.json"
LINHA_DIVISORIA = "=" * 40

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def classificar_agua(litros):
    """Classifica o consumo de água"""
    if litros < 100: return "Meio Ambiente Agradece"
    elif 100 <= litros <= 150: return "Alta Sustentabilidade"
    elif 150 < litros <= 200: return "Moderada Sustentabilidade"
    else: return "Baixa Sustentabilidade"

def classificar_energia(kwh):
    """Classifica o consumo de energia"""
    if kwh < 2.5: return "Meio Ambiente Agradece"
    elif 2.5 <= kwh <= 5: return "Alta Sustentabilidade"
    elif 5 < kwh <= 10: return "Moderada Sustentabilidade"
    else: return "Baixa Sustentabilidade"

def classificar_residuos(percentual):
    """Classifica a geração de resíduos"""
    if percentual < 20: return "Meio Ambiente Agradece"
    elif 20 <= percentual <= 50: return "Alta Sustentabilidade"
    elif 50 < percentual <= 60: return "Moderada Sustentabilidade"
    else: return "Baixa Sustentabilidade"

def classificar_transporte(transporte):
    """Classifica o tipo de transporte"""
    transporte = transporte.lower()
    if "bicicleta" in transporte or "caminhada" in transporte: 
        return "Meio Ambiente Agradece"
    elif "elétrico" in transporte: return "Alta Sustentabilidade"
    elif "público" in transporte: return "Moderada Sustentabilidade"
    else: return "Baixa Sustentabilidade"

def salvar_consumo(dados):
    """Salva os dados no arquivo JSON"""
    try:
        with open(ARQUIVO_CONSUMO, 'r') as f:
            registros = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        registros = []
    
    registros.append(dados)
    
    with open(ARQUIVO_CONSUMO, 'w') as f:
        json.dump(registros, f, indent=4)

def adicionar_consumo():
    """Tela para adicionar novos dados de consumo"""
    limpar_tela()
    print(LINHA_DIVISORIA)
    print("ADICIONAR CONSUMO".center(40))
    print(LINHA_DIVISORIA)
    
    # Seleção de período
    periodo = input("\nPeriodo (Mensal/Diário/Anual): ").capitalize()
    
    # Coleta de dados
    agua = float(input("\nÁgua consumida (litros/dia): "))
    energia = float(input("Energia consumida (kWh/dia): "))
    residuos = float(input("Resíduos não recicláveis (%): "))
    transporte = input("Transporte utilizado: ")
    
    # Classificações
    classificacoes = {
        'Água': classificar_agua(agua),
        'Energia': classificar_energia(energia),
        'Resíduos': classificar_residuos(residuos),
        'Transporte': classificar_transporte(transporte)
    }
    
    # Confirmação
    confirmar = input("\nConfirmar dados? (S/N): ").upper()
    if confirmar == 'S':
        dados = {
            'data': datetime.now().strftime("%d/%m/%Y %H:%M"),
            'periodo': periodo,
            'consumo': {
                'agua': agua,
                'energia': energia,
                'residuos': residuos,
                'transporte': transporte
            },
            'classificacoes': classificacoes
        }
        salvar_consumo(dados)
        print("\nDados salvos com sucesso!")
    else:
        print("\nOperação cancelada!")
    
    input("\nPressione Enter para voltar...")

def menu_principal():
    """Tela inicial do sistema"""
    while True:
        limpar_tela()
        print(LINHA_DIVISORIA)
        print("Bem vindo CONVIDADO".center(40))
        print("O que gostaria de ver?".center(40))
        print(LINHA_DIVISORIA)
        
        print("\n1 - Adicionar Informações de Consumo")
        print("2 - Sair\n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_consumo()
        elif opcao == '2':
            print("\nAté logo!")
            break
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    menu_principal()