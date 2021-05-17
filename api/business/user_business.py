from model.user import User
from dao.user_dao import UserDao

class UserBusiness():
    def __init__(self):
        self.users_dao = UserDao()

    def create_user(self, username, email, password):
        if not username:
            raise Exception('El nombre de usuario no puede ser vacío')
        if not email:
            raise Exception('El email no puede ser vacío')
        if not password:
            raise Exception('La contraseña no puede ser vacía')
        if self.users_dao.user_exists(email):
            raise Exception('No se puede crear el usuario, el email ya ha sido usado para otro usuario')
        return self.users_dao.create_user(User(username, email, password))
