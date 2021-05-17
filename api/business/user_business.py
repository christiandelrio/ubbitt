from model.session import Session
from dao.session_dao import SessionDao
from utils.crypto import Crypto
from model.user import User
from dao.user_dao import UserDao
import uuid

class UserBusiness():
    def __init__(self):
        self.users_dao = UserDao()
        self.session_dao = SessionDao()

    def create_user(self, username, email, password):
        self.validate_user_data(username, email, password)
        crypto = Crypto()
        hashed_password = crypto.cypher(password)
        return self.users_dao.create_user(User(username, email, hashed_password))

    def validate_user_data(self, username, email, password):
        if not username:
            raise Exception('El nombre de usuario no puede ser vacío')
        if not email:
            raise Exception('El email no puede ser vacío')
        if not password:
            raise Exception('La contraseña no puede ser vacía')
        if self.users_dao.email_exists(email):
            raise Exception('No se puede crear el usuario, el email ya ha sido usado para otro usuario')
        if self.users_dao.username_exists(username):
            raise Exception('No se puede crear el usuario, el nombre de usuario ya ha sido usado para otro usuario')

    def login(self, username, password):
        user = self.users_dao.find_by_username(username)
        if user is None:
            raise Exception('El usuario y/o contraseña son incorrectos, por favor intenta de nuevo')
        crypto = Crypto()
        if not crypto.verify_encrypted_password(password, user.password):
            raise Exception('El usuario y/o contraseña son incorrectos, por favor intenta de nuevo')
        session_uuid = str(uuid.uuid4())
        session = Session(username, session_uuid)
        self.session_dao.save_session(session)
        return session_uuid