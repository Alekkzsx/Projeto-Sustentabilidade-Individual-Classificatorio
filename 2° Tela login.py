import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QMessageBox, QFrame, QHBoxLayout,
                             QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

class PlaceholderLineEdit(QLineEdit):
    def __init__(self, placeholder, is_password=False):
        super().__init__()
        self.placeholder_text = placeholder
        self.is_password = is_password
        self.setAlignment(Qt.AlignCenter)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 12pt;
                border: 1px solid #ccc;
                border-radius: 5px;
                color: #808080;
            }
        """)
        
    def focusInEvent(self, event):
        if self.text() == self.placeholder_text:
            self.clear()
            self.setStyleSheet("""
                QLineEdit {
                    padding: 10px;
                    font-size: 12pt;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    color: black;
                }
            """)
            self.setAlignment(Qt.AlignLeft)
            if self.is_password:
                self.setEchoMode(QLineEdit.Password)
        super().focusInEvent(event)
        
    def focusOutEvent(self, event):
        if self.text() == "":
            self.setAlignment(Qt.AlignCenter)
            self.setStyleSheet("""
                QLineEdit {
                    padding: 10px;
                    font-size: 12pt;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    color: #808080;
                }
            """)
            self.setEchoMode(QLineEdit.Normal)
            self.setText(self.placeholder_text)
        super().focusOutEvent(event)

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
        
        # Campos de entrada
        self.username = PlaceholderLineEdit("Nome de Usuário")
        self.password = PlaceholderLineEdit("Senha", is_password=True)
        
        # Botões
        btn_cadastrar = QPushButton('FAÇA SEU CADASTRO')
        btn_cadastrar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 10pt;
            }
        """)
        btn_cadastrar.clicked.connect(self.redirecionar_cadastro)
        
        btn_acessar = QPushButton('ACESSAR')
        btn_acessar.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px 30px;
                border-radius: 5px;
                font-size: 10pt;
            }
        """)
        btn_acessar.clicked.connect(self.validar_login)
        
        # Link de recuperação
        link_senha = QLabel('Esqueceu sua senha? <a href="#" style="color: blue; text-decoration: none;">Clique Aqui</a>')
        link_senha.setOpenExternalLinks(False)
        link_senha.linkActivated.connect(self.esqueceu_senha)
        link_senha.setCursor(QCursor(Qt.PointingHandCursor))
        
        # Layout
        frame = QFrame()
        frame_layout = QVBoxLayout(frame)
        frame_layout.setSpacing(20)
        frame_layout.setContentsMargins(20, 20, 20, 20)
        
        frame_layout.addWidget(self.username)
        frame_layout.addWidget(self.password)
        frame_layout.addWidget(link_senha, alignment=Qt.AlignCenter)
        
        btn_frame = QFrame()
        btn_layout = QHBoxLayout(btn_frame)
        btn_layout.setSpacing(10)
        btn_layout.addWidget(btn_cadastrar)
        btn_layout.addWidget(btn_acessar)
        
        frame_layout.addWidget(btn_frame)
        layout.addWidget(frame)
        self.setLayout(layout)
        
    def validar_login(self):
        usuario = self.username.text()
        senha = self.password.text()
        
        if usuario == "Nome de Usuário" or senha == "Senha" or not usuario or not senha:
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