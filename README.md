# 📦 Sistema de Controle de Estoque

Projeto desenvolvido em **Python** com integração ao **MySQL**, utilizando o XAMPP para gerenciar o banco de dados.

O objetivo é criar um sistema simples para organizar e controlar produtos em estoque, permitindo o armazenamento e a consulta de informações.

## 🚀 Funcionalidades

- [x] Cadastro de produtos
- [x] Listagem de produtos cadastrados
- [x] Pesquisa de produtos pelo nome
- [ ] Exclusão de produtos
- [ ] Atualização de produtos
- [ ] Alerta de estoque baixo
- [ ] Relatórios automáticos

*As funcionalidades marcadas como pendentes serão implementadas durante o desenvolvimento do projeto.*

## 🛠️ Tecnologias utilizadas

- **Python** — lógica e funcionalidades do sistema.
- **MySQL** — armazenamento dos dados dos produtos.
- **XAMPP** — gerenciamento do servidor MySQL.
- **mysql-connector-python** — conexão entre Python e MySQL.
- **Visual Studio Code** — ambiente de desenvolvimento.

## 📋 Informações dos produtos

O sistema trabalha com os seguintes campos:

- ID do produto
- Nome
- Descrição
- Preço
- Quantidade em estoque

## ⚙️ Como executar o projeto

### 1. Instale as ferramentas necessárias

- [Python](https://www.python.org/)
- [XAMPP](https://www.apachefriends.org/)
- [Visual Studio Code](https://code.visualstudio.com/)

### 2. Instale a biblioteca de conexão

No terminal do VS Code, execute:

```bash
python -m pip install mysql-connector-python
```

### 3. Configure o banco de dados

Abra o XAMPP e inicie o Apache e o MySQL.

Acesse o phpMyAdmin pelo endereço:

`http://localhost/phpmyadmin`

Crie um banco de dados chamado `estoque` e uma tabela `produtos` com os campos utilizados pelo programa.

### 4. Execute o sistema

Abra a pasta do projeto no VS Code e execute:

```bash
python main.py
```

## 📚 Objetivo de aprendizagem

Este projeto faz parte dos meus estudos em programação e tem como objetivo praticar Python, integração com banco de dados, operações SQL e desenvolvimento de sistemas.

## 📌 Status do projeto

**Em desenvolvimento.**

Novas funcionalidades serão adicionadas conforme o aprendizado e a evolução do projeto.

---

Desenvolvido como projeto de estudo em Python 💻

