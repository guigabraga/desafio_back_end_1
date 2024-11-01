<h1 align="center"> 
    API de Usuários em Python com Flask e JWT
</h1>

Este projeto fornece uma API REST básica para criação de usuários, autenticação e listagem de usuários. A API é desenvolvida em Python com Flask e inclui uma documentação Swagger.

## Funcionalidades

- **Criação de Usuários** (`POST /user`): Cria um novo usuário após validações.
- **Autenticação de Usuários** (`POST /login`): Autentica um usuário e gera um token JWT.
- **Listagem de Usuários** (`GET /users`): Retorna uma lista de usuários cadastrados, protegida por autenticação JWT.

## Pré-requisitos

- **Python 3.8+**
- **PostgreSQL**
- **Bibliotecas Python**: `Flask`, `flasgger`, `flask_jwt_extended`, `werkzeug`, `psycopg2`

## Instalação e Configuração

1. **Clone o repositório**
    ```bash
    git clone git@github.com:BrayanPletsch/desafio_back_end_1.git
    cd ../desafio_back_end_1
    ```

2. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o banco de dados**

    - Acesse o PostgreSQL:
      ```sql
      CREATE DATABASE mydatabase;
      ```
    - Em seguida, crie a tabela `users`:
      ```sql
      CREATE TABLE users (
          id SERIAL PRIMARY KEY,
          user_name VARCHAR(50) NOT NULL,
          user_email VARCHAR(50) UNIQUE NOT NULL,
          user_pass VARCHAR(255) NOT NULL
      );
      ```

4. **Defina as variáveis de ambiente**

   No arquivo `config.py`, configure o banco de dados e a chave JWT:
   ```python
   DB_HOST = 'localhost'
   DB_NAME = 'mydatabase'
   DB_USER = 'postgres'
   DB_PASSWORD = 'postgres'
   DB_PORT = 5432
   ```

5. **Inicie a aplicação**
    ```bash
    python3 app.py
    ```

6. **Acesse a documentação da API**

   Acesse `http://localhost:5000/apidocs` para ver a documentação completa do Swagger e testar as rotas.

## Exemplos de Uso

### 1. Criação de Usuário

```http
POST /user
Content-Type: application/json

{
  "userName": "Exemplo",
  "userEmail": "exemplo@teste.com",
  "userPass": "senha123",
  "confirmPass": "senha123"
}
```

- **Resposta**: `201 Created`
  ```json
  {
    "message": "usuario criado com sucesso"
  }
  ```

### 2. Autenticação de Usuário

```http
POST /login
Content-Type: application/json

{
  "userEmail": "exemplo@teste.com",
  "userPass": "senha123"
}
```

- **Resposta**: `200 OK`
  ```json
  {
    "message": "usuario autenticado com sucesso",
    "token": "JWT_TOKEN"
  }
  ```

### 3. Listagem de Usuários

```http
GET /users
Content-Type: application/json
Authorization: Bearer JWT_TOKEN
```

- **Resposta**: `200 OK`
  ```json
  {
    "users": [
      {
        "userName": "Exemplo",
        "userEmail": "exemplo@teste.com"
      }
    ]
  }
  ```

## Contribuição

[Brayan Aragão Pletsch](https://www.brayan.blog/)
