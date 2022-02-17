class User:
    def __init__(self, username, password, rights):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def get_user_data(self):
        return {
            "username": self.username,
            "password": self.password,
        }