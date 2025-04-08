import datetime
import os
import json
import tela4_relatório_boas_práticas
import tela5_menu_de_opcoes_para_histórico

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar_dados_json(usuario, agua, energia, residuos, transportes, classificacoes, periodo):
    """
    Salva os dados do usuário em um arquivo JSON chamado 'gastos_usuarios.json'.
    Se o arquivo não existir, ele será criado.
    """
    arquivo_json = "gastos_usuarios.json"
    
    # Carrega os dados existentes do arquivo JSON ou cria um dicionário vazio
    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = {}  # Caso o arquivo esteja vazio ou corrompido
    else:
        dados = {}

    # Adiciona o usuário se não estiver no arquivo
    if usuario not in dados:
        dados[usuario] = []

    # Adiciona o novo registro com data/hora e período
    registro = {
        "data_hora": datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
        "periodo": periodo,
        "agua": {"valor": agua, "classificacao": classificacoes["agua"]},
        "energia": {"valor": energia, "classificacao": classificacoes["energia"]},
        "residuos": {"valor": residuos, "classificacao": classificacoes["residuos"]},
        "transportes": [
            {"meio": t[0], "viagens": t[1], "classificacao": t[2]} for t in transportes
        ]
    }
    dados[usuario].append(registro)
    
    # Salva os dados atualizados no arquivo JSON
    with open(arquivo_json, 'w') as f:
        json.dump(dados, f, indent=4)

def main(usuario_logado):
    while True:
        limpar_tela()
        # Exibe uma mensagem de boas-vindas com o nome do usuário
        print("\n╔" + "═" * 78 + "╗")
        print(f"║" + f" BEM-VINDO, {usuario_logado.upper()} AO SISTEMA DE SUSTENTABILIDADE ".center(78, '─') + "║")
        print("║" + "O QUE VOCÊ GOSTARIA DE FAZER HOJE?".center(78) + "║")
        print("╚" + "═" * 78 + "╝")

        print("\t\t\t    [1] Registrar novos dados")
        print("\t\t\t    [2] Acessar Histórico")
        print("\t\t\t    [3] Relatório de boas práticas")
        print("\t\t\t    [4] Acessar Gráficos")
        print("\t\t\t    [5] Editar Dados Cadastrados")
        print("\t\t\t    [6] Sair do sistema")
        print("─" * 79)

        choice = input("\t\t\t▶ Escolha uma opção (1/2/3/4/5): ")
        
        if choice == '1':
            limpar_tela()
            print("\n" + "═" * 78)
            print(" NOVO REGISTRO ".center(78, '─'))
            print("═" * 78)

            # Escolha do período
            print("Escolha o período para o registro".center(80))
            print("[1] Diário".center(70))
            print("[2] Mensal".center(70))
            print("[3] Anual".center(70))
            periodo_opcao = input("\t\t\t▶ Escolha o período (1/2/3): ").strip()

            if periodo_opcao == "1":
                periodo = "diário"
            elif periodo_opcao == "2":
                periodo = "mensal"
            elif periodo_opcao == "3":
                periodo = "anual"
            else:
                print("Opção inválida! Retornando ao menu principal...")
                input("Pressione Enter para continuar...")
                continue
            
            # Validação para o consumo de água
            while True:
                try:
                    agua = float(input("\n► Consumo de água (litros): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para o consumo de água.")

            # Validação para o consumo de energia
            while True:
                try:
                    energia = float(input("► Consumo de energia (kWh): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para o consumo de energia.")

            transporte_categorias = {
                'transporte_eco': ["bicicleta", "a pé", "caminhada", "patinete", "skate", "monociclo", "triciclo", "bicicleta elétrica", "patinete elétrico", "triciclo elétrico", "segway", "hoverboard", "ciclomóvel", "pedalinho", "remo", "caiaque", "canoagem", "velocípede", "pedestre", "ciclo-táxi", "bicicross", "bicicleta dobrável", "bicicleta de carga", "bicicleta de montanha", "bicicleta de estrada", "bicicleta urbana", "bicicleta híbrida", "bicicleta tandem", "bicicleta infantil", "motocicleta elétrica", "scooter elétrica", "scooter", "caminhada rápida", "trilha a pé", "corrida", "trote", "bicicleta de estrada elétrica", "bicicleta de montanha elétrica", "patins", "roller", "skate elétrico", "skate freestyle", "monociclo elétrico", "bicicleta de trial", "bicicleta off-road", "bicicleta de pista", "bicicleta retrô", "ciclismo", "pedalar", "passo a passo", "movimento sustentável", "transporte ativo", "ciclo urbano", "ciclo popular", "eco pedal", "eco caminho", "ciclovia", "pista ciclável", "rua compartilhada", "corrida sustentável", "caminhada ecológica", "andando a pé", "pedal ecológico", "movimento a pé", "caminho natural", "eco rol", "pedal urbano", "bicicleta solidária", "carona solidária", "carona sustentável", "carona ecológica", "transporte colaborativo", "bicicleta colaborativa", "pedalar juntos", "caminhada coletiva", "movimento coletivo", "eco locomoção", "locomoção sustentável", "locomoção ativa", "caminho ativo", "passeio ativo", "passeio a pé", "passeio de bicicleta", "passeio ecológico", "cicloturismo", "turismo de bicicleta", "turismo a pé", "rota sustentável", "rota ecológica", "rota ativa", "via ativa", "via sustentável", "pedal rotativo", "eco viagem", "viagem a pé", "viagem de bicicleta", "pedalada noturna", "caminhada noturna", "corrida noturna", "eco pedalada", "ciclo sustentável", "bicicleta de passeio", "bicicleta de lazer", "bicicleta recreativa", "caminhada recreativa", "trilha ecológica", "trilha sustentável", "caminhada meditativa", "passeio sustentável", "cicloaventura", "aventura a pé", "eco aventura", "expedição a pé", "expedição ciclística", "pedal aventureiro", "ciclo explorador", "caminhada exploratória", "via verde", "rota verde", "ciclo verde", "pedal verde", "eco viagem urbana", "viagem verde", "transporte verde", "locomoção verde", "movimento verde", "verde a pé", "verde de bicicleta", "bicicleta ecológica", "patinete ecológico", "triciclo ecológico", "veículo ecológico", "transporte humanizado", "caminhada humanizada", "pedal humanizado", "ciclo solidário", "locomoção solidária", "caminhada consciente", "pedalada consciente", "eco consciência", "movimento consciente", "locomoção consciente", "transporte consciente", "eco friendly", "amigo do ambiente", "eco mobilidade", "mobilidade ativa", "mobilidade sustentável", "mobilidade ecológica", "mobilidade urbana sustentável", "rota ciclável sustentável", "ciclo comunitário", "pedal comunitário", "caminhada comunitária", "via comunitária", "eco percurso", "percurso sustentável", "percurso ecológico", "percurso ativo", "ciclo viagem", "pedal viagem", "viagem ativa", "trânsito sustentável", "trânsito ecológico", "trânsito ativo", "via sustentável ativa", "caminhada diária", "pedalada diária", "ciclo diário", "locomoção diária", "movimento diário", "passo diário", "viagem diária", "rota diária", "ciclo de bairro", "pedal de bairro", "caminhada de bairro", "rota de bairro", "trilha de bairro", "eco bairro", "mobilidade local", "transporte local", "ciclo local", "pedal local", "caminhada local", "rota local", "via local", "ciclo intermunicipal", "pedal intermunicipal", "caminhada intermunicipal", "rota intermunicipal", "eco intermunicipal", "mobilidade intermunicipal", "transporte intermunicipal", "ciclo de aventura", "pedalada de aventura", "caminhada de aventura", "rota de aventura", "eco expedição", "ciclo expedição", "pedal expedição"],
                'transporte_sustentavel': ["carro elétrico", "patinete elétrico", "bicicleta elétrica", "ônibus elétrico", "trem elétrico", "veículo híbrido", "carro híbrido", "motocicleta elétrica", "van elétrica", "micro-ônibus elétrico", "caminhão elétrico", "scooter elétrica", "triciclo elétrico", "bonde elétrico", "barco elétrico", "ferry elétrico", "veículo solar", "carro solar", "ônibus solar", "trem solar", "veículo movido a hidrogênio", "carro movido a hidrogênio", "ônibus movido a hidrogênio", "trem movido a hidrogênio", "veículo híbrido plug-in", "carro híbrido plug-in", "ônibus híbrido plug-in", "van híbrida plug-in", "motocicleta híbrida", "scooter híbrida", "bicicleta compartilhada elétrica", "patinete compartilhado elétrico", "carro compartilhado elétrico", "van compartilhada elétrica", "micro-ônibus compartilhado elétrico", "trem leve elétrico", "monotrilho elétrico", "metrô elétrico", "transporte público elétrico", "veículo autônomo elétrico", "carro elétrico compacto", "carro elétrico sedã", "carro elétrico de luxo", "carro elétrico utilitário", "carro elétrico esportivo", "carro elétrico SUV", "carro elétrico hatch", "carro elétrico conversível", "carro elétrico perua", "carro elétrico off-road", "carro elétrico econômico", "carro elétrico urbano", "carro elétrico de alta performance", "ônibus elétrico urbano", "ônibus elétrico intermunicipal", "ônibus elétrico articulado", "ônibus elétrico biarticulado", "ônibus elétrico escolar", "ônibus elétrico executivo", "trem elétrico urbano", "trem elétrico regional", "trem elétrico intermunicipal", "trem elétrico de alta velocidade", "trem elétrico de baixa velocidade", "veículo híbrido urbano", "veículo híbrido intermunicipal", "carro híbrido urbano", "carro híbrido intermunicipal", "motocicleta elétrica urbana", "motocicleta elétrica esportiva", "van elétrica compacta", "van elétrica familiar", "micro-ônibus elétrico urbano", "caminhão elétrico de carga leve", "caminhão elétrico de carga pesada", "caminhão elétrico de distribuição", "scooter elétrica urbana", "scooter elétrica compacta", "triciclo elétrico urbano", "bonde elétrico moderno", "barco elétrico urbano", "ferry elétrico regional", "veículo solar urbano", "veículo solar intermunicipal", "carro solar urbano", "carro solar de luxo", "ônibus solar urbano", "ônibus solar intermunicipal", "trem solar regional", "veículo movido a hidrogênio urbano", "veículo movido a hidrogênio intermunicipal", "carro movido a hidrogênio urbano", "carro movido a hidrogênio de luxo", "ônibus movido a hidrogênio urbano", "trem movido a hidrogênio regional", "veículo híbrido plug-in urbano", "carro híbrido plug-in urbano", "ônibus híbrido plug-in urbano", "van híbrida plug-in urbana", "motocicleta híbrida urbana", "scooter híbrida urbana", "bicicleta elétrica dobrável", "bicicleta elétrica de montanha", "bicicleta elétrica de estrada", "bicicleta elétrica urbana", "bicicleta elétrica de carga", "bicicleta elétrica esportiva", "bicicleta elétrica compacta", "bicicleta elétrica infantil", "bicicleta elétrica tandem", "patinete elétrico compacto", "patinete elétrico de alta performance", "patinete elétrico urbano", "patinete elétrico off-road", "patinete elétrico para crianças", "carro compartilhado elétrico urbano", "carro compartilhado elétrico executivo", "van compartilhada elétrica urbana", "van compartilhada elétrica familiar", "micro-ônibus compartilhado elétrico urbano", "micro-ônibus compartilhado elétrico escolar", "trem leve elétrico urbano", "monotrilho elétrico urbano", "metrô elétrico moderno", "transporte público elétrico urbano", "veículo autônomo elétrico urbano", "carro elétrico com tecnologia autônoma", "ônibus elétrico com tecnologia autônoma", "trem elétrico autônomo", "veículo híbrido com tecnologia autônoma", "carro híbrido com tecnologia autônoma", "motocicleta elétrica autônoma", "van elétrica autônoma", "micro-ônibus elétrico autônomo", "caminhão elétrico autônomo", "scooter elétrica autônoma", "triciclo elétrico autônomo", "bonde elétrico autônomo", "veículo solar com tecnologia autônoma", "carro solar autônomo", "ônibus solar autônomo", "trem solar autônomo", "veículo movido a hidrogênio autônomo", "carro movido a hidrogênio autônomo", "ônibus movido a hidrogênio autônomo", "trem movido a hidrogênio autônomo", "veículo híbrido plug-in autônomo", "carro híbrido plug-in autônomo", "ônibus híbrido plug-in autônomo", "van híbrida plug-in autônoma", "motocicleta híbrida autônoma", "scooter híbrida autônoma", "bicicleta elétrica autônoma", "patinete elétrico autônomo", "carro elétrico com conectividade", "ônibus elétrico com conectividade", "trem elétrico com conectividade", "veículo híbrido com conectividade", "carro híbrido com conectividade", "motocicleta elétrica com conectividade", "van elétrica com conectividade", "micro-ônibus elétrico com conectividade", "caminhão elétrico com conectividade", "scooter elétrica com conectividade", "triciclo elétrico com conectividade", "bonde elétrico com conectividade", "veículo solar com conectividade", "carro solar com conectividade", "ônibus solar com conectividade", "trem solar com conectividade", "veículo movido a hidrogênio com conectividade", "carro movido a hidrogênio com conectividade", "ônibus movido a hidrogênio com conectividade", "trem movido a hidrogênio com conectividade", "veículo híbrido plug-in com conectividade", "carro híbrido plug-in com conectividade", "ônibus híbrido plug-in com conectividade", "van híbrida plug-in com conectividade", "motocicleta híbrida com conectividade", "scooter híbrida com conectividade", "bicicleta elétrica com conectividade", "patinete elétrico com conectividade", "transporte sustentável urbano", "transporte sustentável intermunicipal", "transporte sustentável regional", "mobilidade sustentável urbana", "mobilidade sustentável intermunicipal", "mobilidade sustentável regional", "veículo sustentável avançado", "carro sustentável avançado", "ônibus sustentável avançado", "trem sustentável avançado", "transporte sustentável autônomo", "veículo sustentável autônomo", "carro sustentável autônomo", "ônibus sustentável autônomo", "trem sustentável autônomo", "mobilidade sustentável autônoma", "sistema de transporte sustentável", "rede de transporte sustentável"],
                'transporte_baixo': ["ônibus urbano", "ônibus intermunicipal", "ônibus escolar", "ônibus executivo", "ônibus articulado", "ônibus biarticulado", "ônibus de turismo", "ônibus noturno", "ônibus de luxo", "ônibus de alta capacidade", "ônibus de baixa emissão", "metrô", "metrô leve", "metrô intermunicipal", "metrô urbano", "trem", "trem regional", "trem de alta velocidade", "trem de baixa velocidade", "trem metropolitano", "bonde", "bonde moderno", "bonde histórico", "VLT", "monotrilho", "trólebus", "trólebus urbano", "ferry urbano", "ferry intermunicipal", "barca", "barca elétrica", "carruagem elétrica", "van compartilhada", "micro-ônibus", "micro-ônibus elétrico", "trolebus articulado", "ônibus articulado elétrico", "ônibus biarticulado elétrico", "ônibus turístico elétrico", "trem elétrico", "metrô elétrico", "bonde elétrico", "VLT elétrico", "ônibus híbrido", "ônibus sustentável", "metrô sustentável", "trem sustentável", "bonde sustentável", "VLT sustentável", "ônibus a gás", "ônibus a diesel", "trem a diesel", "metrô a diesel", "ônibus híbrido elétrico", "ônibus com conectividade", "ônibus autônomo", "metrô autônomo", "trem autônomo", "bonde autônomo", "VLT autônomo", "ônibus com Wi-Fi", "metrô com Wi-Fi", "trem com Wi-Fi", "bonde com Wi-Fi", "VLT com Wi-Fi", "ônibus com ar-condicionado", "metrô climatizado", "trem climatizado", "bonde climatizado", "VLT climatizado", "ônibus acessível", "metrô acessível", "trem acessível", "bonde acessível", "VLT acessível", "ônibus para pessoas com deficiência", "metrô para pessoas com deficiência", "trem para pessoas com deficiência", "bonde para pessoas com deficiência", "VLT para pessoas com deficiência", "ônibus ecológico", "metrô ecológico", "trem ecológico", "bonde ecológico", "VLT ecológico", "ônibus de passageiros", "metrô de passageiros", "trem de passageiros", "bonde de passageiros", "VLT de passageiros", "ônibus urbano elétrico", "ônibus urbano híbrido", "metrô urbano elétrico", "metrô urbano híbrido", "trem urbano elétrico", "trem urbano híbrido", "bonde urbano elétrico", "bonde urbano híbrido", "VLT urbano elétrico", "VLT urbano híbrido", "ônibus intermunicipal elétrico", "ônibus intermunicipal híbrido", "metrô intermunicipal elétrico", "metrô intermunicipal híbrido", "trem intermunicipal elétrico", "trem intermunicipal híbrido", "bonde intermunicipal elétrico", "bonde intermunicipal híbrido", "VLT intermunicipal elétrico", "VLT intermunicipal híbrido", "ônibus noturno elétrico", "metrô noturno", "trem noturno", "bonde noturno", "VLT noturno", "ônibus executivo elétrico", "ônibus executivo híbrido", "metrô executivo", "trem executivo", "bonde executivo", "VLT executivo", "ônibus articulado sustentável", "ônibus biarticulado sustentável", "metrô articulado", "trem articulado", "bonde articulado", "VLT articulado", "ônibus escolar elétrico", "ônibus escolar híbrido", "metrô escolar", "trem escolar", "bonde escolar", "VLT escolar", "ônibus de turismo elétrico", "ônibus de turismo híbrido", "metrô de turismo", "trem de turismo", "bonde de turismo", "VLT de turismo", "ônibus a combustível alternativo", "metrô a combustível alternativo", "trem a combustível alternativo", "bonde a combustível alternativo", "VLT a combustível alternativo", "ônibus com tecnologia verde", "metrô com tecnologia verde", "trem com tecnologia verde", "bonde com tecnologia verde", "VLT com tecnologia verde", "ônibus de alta capacidade", "ônibus de grande porte", "metrô de alta capacidade", "trem de alta capacidade", "bonde de alta capacidade", "VLT de alta capacidade", "ônibus intermodal", "metrô intermodal", "trem intermodal", "bonde intermodal", "VLT intermodal", "ônibus urbano rápido", "metrô rápido", "trem rápido", "bonde rápido", "VLT rápido", "ônibus com tecnologia smart", "metrô smart", "trem smart", "bonde smart", "VLT smart", "ônibus com eficiência energética", "metrô com eficiência energética", "trem com eficiência energética", "bonde com eficiência energética", "VLT com eficiência energética", "ônibus de baixo impacto", "metrô de baixo impacto", "trem de baixo impacto", "bonde de baixo impacto", "VLT de baixo impacto", "ônibus econômico", "metrô econômico", "trem econômico", "bonde econômico", "VLT econômico", "ônibus de transporte coletivo", "metrô de transporte coletivo", "trem de transporte coletivo", "bonde de transporte coletivo", "VLT de transporte coletivo", "ônibus de sistema integrado", "metrô de sistema integrado", "trem de sistema integrado", "bonde de sistema integrado", "VLT de sistema integrado", "ônibus de mobilidade urbana", "metrô de mobilidade urbana", "trem de mobilidade urbana", "bonde de mobilidade urbana", "VLT de mobilidade urbana"],
                'transporte_poluente': ["carro", "iate", "moto", "caminhão", "carro a gasolina", "carro a diesel", "carro a etanol", "carro esportivo a gasolina", "carro sedan a gasolina", "carro hatch a gasolina", "carro compacto a gasolina", "carro de luxo a gasolina", "carro familiar a gasolina", "carro conversível a gasolina", "carro cupê a gasolina", "carro perua a diesel", "carro utilitário a diesel", "carro crossover a gasolina", "carro SUV a diesel", "carro off-road a diesel", "carro urbano a gasolina", "carro de corrida a gasolina", "carro antigo a gasolina", "carro esportivo a diesel", "carro sedan a diesel", "carro hatch a diesel", "carro compacto a diesel", "carro de luxo a diesel", "carro familiar a diesel", "carro conversível a diesel", "carro cupê a diesel", "carro perua a gasolina", "carro utilitário a gasolina", "carro crossover a diesel", "carro SUV a gasolina", "carro off-road a gasolina", "carro urbano a diesel", "carro de corrida a diesel", "carro antigo a diesel", "carro esportivo a etanol", "carro sedan a etanol", "carro hatch a etanol", "carro compacto a etanol", "carro de luxo a etanol", "carro familiar a etanol", "carro conversível a etanol", "carro cupê a etanol", "carro perua a etanol", "carro utilitário a etanol", "carro crossover a etanol", "carro SUV a etanol", "carro off-road a etanol", "carro urbano a etanol", "carro de corrida a etanol", "carro antigo a etanol", "moto a gasolina", "moto esportiva a gasolina", "moto scooter a gasolina", "moto custom a gasolina", "moto off-road a gasolina", "moto trail a gasolina", "moto street a gasolina", "moto naked a gasolina", "moto a etanol", "moto esportiva a etanol", "moto scooter a etanol", "moto custom a etanol", "moto off-road a etanol", "moto trail a etanol", "moto street a etanol", "moto naked a etanol", "moto esportiva modificada a gasolina", "moto de competição a gasolina", "moto de corrida a gasolina", "moto de baixa cilindrada a gasolina", "moto de média cilindrada a gasolina", "moto de alta cilindrada a gasolina", "moto esportiva modificada a etanol", "moto de competição a etanol", "moto de corrida a etanol", "moto de baixa cilindrada a etanol", "moto de média cilindrada a etanol", "moto de alta cilindrada a etanol", "caminhão a diesel", "caminhão articulado a diesel", "caminhão basculante a diesel", "caminhão de carga a diesel", "caminhão truck a diesel", "caminhão pesado a diesel", "caminhão leve a diesel", "caminhão rodoviário a diesel", "caminhão logístico a diesel", "caminhão frigorífico a diesel", "caminhão baú a diesel", "caminhão cegonheiro a diesel", "caminhão de lixo a diesel", "caminhão pipa a diesel", "caminhão de bombeiros a diesel", "caminhão tanque a diesel", "caminhão truck a gasolina", "caminhão articulado a gasolina", "caminhão basculante a gasolina", "caminhão de carga a gasolina", "caminhão pesado a gasolina", "caminhão leve a gasolina", "caminhão rodoviário a gasolina", "caminhão logístico a gasolina", "caminhão frigorífico a gasolina", "caminhão baú a gasolina", "caminhão cegonheiro a gasolina", "caminhão de lixo a gasolina", "caminhão pipa a gasolina", "caminhão de bombeiros a gasolina", "caminhão tanque a gasolina", "caminhão a etanol", "caminhão articulado a etanol", "caminhão basculante a etanol", "caminhão de carga a etanol", "caminhão truck a etanol", "caminhão pesado a etanol", "caminhão leve a etanol", "caminhão rodoviário a etanol", "caminhão logístico a etanol", "caminhão frigorífico a etanol", "caminhão baú a etanol", "caminhão cegonheiro a etanol", "caminhão de lixo a etanol", "caminhão pipa a etanol", "caminhão de bombeiros a etanol", "caminhão tanque a etanol", "ônibus a diesel", "ônibus urbano a diesel", "ônibus intermunicipal a diesel", "ônibus escolar a diesel", "ônibus executivo a diesel", "ônibus articulado a diesel", "ônibus biarticulado a diesel", "ônibus a gasolina", "ônibus urbano a gasolina", "ônibus intermunicipal a gasolina", "ônibus escolar a gasolina", "ônibus executivo a gasolina", "ônibus articulado a gasolina", "ônibus biarticulado a gasolina", "ônibus a etanol", "ônibus urbano a etanol", "ônibus intermunicipal a etanol", "ônibus escolar a etanol", "ônibus executivo a etanol", "ônibus articulado a etanol", "ônibus biarticulado a etanol", "van a gasolina", "van a diesel", "van a etanol", "pickup a gasolina", "pickup a diesel", "pickup a etanol", "minivan a gasolina", "minivan a diesel", "minivan a etanol", "jeep a gasolina", "jeep a diesel", "jeep a etanol", "sedã a gasolina", "sedã a diesel", "sedã a etanol", "cupê a gasolina", "cupê a diesel", "cupê a etanol", "perua a gasolina", "perua a diesel", "perua a etanol", "coupé a gasolina", "coupé a diesel", "coupé a etanol", "veículo de passeio a gasolina", "veículo de passeio a diesel", "veículo de passeio a etanol", "automóvel a gasolina", "automóvel a diesel", "automóvel a etanol", "transportadora a diesel", "transportadora a gasolina", "transportadora a etanol", "bugre a gasolina", "bugre a diesel", "bugre a etanol", "limusine a gasolina", "limusine a diesel", "limusine a etanol", "carreta a diesel", "carreta a gasolina", "carreta a etanol", "reboque a diesel", "reboque a gasolina", "reboque a etanol", "trator a diesel", "trator a gasolina", "trator a etanol", "maquinário pesado a diesel", "maquinário pesado a gasolina", "maquinário pesado a etanol", "equipamento de construção a diesel", "equipamento de construção a gasolina"]
            }

            transportes = []
            print("\n" + "─" * 78)
            print(" CATEGORIAS DE TRANSPORTE ".center(78, '─'))
            print("\t🟢 Meio Ambiente Agradece  🟡 Sustentável  🟠 Moderada  🔴 Poluente")
            print("─" * 78)

            # Loop para registrar transportes
            while True:
                transporte = input("\n► Transporte utilizado (deixe em branco para sair): ").lower().strip()
                if not transporte:
                    break

                categoria = None
                if transporte in transporte_categorias['transporte_eco']:
                    categoria = "🟢 Meio Ambiente Agradece"
                elif transporte in transporte_categorias['transporte_sustentavel']:
                    categoria = "🟡 Alta Sustentabilidade"
                elif transporte in transporte_categorias['transporte_baixo']:
                    categoria = "🟠 Moderada Sustentabilidade"
                elif transporte in transporte_categorias['transporte_poluente']:
                    categoria = "🔴 Baixa Sustentabilidade"
                else:
                    print("► Categoria não reconhecida! Use transporte listado.")
                    continue

                # Validação para a quantidade de viagens
                while True:
                    try:
                        vezes = float(input(f"► Quantidade de viagens com {transporte}: "))
                        break
                    except ValueError:
                        print("ERRO: Por favor, insira um número válido para a quantidade de viagens.")

                transportes.append((transporte, vezes, categoria))

            # Validação para resíduos não recicláveis
            while True:
                try:
                    residuos = float(input("\n► Resíduos não recicláveis (%): "))
                    break
                except ValueError:
                    print("ERRO: Por favor, insira um número válido para os resíduos não recicláveis.")

            limpar_tela()

            # Classificação dos dados
            classificacoes = {
                "agua": "🟢 Meio Ambiente Agradece" if agua < 100 else "🟡 Alta Sustentabilidade" if agua <= 150 else "🟠 Moderada Sustentabilidade" if agua <= 200 else "🔴 Baixa Sustentabilidade",
                "energia": "🟢 Meio Ambiente Agradece" if energia < 2.5 else "🟡 Alta Sustentabilidade" if energia <= 5 else "🟠 Moderada Sustentabilidade" if energia <= 10 else "🔴 Baixa Sustentabilidade",
                "residuos": "🟢 Meio Ambiente Agradece" if residuos < 20 else "🟡 Alta Sustentabilidade" if residuos <= 50 else "🟠 Moderada Sustentabilidade" if residuos <= 60 else "🔴 Baixa Sustentabilidade"
            }

            # Salvar os dados no arquivo JSON
            salvar_dados_json(usuario_logado, agua, energia, residuos, transportes, classificacoes, periodo)
            
            data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            print("\n╔" + "═" * 78 + "╗")
            print("║" + " DADOS REGISTRADOS ".center(78, '─') + "║")
            print(f"║ 📅 Data/hora: {data_hora}".ljust(79) + "║")
            print(f"║ 🌊 Água: {agua}L - {classificacoes['agua']}".ljust(79) + "║")
            print(f"║ 💡 Energia: {energia}kWh - {classificacoes['energia']}".ljust(79) + "║")
            # Exibe a classificação dos transportes
            if transportes:
                transportes_classificacao = ", ".join([f"{t[0]} ({t[2]})" for t in transportes])
                print(f"║ 🚦 Transportes registrados: {len(transportes)} - {transportes_classificacao}".ljust(79) + "║")
            else:
                print(f"║ 🚦 Transportes registrados: Nenhum".ljust(79) + "║")

            print(f"║ ♻️ Resíduos: {residuos}% - {classificacoes['residuos']}".ljust(79) + "║")
            print("╚" + "═" * 78 + "╝")
            input("\nPressione Enter para continuar...")
        
        elif choice == '2':
            limpar_tela()
            tela5_menu_de_opcoes_para_histórico.mostrar_menu(usuario_logado)

        elif choice == '3':
            limpar_tela()
            tela4_relatório_boas_práticas.main(usuario_logado)

        elif choice == '4':
            limpar_tela()
            import tela6_gráficos_verticais
            tela6_gráficos_verticais.menu_principal(usuario_logado)
        elif choice == '5':
            import tela7_tela_de_edicao_dados_user
            tela7_tela_de_edicao_dados_user.main(usuario_logado)
        elif choice == '6':
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main("Usuário")