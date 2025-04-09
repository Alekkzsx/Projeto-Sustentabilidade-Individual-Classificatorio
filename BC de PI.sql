-- Criação do banco com charset utf8mb4
CREATE DATABASE pi CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Configuração segura do usuário root (substitua a senha)
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '495321';
FLUSH PRIVILEGES;

USE pi;

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(256) NOT NULL
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabela de gastos (com suporte a caracteres especiais)
CREATE TABLE IF NOT EXISTS gastos_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    gasto_agua DECIMAL(10, 2) NOT NULL,
    classificacao_agua VARCHAR(40),
    gasto_energia DECIMAL(10, 2) NOT NULL,
    classificacao_energia VARCHAR(40),
    gasto_residuos DECIMAL(10, 2) NOT NULL,
    classificacao_residuos VARCHAR(40),
    periodo VARCHAR(10),
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabela de transportes (com suporte a caracteres especiais)
CREATE TABLE IF NOT EXISTS transportes_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    tipo_transporte VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    classificacao_transporte VARCHAR(50) NOT NULL,
    periodo VARCHAR(10),
    data_hora DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;