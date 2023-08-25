-- Criar banco de dados "DataAnonymization"
CREATE DATABASE DataAnonymization;

-- Selecionar o banco de dados "DataAnonymization"
-- Criação da tabela "cliente"
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(100)
);

-- Criação da tabela "contatos"
CREATE TABLE contatos (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    telefone VARCHAR(100),
    email VARCHAR(100),
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

-- Inserção de dados na tabela "cliente"
INSERT INTO cliente (nome, cpf)
VALUES
    ('Lucas Freitas', '580.421.673-26'),
    ('Lavínia Sales', '058.197.234-14'),
    ('Arthur Cavalcanti', '043.685.219-51'),
    ('Maria Sophia Santos', '253.984.617-37'),
    ('Marina das Neves', '562.740.813-80');

-- Inserção de dados na tabela "contatos"
INSERT INTO contatos (cliente_id, telefone, email)
VALUES
    (1, '(71) 43410-7964', 'lucas_freitas@almeida.com'),
    (2, '(58) 31457-0120', 'lavinia_sales@castro.com'),
    (3, '(84) 12251-2343', 'arthur_cavalcanti@nascimento.br'),
    (4, '(91) 09290-5820', 'maria_sophia_santos@costela.com'),
    (5, '(47) 32659-0087', 'marina_das_neves@mendes.org');
