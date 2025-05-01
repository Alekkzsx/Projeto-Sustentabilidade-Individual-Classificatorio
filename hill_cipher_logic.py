# hill_cipher_logic.py
import numpy as np

# --- Configuração da Cifra de Hill ---
MODULUS = 256  # Usando ASCII extendido
BLOCK_SIZE = 2 # Tamanho do bloco (dimensão da matriz chave)

# Matriz Chave (Exemplo: deve ser invertível mod 256)
# K = [[3, 3], [2, 5]]  det = 15 - 6 = 9. gcd(9, 256) = 1 -> Invertível
KEY_MATRIX = np.array([[3, 3], [2, 5]])

# Pré-calcular a Inversa Modular da Chave
# Função para calcular o Inverso Modular Multiplicativo (usando Algoritmo Estendido de Euclides)
def extended_gcd(a, b):
    """Retorna (gcd, x, y) tal que a*x + b*y = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

def modInverse(a, m):
    """Retorna o inverso modular de a % m"""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception(f'O inverso modular não existe para {a} mod {m}')
    else:
        return (x % m + m) % m # Garante resultado positivo

def matrix_mod_inverse(matrix, modulus):
    """Calcula a inversa modular de uma matriz quadrada"""
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = modInverse(det, modulus)

    # Calcula a matriz adjunta (cofatora transposta)
    # Para matriz 2x2 [[a, b], [c, d]], a adjunta é [[d, -b], [-c, a]]
    if matrix.shape == (2, 2):
        adj_matrix = np.array([[matrix[1, 1], -matrix[0, 1]],
                               [-matrix[1, 0], matrix[0, 0]]])
    else:
        # Para matrizes maiores, usar np.linalg.inv e multiplicar pelo determinante
        # Isso pode ter problemas de precisão com float, mas para 2x2 a fórmula exata é melhor
        raise NotImplementedError("Inversa modular implementada apenas para matriz 2x2")
        # Alternativa (pode ter problemas de precisão):
        # adj_matrix = np.round(np.linalg.inv(matrix) * det).astype(int)

    # Calcula a inversa modular: det_inv * adj_matrix mod modulus
    inverse_matrix = (det_inv * adj_matrix) % modulus
    return inverse_matrix.astype(int)

try:
    KEY_MATRIX_INV = matrix_mod_inverse(KEY_MATRIX, MODULUS)
    # print(f"Matriz Chave:\n{KEY_MATRIX}") # Para depuração
    # print(f"Matriz Inversa Chave:\n{KEY_MATRIX_INV}") # Para depuração
except Exception as e:
    print(f"Erro: A matriz chave escolhida não é invertível módulo {MODULUS}. {e}")
    # Você precisaria escolher outra matriz chave se isso acontecer.
    exit()
# --- Fim da Configuração ---


# --- Funções de Criptografia/Descriptografia ---

def _prepare_text(text):
    """Converte texto para números e aplica padding se necessário."""
    # Converte para números ASCII
    numbers = [ord(char) for char in text]
    # Adiciona padding (caractere nulo) se o tamanho for ímpar
    if len(numbers) % BLOCK_SIZE != 0:
        numbers.append(0) # Padding com NUL
    return numbers

def _format_output(numbers):
    """Converte números de volta para texto, removendo padding."""
    # Remove padding (caracteres NUL no final)
    while numbers and numbers[-1] == 0:
        numbers.pop()
    # Converte de volta para caracteres
    return "".join([chr(num) for num in numbers])

def encrypt(plaintext):
    """Criptografa o texto usando a Cifra de Hill."""
    numbers = _prepare_text(plaintext)
    ciphertext_nums = []

    for i in range(0, len(numbers), BLOCK_SIZE):
        block = np.array(numbers[i : i + BLOCK_SIZE])
        # C = P * K mod N
        encrypted_block = np.dot(block, KEY_MATRIX) % MODULUS
        ciphertext_nums.extend(encrypted_block.tolist())

    # Retorna como string (pode conter caracteres não imprimíveis)
    return _format_output(ciphertext_nums)
    # Alternativa: retornar como lista de inteiros ou string base64 se o armazenamento for problema
    # import base64
    # return base64.b64encode(bytes(ciphertext_nums)).decode('utf-8')


def decrypt(ciphertext):
    """Descriptografa o texto usando a Cifra de Hill."""
    # Se estiver usando Base64 para armazenar:
    # import base64
    # try:
    #     numbers = list(base64.b64decode(ciphertext))
    # except: # Tratar caso não seja base64 ou esteja corrompido
    #     print("Erro ao decodificar Base64 do ciphertext.")
    #     return "" # Ou lançar um erro

    # Se estiver armazenando a string diretamente (pode ter NULs):
    numbers = _prepare_text(ciphertext) # Reusa a preparação para garantir padding correto se necessário

    plaintext_nums = []
    for i in range(0, len(numbers), BLOCK_SIZE):
        block = np.array(numbers[i : i + BLOCK_SIZE])
        # P = C * K_inv mod N
        decrypted_block = np.dot(block, KEY_MATRIX_INV) % MODULUS
        plaintext_nums.extend(decrypted_block.tolist())

    return _format_output(plaintext_nums)