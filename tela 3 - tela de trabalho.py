import datetime

def main():
    print("="*80)
    print("                       BEM-VINDO","*nome*!")
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
        if choice=='1':
            print("Data e Hora: ", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            break
        elif choice=='2':
            agua = input("CONSUMO DE ÁGUA (EM LITROS): ")
            energia = input("CONSUMO DE ENERGIA (EM KWh): ")
            transporte = input("VEZES QUE UTILIZOU TRANSPORTE PRIVADO: ")
            residuos = input("GERAÇÃO DE RESÍDUOS NÃO RECICLAVEIS (EM %): ")
            print("Registrando...")
            # Aqui você pode adicionar código para salvar os dados em um arquivo ou banco de dados
            break
        else:
            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()
