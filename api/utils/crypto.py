from passlib.context import CryptContext

class Crypto:
    def __init__(self):
        self.password_context = CryptContext(
                schemes=["pbkdf2_sha256"],
                default="pbkdf2_sha256",
                pbkdf2_sha256__default_rounds=30000
        )

    def cypher(self, password):
        return self.password_context.encrypt(password)