from db_manager import buscar_gastos_usuario, atualizar_gastos_no_mysql, buscar_transportes_usuario, atualizar_transportes_no_mysql, conectar_db
import datetime

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main(id_usuario):
    while True:
        limpar_tela()
        print("\n╔" + "═" * 78 + "╗")
        print("║" + " EDITAR GASTOS E TRANSPORTES ".center(78, '─') + "║")
        print("╚" + "═" * 78 + "╝")

        # Busca os gastos do usuário no banco de dados
        gastos = buscar_gastos_usuario(id_usuario)
        if not gastos:
            print("Nenhum gasto encontrado para este usuário.")
            input("\nPressione Enter para voltar ao menu...")
            return

        # Exibe os gastos cadastrados
        print("\nGastos cadastrados:")
        for i, gasto in enumerate(gastos):
            print(f"[{i}] ID: {gasto['id']}, Data/Hora: {gasto['data_hora']}, Categoria: {gasto['periodo']}")
            print(f"    Água: {gasto['gasto_agua']}L ({gasto['classificacao_agua']}), "
                  f"Energia: {gasto['gasto_energia']}kWh ({gasto['classificacao_energia']}), "
                  f"Resíduos: {gasto['gasto_residuos']}% ({gasto['classificacao_residuos']})")

        # Solicita ao usuário escolher um índice para editar
        try:
            indice = int(input("\nDigite o índice do gasto que deseja editar (ou -1 para sair): "))
            if indice == -1:
                break
            if indice < 0 or indice >= len(gastos):
                print("Índice inválido! Tente novamente.")
                input("\nPressione Enter para continuar...")
                continue
        except ValueError:
            print("Entrada inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")
            continue

        # Obtém o gasto selecionado
        gasto_selecionado = gastos[indice]
        id_gasto = gasto_selecionado['id']  # Obtém o ID da linha específica
        data_hora = gasto_selecionado['data_hora']  # Obtém a data/hora do gasto

        # Solicita os novos valores para o gasto
        print("\nDigite os novos valores para o gasto (deixe em branco para manter o valor atual):")
        try:
            agua = input(f"► Consumo de água atual ({gasto_selecionado['gasto_agua']}L): ").strip()
            agua = float(agua) if agua else gasto_selecionado['gasto_agua']

            energia = input(f"► Consumo de energia atual ({gasto_selecionado['gasto_energia']}kWh): ").strip()
            energia = float(energia) if energia else gasto_selecionado['gasto_energia']

            residuos = input(f"► Resíduos não recicláveis atuais ({gasto_selecionado['gasto_residuos']}%): ").strip()
            residuos = float(residuos) if residuos else gasto_selecionado['gasto_residuos']
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir números válidos.")
            input("\nPressione Enter para continuar...")
            continue

        # Atualiza as classificações com base nos novos valores
        classificacoes = {
            "agua": "🟢 Meio Ambiente Agradece" if agua < 100 else "🟡 Alta Sustentabilidade" if agua <= 150 else "🟠 Moderada Sustentabilidade" if agua <= 200 else "🔴 Baixa Sustentabilidade",
            "energia": "🟢 Meio Ambiente Agradece" if energia < 2.5 else "🟡 Alta Sustentabilidade" if energia <= 5 else "🟠 Moderada Sustentabilidade" if energia <= 10 else "🔴 Baixa Sustentabilidade",
            "residuos": "🟢 Meio Ambiente Agradece" if residuos < 20 else "🟡 Alta Sustentabilidade" if residuos <= 50 else "🟠 Moderada Sustentabilidade" if residuos <= 60 else "🔴 Baixa Sustentabilidade"
        }

        # Atualiza o gasto no banco de dados
        atualizado = atualizar_gastos_no_mysql(
            id_gasto=id_gasto,  # Atualiza com base no ID da linha
            agua=agua,
            classificacao_agua=classificacoes["agua"],
            energia=energia,
            classificacao_energia=classificacoes["energia"],
            residuos=residuos,
            classificacao_residuos=classificacoes["residuos"]
        )

        if atualizado:
            print("\nGasto atualizado com sucesso!")
        else:
            print("\nErro ao atualizar o gasto no banco de dados.")

        # Busca os transportes relacionados à mesma data/hora
        transportes = buscar_transportes_usuario(id_usuario)
        transportes_relacionados = [t for t in transportes if t['data_hora'] == data_hora]

        if transportes_relacionados:
            print("\nTransportes relacionados:")
            for i, transporte in enumerate(transportes_relacionados):
                print(f"[{i}] Meio: {transporte['tipo_transporte']}, Viagens: {transporte['quantidade']}, Classificação: {transporte['classificacao_transporte']}")

        while True:
            print("\nOpções para transportes:")
            print("[1] Editar transporte existente")
            print("[2] Remover transporte")
            print("[3] Adicionar novo transporte")
            print("[4] Editar data/hora")
            print("[5] Salvar e sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                try:
                    indice_transporte = int(input("Digite o índice do transporte que deseja editar: "))
                    if indice_transporte < 0 or indice_transporte >= len(transportes_relacionados):
                        print("Índice inválido! Tente novamente.")
                        continue

                    transporte_selecionado = transportes_relacionados[indice_transporte]
                    novo_meio = input(f"► Novo meio de transporte ({transporte_selecionado['tipo_transporte']}): ").strip()
                    novo_meio = novo_meio if novo_meio else transporte_selecionado['tipo_transporte']

                    try:
                        novas_viagens = input(f"► Nova quantidade de viagens ({transporte_selecionado['quantidade']}): ").strip()
                        novas_viagens = int(novas_viagens) if novas_viagens else transporte_selecionado['quantidade']
                    except ValueError:
                        print("Quantidade inválida! Tente novamente.")
                        continue

                    transporte_selecionado['tipo_transporte'] = novo_meio
                    transporte_selecionado['quantidade'] = novas_viagens
                    print("Transporte atualizado com sucesso!")
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                    continue

            elif opcao == "2":
                try:
                    indice_transporte = int(input("Digite o índice do transporte que deseja remover: "))
                    if indice_transporte < 0 or indice_transporte >= len(transportes_relacionados):
                        print("Índice inválido! Tente novamente.")
                        continue

                    transportes_relacionados.pop(indice_transporte)
                    print("Transporte removido com sucesso!")
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                    continue

            elif opcao == "3":
                novo_meio = input("► Novo meio de transporte: ").strip()
                if not novo_meio:
                    print("Meio de transporte não pode ser vazio!")
                    continue
            
                # Classifica automaticamente o transporte com base nas categorias
                transporte_categorias = {
                    'transporte_eco': ['a pé', 'bicicleta'],
                    'transporte_sustentavel': ['carro elétrico', 'ônibus elétrico'],
                    'transporte_baixo': ['ônibus', 'metrô', 'trem'],
                    'transporte_poluente': ['carro', 'moto', 'avião']
                }
            
                def classificar_transporte(tipo_transporte):
                    """Classifica o transporte com base nas categorias."""
                    if tipo_transporte in transporte_categorias['transporte_eco']:
                        return "🟢 Meio Ambiente Agradece"
                    elif tipo_transporte in transporte_categorias['transporte_sustentavel']:
                        return "🟡 Alta Sustentabilidade"
                    elif tipo_transporte in transporte_categorias['transporte_baixo']:
                        return "🟠 Moderada Sustentabilidade"
                    elif tipo_transporte in transporte_categorias['transporte_poluente']:
                        return "🔴 Baixa Sustentabilidade"
                    else:
                        return None  # Retorna None se o transporte não for reconhecido
            
                nova_classificacao = classificar_transporte(novo_meio)
                if not nova_classificacao:
                    print("► Transporte não reconhecido! Use um transporte listado nas categorias.")
                    continue
            
                try:
                    novas_viagens = int(input("► Quantidade de viagens: ").strip())
                except ValueError:
                    print("Quantidade inválida! Tente novamente.")
                    continue
            
                transportes_relacionados.append({
                    "tipo_transporte": novo_meio,
                    "quantidade": novas_viagens,
                    "classificacao_transporte": nova_classificacao,
                    "data_hora": data_hora
                })
                print("Novo transporte adicionado com sucesso!")
            
            
            elif opcao == "4":
                try:
                    # Solicita a nova data/hora ao usuário, parte por parte
                    print("Digite a nova data e hora:")
                    ano = int(input("► Ano (yyyy): "))
                    mes = int(input("► Mês (mm): "))
                    dia = int(input("► Dia (dd): "))
                    hora = int(input("► Hora (hh): "))
                    minuto = int(input("► Minuto (mm): "))
                    segundo = int(input("► Segundo (ss): "))
            
                    # Valida e formata a nova data/hora
                    try:
                        nova_data_hora = datetime.datetime(ano, mes, dia, hora, minuto, segundo)
                        nova_data_hora_str = nova_data_hora.strftime("%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        print("Data/hora inválida! Certifique-se de inserir valores válidos.")
                        continue
            
                    # Conecta ao banco de dados
                    conexao = conectar_db()
                    if conexao is None:
                        print("Erro ao conectar ao banco de dados. Tente novamente.")
                        continue
            
                    try:
                        cursor = conexao.cursor()
            
                        # Atualiza a data/hora na tabela de gastos
                        query_gastos = """UPDATE gastos_usuarios
                                          SET data_hora = %s
                                          WHERE id = %s"""
                        cursor.execute(query_gastos, (nova_data_hora_str, id_gasto))
            
                        # Atualiza a data/hora na tabela de transportes
                        query_transportes = """UPDATE transportes_usuario
                                               SET data_hora = %s
                                               WHERE id_usuario = %s AND data_hora = %s"""
                        cursor.execute(query_transportes, (nova_data_hora_str, id_usuario, data_hora))
            
                        # Confirma as alterações no banco de dados
                        conexao.commit()
                        print("Data/hora atualizada com sucesso para todas as categorias!")
            
                        # Atualiza a variável local `data_hora` para refletir a nova data/hora
                        data_hora = nova_data_hora_str
            
                    except mysql.connector.Error as err:
                        print("Erro ao atualizar a data/hora no banco de dados:", err)
                        conexao.rollback()
                    finally:
                        cursor.close()
                        conexao.close()
            
                except ValueError:
                    print("Entrada inválida! Certifique-se de inserir valores numéricos válidos.")
                    continue
                
                
            
            
            elif opcao == "5":
                # Classifica todos os transportes antes de salvar
                transporte_categorias = {
                    'transporte_eco': ['a pé', 'bicicleta'],
                    'transporte_sustentavel': ['carro elétrico', 'ônibus elétrico'],
                    'transporte_baixo': ['ônibus', 'metrô', 'trem'],
                    'transporte_poluente': ['carro', 'moto', 'avião']
                }

                def classificar_transporte(tipo_transporte):
                    """Classifica o transporte com base nas categorias."""
                    if tipo_transporte in transporte_categorias['transporte_eco']:
                        return "🟢 Meio Ambiente Agradece"
                    elif tipo_transporte in transporte_categorias['transporte_sustentavel']:
                        return "🟡 Alta Sustentabilidade"
                    elif tipo_transporte in transporte_categorias['transporte_baixo']:
                        return "🟠 Moderada Sustentabilidade"
                    elif tipo_transporte in transporte_categorias['transporte_poluente']:
                        return "🔴 Baixa Sustentabilidade"
                    else:
                        return "Categoria desconhecida"

                # Atualiza as classificações de todos os transportes
                for transporte in transportes_relacionados:
                    transporte['classificacao_transporte'] = classificar_transporte(transporte['tipo_transporte'])

                # Atualiza os transportes no banco de dados
                transportes_atualizados = atualizar_transportes_no_mysql(
                    id_usuario=id_usuario,
                    transportes=transportes_relacionados,
                    periodo=gasto_selecionado['periodo'],
                    data_hora=data_hora
                )

                if transportes_atualizados:
                    print("Transportes atualizados com sucesso!")
                else:
                    print("Erro ao atualizar transportes no banco de dados.")
                break

        input("\nPressione Enter para continuar...")