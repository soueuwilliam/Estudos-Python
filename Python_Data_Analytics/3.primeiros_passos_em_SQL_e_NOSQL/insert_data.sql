--Inserção do usuario
INSERT INTO usuario(id,nome,email,data_nascimeto,endereco) VALUES
(1,"william","teste@teste.com","1999-02-25","Rua caminho das pedras brilhantes,22 Recife/PE"),
(1, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(2, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(3, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

--Inserçao do destino
INSERT INTO Destino(Destino.id,Destino.nome,Destino.descricao) VALUES
(1, 'Praia do rosa', 'linda praia'),
(1, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(2, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(3, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

--Inserção da resversas
INSERT INTO reservas (reservas.id,reservas.id_usuario,reservas.id_destino,reservas.data,reservas.status) VALUES
(1, 1, 2, '2023-07-10', 'confirmada'),
(2, 2, 1, '2023-08-05', 'pendente'),
(3, 3, 3, '2023-09-20', 'cancelada');
