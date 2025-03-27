import json
import os
from datetime import datetime

# Configuração do arquivo JSON
ARQUIVO_GASTOS = 'gastos_usuarios.json'

def carregar_historico():
    """Carrega os dados do arquivo JSON"""
    if not os.path.exists(ARQUIVO_GASTOS):
        return {"usuarios": {}}
    
    with open(ARQUIVO_GASTOS, 'r') as f:
        return json.load(f)

def exibir_historico(usuario):
    """Exibe o histórico de um usuário"""
    dados = carregar_historico()
    usuario = usuario.lower()
    
    print("\n" + "═" * 40)
    print(f"{' HISTÓRICO ':=^40}")
    
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
    
    for idx, registro in enumerate(registros, 1):
        print(f"\n📅 Registro #{idx} - {registro.get('data', 'Sem data')}")
        print(f"💧 Água: {registro.get('agua', 0)} litros")
        print(f"⚡ Energia: {registro.get('energia', 0)} kWh")
        print(f"🚌 Transporte: {registro.get('transporte', 0)}%")
        print(f"♻️ Resíduos: {registro.get('residuos', 0)}%")
    
    print("\n" + "═" * 40)

# Exemplo de uso
if __name__ == "__main__":
    print("Sistema de Histórico - Versão Simplificada")
    usuario = input("\nDigite o nome do usuário: ").strip()
    exibir_historico(usuario)