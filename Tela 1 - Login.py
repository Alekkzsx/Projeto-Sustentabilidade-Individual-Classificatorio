#Banco de dados de usuários cadastrados
from BancoDados_UsuarioSenha import database_usuarios

#Boas vindas ao usuário
print("="*48)
print("\tBem Vindo - Faça Seu Login")
print("="*48)


#Entrada de nome de Usuário e Senha
NomeDeUsuario = input("\t\tNome de Usuário: ")

#Repetição para caso usuário não cadastrado
while NomeDeUsuario != database_usuarios
SenhaDoUsuario = input("\t\tSenha: ")
