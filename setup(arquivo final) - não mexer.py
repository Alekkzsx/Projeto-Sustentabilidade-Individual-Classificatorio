import tela1_login
import tela3_tela_de_trabalho

def main():
    usuario_logado = tela1_login.executar_fluxo_login()
    
    # Correção 1: Verificação correta do retorno
    if usuario_logado:  # Remove a comparação com "True"
        # Correção 2: Usar a variável correta
        tela3_tela_de_trabalho.main(usuario_logado)  # "usuario_logado" em vez de "usuario_correto"

if __name__ == "__main__":
    main()