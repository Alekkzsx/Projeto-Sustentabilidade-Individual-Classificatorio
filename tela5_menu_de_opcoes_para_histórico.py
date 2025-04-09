import os
from db_manager import buscar_gastos_usuario, buscar_transportes_usuario

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados_usuario_mysql(id_usuario):
    """
    Carrega os dados do usuário diretamente do banco de dados MySQL.
    """
    dados = buscar_gastos_usuario(id_usuario)
    if not dados:
        print("Nenhum dado encontrado para o usuário.")
        return []
    return dados

def exibir_tabela(categoria, dados, id_usuario):
    """
    Exibe os dados do usuário em formato de tabela para a categoria escolhida.
    """
    limpar_tela()
    print("\n" + "═" * 70)
    print(f" HISTÓRICO DE {categoria.upper()} ".center(70, '─'))
    print("═" * 70)
    print(f"{'Categoria':<20}{'Data e Hora':<30}{'Classificação':<25}")
    print("─" * 70)

    encontrou_dados = False
    for registro in dados:
        data_hora = registro['data_hora']  # Copia diretamente o valor do MySQL
        if categoria == "água":
            print(f"{'Água':<15}   {data_hora}      {registro['classificacao_agua']:<25}")
            encontrou_dados = True
        elif categoria == "energia":
            print(f"{'Energia':<15}   {data_hora}      {registro['classificacao_energia']:<25}")
            encontrou_dados = True
        elif categoria == "resíduos":
            print(f"{'Resíduos':<15}   {data_hora}      {registro['classificacao_residuos']:<25}")
            encontrou_dados = True
        elif categoria == "transporte":
            transportes = buscar_transportes_usuario(id_usuario)
            for transporte in transportes:
                data_hora_transporte = transporte['data_hora']  # Copia diretamente o valor do MySQL
                print(f"{'Transporte':<15}   {data_hora_transporte}      {transporte['classificacao_transporte']:<25}")
                encontrou_dados = True

    if not encontrou_dados:
        print(f"\nNenhum dado encontrado para a categoria {categoria.capitalize()}.")

    print("═" * 70)
    input("\nPressione Enter para voltar ao menu...")

def exibir_todas_categorias(dados, id_usuario):
    """
    Exibe os dados de todas as categorias em formato de tabela.
    """
    limpar_tela()
    print("\n" + "═" * 70)
    print(" HISTÓRICO DE TODAS AS CATEGORIAS ".center(70, '─'))
    print("═" * 70)
    print(f"{'Categoria':<20}{'Data e Hora':<30}{'Classificação':<25}")
    print("─" * 70)

    encontrou_dados = False
    for registro in dados:
        data_hora = registro['data_hora']  # Copia diretamente o valor do MySQL
        # Água
        print(f"{'Água':<15}   {data_hora}      {registro['classificacao_agua']:<25}")
        encontrou_dados = True
        # Energia
        print(f"{'Energia':<15}   {data_hora}      {registro['classificacao_energia']:<25}")
        encontrou_dados = True
        # Resíduos
        print(f"{'Resíduos':<15}   {data_hora}      {registro['classificacao_residuos']:<25}")
        encontrou_dados = True
        # Transportes
        transportes = buscar_transportes_usuario(id_usuario)
        for transporte in transportes:
            data_hora_transporte = transporte['data_hora']  # Copia diretamente o valor do MySQL
            print(f"{'Transporte':<15}   {data_hora_transporte}      {transporte['classificacao_transporte']:<25}")
            encontrou_dados = True

    if not encontrou_dados:
        print("\nNenhum dado encontrado para o usuário.")

    print("═" * 70)
    input("\nPressione Enter para voltar ao menu...")

def mostrar_menu(usuario_logado, id_usuario):
    """
    Exibe o menu principal para escolha de históricos.
    """
    while True:
        limpar_tela()
        print("\n" + "═" * 50)
        print(f" HISTÓRICO DO USUÁRIO: {usuario_logado.upper()} ".center(50, '─'))
        print("═" * 50)
        print(f"{'1. Histórico de Água':<38}".center(70))
        print(f"{'2. Histórico de Energia':<38}".center(70))
        print(f"{'3. Histórico de Transporte':<38}".center(70))
        print(f"{'4. Histórico de Resíduos':<38}".center(70))
        print(f"{'5. Todas as Categorias':<38}".center(70))
        print(f"{'6. Sair':<38}".center(70))
        print("═" * 50)

        opcao = input("Escolha o histórico desejado (1-6): ").strip()

        dados = carregar_dados_usuario_mysql(id_usuario)
        if not dados:
            print("\nNenhum dado encontrado para o usuário.")
            input("Pressione Enter para voltar...")
            return

        if opcao == "1":
            limpar_tela()
            exibir_tabela("água", dados, id_usuario)
        elif opcao == "2":
            limpar_tela()
            exibir_tabela("energia", dados, id_usuario)
        elif opcao == "3":
            limpar_tela()
            exibir_tabela("transporte", dados, id_usuario)
        elif opcao == "4":
            limpar_tela()
            exibir_tabela("resíduos", dados, id_usuario)
        elif opcao == "5":
            limpar_tela()
            exibir_todas_categorias(dados, id_usuario)
        elif opcao == "6":
            print("\nSaindo do histórico...")
            break
        else:
            print("\n⚠ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")