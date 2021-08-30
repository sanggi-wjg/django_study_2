import sys
import traceback


def brief_error():
    exc_type, exc_value, exc_tb = sys.exc_info()
    return "(Type) : {} | (Line) : {} | (Msg) : {}\n{}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value, traceback.format_exc())


class InvalidPath(Exception):

    def __init__(self, path: str, message: str = ' is not valid path'):
        self.path = path
        self.message = message
        super().__init__(path, message)

    def __str__(self):
        return self.path + self.message
