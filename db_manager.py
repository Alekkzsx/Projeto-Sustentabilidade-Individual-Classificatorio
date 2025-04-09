import mysql.connector
from datetime import datetime

def conectar_db():
    try:
        conexao = mysql.connector.connect(
            host="BD-ACD", #No SQL puc mudar para as informações da pucc
            user="BD26022511",
            password="Xgiaz10",
            database="BD26022511",  # Nome em maiúsculas
            auth_plugin='mysql_native_password'  # Força o uso do plugin antigo
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar com o banco de dados:", err)
        return None

# --- Funções para Usuários ---
def criar_usuario(username, nome, cpf, email, senha):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """INSERT INTO usuarios 
                   (username, nome, cpf, email, senha) 
                   VALUES (%s, %s, %s, %s, %s)"""
        valores = (username, nome, cpf, email, senha)
        cursor.execute(query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao criar usuário:", err)
        return False
    finally:
        cursor.close()
        conexao.close()

# --- Funções para Gastos ---
def registrar_gasto(id_usuario, agua, energia, residuos):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """INSERT INTO gastos_usuarios 
                   (id_usuario, gasto_agua, gasto_energia, gasto_residuos, data_hora) 
                   VALUES (%s, %s, %s, %s, %s)"""
        valores = (id_usuario, agua, energia, residuos, datetime.now())
        cursor.execute(query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao registrar gastos:", err)
        return False
    finally:
        cursor.close()
        conexao.close()

# --- Funções para Transportes ---
def registrar_transporte(id_usuario, transporte, quantidade, classificacao):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """INSERT INTO transportes_usuario 
                   (id_usuario, tipo_transporte, quantidade, classificacao_transporte, data_hora) 
                   VALUES (%s, %s, %s, %s, %s)"""
        valores = (id_usuario, transporte, quantidade, classificacao, datetime.now())
        cursor.execute(query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao registrar transporte:", err)
        return False
    finally:
        cursor.close()
        conexao.close()

# --- Funções de Consulta ---
def buscar_usuario_por_id(id_usuario):
    conexao = conectar_db()
    if conexao is None:
        return None

    try:
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM usuarios WHERE id = %s"
        cursor.execute(query, (id_usuario,))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print("Erro ao buscar usuário:", err)
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar_gastos_usuario(id_usuario):
    conexao = conectar_db()
    if conexao is None:
        return None

    try:
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM gastos_usuarios WHERE id_usuario = %s ORDER BY data_hora DESC"
        cursor.execute(query, (id_usuario,))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Erro ao buscar gastos:", err)
        return None
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    # Exemplo de uso:
    # Criar novo usuário
    if criar_usuario(
        username="joaosilva",
        nome="João Silva",
        cpf="123.456.789-00",
        email="joao@email.com",
        senha="senha_segura_123"
    ):
        print("Usuário criado com sucesso!")
        
        # Buscar usuário recém-criado (supondo que seja o ID 1)
        usuario = buscar_usuario_por_id(1)
        print("\nDados do usuário:")
        print(usuario)
        
        # Registrar gastos
        if registrar_gasto(
            id_usuario=1,
            agua=15.50,
            energia=78.30,
            residuos=5.75
        ):
            print("\nGastos registrados!")
            
            # Buscar histórico de gastos
            gastos = buscar_gastos_usuario(1)
            print("\nHistórico de gastos:")
            for gasto in gastos:
                print(gasto)
        
        # Registrar transporte
        if registrar_transporte(
            id_usuario=1,
            transporte="Carro",
            quantidade=3,
            classificacao="Alta emissão"
        ):
            print("\nTransporte registrado!")