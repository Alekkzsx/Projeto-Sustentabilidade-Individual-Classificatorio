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
            print(f"    Água: {gasto['gasto_agua']}L ({gasto['classificacao_agua']}), \n"
                  f"    Energia: {gasto['gasto_energia']}kWh ({gasto['classificacao_energia']}), \n"
                  f"    Resíduos: {gasto['gasto_residuos']}% ({gasto['classificacao_residuos']})")

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
        
        limpar_tela()
    
        while True:
            limpar_tela()
            print("\nTransportes relacionados:")
            for i, transporte in enumerate(transportes_relacionados):
                print(f"[{i}] Meio: {transporte['tipo_transporte']}, Viagens: {transporte['quantidade']}, Classificação: {transporte['classificacao_transporte']}")            
            
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
                    'transporte_eco': ["bicicleta", "a pé", "caminhada", "patinete", "skate", "monociclo", "triciclo", "bicicleta elétrica", "patinete elétrico", "triciclo elétrico", "segway", "hoverboard", "ciclomóvel", "pedalinho", "remo", "caiaque", "canoagem", "velocípede", "pedestre", "ciclo-táxi", "bicicross", "bicicleta dobrável", "bicicleta de carga", "bicicleta de montanha", "bicicleta de estrada", "bicicleta urbana", "bicicleta híbrida", "bicicleta tandem", "bicicleta infantil", "motocicleta elétrica", "scooter elétrica", "scooter", "caminhada rápida", "trilha a pé", "corrida", "trote", "bicicleta de estrada elétrica", "bicicleta de montanha elétrica", "patins", "roller", "skate elétrico", "skate freestyle", "monociclo elétrico", "bicicleta de trial", "bicicleta off-road", "bicicleta de pista", "bicicleta retrô", "ciclismo", "pedalar", "passo a passo", "movimento sustentável", "transporte ativo", "ciclo urbano", "ciclo popular", "eco pedal", "eco caminho", "ciclovia", "pista ciclável", "rua compartilhada", "corrida sustentável", "caminhada ecológica", "andando a pé", "pedal ecológico", "movimento a pé", "caminho natural", "eco rol", "pedal urbano", "bicicleta solidária", "carona solidária", "carona sustentável", "carona ecológica", "transporte colaborativo", "bicicleta colaborativa", "pedalar juntos", "caminhada coletiva", "movimento coletivo", "eco locomoção", "locomoção sustentável", "locomoção ativa", "caminho ativo", "passeio ativo", "passeio a pé", "passeio de bicicleta", "passeio ecológico", "cicloturismo", "turismo de bicicleta", "turismo a pé", "rota sustentável", "rota ecológica", "rota ativa", "via ativa", "via sustentável", "pedal rotativo", "eco viagem", "viagem a pé", "viagem de bicicleta", "pedalada noturna", "caminhada noturna", "corrida noturna", "eco pedalada", "ciclo sustentável", "bicicleta de passeio", "bicicleta de lazer", "bicicleta recreativa", "caminhada recreativa", "trilha ecológica", "trilha sustentável", "caminhada meditativa", "passeio sustentável", "cicloaventura", "aventura a pé", "eco aventura", "expedição a pé", "expedição ciclística", "pedal aventureiro", "ciclo explorador", "caminhada exploratória", "via verde", "rota verde", "ciclo verde", "pedal verde", "eco viagem urbana", "viagem verde", "transporte verde", "locomoção verde", "movimento verde", "verde a pé", "verde de bicicleta", "bicicleta ecológica", "patinete ecológico", "triciclo ecológico", "veículo ecológico", "transporte humanizado", "caminhada humanizada", "pedal humanizado", "ciclo solidário", "locomoção solidária", "caminhada consciente", "pedalada consciente", "eco consciência", "movimento consciente", "locomoção consciente", "transporte consciente", "eco friendly", "amigo do ambiente", "eco mobilidade", "mobilidade ativa", "mobilidade sustentável", "mobilidade ecológica", "mobilidade urbana sustentável", "rota ciclável sustentável", "ciclo comunitário", "pedal comunitário", "caminhada comunitária", "via comunitária", "eco percurso", "percurso sustentável", "percurso ecológico", "percurso ativo", "ciclo viagem", "pedal viagem", "viagem ativa", "trânsito sustentável", "trânsito ecológico", "trânsito ativo", "via sustentável ativa", "caminhada diária", "pedalada diária", "ciclo diário", "locomoção diária", "movimento diário", "passo diário", "viagem diária", "rota diária", "ciclo de bairro", "pedal de bairro", "caminhada de bairro", "rota de bairro", "trilha de bairro", "eco bairro", "mobilidade local", "transporte local", "ciclo local", "pedal local", "caminhada local", "rota local", "via local", "ciclo intermunicipal", "pedal intermunicipal", "caminhada intermunicipal", "rota intermunicipal", "eco intermunicipal", "mobilidade intermunicipal", "transporte intermunicipal", "ciclo de aventura", "pedalada de aventura", "caminhada de aventura", "rota de aventura", "eco expedição", "ciclo expedição", "pedal expedição", "bike", "magrela", "zica", "caminhar", "andar", "correr", "trotar", "pedalar", "rolezinho", "role", "footing", "trekking", "hiking", "nordic walking", "power walking", "patins inline", "longboard", "penny board", "waveboard", "streetboard", "freebord", "mountainboard", "bicicleta fixa", "fixie", "bicicleta de bambu", "bicicleta reclinada", "handbike", "ciclofaixa", "faixa compartilhada", "zona 30", "zona calma", "rua de pedestres", "calçadão", "parque linear", "corredor verde", "micromobilidade", "mobilidade suave", "deslocamento ativo", "transporte não motorizado", "zero emissão", "pegada de carbono zero", "mobilidade de baixo carbono", "pedal assistido", "e-bike", "e-scooter", "pedal em grupo", "bicicletada", "massa crítica", "evento ciclístico", "corrida de rua", "maratona", "meia maratona", "ultramaratona", "caminhada solidária", "corrida beneficente", "bicicreta", "bisicleta", "bicleta", "bicicreta eletrica", "bicicleta eletrica", "caminhada", "caminada", "camiada", "patinet", "patinette", "patineti", "patinet eletrico", "patinete eletrico", "esqueite", "iskeite", "skat", "skeit", "monociclo", "monossiclo", "monociclo eletrico", "hoverbord", "overboard", "roverboard", "rouverboard", "seguei", "segway", "roler", "patis", "ciclismo", "siclismo", "pedala", "pedalá", "a pe", "ape", "caminhando", "correndo", "pedalando", "ciclovia", "siclovia", "ciclo via", "ecopédal", "eco pedal", "eko pedal", "eco caminho", "eko caminho", "bicicros", "bicicross"],
                    'transporte_sustentavel': ["carro elétrico", "patinete elétrico", "bicicleta elétrica", "ônibus elétrico", "trem elétrico", "veículo híbrido", "carro híbrido", "motocicleta elétrica", "van elétrica", "micro-ônibus elétrico", "caminhão elétrico", "scooter elétrica", "triciclo elétrico", "bonde elétrico", "barco elétrico", "ferry elétrico", "veículo solar", "carro solar", "ônibus solar", "trem solar", "veículo movido a hidrogênio", "carro movido a hidrogênio", "ônibus movido a hidrogênio", "trem movido a hidrogênio", "veículo híbrido plug-in", "carro híbrido plug-in", "ônibus híbrido plug-in", "van híbrida plug-in", "motocicleta híbrida", "scooter híbrida", "bicicleta compartilhada elétrica", "patinete compartilhado elétrico", "carro compartilhado elétrico", "van compartilhada elétrica", "micro-ônibus compartilhado elétrico", "trem leve elétrico", "monotrilho elétrico", "metrô elétrico", "transporte público elétrico", "veículo autônomo elétrico", "carro elétrico compacto", "carro elétrico sedã", "carro elétrico de luxo", "carro elétrico utilitário", "carro elétrico esportivo", "carro elétrico SUV", "carro elétrico hatch", "carro elétrico conversível", "carro elétrico perua", "carro elétrico off-road", "carro elétrico econômico", "carro elétrico urbano", "carro elétrico de alta performance", "ônibus elétrico urbano", "ônibus elétrico intermunicipal", "ônibus elétrico articulado", "ônibus elétrico biarticulado", "ônibus elétrico escolar", "ônibus elétrico executivo", "trem elétrico urbano", "trem elétrico regional", "trem elétrico intermunicipal", "trem elétrico de alta velocidade", "trem elétrico de baixa velocidade", "veículo híbrido urbano", "veículo híbrido intermunicipal", "carro híbrido urbano", "carro híbrido intermunicipal", "motocicleta elétrica urbana", "motocicleta elétrica esportiva", "van elétrica compacta", "van elétrica familiar", "micro-ônibus elétrico urbano", "caminhão elétrico de carga leve", "caminhão elétrico de carga pesada", "caminhão elétrico de distribuição", "scooter elétrica urbana", "scooter elétrica compacta", "triciclo elétrico urbano", "bonde elétrico moderno", "barco elétrico urbano", "ferry elétrico regional", "veículo solar urbano", "veículo solar intermunicipal", "carro solar urbano", "carro solar de luxo", "ônibus solar urbano", "ônibus solar intermunicipal", "trem solar regional", "veículo movido a hidrogênio urbano", "veículo movido a hidrogênio intermunicipal", "carro movido a hidrogênio urbano", "carro movido a hidrogênio de luxo", "ônibus movido a hidrogênio urbano", "trem movido a hidrogênio regional", "veículo híbrido plug-in urbano", "carro híbrido plug-in urbano", "ônibus híbrido plug-in urbano", "van híbrida plug-in urbana", "motocicleta híbrida urbana", "scooter híbrida urbana", "bicicleta elétrica dobrável", "bicicleta elétrica de montanha", "bicicleta elétrica de estrada", "bicicleta elétrica urbana", "bicicleta elétrica de carga", "bicicleta elétrica esportiva", "bicicleta elétrica compacta", "bicicleta elétrica infantil", "bicicleta elétrica tandem", "patinete elétrico compacto", "patinete elétrico de alta performance", "patinete elétrico urbano", "patinete elétrico off-road", "patinete elétrico para crianças", "carro compartilhado elétrico urbano", "carro compartilhado elétrico executivo", "van compartilhada elétrica urbana", "van compartilhada elétrica familiar", "micro-ônibus compartilhado elétrico urbano", "micro-ônibus compartilhado elétrico escolar", "trem leve elétrico urbano", "monotrilho elétrico urbano", "metrô elétrico moderno", "transporte público elétrico urbano", "veículo autônomo elétrico urbano", "carro elétrico com tecnologia autônoma", "ônibus elétrico com tecnologia autônoma", "trem elétrico autônomo", "veículo híbrido com tecnologia autônoma", "carro híbrido com tecnologia autônoma", "motocicleta elétrica autônoma", "van elétrica autônoma", "micro-ônibus elétrico autônomo", "caminhão elétrico autônomo", "scooter elétrica autônoma", "triciclo elétrico autônomo", "bonde elétrico autônomo", "veículo solar com tecnologia autônoma", "carro solar autônomo", "ônibus solar autônomo", "trem solar autônomo", "veículo movido a hidrogênio autônomo", "carro movido a hidrogênio autônomo", "ônibus movido a hidrogênio autônomo", "trem movido a hidrogênio autônomo", "veículo híbrido plug-in autônomo", "carro híbrido plug-in autônomo", "ônibus híbrido plug-in autônomo", "van híbrida plug-in autônoma", "motocicleta híbrida autônoma", "scooter híbrida autônoma", "bicicleta elétrica autônoma", "patinete elétrico autônomo", "carro elétrico com conectividade", "ônibus elétrico com conectividade", "trem elétrico com conectividade", "veículo híbrido com conectividade", "carro híbrido com conectividade", "motocicleta elétrica com conectividade", "van elétrica com conectividade", "micro-ônibus elétrico com conectividade", "caminhão elétrico com conectividade", "scooter elétrica com conectividade", "triciclo elétrico com conectividade", "bonde elétrico com conectividade", "veículo solar com conectividade", "carro solar com conectividade", "ônibus solar com conectividade", "trem solar com conectividade", "veículo movido a hidrogênio com conectividade", "carro movido a hidrogênio com conectividade", "ônibus movido a hidrogênio com conectividade", "trem movido a hidrogênio com conectividade", "veículo híbrido plug-in com conectividade", "carro híbrido plug-in com conectividade", "ônibus híbrido plug-in com conectividade", "van híbrida plug-in com conectividade", "motocicleta híbrida com conectividade", "scooter híbrida com conectividade", "bicicleta elétrica com conectividade", "patinete elétrico com conectividade", "transporte sustentável urbano", "transporte sustentável intermunicipal", "transporte sustentável regional", "mobilidade sustentável urbana", "mobilidade sustentável intermunicipal", "mobilidade sustentável regional", "veículo sustentável avançado", "carro sustentável avançado", "ônibus sustentável avançado", "trem sustentável avançado", "transporte sustentável autônomo", "veículo sustentável autônomo", "carro sustentável autônomo", "ônibus sustentável autônomo", "trem sustentável autônomo", "mobilidade sustentável autônoma", "sistema de transporte sustentável", "rede de transporte sustentável", "EV", "HEV", "PHEV", "FCEV", "carro a hidrogênio", "ônibus a hidrogênio", "caminhão a hidrogênio", "carro movido a energia solar", "ônibus movido a energia solar", "trem movido a energia solar", "e-bus", "e-train", "e-truck", "e-van", "e-moto", "e-scooter", "e-bike", "carsharing elétrico", "ridesharing elétrico", "mobilidade elétrica", "eletromobilidade", "infraestrutura de recarga", "estação de carregamento", "eletroposto", "wallbox", "carregador rápido", "carregador ultrarrápido", "bateria de estado sólido", "célula de combustível", "energia renovável", "smart grid", "V2G (Vehicle-to-Grid)", "transporte verde", "logística verde", "última milha sustentável", "drone de entrega elétrico", "VTOL elétrico", "mobilidade como serviço (MaaS)", "zona de baixa emissão (ZBE)", "LEZ (Low Emission Zone)", "incentivo fiscal para elétricos", "crédito de carbono", "carro eletrico", "carro elétrico", "carro eletrico", "carro hibrido", "carro hibrído", "onibus eletrico", "ônibus elétrico", "onibus eletrico", "trem eletrico", "trem elétrico", "moto eletrica", "moto elétrica", "caminhao eletrico", "caminhão elétrico", "hidrogenio", "idrogênio", "hidrogênio", "híbrido", "hibrido", "plug-in", "plugin", "pluguim", "sustentavel", "sustentável", "sustentaveu", "elétrico", "eletrico", "eletrico", "compartilhado", "conpartilhado", "compartiliado", "autônomo", "autonomo", "autonomu"],
                    'transporte_baixo': ["ônibus urbano", "ônibus intermunicipal", "ônibus escolar", "ônibus executivo", "ônibus articulado", "ônibus biarticulado", "ônibus de turismo", "ônibus noturno", "ônibus de luxo", "ônibus de alta capacidade", "ônibus de baixa emissão", "metrô", "metrô leve", "metrô intermunicipal", "metrô urbano", "trem", "trem regional", "trem de alta velocidade", "trem de baixa velocidade", "trem metropolitano", "bonde", "bonde moderno", "bonde histórico", "VLT", "monotrilho", "trólebus", "trólebus urbano", "ferry urbano", "ferry intermunicipal", "barca", "barca elétrica", "carruagem elétrica", "van compartilhada", "micro-ônibus", "micro-ônibus elétrico", "trolebus articulado", "ônibus articulado elétrico", "ônibus biarticulado elétrico", "ônibus turístico elétrico", "trem elétrico", "metrô elétrico", "bonde elétrico", "VLT elétrico", "ônibus híbrido", "ônibus sustentável", "metrô sustentável", "trem sustentável", "bonde sustentável", "VLT sustentável", "ônibus a gás", "ônibus a diesel", "trem a diesel", "metrô a diesel", "ônibus híbrido elétrico", "ônibus com conectividade", "ônibus autônomo", "metrô autônomo", "trem autônomo", "bonde autônomo", "VLT autônomo", "ônibus com Wi-Fi", "metrô com Wi-Fi", "trem com Wi-Fi", "bonde com Wi-Fi", "VLT com Wi-Fi", "ônibus com ar-condicionado", "metrô climatizado", "trem climatizado", "bonde climatizado", "VLT climatizado", "ônibus acessível", "metrô acessível", "trem acessível", "bonde acessível", "VLT acessível", "ônibus para pessoas com deficiência", "metrô para pessoas com deficiência", "trem para pessoas com deficiência", "bonde para pessoas com deficiência", "VLT para pessoas com deficiência", "ônibus ecológico", "metrô ecológico", "trem ecológico", "bonde ecológico", "VLT ecológico", "ônibus de passageiros", "metrô de passageiros", "trem de passageiros", "bonde de passageiros", "VLT de passageiros", "ônibus urbano elétrico", "ônibus urbano híbrido", "metrô urbano elétrico", "metrô urbano híbrido", "trem urbano elétrico", "trem urbano híbrido", "bonde urbano elétrico", "bonde urbano híbrido", "VLT urbano elétrico", "VLT urbano híbrido", "ônibus intermunicipal elétrico", "ônibus intermunicipal híbrido", "metrô intermunicipal elétrico", "metrô intermunicipal híbrido", "trem intermunicipal elétrico", "trem intermunicipal híbrido", "bonde intermunicipal elétrico", "bonde intermunicipal híbrido", "VLT intermunicipal elétrico", "VLT intermunicipal híbrido", "ônibus noturno elétrico", "metrô noturno", "trem noturno", "bonde noturno", "VLT noturno", "ônibus executivo elétrico", "ônibus executivo híbrido", "metrô executivo", "trem executivo", "bonde executivo", "VLT executivo", "ônibus articulado sustentável", "ônibus biarticulado sustentável", "metrô articulado", "trem articulado", "bonde articulado", "VLT articulado", "ônibus escolar elétrico", "ônibus escolar híbrido", "metrô escolar", "trem escolar", "bonde escolar", "VLT escolar", "ônibus de turismo elétrico", "ônibus de turismo híbrido", "metrô de turismo", "trem de turismo", "bonde de turismo", "VLT de turismo", "ônibus a combustível alternativo", "metrô a combustível alternativo", "trem a combustível alternativo", "bonde a combustível alternativo", "VLT a combustível alternativo", "ônibus com tecnologia verde", "metrô com tecnologia verde", "trem com tecnologia verde", "bonde com tecnologia verde", "VLT com tecnologia verde", "ônibus de alta capacidade", "ônibus de grande porte", "metrô de alta capacidade", "trem de alta capacidade", "bonde de alta capacidade", "VLT de alta capacidade", "ônibus intermodal", "metrô intermodal", "trem intermodal", "bonde intermodal", "VLT intermodal", "ônibus urbano rápido", "metrô rápido", "trem rápido", "bonde rápido", "VLT rápido", "ônibus com tecnologia smart", "metrô smart", "trem smart", "bonde smart", "VLT smart", "ônibus com eficiência energética", "metrô com eficiência energética", "trem com eficiência energética", "bonde com eficiência energética", "VLT com eficiência energética", "ônibus de baixo impacto", "metrô de baixo impacto", "trem de baixo impacto", "bonde de baixo impacto", "VLT de baixo impacto", "ônibus econômico", "metrô econômico", "trem econômico", "bonde econômico", "VLT econômico", "ônibus de transporte coletivo", "metrô de transporte coletivo", "trem de transporte coletivo", "bonde de transporte coletivo", "VLT de transporte coletivo", "ônibus de sistema integrado", "metrô de sistema integrado", "trem de sistema integrado", "bonde de sistema integrado", "VLT de sistema integrado", "ônibus de mobilidade urbana", "metrô de mobilidade urbana", "trem de mobilidade urbana", "bonde de mobilidade urbana", "VLT de mobilidade urbana", "transporte público", "transporte coletivo", "transporte de massa", "busão", "bus", "coletivo", "lotação", "perua", "circular", "alimentador", "troncal", "expresso", "parador", "metropolitano", "suburbano", "trem de subúrbio", "trem urbano", "CPTM", "Supervia", "Trensurb", "Metrofor", "MetrôRio", "Metrô SP", "Metrô BH", "Metrô DF", "bonde de Santa Teresa", "bondinho", "Veículo Leve sobre Trilhos", "Veículo Leve sobre Pneus (VLP)", "BRT (Bus Rapid Transit)", "corredor de ônibus", "faixa exclusiva", "terminal de integração", "estação tubo", "ponto de ônibus", "parada de ônibus", "bilhete único", "cartão de transporte", "vale-transporte", "tarifa social", "passe livre", "integração tarifária", "sistema intermodal", "transporte hidroviário", "catamarã", "lancha coletiva", "travessia", "balsa", "transporte por cabo", "teleférico", "funicular", "elevador Lacerda", "onibus", "onibûs", "onibuz", "ônibus", "metro", "metrô", "metroo", "trem", "tren", "treim", "bonde", "bondi", "VLT", "VTL", "velete", "monotrilho", "monotrilio", "trolebus", "trólebus", "troleibus", "ferry", "ferri", "feri", "barca", "barça", "microonibus", "micro-ônibus", "micro ônibuz", "van", "vam"],
                    'transporte_poluente': ["mobilete","canoa","barco","carro", "iate", "moto", "caminhão", "carro a gasolina", "carro a diesel", "carro a etanol", "carro esportivo a gasolina", "carro sedan a gasolina", "carro hatch a gasolina", "carro compacto a gasolina", "carro de luxo a gasolina", "carro familiar a gasolina", "carro conversível a gasolina", "carro cupê a gasolina", "carro perua a diesel", "carro utilitário a diesel", "carro crossover a gasolina", "carro SUV a diesel", "carro off-road a diesel", "carro urbano a gasolina", "carro de corrida a gasolina", "carro antigo a gasolina", "carro esportivo a diesel", "carro sedan a diesel", "carro hatch a diesel", "carro compacto a diesel", "carro de luxo a diesel", "carro familiar a diesel", "carro conversível a diesel", "carro cupê a diesel", "carro perua a gasolina", "carro utilitário a gasolina", "carro crossover a diesel", "carro SUV a gasolina", "carro off-road a gasolina", "carro urbano a diesel", "carro de corrida a diesel", "carro antigo a diesel", "carro esportivo a etanol", "carro sedan a etanol", "carro hatch a etanol", "carro compacto a etanol", "carro de luxo a etanol", "carro familiar a etanol", "carro conversível a etanol", "carro cupê a etanol", "carro perua a etanol", "carro utilitário a etanol", "carro crossover a etanol", "carro SUV a etanol", "carro off-road a etanol", "carro urbano a etanol", "carro de corrida a etanol", "carro antigo a etanol", "moto a gasolina", "moto esportiva a gasolina", "moto scooter a gasolina", "moto custom a gasolina", "moto off-road a gasolina", "moto trail a gasolina", "moto street a gasolina", "moto naked a gasolina", "moto a etanol", "moto esportiva a etanol", "moto scooter a etanol", "moto custom a etanol", "moto off-road a etanol", "moto trail a etanol", "moto street a etanol", "moto naked a etanol", "moto esportiva modificada a gasolina", "moto de competição a gasolina", "moto de corrida a gasolina", "moto de baixa cilindrada a gasolina", "moto de média cilindrada a gasolina", "moto de alta cilindrada a gasolina", "moto esportiva modificada a etanol", "moto de competição a etanol", "moto de corrida a etanol", "moto de baixa cilindrada a etanol", "moto de média cilindrada a etanol", "moto de alta cilindrada a etanol", "caminhão a diesel", "caminhão articulado a diesel", "caminhão basculante a diesel", "caminhão de carga a diesel", "caminhão truck a diesel", "caminhão pesado a diesel", "caminhão leve a diesel", "caminhão rodoviário a diesel", "caminhão logístico a diesel", "caminhão frigorífico a diesel", "caminhão baú a diesel", "caminhão cegonheiro a diesel", "caminhão de lixo a diesel", "caminhão pipa a diesel", "caminhão de bombeiros a diesel", "caminhão tanque a diesel", "caminhão truck a gasolina", "caminhão articulado a gasolina", "caminhão basculante a gasolina", "caminhão de carga a gasolina", "caminhão pesado a gasolina", "caminhão leve a gasolina", "caminhão rodoviário a gasolina", "caminhão logístico a gasolina", "caminhão frigorífico a gasolina", "caminhão baú a gasolina", "caminhão cegonheiro a gasolina", "caminhão de lixo a gasolina", "caminhão pipa a gasolina", "caminhão de bombeiros a gasolina", "caminhão tanque a gasolina", "caminhão a etanol", "caminhão articulado a etanol", "caminhão basculante a etanol", "caminhão de carga a etanol", "caminhão truck a etanol", "caminhão pesado a etanol", "caminhão leve a etanol", "caminhão rodoviário a etanol", "caminhão logístico a etanol", "caminhão frigorífico a etanol", "caminhão baú a etanol", "caminhão cegonheiro a etanol", "caminhão de lixo a etanol", "caminhão pipa a etanol", "caminhão de bombeiros a etanol", "caminhão tanque a etanol", "ônibus a diesel", "ônibus urbano a diesel", "ônibus intermunicipal a diesel", "ônibus escolar a diesel", "ônibus executivo a diesel", "ônibus articulado a diesel", "ônibus biarticulado a diesel", "ônibus a gasolina", "ônibus urbano a gasolina", "ônibus intermunicipal a gasolina", "ônibus escolar a gasolina", "ônibus executivo a gasolina", "ônibus articulado a gasolina", "ônibus biarticulado a gasolina", "ônibus a etanol", "ônibus urbano a etanol", "ônibus intermunicipal a etanol", "ônibus escolar a etanol", "ônibus executivo a etanol", "ônibus articulado a etanol", "ônibus biarticulado a etanol", "van a gasolina", "van a diesel", "van a etanol", "pickup a gasolina", "pickup a diesel", "pickup a etanol", "minivan a gasolina", "minivan a diesel", "minivan a etanol", "jeep a gasolina", "jeep a diesel", "jeep a etanol", "sedã a gasolina", "sedã a diesel", "sedã a etanol", "cupê a gasolina", "cupê a diesel", "cupê a etanol", "perua a gasolina", "perua a diesel", "perua a etanol", "coupé a gasolina", "coupé a diesel", "coupé a etanol", "veículo de passeio a gasolina", "veículo de passeio a diesel", "veículo de passeio a etanol", "automóvel a gasolina", "automóvel a diesel", "automóvel a etanol", "transportadora a diesel", "transportadora a gasolina", "transportadora a etanol", "bugre a gasolina", "bugre a diesel", "bugre a etanol", "limusine a gasolina", "limusine a diesel", "limusine a etanol", "carreta a diesel", "carreta a gasolina", "carreta a etanol", "reboque a diesel", "reboque a gasolina", "reboque a etanol", "trator a diesel", "trator a gasolina", "trator a etanol", "maquinário pesado a diesel", "maquinário pesado a gasolina", "maquinário pesado a etanol", "equipamento de construção a diesel", "equipamento de construção a gasolina", "automóvel", "veículo particular", "carro de passeio", "motocicleta", "motociclo", "caminhonete", "picape", "jipe", "SUV", "utilitário esportivo", "furgão", "motorhome", "trailer", "lancha", "jet ski", "barco a motor", "navio", "avião", "helicóptero", "jato", "jatinho", "avião de carga", "navio cargueiro", "navio petroleiro", "navio graneleiro", "porta-container", "navio de cruzeiro", "balsa a diesel", "motor a combustão interna", "motor diesel", "motor a gasolina", "motor a álcool", "motor flex", "combustível fóssil", "gasolina comum", "gasolina aditivada", "gasolina premium", "diesel comum", "diesel S10", "diesel S500", "etanol hidratado", "GNV (Gás Natural Veicular)", "querosene de aviação (QAV)", "óleo combustível", "emissão de poluentes", "CO2", "dióxido de carbono", "monóxido de carbono", "óxidos de nitrogênio (NOx)", "material particulado (MP)", "poluição do ar", "poluição sonora", "congestionamento", "tráfego intenso", "carro", "caro", "carrro", "iate", "iate", "iati", "moto", "motto", "motoca", "caminhao", "caminhão", "camiao", "caminhon", "gasolina", "gazolina", "gasolna", "diesel", "disel", "diezel", "dísel", "diezeu", "etanol", "etanol", "alcool", "álcool", "alcóol", "suv", "utilitario", "utilitário", "of-road", "offroad", "off road", "onibus", "ônibus", "onibuz", "picape", "picapi", "pickup", "pick-up", "van", "vam", "jip", "jipe", "jeep", "sedan", "sedã", "cupe", "cupê", "coupe", "perua", "perúa", "limusine", "limosine", "limusini", "carreta", "careta", "trator", "tratorr", "aviao", "avião", "elicoptero", "helicóptero", "elicóptero", "jato", "jatinho", "navio", "naviu", "lancha", "lacha", "jetski", "jet ski", "jetesqui"]
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