import tela1_login
import tela3_tela_de_trabalho

def main():
    usuario_logado = tela1_login.executar_fluxo_login()
    
    if usuario_logado:
        tela3_tela_de_trabalho.main(usuario_logado)
# Main
if __name__ == "__main__":
    main()
