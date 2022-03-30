import os
from PIL import Image
from django.core.mail import send_mail


def get_file_path(obj, fname):
    return os.path.join(
        'media',
        'user_avatar',
        obj.email,
        fname
    )


def send_messages(user_1, user_2):
    send_mail(
        'Hello',
        f'Вы понравились {user_1.name}! Почта участника: {user_1.email}',
        'apptrixtesttask1@gmail.com',
        [user_2],
        fail_silently=False
    )
    send_mail(
        'Hello',
        f'Вы понравились {user_2.name}! Почта участника: {user_2.email}',
        'apptrixtesttask1@gmail.com',
        [user_1],
        fail_silently=False
    )
