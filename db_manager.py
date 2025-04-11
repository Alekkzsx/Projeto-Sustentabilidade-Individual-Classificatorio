import mysql.connector
from datetime import datetime

def conectar_db(): #Funcionando corretamente
    try:
        conexao = mysql.connector.connect(
            host="localhost", #No SQL puc mudar para as informações da pucc
            user="root",
            password="495321",
            database="pi",  # Nome em maiúsculas
            charset="utf8mb4",
            auth_plugin='mysql_native_password'  # Força o uso do plugin antigo
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro ao conectar com o banco de dados:", err)
        return None

# --- Funções para Usuários ---
def criar_usuario(username, nome, cpf, email, senha): #Funcionando corretamente
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
        
def buscar_transportes_usuario(id_usuario):
    conexao = conectar_db()
    if conexao is None:
        return None

    try:
        cursor = conexao.cursor(dictionary=True)
        query = "SELECT * FROM transportes_usuario WHERE id_usuario = %s ORDER BY data_hora DESC"
        cursor.execute(query, (id_usuario,))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print("Erro ao buscar transportes:", err)
        return None
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
        
def salvar_gastos_no_mysql(id_usuario, agua, classificacao_agua, energia, classificacao_energia, residuos, classificacao_residuos, periodo, data_hora):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """INSERT INTO gastos_usuarios 
                   (id_usuario, gasto_agua, classificacao_agua, gasto_energia, classificacao_energia, 
                    gasto_residuos, classificacao_residuos, periodo, data_hora) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (id_usuario, agua, classificacao_agua, energia, classificacao_energia, 
                   residuos, classificacao_residuos, periodo, data_hora)
        cursor.execute(query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao salvar gastos no MySQL:", err)
        return False
    finally:
        cursor.close()
        conexao.close()

def salvar_transportes_no_mysql(id_usuario, transportes, periodo, data_hora):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """INSERT INTO transportes_usuario 
                   (id_usuario, tipo_transporte, quantidade, classificacao_transporte, periodo, data_hora) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        for transporte in transportes:
            valores = (id_usuario, transporte['meio'], transporte['viagens'], transporte['classificacao'], periodo, data_hora)
            cursor.execute(query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao salvar transportes no MySQL:", err)
        return False
    finally:
        cursor.close()
        conexao.close()
        
def atualizar_gastos_no_mysql(id_gasto, agua, classificacao_agua, energia, classificacao_energia, residuos, classificacao_residuos):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        query = """UPDATE gastos_usuarios
                   SET gasto_agua = %s, classificacao_agua = %s,
                       gasto_energia = %s, classificacao_energia = %s,
                       gasto_residuos = %s, classificacao_residuos = %s
                   WHERE id = %s"""
        valores = (agua, classificacao_agua, energia, classificacao_energia, residuos, classificacao_residuos, id_gasto)
        cursor.execute(query, valores)
        conexao.commit()
        return cursor.rowcount > 0  # Retorna True se algum registro foi atualizado
    except mysql.connector.Error as err:
        print("Erro ao atualizar gastos no MySQL:", err)
        return False
    finally:
        cursor.close()
        conexao.close()

def atualizar_transportes_no_mysql(id_usuario, transportes, periodo, data_hora):
    conexao = conectar_db()
    if conexao is None:
        return False

    try:
        cursor = conexao.cursor()
        # Remove os transportes existentes para o mesmo usuário e data_hora
        delete_query = """DELETE FROM transportes_usuario 
                          WHERE id_usuario = %s AND data_hora = %s"""
        cursor.execute(delete_query, (id_usuario, data_hora))

        # Insere os novos transportes
        insert_query = """INSERT INTO transportes_usuario 
                          (id_usuario, tipo_transporte, quantidade, classificacao_transporte, periodo, data_hora) 
                          VALUES (%s, %s, %s, %s, %s, %s)"""
        for transporte in transportes:
            valores = (
                id_usuario,
                transporte['tipo_transporte'],  # Corrigido para usar a chave correta
                transporte['quantidade'],      # Corrigido para usar a chave correta
                transporte['classificacao_transporte'],  # Corrigido para usar a chave correta
                periodo,
                data_hora
            )
            cursor.execute(insert_query, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as err:
        print("Erro ao atualizar transportes no MySQL:", err)
        return False
    finally:
        cursor.close()
        conexao.close()