import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QLabel, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

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
        
        # Título "Nome de Usuário"
        lbl_usuario = QLabel("Nome de Usuário")
        lbl_usuario.setFont(QFont("Arial", 14, QFont.Bold))
        lbl_usuario.setStyleSheet("color: #333; margin-bottom: 8px;")
        
        # Campo de entrada para o nome de usuário
        self.txt_usuario = QLineEdit()
        self.txt_usuario.setStyleSheet("""
            QLineEdit {
                padding: 16px;
                font-size: 18px;
                border: 2px solid #ddd;
                border-radius: 20px;
                margin: 12px 0;
            }
        """)
        
        # Título "Senha"
        lbl_senha = QLabel("Senha")
        lbl_senha.setFont(QFont("Arial", 14, QFont.Bold))
        lbl_senha.setStyleSheet("color: #333; margin-bottom: 8px; margin-top: 20px;")
        
        # Campo de entrada para a senha
        self.txt_senha = QLineEdit()
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setStyleSheet("""
            QLineEdit {
                padding: 16px;
                font-size: 18px;
                border: 2px solid #ddd;
                border-radius: 20px;
                margin: 12px 0;
            }
        """)
        
        # Link "Esqueceu sua senha? Clique Aqui"
        link_senha = QLabel('<a href="#" style="color: #2196F3; text-decoration: none; font-size: 14px;">Esqueceu sua senha? Clique Aqui</a>')
        link_senha.setAlignment(Qt.AlignCenter)
        link_senha.setOpenExternalLinks(False)
        
        # Botões
        btn_cadastrar = QPushButton('FAÇA SEU CADASTRO')
        btn_acessar = QPushButton('ACESSAR')
        
        # Estilo dos botões
        btn_style = """
            QPushButton {
                padding: 16px;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                color: white;
            }
            QPushButton:hover {
                opacity: 0.9;
            }
        """
        btn_cadastrar.setStyleSheet(btn_style + "background-color: #4CAF50;")
        btn_acessar.setStyleSheet(btn_style + "background-color: #2196F3;")
        
        # Layout dos botões
        btn_container = QHBoxLayout()
        btn_container.setSpacing(20)
        btn_container.addWidget(btn_cadastrar)
        btn_container.addWidget(btn_acessar)
        
        # Adicionar elementos ao layout
        layout.addWidget(lbl_usuario)
        layout.addWidget(self.txt_usuario)
        layout.addWidget(lbl_senha)
        layout.addWidget(self.txt_senha)
        layout.addWidget(link_senha)
        layout.addLayout(btn_container)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())