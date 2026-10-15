import mysql.connector
conexao=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estoque"
)
print("Conexão realizada com sucesso!")