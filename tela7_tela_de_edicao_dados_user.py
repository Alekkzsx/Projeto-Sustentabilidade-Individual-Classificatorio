import json
import os

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
    nova_data_hora = input("\nNova data/hora (deixe em branco para manter): ").strip()
    if nova_data_hora:
        registro["data_hora"] = nova_data_hora

    # Editar consumo de água
    try:
        novo_agua = input("Novo consumo de água (L) (deixe em branco para manter): ").strip()
        if novo_agua:
            registro["agua"]["valor"] = float(novo_agua)
    except ValueError:
        print("Valor inválido para água. Mantendo o valor atual.")

    # Editar consumo de energia
    try:
        novo_energia = input("Novo consumo de energia (kWh) (deixe em branco para manter): ").strip()
        if novo_energia:
            registro["energia"]["valor"] = float(novo_energia)
    except ValueError:
        print("Valor inválido para energia. Mantendo o valor atual.")

    # Editar resíduos
    try:
        novo_residuos = input("Novo percentual de resíduos (%) (deixe em branco para manter): ").strip()
        if novo_residuos:
            registro["residuos"]["valor"] = float(novo_residuos)
    except ValueError:
        print("Valor inválido para resíduos. Mantendo o valor atual.")

    # Editar transportes
    while True:
        print("\nTransportes:")
        for i, transporte in enumerate(registro["transportes"]):
            print(f"  [{i}] Meio: {transporte['meio']}, Viagens: {transporte['viagens']}, Classificação: {transporte['classificacao']}")
        print("[A] Adicionar transporte")
        print("[R] Remover transporte")
        print("[S] Sair da edição de transportes")
        opcao = input("Escolha uma opção: ").strip().upper()

        if opcao == "A":
            meio = input("Meio de transporte: ").strip()
            try:
                viagens = float(input("Quantidade de viagens: ").strip())
                classificacao = input("Classificação: ").strip()
                registro["transportes"].append({"meio": meio, "viagens": viagens, "classificacao": classificacao})
            except ValueError:
                print("Valor inválido para viagens. Transporte não adicionado.")
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