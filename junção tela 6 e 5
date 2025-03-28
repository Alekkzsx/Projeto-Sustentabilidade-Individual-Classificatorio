import json
import os
from datetime import datetime

# Configuração do arquivo JSON
ARQUIVO_GASTOS = 'gastos_usuarios.json'

def carregar_historico():
    """Carrega os dados do arquivo JSON"""
    if not os.path.exists(ARQUIVO_GASTOS):
        print(f"⚠️ O arquivo {ARQUIVO_GASTOS} não foi encontrado. Criando um novo arquivo...")
        return {"usuarios": {}}

    try:
        with open(ARQUIVO_GASTOS, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ O arquivo JSON está corrompido. Criando um novo arquivo...")
        return {"usuarios": {}}
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return {"usuarios": {}}

def exibir_historico_categoria(usuario, tipo):
    """Exibe o histórico de uma categoria específica"""
    dados = carregar_historico()
    usuario = usuario.lower()
    
    print("\n" + "═" * 40)
    print(f" HISTÓRICO DE {tipo.upper()} ".center(40, '─'))
    print("═" * 40)
    
    if usuario not in dados['usuarios']:
        print("\n🔍 Usuário não encontrado")
        print("═" * 40)
        return
    
    registros = dados['usuarios'][usuario]
    
    if not registros:
        print("\n📭 Nenhum registro encontrado para este usuário")
        print("═" * 40)
        return
    
    print(f"\nUsuário: {usuario.capitalize()}")
    print(f"Total de registros: {len(registros)}")
    print("═" * 40)

    # Exibindo os registros conforme o tipo solicitado
    for idx, registro in enumerate(registros, 1):
        print(f"\n📅 Registro #{idx} - {registro.get('data_hora', 'Sem data')}")
        
        if tipo == 'agua':
            print(f"💧 Água: {registro['agua']['valor']} litros")
            print(f"Classificação: {registro['agua']['classificacao']}")
        elif tipo == 'energia':
            print(f"⚡ Energia: {registro['energia']['valor']} kWh")
            print(f"Classificação: {registro['energia']['classificacao']}")
        elif tipo == 'residuos':
            print(f"♻️ Resíduos: {registro['residuos']['valor']}%")
            print(f"Classificação: {registro['residuos']['classificacao']}")
        elif tipo == 'transporte':
            print(f"🚌 Transportes:")
            for transporte in registro['transportes']:
                print(f"  Meio: {transporte['meio']} | Viagens: {transporte['viagens']} | Classificação: {transporte['classificacao']}")
        
    print("═" * 40)

def exibir_todas_categorias():
    """Exibe a visão combinada de todas as categorias"""
    print("\n" + "═" * 40)
    print(" VISUALIZAÇÃO INTEGRADA ".center(40, '─'))
    print("═" * 40)
    
    dados = carregar_historico()
    print("\nCarregando dados combinados...")
    
    for usuario, registros in dados['usuarios'].items():
        print(f"\nUsuário: {usuario.capitalize()}")
        print("Total de registros: ", len(registros))
        print("═" * 40)

        for idx, registro in enumerate(registros, 1):
            print(f"\n📅 Registro #{idx} - {registro.get('data_hora', 'Sem data')}")
            print(f"💧 Água: {registro['agua']['valor']} litros - {registro['agua']['classificacao']}")
            print(f"⚡ Energia: {registro['energia']['valor']} kWh - {registro['energia']['classificacao']}")
            print(f"♻️ Resíduos: {registro['residuos']['valor']}% - {registro['residuos']['classificacao']}")
            print(f"🚌 Transportes: ")
            for transporte in registro['transportes']:
                print(f"  Meio: {transporte['meio']} | Viagens: {transporte['viagens']} | Classificação: {transporte['classificacao']}")
            print("═" * 40)
    
    print("═" * 40)

def mostrar_menu():
    """Exibe o menu principal para escolha de históricos"""
    print("\n" + "═" * 40)
    print(f"{' MENU DE HISTÓRICOS ':=^40}")
    print("═" * 40)
    print(f"{'1. Histórico de Água':<38} ")
    print(f"{'2. Histórico de Energia':<38} ")
    print(f"{'3. Histórico de Transporte':<38} ")
    print(f"{'4. Histórico de Resíduos':<38} ") 
    print(f"{'5. Todas as Categorias':<38} ")  # Nova opção
    print(f"{'6. Sair do Sistema':<38} ")      # Opção de saída ajustada
    print("═" * 40)

def main():
    """Função principal com nova opção integrada"""
    usuario = input("Digite o nome do usuário para acessar o histórico: ").strip()

    while True:
        mostrar_menu()
        opcao = input("\nEscolha o histórico desejado (1-6): ").strip()  # Ajustado para 6 opções
        
        if opcao == "1":
            exibir_historico_categoria(usuario, 'agua')
        elif opcao == "2":
            exibir_historico_categoria(usuario, 'energia')
        elif opcao == "3":
            exibir_historico_categoria(usuario, 'transporte')
        elif opcao == "4":
            exibir_historico_categoria(usuario, 'residuos')
        elif opcao == "5":  # Nova opção
            exibir_todas_categorias()
        elif opcao == "6":
            print("\n" + "═" * 40)
            print(f"{' OBRIGADO POR USAR O SISTEMA! ':=^40}")
            print("═" * 40 + "\n")
            break
        else:
            print("\n⚠ Opção inválida! Use valores de 1 a 6.") 
            input("Pressione Enter para tentar novamente...")

if __name__ == "__main__":
    main()
