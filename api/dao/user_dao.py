class UserDao():
    def __init__(self):
        self.users = []

    def create_user(self, user):
        self.users.append(user)

        return len(self.users)

    def user_exists(self, email):
        return len(list(filter(lambda ex_user: (ex_user.email == email), self.users))) > 0