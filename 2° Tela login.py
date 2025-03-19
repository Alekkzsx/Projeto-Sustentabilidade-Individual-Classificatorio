import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QMessageBox, QFrame, QHBoxLayout,
                             QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Sistema de Login')
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color: white;")
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # Frame principal
        frame = QFrame()
        frame_layout = QVBoxLayout(frame)
        frame_layout.setSpacing(20)
        frame_layout.setContentsMargins(40, 40, 40, 40)

        # Campos de entrada
        self.txt_usuario = QLineEdit()
        self.txt_senha = QLineEdit()
        self.txt_senha.setEchoMode(QLineEdit.Password)

        # Estilização dos campos
        campo_style = """
            QLineEdit {
                padding: 16px;
                font-size: 18px;
                border: 2px solid #ddd;
                border-radius: 20px;
                margin: 12px 0;
            }
        """
        self.txt_usuario.setStyleSheet(campo_style)
        self.txt_senha.setStyleSheet(campo_style)
        self.txt_usuario.setPlaceholderText("Nome de Usuário")
        self.txt_senha.setPlaceholderText("Senha")

        # Link de recuperação
        link_senha = QLabel('Esqueceu sua senha? <a href="#" style="color: blue; text-decoration: none; font-size: 12px;">Clique Aqui</a>')
        link_senha.setOpenExternalLinks(False)
        link_senha.linkActivated.connect(self.esqueceu_senha)
        link_senha.setCursor(QCursor(Qt.PointingHandCursor))

        # Botões
        btn_cadastrar = QPushButton('FAÇA SEU CADASTRO')
        btn_acessar = QPushButton('ACESSAR')

        # Estilo dos botões
        btn_style = """
            QPushButton {{
                padding: 15px 30px;
                border-radius: 8px;
                font-weight: bold;
                font-size: 16px;
                min-width: 180px;
                {0}
            }}
            QPushButton:hover {{
                {1}
            }}
        """

        estilo_cadastro = btn_style.format(
            "background-color: #4CAF50; color: white;",
            "background-color: #45a049;"
        )

        estilo_acesso = btn_style.format(
            "background-color: #2196F3; color: white;",
            "background-color: #1976D2;"
        )

        btn_cadastrar.setStyleSheet(estilo_cadastro)
        btn_acessar.setStyleSheet(estilo_acesso)

        # Layout dos botões
        btn_container = QHBoxLayout()
        btn_container.setSpacing(20)
        btn_container.addWidget(btn_cadastrar)
        btn_container.addWidget(btn_acessar)

        # Adicionar elementos
        
        frame_layout.addWidget(self.txt_usuario)
        frame_layout.addWidget(self.txt_senha)
        frame_layout.addWidget(link_senha, alignment=Qt.AlignCenter)
        frame_layout.addLayout(btn_container)

        # Conectar eventos
        btn_cadastrar.clicked.connect(self.redirecionar_cadastro)
        btn_acessar.clicked.connect(self.validar_login)

        layout.addWidget(frame)
        self.setLayout(layout)

    def validar_login(self):
        usuario = self.txt_usuario.text().strip()
        senha = self.txt_senha.text().strip()
        
        if not usuario or not senha:
            QMessageBox.critical(self, 'Erro', 'Preencha todos os campos!')
        else:
            QMessageBox.information(self, 'Sucesso', 'Login realizado!')
            
    def esqueceu_senha(self):
        QMessageBox.information(self, 'Recuperação', 'Entre em contato com o suporte')
        
    def redirecionar_cadastro(self):
        QMessageBox.information(self, 'Cadastro', 'Redirecionando...')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())