import os


def is_exist_filepath(filepath: str) -> bool:
    if filepath == '':
        raise ValueError('filepath is empty')

    if os.path.exists(filepath):
        return True
    return False
