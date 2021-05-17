from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/user', methods=["POST"])
def register_user():
    return 'This works!'

@app.route('/login', methods=["POST"])
def login():
    return 'This works!'

@app.route('/user/:userId', methods=["PATCH"])
def update_user():
    return 'This works!'

@app.route('/user/:userId/password', methods=["PATCH"])
def update_user_password():
    return 'This works!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
