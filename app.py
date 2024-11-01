import yaml
from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import check_password_hash
from config import Config
from models import Database

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_SORT_KEYS'] = False  

with open("docs/swagger.yaml", "r") as file:
    swagger_template = yaml.safe_load(file)
swagger = Swagger(app, template=swagger_template)

jwt = JWTManager(app)   

db = Database()
db.create_tables()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data.get('userName')
    user_email = data.get('userEmail')
    user_pass = data.get('userPass')
    confirm_pass = data.get('confirmPass')
    
    if not all([user_name, user_email, user_pass, confirm_pass]):
        return jsonify({"message": "Todos os campos são obrigatórios"}), 400

    if user_pass != confirm_pass:
        return jsonify({"message": "As senhas não coincidem"}), 400
    
    if db.get_user_by_email(user_email):
        return jsonify({"message": "Email já registrado"}), 400
    
    user_id = db.add_user(user_name, user_email, user_pass)
    if user_id:
        return jsonify({"message": "usuario criado com sucesso"}), 201
    else:
        return jsonify({"message": "Erro ao criar usuário"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_email = data.get("userEmail")
    user_pass = data.get("userPass")

    if not user_email or not user_pass:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400

    user = db.get_user_by_email(user_email)
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 400

    if not check_password_hash(user["user_pass"], user_pass):
        return jsonify({"message": "Senha incorreta"}), 400

    access_token = create_access_token(identity=user_email)
    return jsonify({"message": "usuario autenticado com sucesso", "token": access_token}), 200

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    try:
        users = db.get_all_users()
        return jsonify({"users": users}), 200
    except Exception as e:
        return jsonify({"message": "Erro ao buscar usuários"}), 400

if __name__ == "__main__":
    app.run(debug=True)
