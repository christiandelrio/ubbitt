from flask.json import jsonify
from business.user_business import UserBusiness
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

userBusiness = UserBusiness()

@app.route('/user', methods=["POST"])
def register_user():
    user_data = request.get_json()
    try:
        user_id = userBusiness.create_user(user_data['username'], user_data['email'], user_data['password'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'userId': user_id, 'message': 'Usuario creado exitosamente'}), 200

@app.route('/login', methods=["POST"])
def login():
    user_data = request.get_json()
    try:
        session_uuid = userBusiness.login(user_data['username'], user_data['password'])
    except Exception as err:
        return jsonify({'message': str(err)}), 400
    return jsonify({'token': session_uuid}), 200

@app.route('/user/:userId', methods=["PATCH"])
def update_user():
    return 'This works!'

@app.route('/user/:userId/password', methods=["PATCH"])
def update_user_password():
    return 'This works!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
