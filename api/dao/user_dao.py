class UserDao():
    def __init__(self):
        self.users = []

    def create_user(self, user):
        self.users.append(user)

        return len(self.users)

    def email_exists(self, email):
        return len(list(filter(lambda ex_user: (ex_user.email == email), self.users))) > 0

    def username_exists(self, username):
        return len(list(filter(lambda ex_user: (ex_user.username == username), self.users))) > 0

    def find_by_username(self, username):
        found_users = list(filter(lambda user: (user.username == username), self.users))
        user = None
        if len(found_users) > 0:
            user = found_users[0]
        return user