import json
import os

DATABASE_FILE = "usuarios.json"

# Carrega dados do arquivo se existir
if os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, 'r') as f:
        database_usuarios = json.load(f)
else:
    database_usuarios = {
        "ADM": {
            "nome": "ADM",
            "cpf": "455.251.987-75",
            "email": "xvidros@email.com",
            "senha": "123"
        }
    }

def salvar_dados():
    """Salva o dicionário no arquivo JSON"""
    with open(DATABASE_FILE, 'w') as f:
        json.dump(database_usuarios, f, indent=4)