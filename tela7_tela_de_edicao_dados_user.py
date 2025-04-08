import json
import os
import datetime

# Caminho para o arquivo JSON
JSON_FILE = "gastos_usuarios.json"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    """Carrega os dados do arquivo JSON."""
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def listar_registros(usuario, dados):
    """Lista os registros de um usuário."""
    if usuario not in dados or not dados[usuario]:
        print("\nNenhum registro encontrado para o usuário.")
        return None

    print("\nRegistros disponíveis:")
    for i, registro in enumerate(dados[usuario]):
        print(f"[{i}] Data/Hora: {registro['data_hora']}, Água: {registro['agua']['valor']}L, Energia: {registro['energia']['valor']}kWh, Resíduos: {registro['residuos']['valor']}%")
    return dados[usuario]

def exibir_registro(registro):
    """Exibe os detalhes de um registro em formato de tabela."""
    limpar_tela()
    print("\n" + "═" * 70)
    print(" DETALHES DO REGISTRO ".center(70, ' '))
    print("═" * 70)
    print(f"📅 Data/Hora: {registro['data_hora']}".center(70))
    print("═" * 70)
    print(f"🌊 Água:".ljust(25) + f"{registro['agua']['valor']}L".ljust(15) + f"{registro['agua']['classificacao']}")
    print(f"💡 Energia:".ljust(25) + f"{registro['energia']['valor']}kWh".ljust(15) + f"{registro['energia']['classificacao']}")
    print(f"♻️ Resíduos:".ljust(25) + f"  {registro['residuos']['valor']}%".ljust(15) + f"  {registro['residuos']['classificacao']}")
    print("═" * 70)
    print("🚦 Transportes:".center(70))
    print("═" * 70)
    print(f"{'Índice':<8}{'Meio':<15}{'Viagens':<20}{'Classificação':<15}")
    print("─" * 70)
    for i, transporte in enumerate(registro["transportes"]):
        print(f"{i:<8}{transporte['meio']:<16}{transporte['viagens']:<18}{transporte['classificacao']:<20}")
    print("═" * 70)

def editar_registro(usuario, indice, dados):
    """Edita um registro específico de um usuário."""
    registro = dados[usuario][indice]
    exibir_registro(registro)

    # Editar data/hora
    while True:
        nova_data_hora = input("\nNova data/hora (formato DIA/MES/ANO HORARIO, deixe em branco para manter): ").strip()
        if not nova_data_hora:
            break  # Mantém o valor atual
        try:
            nova_data_hora_formatada = datetime.strptime(nova_data_hora, "%d/%m/%Y %H:%M")
            if nova_data_hora != registro["data_hora"]:
                registro["data_hora"] = nova_data_hora
                break
            else:
                print("A nova data/hora deve ser diferente da atual.")
        except ValueError:
            print("Formato inválido! Insira a data/hora no formato DIA/MES/ANO HORARIO.")

    # Editar consumo de água
    while True:
        try:
            novo_agua = input("Novo consumo de água (L) (deixe em branco para manter): ").strip()
            if not novo_agua:
                break  # Mantém o valor atual
            novo_agua = float(novo_agua)
            if novo_agua != registro["agua"]["valor"]:
                registro["agua"]["valor"] = novo_agua
                break
            else:
                print("O novo consumo de água deve ser diferente do atual.")
        except ValueError:
            print("Valor inválido para água. Por favor, insira um número válido.")

    # Editar consumo de energia
    while True:
        try:
            novo_energia = input("Novo consumo de energia (kWh) (deixe em branco para manter): ").strip()
            if not novo_energia:
                break  # Mantém o valor atual
            novo_energia = float(novo_energia)
            if novo_energia != registro["energia"]["valor"]:
                registro["energia"]["valor"] = novo_energia
                break
            else:
                print("O novo consumo de energia deve ser diferente do atual.")
        except ValueError:
            print("Valor inválido para energia. Por favor, insira um número válido.")

    # Editar resíduos
    while True:
        try:
            novo_residuos = input("Novo percentual de resíduos (%) (deixe em branco para manter): ").strip()
            if not novo_residuos:
                break  # Mantém o valor atual
            novo_residuos = float(novo_residuos)
            if novo_residuos != registro["residuos"]["valor"]:
                registro["residuos"]["valor"] = novo_residuos
                break
            else:
                print("O novo percentual de resíduos deve ser diferente do atual.")
        except ValueError:
            print("Valor inválido para resíduos. Por favor, insira um número válido.")

    # Editar transportes
    while True:
        print("\nTransportes:")
        for i, transporte in enumerate(registro["transportes"]):
            print(f"  [{i}] Meio: {transporte['meio']}, Viagens: {transporte['viagens']}")
        print("[A] Adicionar transporte")
        print("[E] Editar transporte existente")
        print("[R] Remover transporte")
        print("[S] Sair da edição de transportes")
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "A":
            while True:
                meio = input("Meio de transporte: ").strip().lower()
                if meio:
                    try:
                        viagens = float(input("Quantidade de viagens: ").strip())
                        registro["transportes"].append({"meio": meio, "viagens": viagens})
                        break
                    except ValueError:
                        print("Valor inválido para viagens. Por favor, insira um número válido.")
                else:
                    print("O meio de transporte não pode ser vazio.")
        elif opcao == "E":
            try:
                indice_transporte = int(input("Índice do transporte a editar: ").strip())
                if 0 <= indice_transporte < len(registro["transportes"]):
                    transporte = registro["transportes"][indice_transporte]
                    while True:
                        novo_meio = input(f"Novo meio de transporte (atual: {transporte['meio']}, deixe em branco para manter): ").strip().lower()
                        if novo_meio and novo_meio != transporte["meio"]:
                            transporte["meio"] = novo_meio
                            break
                        elif not novo_meio:
                            break
                        else:
                            print("O novo meio de transporte deve ser diferente do atual.")
                    while True:
                        try:
                            novas_viagens = input(f"Nova quantidade de viagens (atual: {transporte['viagens']}, deixe em branco para manter): ").strip()
                            if not novas_viagens:
                                break
                            novas_viagens = float(novas_viagens)
                            if novas_viagens != transporte["viagens"]:
                                transporte["viagens"] = novas_viagens
                                break
                            else:
                                print("A nova quantidade de viagens deve ser diferente da atual.")
                        except ValueError:
                            print("Valor inválido para viagens. Por favor, insira um número válido.")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Índice inválido.")
        elif opcao == "R":
            try:
                indice_transporte = int(input("Índice do transporte a remover: ").strip())
                if 0 <= indice_transporte < len(registro["transportes"]):
                    registro["transportes"].pop(indice_transporte)
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Índice inválido.")
        elif opcao == "S":
            break
        else:
            print("Opção inválida.")

    # Recalcular classificações
    agua = registro["agua"]["valor"]
    energia = registro["energia"]["valor"]
    residuos = registro["residuos"]["valor"]

    registro["agua"]["classificacao"] = "🟢 Meio Ambiente Agradece" if agua < 100 else "🟡 Alta Sustentabilidade" if agua <= 150 else "🟠 Moderada Sustentabilidade" if agua <= 200 else "🔴 Baixa Sustentabilidade"
    registro["energia"]["classificacao"] = "🟢 Meio Ambiente Agradece" if energia < 2.5 else "🟡 Alta Sustentabilidade" if energia <= 5 else "🟠 Moderada Sustentabilidade" if energia <= 10 else "🔴 Baixa Sustentabilidade"
    registro["residuos"]["classificacao"] = "🟢 Meio Ambiente Agradece" if residuos < 20 else "🟡 Alta Sustentabilidade" if residuos <= 50 else "🟠 Moderada Sustentabilidade" if residuos <= 60 else "🔴 Baixa Sustentabilidade"

    # Salvar alterações
    dados[usuario][indice] = registro
    salvar_dados(dados)
    print("\nRegistro atualizado com sucesso!")

def main(usuario_logado):
    """Função principal para editar dados."""
    limpar_tela()
    dados = carregar_dados()

    if usuario_logado not in dados or not dados[usuario_logado]:
        print("\nNenhum registro encontrado para o usuário.")
        input("Pressione Enter para voltar ao menu...")
        return

    registros = listar_registros(usuario_logado, dados)
    if not registros:
        input("Pressione Enter para voltar ao menu...")
        return

    try:
        indice = int(input("\nEscolha o índice do registro para editar: ").strip())
        if 0 <= indice < len(registros):
            editar_registro(usuario_logado, indice, dados)
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")
    input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main("Usuário")