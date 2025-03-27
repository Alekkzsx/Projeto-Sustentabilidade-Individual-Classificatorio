import json
import os
from datetime import datetime

def carregar_gastos():
    arquivo = 'gastos_usuarios.json'
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump({"usuarios": {}}, f)
    
    with open(arquivo, 'r') as f:
        return json.load(f)

def verificar_usuario(usuario, dados):
    return usuario.lower() in dados['usuarios']

def obter_dados_usuario(usuario, dados):
    return dados['usuarios'].get(usuario.lower(), None)

def classificar_sustentabilidade(total_gasto):
    if total_gasto <= 50:
        return "Meio ambiente agradece !!! 🌱"
    elif total_gasto <= 100:
        return "Sustentável ✅"
    elif total_gasto <= 200:
        return "Baixo nível de sustentabilidade ⚠️"
    else:
        return "Desperdício !!! 💸"

def exibir_resultado(dados):
    print("\n" + "═" * 40)
    print("*** HISTÓRICO DO USUÁRIO ***".center(40))
    print("═" * 40)
    print(f"Última atualização: {dados['data_registro']} ⏰")
    print(f"Água: {dados['agua']} litros 💧")
    print(f"Energia: {dados['energia']} kWh ⚡")
    print(f"Uso de Transporte: {dados['transporte']}% 🚌")
    print(f"Resíduos Não Recicláveis: {dados['reciclavel']}% ♻️")
    
    total = dados['agua'] + dados['energia'] + dados['transporte'] + dados['reciclavel']
    print("═" * 40)
    print(f"Total combinado: {total} 📊")
    print(f"Classificação: {classificar_sustentabilidade(total)} 🏷️")
    print("═" * 40 + "\n")

def main():
    dados = carregar_gastos()
    
    print("\n" + "═" * 40)
    usuario = input("Digite seu nome de usuário: ").strip()
    
    if verificar_usuario(usuario, dados):
        dados_usuario = obter_dados_usuario(usuario, dados)
        if dados_usuario:
            exibir_resultado(dados_usuario)
        else:
            print("\n⚠️  Usuário sem informações registradas ⚠️\n")
    else:
        print("\n🔍  Usuário não encontrado no sistema 🔍\n")

if __name__ == "__main__":
    main()