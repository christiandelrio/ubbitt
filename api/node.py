from flask.json import jsonify
from business.user_business import UserBusiness
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

userBusiness = UserBusiness()

# Creación de usuarios
@app.route('/user', methods=["POST"])
def register_user():
    user_data = request.get_json()
    try:
        user_id = userBusiness.create_user(user_data['username'], user_data['email'], user_data['password'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'userId': user_id, 'message': 'Usuario creado exitosamente'}), 200

# Login
@app.route('/login', methods=["POST"])
def login():
    user_data = request.get_json()
    try:
        session_uuid = userBusiness.login(user_data['username'], user_data['password'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'token': session_uuid}), 200

# Logout
@app.route('/logout', methods=["POST"])
def logout():
    try:
        userBusiness.logout(request.headers['token'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'message': 'Sesion cerrada correctamente'}), 200

# Actualización de datos de usuario
@app.route('/user', methods=["PATCH"])
def update_user():
    return 'This works!'

# Actualización de datos de usuario
@app.route('/user', methods=["GET"])
def get_user_data():
    try:
        user = userBusiness.get_user_data(request.headers['token'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify(user.__dict__), 200

# Cambio de contraseña
@app.route('/user/password', methods=["PATCH"])
def update_user_password():
    password_data = request.get_json()
    try:
        userBusiness.update_password(request.headers['token'], password_data['password'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'message': 'Contraseña actualizada exitosamente'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
