from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'dev-secret-key-2026'
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

users_db = {}

@app.route('/')
def index():
    return jsonify({"status": "running", "endpoints": ["/register", "/login", "/profile"]})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password or username in users_db:
        return jsonify({"msg": "Invalid data or user exists"}), 400

    users_db[username] = bcrypt.generate_password_hash(password).decode('utf-8')
    return jsonify({"msg": "User created"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users_db or not bcrypt.check_password_hash(users_db[username], password):
        return jsonify({"msg": "Unauthorized"}), 401

    token = create_access_token(identity=username)
    return jsonify(access_token=token), 200

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return jsonify({"user": get_jwt_identity(), "access": "granted"}), 200

if __name__ == '__main__':
    app.run(debug=True)