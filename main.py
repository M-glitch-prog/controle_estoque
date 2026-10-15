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

def listar_prod():
    print("==Listagem de produtos==")
    conexao=conectar()
    cursor=conexao.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos=cursor.fetchall()
    if len (produtos)==0:
        print("Nenum produto cadastrado!")
    else:
        for p in produtos:
            print("ID: ",produtos[0],
                  "Nome: ",produtos[1],
                  "Descrição: ",produtos[2],
                  "Preço: ",produtos[3],
                  "Quantidade: ",produtos[4])
    cursor.close()
    conexao.close()
def pesquisa_prod():
    print("==Pesquisa de produtos==")
    achar=input("produto a encontrar: ")
    conexao=conectar()
    cursor=conexao.cursor()
    sql="SELECT * FROM produtos WHERE nome LIKE %s"
    cursor.execute(sql,("%"+achar+"%",))
    produtos=cursor.fetchall()
    if len(produtos)==0:
        print("Nenhum produto encontrado!")
    else:
        for p in produtos:
            print("ID: ",p[0],
                  "Nome: ",p[1],
                  "Descrição: ",p[2],
                  "Preço: ",p[3],
                  "Quantidade: ",p[4])
    cursor.close()
    conexao.close()
def menu():
    while True:
        print("==Menu de opções==")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Pesquisar produto")
        print("4 - Sair")
        opcao=input("Escolha uma opção: ")
        if opcao=="1":
            cadastrar_prod()
        elif opcao=="2":
            listar_prod()
        elif opcao=="3":
            pesquisa_prod()
        elif opcao=="4":
            break
        else:
            print("Opção inválida!")
menu()