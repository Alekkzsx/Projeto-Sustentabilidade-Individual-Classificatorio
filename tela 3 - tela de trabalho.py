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
                    
                    
                    wefewf
                    
                    transporte_opcoes = [
                        "carro", "bicicleta", "ônibus", "moto", "a pé", "trem", "metrô", "avião", "barco", "navio",
                        "patinete", "skate", "triciclo", "quadriciclo", "helicóptero", "balão", "segway", "hoverboard",
                        "carroça", "carruagem", "caminhão", "van", "micro-ônibus", "táxi", "uber", "lyft", "carona",
                        "carro elétrico", "carro híbrido", "carro a gás", "carro a diesel", "carro a etanol", "carro a hidrogênio",
                        "bicicleta elétrica", "bicicleta compartilhada", "bicicleta dobrável", "bicicleta de carga", "bicicleta tandem",
                        "patins", "patins elétrico", "monociclo", "monociclo elétrico", "triciclo elétrico", "quadriciclo elétrico",
                        "scooter", "scooter elétrica", "moto elétrica", "moto a gasolina", "moto a diesel", "moto a etanol",
                        "moto a hidrogênio", "moto compartilhada", "moto de carga", "moto de corrida", "moto de trilha",
                        "moto de passeio", "moto de turismo", "moto de aventura", "moto de enduro", "moto de motocross",
                        "moto de trial", "moto de velocidade", "moto de estrada", "moto de cidade", "moto de trabalho",
                        "moto de luxo", "moto de custom", "moto de chopper", "moto de cruiser", "moto de naked",
                        "moto de sport", "moto de touring", "moto de dual-sport", "moto de supermoto", "moto de café racer",
                        "moto de bobber", "moto de scrambler", "moto de tracker", "moto de flat track", "moto de dirt bike",
                        "moto de pit bike", "moto de pocket bike", "moto de mini bike", "moto de maxi scooter", "moto de scooter",
                        "moto de vespa", "moto de lambreta", "moto de ciclomotor", "moto de motoneta", "moto de quadriciclo",
                        "moto de triciclo", "moto de sidecar", "moto de quadriciclo esportivo", "moto de quadriciclo utilitário",
                        "moto de quadriciclo recreativo", "moto de quadriciclo infantil", "moto de quadriciclo adulto", "moto de quadriciclo profissional"
                    ]
                    
                    transporte = input("VEZES QUE UTILIZOU TRANSPORTE PRIVADO (carro, bicicleta, ônibus, etc.): ").lower()
                    if transporte not in transporte_opcoes:
                        print("Opção de transporte inválida. Tente novamente.")
                        continue
                    
                    residuos = float(input("GERAÇÃO DE RESÍDUOS NÃO RECICLAVEIS (EM %): "))
                    print("Registrando...")
                    # Aqui você pode adicionar código para salvar os dados em um arquivo ou banco de dados
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
