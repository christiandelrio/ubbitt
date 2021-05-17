from model.session import Session
from dao.session_dao import SessionDao
from utils.crypto import Crypto
from model.user import User
from dao.user_dao import UserDao
import copy
import uuid

class UserBusiness():
    def __init__(self):
        self.users_dao = UserDao()
        self.session_dao = SessionDao()

    # Crea un nuevo usuario
    def create_user(self, username, email, password):
        self.validate_user_data(username, email, password)
        crypto = Crypto()
        hashed_password = crypto.cypher(password)
        return self.users_dao.create_user(User(username, email, hashed_password))

    # Valida que la información en viada para crear un nuevo usuario sea válida
    def validate_user_data(self, username, email, password):
        if not username:
            raise Exception('El nombre de usuario no puede ser vacío.')
        if not email:
            raise Exception('El email no puede ser vacío.')
        if not password:
            raise Exception('La contraseña no puede ser vacía.')
        if self.users_dao.email_exists(email):
            raise Exception('No se puede crear el usuario, el email ya ha sido usado para otro usuario.')
        if self.users_dao.username_exists(username):
            raise Exception('No se puede crear el usuario, el nombre de usuario ya ha sido usado para otro usuario.')

    # Inicia la sesión del usuario
    def login(self, username, password):
        user = self.users_dao.find_by_username(username)
        if user is None:
            raise Exception('El usuario y/o contraseña son incorrectos, por favor intenta de nuevo.')
        crypto = Crypto()
        if not crypto.verify_encrypted_password(password, user.password):
            raise Exception('El usuario y/o contraseña son incorrectos, por favor intenta de nuevo.')
        session_uuid = str(uuid.uuid4())
        session = Session(username, session_uuid)
        self.session_dao.save_session(session)
        return session_uuid

    # Cierra la sesión del usuario
    def logout(self, session_id):
        session = self.session_dao.find_user_by_session(session_id)
        if session is None:
            raise Exception('La sesión es inválida.')
        self.session_dao.delete_session_by_id(session_id)

    # Actualiza la contraseña del usuario
    def update_password(self, session_id, new_password):
        session = self.session_dao.find_user_by_session(session_id)
        if session is None:
            raise Exception('La sesión es inválida.')
        crypto = Crypto()
        new_hashed_password = crypto.cypher(new_password)
        self.users_dao.update_user_password(session.username, new_hashed_password)

    # Actualiza la información del usuario
    def update_user_data(self, session_id, email):
        session = self.session_dao.find_user_by_session(session_id)
        if session is None:
            raise Exception('La sesión es inválida.')
        self.users_dao.update_user_data(session.username, email)

    # Recupera los datos del usuario excepto la contraseña
    def get_user_data(self, session_id):
        session = self.session_dao.find_user_by_session(session_id)
        if session is None:
            raise Exception('La sesión es inválida.')
        user = copy.copy(self.users_dao.find_by_username(session.username))
        del user.password
        return user