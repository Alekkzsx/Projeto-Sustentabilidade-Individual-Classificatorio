#Arquivo SETUP.EXE
from tela1_login import limpar_tela
import tela1_login
import tela2_registro
import tela3_tela_de_trabalho

def main():
    while True:
        # Tela de Login/Cadastro
        usuario_logado = tela1_login.executar_fluxo_login()
        
        if usuario_logado:
            # Tela de Trabalho após login bem-sucedido
            tela3_tela_de_trabalho.main(usuario_logado)

if __name__ == "__main__":
    main()