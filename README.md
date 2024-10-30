## Descrição:
- Faça um fork deste repositório;
- Crie uma API REST básica;
- Utilize Node.JS ou Python;
- Caso utilize Node, preferencialmente utilize o Express para construção da sua API;
- Caso utilize Python, preferencialmente utilize o Flask para construção da sua API.

## Rotas
### - Rota para criação de usuário

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


### - Rota para autenticação de usuário

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
