# Descrição:
- Faça um fork deste repositório;
- Crie uma API REST básica;
- Crie um swagger para documentar sua API;
- Utilize Node.JS ou Python;
- Caso utilize Node, preferencialmente utilize o Express para construção da sua API;
- Caso utilize Python, preferencialmente utilize o Flask para construção da sua API.

## Rota para criação de usuário

`POST /user`
<br>
`application/json`
<br>
`body: {"userName": string, "userEmail": string, "userPass": string, "confirmPass": string}"`

Respostas:

`STATUS_CODE: 201`
<br>
`{"message": "usuario criado com sucesso"}`

`STATUS_CODE: 400`
<br>
`{"message": ${mensagem_de_erro}}`

Observações:
- Validar se o userPass e confirmPass são iguais;
- Validar se o email já está cadastrado;
- Insira os dados de nome, email e senha no banco de dados;
- Transforme a senha em um hash antes de inserir no banco de dados;


## Rota para autenticação de usuário

`POST /login`
<br>
`application/json`
<br>
`body: {"userEmail": string, "userPass": string}"`

Respostas:

`STATUS_CODE: 200`
<br>
`{"message": "usuario autenticado com sucesso", "token": string}`

`STATUS_CODE: 400`
<br>
`{"message": ${mensagem_de_erro}}`

Observações:
- Validar se email existe no banco de dados;
- Confirmar senha;
- Gerar um token JWT com validade de 2 minutos;

## Rota buscar usuários cadastrados

`GET /users`
<br>
`application/json`
<br>
`HEADER: Authorization: Bearer ${TOKEN}`

Respostas:

`STATUS_CODE: 200`
<br>
`{"users": [{"userName": string, "userEmail": string}]}`

`STATUS_CODE: 400`
<br>
`{"message": ${mensagem_de_erro}}`

Observações:
- Validar se o token de acesso.
