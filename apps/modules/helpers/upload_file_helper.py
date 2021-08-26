import os

from django.core.files.storage import default_storage

from amk_demo.settings.base import MEDIA_ROOT
from apps.modules.exceptions.exceptions import FileAlreadyExist, InvalidPath
from apps.modules.utils.file_utils import is_exist_filepath


def upload_file_to_server(upload_file, media_save_path: str) -> bool:
    filename = upload_file.name
    filepath = os.path.join(MEDIA_ROOT, media_save_path, filename)

    if is_exist_filepath(filepath):
        raise FileAlreadyExist(filename)

    default_storage.save(filepath, upload_file)
    return True
