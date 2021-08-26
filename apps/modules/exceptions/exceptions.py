class AlreadyExist(Exception):

    def __init__(self, name: str, message: str = ' is already exist'):
        self.name = name
        self.message = message
        super().__init__(name, message)

    def __str__(self):
        return self.name + self.message


class FileAlreadyExist(AlreadyExist):
    pass


class InvalidPath(Exception):

    def __init__(self, path: str, message: str = ' is not valid path '):
        self.path = path
        self.message = message
        super().__init__(path, message)

    def __str__(self):
        return self.path + self.message
