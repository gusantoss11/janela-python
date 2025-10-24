import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,QCheckBox, QHBoxLayout, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize


class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()

        # ======= Configurações básicas =======
        self.setWindowTitle("Welcome to email")
        self.setGeometry(800, 100, 400, 500)
        self.setFixedHeight(500)
        self.setWindowIcon(QIcon("icone.png"))  # opcional

        # ======= Layout principal =======
        self.meio_da_tela = QVBoxLayout()
        self.meio_da_tela.setAlignment(Qt.AlignCenter)

        # ======= Título =======
        self.titulo = QLabel("Bem-vindo ao email")
        self.titulo.setFont(QFont("Arial", 18, QFont.Bold))
        self.titulo.setAlignment(Qt.AlignCenter)

        self.subtitulo = QLabel("Por favor, faça login na sua conta")
        self.subtitulo.setFont(QFont("Arial", 10))
        self.subtitulo.setAlignment(Qt.AlignCenter)

        self.meio_da_tela.addWidget(self.titulo)
        self.meio_da_tela.addWidget(self.subtitulo)

        # ======= Campo de e-mail =======
        self.lbl_email = QLabel("Email ou Endereço")
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("johndoe@gmail.com")
        self.input_email.setFixedHeight(40)

        # ======= Campo de senha =======
        self.lbl_senha = QLabel("Senha")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.input_senha.setFixedHeight(40)

        # ======= Check e link =======
        self.checkbox = QCheckBox("Relembre-me")
        self.esqueci = QLabel('<a href="#">Esqueceu sua senha?</a>')
        self.esqueci.setTextFormat(Qt.RichText)
        self.esqueci.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.esqueci.setOpenExternalLinks(False)
        self.esqueci.setAlignment(Qt.AlignRight)
        self.esqueci.linkActivated.connect(self.recuperar_senha)

        self.linha_check = QHBoxLayout()
        self.linha_check.addWidget(self.checkbox)
        self.linha_check.addWidget(self.esqueci)

        # ======= Botão de login =======
        self.btn_login = QPushButton("Conecte-se")
        self.btn_login.setStyleSheet(
            "background-color: #2b9bd7; color: white; font-weight: bold; height: 35px; border-radius: 5px;"
        )
        self.btn_login.clicked.connect(self.login)

        # ======= Criar conta =======
        self.criar = QLabel('Novo usuário? <a href="#">Crie uma conta</a>')
        self.criar.setAlignment(Qt.AlignCenter)
        self.criar.setTextFormat(Qt.RichText)
        self.criar.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.criar.setOpenExternalLinks(False)
        self.criar.linkActivated.connect(self.criar_conta)

        # ======= OU =======
        self.ou = QLabel("──────────────  OR  ──────────────")
        self.ou.setAlignment(Qt.AlignCenter)
        self.ou.setStyleSheet("color: gray;")

        # ======= Botões sociais =======
        self.botão_label = QPushButton("Entrar com Facebook")
        self.botão_label.setIcon(QIcon("facebook.png"))   # ÍCONE DO FACEBOOK
        self.botão_label.setIconSize(QSize(20, 20))
        self.botão_label.setStyleSheet("background-color: #3b5998; color: white; height: 35px; border-radius: 5px;")
        self.botão_label.clicked.connect(self.login_facebook)

        self.botão_label_google = QPushButton("Entrar com Google")
        self.botão_label_google.setIcon(QIcon("google.png"))  # ÍCONE DO GOOGLE
        self.botão_label_google.setIconSize(QSize(20, 20))
        self.botão_label_google.setStyleSheet(
            "background-color: #db4437; color: white; height: 35px; border-radius: 5px;"
        )
        self.botão_label_google.clicked.connect(self.login_google)

        self.linha_social = QHBoxLayout()
        self.linha_social.addWidget(self.botão_label)
        self.linha_social.addWidget(self.botão_label_google)

        # ======= Montagem =======
        self.meio_da_tela.addSpacing(15)
        self.meio_da_tela.addWidget(self.lbl_email)
        self.meio_da_tela.addWidget(self.input_email)
        self.meio_da_tela.addWidget(self.lbl_senha)
        self.meio_da_tela.addWidget(self.input_senha)
        self.meio_da_tela.addLayout(self.linha_check)
        self.meio_da_tela.addWidget(self.btn_login)
        self.meio_da_tela.addWidget(self.criar)
        self.meio_da_tela.addSpacing(15)
        self.meio_da_tela.addWidget(self.ou)
        self.meio_da_tela.addLayout(self.linha_social)

        self.setLayout(self.meio_da_tela)

    # ======= Funções =======
    def login(self):
        email = self.input_email.text()
        senha = self.input_senha.text()

        if email == "" or senha == "":
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
        else:
            QMessageBox.information(self, "Login", f"Bem-vindo(a), {email}!")

    def recuperar_senha(self):
        QMessageBox.information(self, "Recuperar senha", "Link de recuperação enviado ao seu e-mail.")

    def criar_conta(self):
        QMessageBox.information(self, "Nova conta", "Redirecionando para criar uma nova conta.")

    def login_facebook(self):
        QMessageBox.information(self, "Facebook", "Login com Facebook (simulado).")

    def login_google(self):
        QMessageBox.information(self, "Google", "Login com Google (simulado).")


# ======= Execução =======
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec_())

