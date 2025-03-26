import datetime

def main():
    print("="*80)
    print("                       BEM-VINDO", "*nome*!")
    print("                     O QUE GOSTARIA DE VER?                ")
    print("="*80)
    print("CONSUMO DE ÁGUA (EM LITROS):________________________")
    print("CONSUMO DE ENERGIA (EM KWh):________________________")
    print("VEZES QUE UTILIZOU TRANSPORTE PRIVADO:________________________")
    print("GERAÇÃO DE RESÍDUOS NÃO RECICLAVEIS (EM %):________________________")
    print("="*80)
    print("[1] DATA E HORA")
    print("[2] CADASTRAR")   
    print("="*80)
    
    while True:
        choice = input("Escolha uma opção: ")
        if choice == '1':
            print("Data e Hora do sistema: ", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            break
        elif choice == '2':
            while True:
                try:
                    agua = float(input("CONSUMO DE ÁGUA (EM LITROS): "))
                    energia = float(input("CONSUMO DE ENERGIA (EM KWh): "))
                    
                    transporte_meio_ambiente_agradece = [
                        "bicicleta", "BICICLETA", "Bicicleta",
                        "a pé", "A PÉ", "A pé", "a pe", "A PE", "A pe",
                        "patinete", "PATINETE", "Patinete",
                        "skate", "SKATE", "Skate"
                    ]
                    
                    transporte_sustentavel = [
                        "ônibus", "ÔNIBUS", "Onibus", "ONIBUS", "onibus",
                        "metrô", "METRÔ", "Metro", "METRO", "metro",
                        "trem", "TREM", "Trem",
                        "carro elétrico", "CARRO ELÉTRICO", "Carro Eletrico", "CARRO ELETRICO", "carro eletrico",
                        "carro híbrido", "CARRO HÍBRIDO", "Carro Hibrido", "CARRO HIBRIDO", "carro hibrido",
                        "uber", "UBER", "Uber",
                        "lyft", "LYFT", "Lyft",
                        "carona", "CARONA", "Carona"
                    ]
                    
                    transporte_baixo_nivel_sustentabilidade = [
                        "bicicleta elétrica", "BICICLETA ELÉTRICA", "Bicicleta Eletrica", "BICICLETA ELETRICA", "bicicleta eletrica",
                        "bicicleta compartilhada", "BICICLETA COMPARTILHADA", "Bicicleta Compartilhada",
                        "bicicleta dobrável", "BICICLETA DOBRÁVEL", "Bicicleta Dobrável", "BICICLETA DOBRAVEL", "bicicleta dobravel",
                        "bicicleta de carga", "BICICLETA DE CARGA", "Bicicleta de Carga",
                        "bicicleta tandem", "BICICLETA TANDEM", "Bicicleta Tandem",
                        "patins", "PATINS", "Patins",
                        "patins elétrico", "PATINS ELÉTRICO", "Patins Eletrico", "PATINS ELETRICO", "patins eletrico",
                        "monociclo", "MONOCICLO", "Monociclo",
                        "monociclo elétrico", "MONOCICLO ELÉTRICO", "Monociclo Eletrico", "MONOCICLO ELETRICO", "monociclo eletrico",
                        "triciclo elétrico", "TRICICLO ELÉTRICO", "Triciclo Eletrico", "TRICICLO ELETRICO", "triciclo eletrico",
                        "quadriciclo elétrico", "QUADRICICLO ELÉTRICO", "Quadriciclo Eletrico", "QUADRICICLO ELETRICO", "quadriciclo eletrico",
                        "scooter elétrica", "SCOOTER ELÉTRICA", "Scooter Eletrica", "SCOOTER ELETRICA", "scooter eletrica",
                        "moto elétrica", "MOTO ELÉTRICA", "Moto Eletrica", "MOTO ELETRICA", "moto eletrica"
                    ]
                    
                    transporte_desperdicio = [
                        "carro", "CARRO", "Carro",
                        "moto", "MOTO", "Moto",
                        "avião", "AVIÃO", "Aviao", "AVIAO", "aviao",
                        "barco", "BARCO", "Barco",
                        "navio", "NAVIO", "Navio",
                        "helicóptero", "HELICÓPTERO", "Helicoptero", "HELICOPTERO", "helicoptero",
                        "balão", "BALÃO", "Balao", "BALAO", "balao",
                        "segway", "SEGWAY", "Segway",
                        "hoverboard", "HOVERBOARD", "Hoverboard",
                        "carroça", "CARROÇA", "Carroca", "CARROCA", "carroca",
                        "carruagem", "CARRUAGEM", "Carruagem",
                        "caminhão", "CAMINHÃO", "Caminhao", "CAMINHAO", "caminhao",
                        "van", "VAN", "Van",
                        "micro-ônibus", "MICRO-ÔNIBUS", "Micro-Onibus", "MICRO-ONIBUS", "micro-onibus",
                        "táxi", "TÁXI", "Taxi", "TAXI", "taxi",
                        "carro a gás", "CARRO A GÁS", "Carro a Gas", "CARRO A GAS", "carro a gas",
                        "carro a diesel", "CARRO A DIESEL", "Carro a Diesel", "carro a diesel",
                        "carro a etanol", "CARRO A ETANOL", "Carro a Etanol", "carro a etanol",
                        "carro a hidrogênio", "CARRO A HIDROGÊNIO", "Carro a Hidrogenio", "CARRO A HIDROGENIO", "carro a hidrogenio",
                        "moto a gasolina", "MOTO A GASOLINA", "Moto a Gasolina",
                        "moto a diesel", "MOTO A DIESEL", "Moto a Diesel",
                        "moto a etanol", "MOTO A ETANOL", "Moto a Etanol",
                        "moto a hidrogênio", "MOTO A HIDROGÊNIO", "Moto a Hidrogenio", "MOTO A HIDROGENIO", "moto a hidrogenio",
                        "moto de carga", "MOTO DE CARGA", "Moto de Carga",
                        "moto de corrida", "MOTO DE CORRIDA", "Moto de Corrida",
                        "moto de trilha", "MOTO DE TRILHA", "Moto de Trilha",
                        "moto de passeio", "MOTO DE PASSEIO", "Moto de Passeio",
                        "moto de turismo", "MOTO DE TURISMO", "Moto de Turismo",
                        "moto de aventura", "MOTO DE AVENTURA", "Moto de Aventura",
                        "moto de enduro", "MOTO DE ENDURO", "Moto de Enduro",
                        "moto de motocross", "MOTO DE MOTOCROSS", "Moto de Motocross",
                        "moto de trial", "MOTO DE TRIAL", "Moto de Trial",
                        "moto de velocidade", "MOTO DE VELOCIDADE", "Moto de Velocidade",
                        "moto de estrada", "MOTO DE ESTRADA", "Moto de Estrada",
                        "moto de cidade", "MOTO DE CIDADE", "Moto de Cidade",
                        "moto de trabalho", "MOTO DE TRABALHO", "Moto de Trabalho",
                        "moto de luxo", "MOTO DE LUXO", "Moto de Luxo",
                        "moto de custom", "MOTO DE CUSTOM", "Moto de Custom",
                        "moto de chopper", "MOTO DE CHOPPER", "Moto de Chopper",
                        "moto de cruiser", "MOTO DE CRUISER", "Moto de Cruiser",
                        "moto de naked", "MOTO DE NAKED", "Moto de Naked",
                        "moto de sport", "MOTO DE SPORT", "Moto de Sport",
                        "moto de touring", "MOTO DE TOURING", "Moto de Touring",
                        "moto de dual-sport", "MOTO DE DUAL-SPORT", "Moto de Dual-Sport",
                        "moto de supermoto", "MOTO DE SUPERMOTO", "Moto de Supermoto",
                        "moto de café racer", "MOTO DE CAFÉ RACER", "Moto de Café Racer", "MOTO DE CAFE RACER", "Moto de Cafe Racer",
                        "moto de bobber", "MOTO DE BOBBER", "Moto de Bobber",
                        "moto de scrambler", "MOTO DE SCRAMBLER", "Moto de Scrambler",
                        "moto de tracker", "MOTO DE TRACKER", "Moto de Tracker",
                        "moto de flat track", "MOTO DE FLAT TRACK", "Moto de Flat Track",
                        "moto de dirt bike", "MOTO DE DIRT BIKE", "Moto de Dirt Bike",
                        "moto de pit bike", "MOTO DE PIT BIKE", "Moto de Pit Bike",
                        "moto de pocket bike", "MOTO DE POCKET BIKE", "Moto de Pocket Bike",
                        "moto de mini bike", "MOTO DE MINI BIKE", "Moto de Mini Bike",
                        "moto de maxi scooter", "MOTO DE MAXI SCOOTER", "Moto de Maxi Scooter",
                        "moto de scooter", "MOTO DE SCOOTER", "Moto de Scooter",
                        "moto de vespa", "MOTO DE VESPA", "Moto de Vespa",
                        "moto de lambreta", "MOTO DE LAMBRETA", "Moto de Lambreta",
                        "moto de ciclomotor", "MOTO DE CICLOMOTOR", "Moto de Ciclomotor",
                        "moto de motoneta", "MOTO DE MOTONETA", "Moto de Motoneta",
                        "moto de quadriciclo", "MOTO DE QUADRICICLO", "Moto de Quadriciclo",
                        "moto de triciclo", "MOTO DE TRICICLO", "Moto de Triciclo",
                        "moto de sidecar", "MOTO DE SIDECAR", "Moto de Sidecar",
                        "moto de quadriciclo esportivo", "MOTO DE QUADRICICLO ESPORTIVO", "Moto de Quadriciclo Esportivo",
                        "moto de quadriciclo utilitário", "MOTO DE QUADRICICLO UTILITÁRIO", "Moto de Quadriciclo Utilitário", "MOTO DE QUADRICICLO UTILITARIO", "Moto de Quadriciclo Utilitario",
                        "moto de quadriciclo recreativo", "MOTO DE QUADRICICLO RECREATIVO", "Moto de Quadriciclo Recreativo",
                        "moto de quadriciclo infantil", "MOTO DE QUADRICICLO INFANTIL", "Moto de Quadriciclo Infantil",
                        "moto de quadriciclo adulto", "MOTO DE QUADRICICLO ADULTO", "Moto de Quadriciclo Adulto",
                        "moto de quadriciclo profissional", "MOTO DE QUADRICICLO PROFISSIONAL", "Moto de Quadriciclo Profissional"
                    ]
                    
                    transportes = []
                    while True:
                        transporte = input("TIPO DE TRANSPORTE UTILIZADO (carro, bicicleta, ônibus, etc.): ").lower()
                        categoria = None
                        if transporte in transporte_meio_ambiente_agradece:
                            categoria = "Meio ambiente agradece (alta sustentabilidade)"
                        elif transporte in transporte_sustentavel:
                            categoria = "Sustentabilidade"
                        elif transporte in transporte_baixo_nivel_sustentabilidade:
                            categoria = "Baixo nível de sustentabilidade"
                        elif transporte in transporte_desperdicio:
                            categoria = "Desperdício"
                        else:
                            print("Opção de transporte inválida. Tente novamente.")
                            continue
                        
                        vezes_transporte = int(input(f"QUANTIDADE DE VEZES QUE UTILIZOU {transporte.upper()}: "))
                        transportes.append((transporte, vezes_transporte, categoria))
                        
                        mais_transporte = input("Deseja adicionar outro tipo de transporte? (s/n): ").lower()
                        if mais_transporte != 's':
                            break
                    
                    residuos = float(input("GERAÇÃO DE RESÍDUOS NÃO RECICLAVEIS (EM %): "))
                    print("Registrando...")
                    # Aqui você pode adicionar código para salvar os dados em um arquivo ou banco de dados
                    print(f"Água: {agua} litros, Energia: {energia} KWh, Transportes: {transportes}, Resíduos: {residuos}%")
                    break  # Sai do loop se todos os dados forem válidos
                except ValueError:
                    print("\n                  ERROR!!          ")
                    print("OS DADOS INSERIDOS DEVEM SER VALORES NUMERICOS")
                    print("              TENTE NOVAMENTE       ")
                    print("  ") 
            break  # Sai do loop principal após o registro dos dados
        else:
            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()
