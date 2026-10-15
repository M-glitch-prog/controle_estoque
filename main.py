import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="estoque"
    )
    return conexao

def cadastrar_prod():
    print("==Cadastro de produtos==")
    nome=input("Nome do produto: ")
    descricao=input("Descrição do produto: ")
    preco=float(input("Preço do produto: "))
    quantidade=int(input("Quantidade em estoque: "))

    conexao=conectar()
    cursor=conexao.cursor()

    sql="INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
    valores=(nome, descricao, preco, quantidade)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Produto cadastrado com sucesso!")
    cursor.close()
    conexao.close()
cadastrar_prod()