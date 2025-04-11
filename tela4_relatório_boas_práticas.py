import random
import os
from db_manager import conectar_db, buscar_gastos_usuario, buscar_transportes_usuario

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Textos de recomendações e boas práticas
recomendacoes = {
    "agua": [
        "Reduza o tempo no banho para economizar água e energia. Pequenas mudanças fazem uma grande diferença!",
        "Conserte vazamentos em torneiras e encanamentos. Um pequeno gotejamento pode desperdiçar litros de água por dia.",
    ],
    "energia": [
        "Desligue aparelhos eletrônicos quando não estiverem em uso. Isso ajuda a economizar energia e reduzir custos.",
        "Troque lâmpadas incandescentes por LED. Elas consomem menos energia e duram mais.",
    ],
    "residuos": [
        "Separe o lixo reciclável do orgânico. Isso facilita a reciclagem e reduz o impacto ambiental.",
        "Evite o uso de plásticos descartáveis. Prefira alternativas reutilizáveis, como garrafas e sacolas.",
    ],
    "transportes": [
        "Considere usar bicicleta ou caminhar para trajetos curtos. Isso reduz emissões e melhora sua saúde.",
        "Use transporte público sempre que possível. É uma alternativa mais sustentável e econômica.",
    ]
}

boas_praticas = {
    "agua": [
        "Parabéns por economizar água! Continue reduzindo o consumo e inspire outras pessoas a fazerem o mesmo.",
        "Seu consumo de água está excelente! Pequenas ações como a sua ajudam a preservar recursos naturais.",
    ],
    "energia": [
        "Ótimo trabalho economizando energia! Continue desligando aparelhos e usando fontes renováveis.",
        "Seu consumo de energia está exemplar! Isso ajuda a reduzir emissões de carbono e proteger o planeta.",
    ],
    "residuos": [
        "Parabéns por reciclar! Sua contribuição é essencial para reduzir o impacto ambiental.",
        "Seu esforço em separar resíduos é admirável. Continue assim para um futuro mais sustentável.",
    ],
    "transportes": [
        "Ótima escolha ao usar transportes sustentáveis! Isso faz uma grande diferença para o meio ambiente.",
        "Seu uso de bicicleta ou caminhada é inspirador. Continue promovendo a mobilidade sustentável.",
    ]
}

textos_media_geral = {
    "alta": [
        "Sua média geral é excelente! Continue com suas práticas sustentáveis e inspire outras pessoas a fazerem o mesmo.",
        "Parabéns! Sua média geral mostra que você está no caminho certo para um estilo de vida sustentável.",
    ],
    "moderada": [
        "Sua média geral é boa, mas há espaço para melhorias. Continue se esforçando!",
        "Você está indo bem, mas pode melhorar em algumas áreas. Pequenas mudanças fazem a diferença.",
    ],
    "baixa": [
        "Sua média geral está baixa. Considere adotar práticas mais sustentáveis para melhorar.",
        "Há espaço para melhorias. Comece com pequenas mudanças para reduzir seu impacto ambiental.",
    ]
}

def carregar_dados_usuario(id_usuario):
    """
    Carrega os dados do usuário do banco de dados MySQL.
    """
    gastos = buscar_gastos_usuario(id_usuario)
    transportes = buscar_transportes_usuario(id_usuario)
    if not gastos and not transportes:
        return None

    dados = []
    for gasto in gastos:
        registro = {
            "agua": {"classificacao": gasto["classificacao_agua"]},
            "energia": {"classificacao": gasto["classificacao_energia"]},
            "residuos": {"classificacao": gasto["classificacao_residuos"]},
            "transportes": []
        }
        for transporte in transportes:
            registro["transportes"].append({
                "classificacao": transporte["classificacao_transporte"]
            })
        dados.append(registro)
    return dados

def calcular_media_classificacao(dados):
    """
    Calcula a média geral das classificações do usuário.
    """
    classificacoes = {"🟢": 4, "🟡": 3, "🟠": 2, "🔴": 1}
    total = 0
    count = 0

    for registro in dados:
        total += classificacoes[registro["agua"]["classificacao"][0]]
        total += classificacoes[registro["energia"]["classificacao"][0]]
        total += classificacoes[registro["residuos"]["classificacao"][0]]
        for transporte in registro["transportes"]:
            total += classificacoes[transporte["classificacao"][0]]
        count += 3 + len(registro["transportes"])

    return total / count if count > 0 else 0

def exibir_recomendacoes(dados):
    """
    Exibe recomendações com base na pior classificação do usuário.
    """
    pior_categoria = None
    pior_classificacao = "🔴"

    for registro in dados:
        if registro["agua"]["classificacao"] == pior_classificacao:
            pior_categoria = "agua"
        elif registro["energia"]["classificacao"] == pior_classificacao:
            pior_categoria = "energia"
        elif registro["residuos"]["classificacao"] == pior_classificacao:
            pior_categoria = "residuos"
        for transporte in registro["transportes"]:
            if transporte["classificacao"] == pior_classificacao:
                pior_categoria = "transportes"

    if pior_categoria:
        recomendacao = random.choice(recomendacoes[pior_categoria])
        print(f"\nRecomendação para melhorar sua classificação em {pior_categoria.capitalize()}:")
        print(recomendacao)
    else:
        print("\nParabéns! Nenhuma recomendação necessária, suas classificações estão ótimas!")

def exibir_boas_praticas(dados):
    """
    Exibe boas práticas com base na melhor classificação do usuário.
    """
    melhor_categoria = None
    melhor_classificacao = "🟢"

    for registro in dados:
        if registro["agua"]["classificacao"] == melhor_classificacao:
            melhor_categoria = "agua"
        elif registro["energia"]["classificacao"] == melhor_classificacao:
            melhor_categoria = "energia"
        elif registro["residuos"]["classificacao"] == melhor_classificacao:
            melhor_categoria = "residuos"
        for transporte in registro["transportes"]:
            if transporte["classificacao"] == melhor_classificacao:
                melhor_categoria = "transportes"

    if melhor_categoria:
        boas_pratica = random.choice(boas_praticas[melhor_categoria])
        print(f"\nBoas práticas para {melhor_categoria.capitalize()}:")
        print(boas_pratica)
    else:
        print("\nContinue se esforçando para alcançar classificações melhores!")

def exibir_media_geral(dados):
    """
    Exibe a média geral das classificações do usuário.
    """
    media = calcular_media_classificacao(dados)
    if media >= 3.5:
        texto = random.choice(textos_media_geral["alta"])  # Textos para médias altas
    elif media >= 2.5:
        texto = random.choice(textos_media_geral["moderada"])  # Textos para médias moderadas
    else:
        texto = random.choice(textos_media_geral["baixa"])  # Textos para médias baixas

    print(f"\nSua média geral é: {media:.2f}")
    print(texto)

def main(id_usuario):
    dados = carregar_dados_usuario(id_usuario)
    if not dados:
        print("Nenhum dado encontrado para o usuário.")
        return

    while True:
        limpar_tela()
        print("\n╔" + "═" * 78 + "╗")
        print("║" + " RELATÓRIO DE BOAS PRÁTICAS ".center(78, '─') + "║")
        print("╠" + "═" * 78 + "╣")
        print("║" + " [1] Recomendações ".ljust(77) + " ║")
        print("║" + " [2] Boas Práticas ".ljust(77) + " ║")
        print("║" + " [3] Média Geral ".ljust(77) + " ║")
        print("║" + " [4] Sair ".ljust(77) + " ║")
        print("╚" + "═" * 78 + "╝")

        choice = input("▶ Escolha uma opção: ")

        if choice == '1':
            exibir_recomendacoes(dados)
        elif choice == '2':
            exibir_boas_praticas(dados)
        elif choice == '3':
            exibir_media_geral(dados)
        elif choice == '4':
            break
        else:
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")