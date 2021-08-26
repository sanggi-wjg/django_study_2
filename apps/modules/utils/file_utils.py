import os


def is_exist_filepath(filepath: str) -> bool:
    if os.path.exists(filepath):
        return True
    return False
