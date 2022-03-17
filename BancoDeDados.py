# Como criar um CRUD em Python usando em MySQl
# Geralmente o banco ja estara criado, mas nao significa que não posse ser criado
# O python, na essencia, vai somente interagir com banco de dados.
# Ja que o CRUD somente ira adicionar alguma informação no BD, não cria-lo.
# Mas antes de inserir as informações, deve-se conectar ao banco.

import mysql.connector

# realiza a criacao da conexao ao banco
conexao = mysql.connector.connect(
    host= 'http://localhost:881',
    user= 'root',
    password= '',
    database= 'peitos',
) # ao criar a conexão, deve testa-la (quando rodar nada deve acontecer, senão havera algum erro)

# realiza a execução da conexao 
cursor = conexao.cursor()

# CRUD

# Ao criar uma conexão e seu cursor, deve-se fecha-la ao final do codigo
cursor.close()
conexao.close()

#CREATE

#READ
#UPDATE
#DELETE