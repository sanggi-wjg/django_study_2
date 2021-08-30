import os

from apps.modules.utils.colorful import debug

from amk_demo.settings.base import MEDIA_ROOT
from apps.modules.utils.file_utils import is_exist_filepath
from django.core.files.storage import default_storage, Storage


def upload_file_to_server(upload_file, media_save_path: str) -> bool:
    filename = upload_file.name
    filepath = os.path.join(MEDIA_ROOT, media_save_path, filename)
    debug('[upload_file_to_server]', 'filename', filename, 'filepath', filepath)

    if is_exist_filepath(filepath):
        raise FileExistsError(f'{filename} is already exists')

    default_storage.save(filepath, upload_file)
    return True
