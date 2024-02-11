import sqlite3

conexao = sqlite3.connect('estudantes')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).

#Resposta
#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#Resposta
#cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (1,"Debora",21,"Medicina")')
#cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (2,"Maria",19,"Engenharia")')
#cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (3,"Anderson",25,"Direito")')
#cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (4,"Paulo",22,"Fisioterapia")')
#cursor.execute('INSERT INTO alunos (id,nome,idade,curso) VALUES (5,"Max",27,"Biologia")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:

#a) Selecionar todos os registros da tabela "alunos".

#Resposta

#dados = cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
    #print(alunos)


#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

#Resposta

#dados = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
#for alunos in dados:
    #print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

#Resposta

#dados = cursor.execute('SELECT nome FROM alunos WHERE curso == "Engenharia" ORDER BY nome ASC')
#for alunos in dados:
    #print(alunos)


#d) Contar o número total de alunos na tabela

#Resposta

#dados = cursor.execute('SELECT count (nome) FROM alunos')
#for alunos in dados:
    #print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

#Resposta
#cursor.execute('UPDATE alunos SET idade=24 WHERE nome="Max"')

#b) Remova um aluno pelo seu ID.

#Resposta
#cursor.execute('DELETE FROM alunos WHERE id=2')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#Resposta
#cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo  FLOAT);')

#cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (1,"Debora",21,2.00)')
#cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (2,"Maria",19,15.00)')
#cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (3,"Anderson",25,16.75)')
#cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (4,"Paulo",22,500.00)')
#cursor.execute('INSERT INTO clientes (id,nome,idade,saldo) VALUES (5,"Max",27,"328.30")')

#cursor.execute('UPDATE clientes SET idade=44 WHERE nome="Max"')

#6. Consultas e Funções Agregadas
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#dadoscliente = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30')
#for clientes in dadoscliente:
    #print(clientes)

#b) Calcule o saldo médio dos clientes

#cursor.execute('SELECT AVG(saldo) FROM clientes')
#saldo_medio = cursor.fetchone()[0]
#if saldo_medio is not None:
    #print(f'O saldo médio dos clientes é: {saldo_medio:.2f}')

#c) Encontre o cliente com o saldo máximo.

#cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
#saldo_max = cursor.fetchone()
#if saldo_max is not None:
    #print(f'Cliente com saldo máximo:')
    #print(f'Nome: {saldo_max[1]}')
    #print(f'Saldo: {saldo_max[3]:.2f}')

#d) Conte quantos clientes têm saldo acima de 1000.

#cursor.execute('SELECT count (*) FROM clientes WHERE saldo > 1000')
#maiorqmil = cursor.fetchone()[0]
#print(f'Número de clientes com saldo acima de 1000: {maiorqmil}')

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

#cursor.execute('UPDATE clientes SET saldo = 2037.35 WHERE id = 3')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# Criando a tabela "compras"
#cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(200), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Inserindo algumas compras associadas a clientes existentes na tabela "clientes"
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "Pente", 50.00)')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (2, "Escova", 75.50)')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (3, "Secador", 120.75)')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (4, "Espelho", 200.00)')
#cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (5, "Pomada", 30.50)')

# Consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
resultados = cursor.fetchall()
for resultado in resultados:
    print(f'Cliente: {resultado[0]}, Produto: {resultado[1]}, Valor: {resultado[2]:.2f}')

conexao.commit()
conexao.close