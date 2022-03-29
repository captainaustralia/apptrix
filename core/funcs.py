import os
from PIL import Image


def get_file_path(obj, fname):
    return os.path.join(
        'media',
        'user_avatar',
        obj.email,
        fname
    )

