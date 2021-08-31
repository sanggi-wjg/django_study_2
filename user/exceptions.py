class UserModelError(Exception):
    pass


class UserAlreadyExist(UserModelError):

    def __init__(self, username: str, message = ' is already exist'):
        self.username = username
        self.message = message
        super().__init__(username, message)

    def __str__(self):
        return self.username + self.message


class UserEmailAlreadyExist(UserModelError):

    def __init__(self, email: str, message = ' is already exist'):
        self.email = email
        self.message = message
        super().__init__(email, message)

    def __str__(self):
        return self.email + self.message
