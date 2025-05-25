/*create database estoque_automoveis;

-- Tabela de usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    tipo ENUM('cliente','estoquista') NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(100),
    data_nascimento DATE,
    CONSTRAINT uq_cpf UNIQUE (cpf)
);
    
    INSERT INTO usuarios (nome, cpf, tipo, telefone, endereco, data_nascimento) VALUES
('João Silva', '32165498712', 'cliente', '987654321', 'Rua das Flores, 100', '1990-05-10'),
('Maria Souza', '65498732145', 'estoquista', '998765432', 'Av. Paulista, 200', '1985-08-15'),
('Carlos Lima', '78912345678', 'cliente', '912345678', 'Rua A, 50', '1992-12-20'),
('Fernanda Rocha', '14725836900', 'estoquista', '934567890', 'Av. B, 80', '1988-03-30'),
('Lucas Costa', '96385274155', 'cliente', '956789012', 'Rua C, 150', '1995-07-25'),
('Patrícia Gomes', '85274196333', 'estoquista', '978901234', 'Rua D, 250', '1993-11-12'),
('Ricardo Alves', '74196385211', 'cliente', '990123456', 'Av. E, 300', '1987-09-18'),
('Larissa Melo', '15975348622', 'estoquista', '912345678', 'Rua F, 350', '1990-01-22'),
('Thiago Martins', '25836914733', 'cliente', '934567890', 'Rua G, 400', '1998-04-05'),
('Pires', '36914725874', 'estoquista', '956789012', 'Av. H, 450', '1991-06-14'),
('Gomes', '36914775844', 'cliente', '956789812', 'Av. I, 450', '1991-06-14'),
('Alves', '36917725844', 'estoquista', '956889012', 'Av. J, 450', '1991-06-14'),
('Lima', '36914725744', 'cliente', '956789812', 'Av. K, 450', '1991-06-14');

    
-- Tabela de carros
CREATE TABLE carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100),
    marca VARCHAR(100),
    ano INT
);
    
    INSERT INTO carros (modelo, marca, ano) VALUES
('Civic', 'Honda', 2020),
('Corolla', 'Toyota', 2019),
('Gol', 'Volkswagen', 2018),
('Fiesta', 'Ford', 2017),
('HB20', 'Hyundai', 2021),
('Onix', 'Chevrolet', 2020),
('Renegade', 'Jeep', 2022),
('Argo', 'Fiat', 2019),
('Kwid', 'Renault', 2021),
('Compass', 'Jeep', 2023),
('Fusca', 'Fusca', 2023),
('Ferrari', 'Ferrari', 2023),
('Xut', 'XKX', 2023);
    
-- Tabela de peças
CREATE TABLE pecas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    marca VARCHAR(100),
    valor DECIMAL(10,2),
    qtd_estoque INT DEFAULT 0,
    estoque_min INT DEFAULT 1,
    carro_id INT,
    CONSTRAINT fk_peca_carro FOREIGN KEY (carro_id) REFERENCES carros(id)
);
    
    INSERT INTO pecas (nome, marca, valor, qtd_estoque, estoque_min, carro_id) VALUES
('Pastilha de Freio', 'Bosch', 150.00, 200, 10, 1),
('Filtro de Óleo', 'Fram', 30.00, 50, 10, 2),
('Correia Dentada', 'Continental', 120.00, 150, 10, 3),
('Amortecedor', 'Monroe', 250.00, 100, 10, 4),
('Bateria', 'Moura', 400.00, 80, 10, 5),
('Velas de Ignição', 'NGK', 90.00, 300, 10, 6),
('Filtro de Ar', 'Tecfil', 40.00, 250, 10, 7),
('Disco de Freio', 'Bosch', 200.00, 120, 10, 8),
('Pneu', 'Pirelli', 500.00, 200, 10, 9),
('Radiador', 'Valeo', 600.00, 50, 5, 10),
('Retrovisor', 'Vale', 600.00, 50, 5, 11),
('Embreagem', 'Vao', 600.00, 50, 5, 12);

    
-- Tabela de movimentações de estoque
CREATE TABLE estoque_movimentacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    peca_id INT,
    usuario_id INT,
    tipo_movimentacao ENUM('entrada','saida') NOT NULL,
    qtd INT NOT NULL,
    data_movimentacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_movimentacao_peca FOREIGN KEY (peca_id) REFERENCES pecas(id),
    CONSTRAINT fk_movimentacao_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
    
    INSERT INTO estoque_movimentacao (peca_id, usuario_id, tipo_movimentacao, qtd, data_movimentacao)
VALUES
(1, 1, 'entrada', 100, '2025-04-05 00:00:00'),
(2, 1, 'saida', 5, '2025-05-13 01:12:02'),
(3, 2, 'entrada', 100, '2025-05-05 15:30:07'),
(4, 2, 'saida', 8, '2025-04-06 14:00:00'),
(5, 3, 'entrada', 120, '2025-03-05 17:40:05'),
(6, 3, 'saida', 4, '2025-04-16 23:46:09'),
(7, 4, 'entrada', 90, '2025-05-20 16:48:37'),
(8, 4, 'saida', 7, '2025-05-21 18:33:26'),
(9, 5, 'entrada', 60, '2025-05-21 00:00:00'),
(10, 5, 'saida', 3, '2025-05-17 23:59:59'),
(11, 1, 'entrada', 110, '2025-04-08 19:58:02');



# rodou e excluiu o carro com id 13 porque não tinha nenhuma peça vinculada
delete from carros where id = 13;
# não rodou porque o carro com o id 12 tem uma peça vinculada no carro
delete from carros where id = 12;
# Atualizando o modelo do carro com id 12, antes estava com o nome Ferrari
update carros set modelo = 'Lamborguini' where id = 12; */



