from colorama import Fore, Back, Style, init
import os

# Inicializa o colorama e configura auto-reset
init(autoreset=True)

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Exibe o menu principal de opções com formatação estilizada"""
    limpar_tela()
    print(f"\n{Fore.CYAN}╔{'═'*25}╗")
    print(f"║{Fore.YELLOW}      MENU PRINCIPAL      {Fore.CYAN}║")
    print(f"╠{'═'*25}╣")
    print(f"║ {Fore.WHITE}1. Relatórios Semanais   {Fore.CYAN}║")
    print(f"║ {Fore.WHITE}2. Revisar Informações    {Fore.CYAN}║")
    print(f"║ {Fore.WHITE}3. Configurações         {Fore.CYAN}║")
    print(f"║ {Fore.WHITE}4. Logout                {Fore.CYAN}║")
    print(f"║ {Fore.WHITE}5. Sair do Programa      {Fore.CYAN}║")
    print(f"╚{'═'*25}╝{Style.RESET_ALL}")

def cabecalho(titulo):
    """Cria um cabeçalho estilizado"""
    print(f"\n{Fore.GREEN}┌{'─'*40}┐")
    print(f"│{Style.BRIGHT}{titulo:^40}{Style.NORMAL}{Fore.GREEN}│")
    print(f"└{'─'*40}┘{Style.RESET_ALL}")

def relatorio_semanal(dados):
    """Exibe o relatório semanal com formatação tabelada"""
    cabecalho("RELATÓRIO SEMANAL")
    print(f"{Fore.BLUE}► {Fore.WHITE}Consumo de Água: {Fore.GREEN}{dados['consumo_agua']} litros")
    print(f"{Fore.BLUE}► {Fore.WHITE}Consumo de Energia: {Fore.GREEN}{dados['consumo_energia']} kWh")
    print(f"{Fore.BLUE}► {Fore.WHITE}Uso de Transporte: {Fore.GREEN}{dados['uso_transporte']}%")
    print(f"{Fore.BLUE}► {Fore.WHITE}Resíduos Não Recicláveis: {Fore.GREEN}{dados['residuos_nao_reciclaveis']}%")
    input(f"\n{Fore.YELLOW}Pressione Enter para continuar...")

def revisar_informacoes(dados):
    """Interface de revisão com highlights"""
    while True:
        cabecalho("REVISAR INFORMAÇÕES")
        print(f"{Fore.MAGENTA}[1]{Fore.WHITE} Água: {Fore.CYAN}{dados['consumo_agua']}L")
        print(f"{Fore.MAGENTA}[2]{Fore.WHITE} Energia: {Fore.CYAN}{dados['consumo_energia']}kWh")
        print(f"{Fore.MAGENTA}[3]{Fore.WHITE} Transporte: {Fore.CYAN}{dados['uso_transporte']}%")
        print(f"{Fore.MAGENTA}[4]{Fore.WHITE} Resíduos: {Fore.CYAN}{dados['residuos_nao_reciclaveis']}%")
        print(f"{Fore.MAGENTA}[5]{Fore.WHITE} Voltar ao Menu Principal\n")
        
        opcao = input(f"{Fore.YELLOW}❯❯ {Fore.WHITE}Escolha uma opção (1-5): ")

        if opcao == '5':
            break
        try:
            if opcao in ['1','2','3','4']:
                novos_dados = {
                    '1': ('consumo de água (litros)', 'consumo_agua'),
                    '2': ('consumo de energia (kWh)', 'consumo_energia'),
                    '3': ('uso de transporte (%)', 'uso_transporte'),
                    '4': ('resíduos não recicláveis (%)', 'residuos_nao_reciclaveis')
                }
                prompt = f"{Fore.GREEN}►► {Fore.WHITE}Novo valor para {novos_dados[opcao][0]}: "
                dados[novos_dados[opcao][1]] = float(input(prompt))
                print(f"{Fore.GREEN}✓ Valor atualizado com sucesso!")
            else:
                print(f"{Fore.RED}⚠ Opção inválida!")
        except ValueError:
            print(f"{Fore.RED}⚠ Erro! Insira um valor numérico válido.")
        input(f"{Fore.YELLOW}Pressione Enter para continuar...")

def configuracoes():
    """Configurações com visual melhorado"""
    cabecalho("CONFIGURAÇÕES")
    print(f"{Fore.BLUE}⚙ {Fore.WHITE}Esta funcionalidade está em desenvolvimento")
    print(f"{Fore.BLUE}⚙ {Fore.WHITE}Previsão de lançamento: versão 2.0\n")
    input(f"{Fore.YELLOW}Pressione Enter para continuar...")

def logout():
    """Logout com efeito visual"""
    print(f"\n{Fore.YELLOW}⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋")
    print(f"{Fore.CYAN}       Sessão encerrada com sucesso!")
    print(f"{Fore.YELLOW}⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋⎋{Style.RESET_ALL}\n")
    input(f"{Fore.YELLOW}Pressione Enter para sair...")

def main():
    """Função principal com tratamento visual"""
    dados = {
        'consumo_agua': 150.0,
        'consumo_energia': 85.5,
        'uso_transporte': 30.0,
        'residuos_nao_reciclaveis': 15.0
    }

    while True:
        mostrar_menu()
        opcao = input(f"\n{Fore.YELLOW}❯ {Fore.WHITE}Digite sua opção (1-5): ")

        if opcao == '1':
            relatorio_semanal(dados)
        elif opcao == '2':
            revisar_informacoes(dados)
        elif opcao == '3':
            tela de trabalho()
        elif opcao == '4':
            logout()
            break
        elif opcao == '5':
            print(f"\n{Fore.RED}✖ {Fore.WHITE}Encerrando programa...")
            print(f"{Fore.BLUE}👋 Até logo!\n{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}⚠ Opção inválida! Tente novamente.")
            input(f"{Fore.YELLOW}Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
